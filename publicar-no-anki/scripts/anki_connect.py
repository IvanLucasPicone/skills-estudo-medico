#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ponte AnkiConnect — publica material de estudo no Anki de forma IDEMPOTENTE.

Uso como módulo:
    import anki_connect as ak
    ak.publish_batch({"sync": True, "notes": [ {deck, model, fields, tags, key_field?}, ... ]})

Uso como CLI (lote em JSON via arquivo ou stdin):
    python3 anki_connect.py lote.json
    cat lote.json | python3 anki_connect.py

Formato do lote:
    {
      "sync": true,
      "notes": [
        {"deck":"Cardiologia::Flashcards","model":"Básico","fields":{"Frente":"...","Verso":"..."},
         "tags":["Cardiologia","DiabetesInsipidus"], "key_field":"Frente"}
      ]
    }

Idempotência: se o note type tiver o campo "UID", usa UID = sha1(deck + key_field) como
chave estável (atualiza se já existe, insere se não). Sem UID, cai no dedup nativo do
Anki pelo 1º campo. Se o AnkiConnect estiver offline, NÃO perde conteúdo: grava um
fallback JSONL para importação posterior e retorna ok=False com o motivo.
"""
import json
import sys
import hashlib
import urllib.request

# 127.0.0.1 e NAO "localhost": no Windows, urllib tenta resolver localhost por IPv6 (::1)
# primeiro, espera o timeout e so entao cai para IPv4 — 2,1 s de overhead FIXO por chamada,
# independente da operacao. Num lote de ~290 notas (≈1.100 chamadas) isso e' a diferenca entre
# ~40 minutos e ~40 segundos. Medido em 2026-07-29: 2,097 s vs 0,038 s por chamada.
ANKI_URL = "http://127.0.0.1:8765"
TIMEOUT = 15


class AnkiError(RuntimeError):
    pass


def invoke(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    try:
        req = urllib.request.Request(ANKI_URL, payload, {"Content-Type": "application/json"})
        r = urllib.request.urlopen(req, timeout=TIMEOUT)
    except Exception as e:
        raise AnkiError(f"AnkiConnect inacessível em {ANKI_URL}: {e}")
    res = json.load(r)
    if res.get("error"):
        raise AnkiError(f"{action}: {res['error']}")
    return res["result"]


def is_available():
    try:
        invoke("version")
        return True
    except AnkiError:
        return False


def ensure_deck(name):
    invoke("createDeck", deck=name)  # idempotente
    return name


def model_exists(name):
    return name in invoke("modelNames")


def model_fields(name):
    return invoke("modelFieldNames", modelName=name)


def ensure_model(spec):
    """Cria o note type se faltar (idempotente). spec = CANONICAL_MODELS[...] ."""
    if model_exists(spec["name"]):
        return False
    invoke("createModel", modelName=spec["name"], inOrderFields=spec["fields"],
           css=spec.get("css", ""),
           cardTemplates=[{"Name": "Cartão 1", "Front": spec["front"], "Back": spec["back"]}])
    return True


def ensure_uid_field(model):
    """Melhor esforço: adiciona campo UID a um modelo existente (idempotência robusta).
    Requer AnkiConnect com 'modelFieldAdd'; se não houver, ignora silenciosamente."""
    try:
        if "UID" not in model_fields(model):
            invoke("modelFieldAdd", modelName=model, fieldName="UID", index=99)
            return True
    except AnkiError:
        pass
    return False


def uid_for(deck, key_text):
    return hashlib.sha1(f"{deck}\x1f{key_text}".encode("utf-8")).hexdigest()[:16]


def _escape(text):
    return text.replace("\\", "\\\\").replace('"', '\\"')


def upsert_note(deck, model, fields, tags=None, key_field=None):
    """Insere OU atualiza uma nota sem duplicar. Retorna ('added'|'updated', noteId)."""
    tags = tags or []
    key_field = key_field or next(iter(fields))
    key_text = fields.get(key_field, "")
    mfields = model_fields(model)

    if "UID" in mfields:
        uid = uid_for(deck, key_text)
        fields = dict(fields, UID=uid)
        found = invoke("findNotes", query=f'deck:"{deck}" UID:{uid}')
        if found:
            invoke("updateNoteFields", note={"id": found[0], "fields": fields})
            if tags:
                invoke("addTags", notes=found, tags=" ".join(tags))
            return ("updated", found[0])
        nid = invoke("addNote", note={"deckName": deck, "modelName": model, "fields": fields,
                                      "tags": tags, "options": {"allowDuplicate": False}})
        return ("added", nid)

    # sem UID -> dedup nativo pelo 1º campo
    try:
        nid = invoke("addNote", note={"deckName": deck, "modelName": model, "fields": fields,
                                      "tags": tags, "options": {"allowDuplicate": False}})
        return ("added", nid)
    except AnkiError:
        found = invoke("findNotes", query=f'deck:"{deck}" "{key_field}:{_escape(key_text)}"')
        if found:
            invoke("updateNoteFields", note={"id": found[0], "fields": fields})
            if tags:
                invoke("addTags", notes=found, tags=" ".join(tags))
            return ("updated", found[0])
        raise


def _write_fallback(batch, path="anki_fallback.jsonl"):
    with open(path, "w", encoding="utf-8") as f:
        for n in batch.get("notes", []):
            f.write(json.dumps(n, ensure_ascii=False) + "\n")
    return path


def publish_batch(batch, fallback_path="anki_fallback.jsonl"):
    """Publica um lote. Se o Anki estiver offline, grava fallback e não perde nada."""
    if not is_available():
        p = _write_fallback(batch, fallback_path)
        return {"ok": False, "reason": "anki_offline", "fallback": p,
                "n": len(batch.get("notes", []))}
    res = {"ok": True, "added": 0, "updated": 0, "errors": []}
    for n in batch.get("notes", []):
        try:
            ensure_deck(n["deck"])
            status, _ = upsert_note(n["deck"], n["model"], n["fields"],
                                    n.get("tags"), n.get("key_field"))
            res[status] += 1
        except AnkiError as e:
            res["errors"].append(str(e))
    if batch.get("sync"):
        try:
            invoke("sync")
            res["synced"] = True
        except AnkiError as e:
            res["synced"] = False
            res["errors"].append(f"sync: {e}")
    return res


# --- Note types canônicos (criados só se faltarem; incluem UID p/ idempotência) ---
CANONICAL_MODELS = {
    "flashcard": {
        "name": "Estudo Flashcard", "fields": ["Frente", "Verso", "Fonte", "UID"],
        "css": ".card{font-family:-apple-system,Arial;font-size:19px;text-align:center;color:#222}"
               ".fonte{color:#888;font-size:12px;margin-top:12px}"
               ".nightMode .card{color:#eee;background:#2b2b2b}.nightMode .fonte{color:#a6a6a6}",
        "front": "{{Frente}}",
        "back": "{{FrontSide}}<hr id=answer>{{Verso}}{{#Fonte}}<div class=fonte>{{Fonte}}</div>{{/Fonte}}",
    },
    "mcq": {
        "name": "Estudo MCQ (A-E)",
        "fields": ["Enunciado", "A", "B", "C", "D", "E", "Correta", "Comentário", "Fonte", "UID"],
        "css": ".card{font-family:-apple-system,Arial;font-size:17px;color:#222}"
               ".alt{margin:4px 0}.resp{font-weight:bold;margin-top:8px}.fonte{color:#888;font-size:12px}"
               ".nightMode .card{color:#eee;background:#2b2b2b}.nightMode .fonte{color:#a6a6a6}",
        "front": '<div class=enun>{{Enunciado}}</div><div class=alt>(A) {{A}}</div>'
                 '<div class=alt>(B) {{B}}</div><div class=alt>(C) {{C}}</div>'
                 '<div class=alt>(D) {{D}}</div>{{#E}}<div class=alt>(E) {{E}}</div>{{/E}}',
        "back": '{{FrontSide}}<hr id=answer><div class=resp>Resposta: <b>{{Correta}}</b></div>'
                '<div class=coment>{{Comentário}}</div>{{#Fonte}}<div class=fonte>{{Fonte}}</div>{{/Fonte}}',
    },
    "discursiva": {
        "name": "Estudo Discursiva", "fields": ["Enunciado", "Espelho", "Fonte", "UID"],
        "css": ".card{font-family:-apple-system,Arial;font-size:16px;color:#222;text-align:left}"
               ".fonte{color:#888;font-size:12px}"
               ".nightMode .card{color:#eee;background:#2b2b2b}.nightMode .fonte{color:#a6a6a6}",
        "front": "{{Enunciado}}",
        "back": "{{FrontSide}}<hr id=answer>{{Espelho}}{{#Fonte}}<div class=fonte>{{Fonte}}</div>{{/Fonte}}",
    },
}


def ensure_canonical_models():
    return {k: ensure_model(v) for k, v in CANONICAL_MODELS.items()}


if __name__ == "__main__":
    data = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 1 else json.load(sys.stdin)
    print(json.dumps(publish_batch(data), ensure_ascii=False, indent=2))

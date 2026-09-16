#!/usr/bin/env python3
"""Concurrent xAI hello probe: catalog + chat completions (+ multi-agent via responses).

Usage:
  XAI_API_KEY=... python3 xai_hello_probe.py
  # or with Hermes OAuth already in ~/.hermes/auth.json:
  python3 xai_hello_probe.py

Never prints the bearer token. Exit 0 always; failures are rows in the report.
"""
from __future__ import annotations

import concurrent.futures
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = os.environ.get("XAI_BASE_URL", "https://api.x.ai/v1").rstrip("/")
AUTH_PATH = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")) / "auth.json"


def load_token() -> str:
    env = os.environ.get("XAI_API_KEY") or os.environ.get("XAI_TOKEN")
    if env:
        return env.strip()
    if not AUTH_PATH.exists():
        raise SystemExit(f"No token: set XAI_API_KEY or create {AUTH_PATH}")
    auth = json.loads(AUTH_PATH.read_text())
    prov = (auth.get("providers") or {}).get("xai-oauth") or {}
    tokens = prov.get("tokens") or {}
    token = tokens.get("access_token") or tokens.get("token")
    if token:
        return token
    pool = (auth.get("credential_pool") or {}).get("xai-oauth") or []
    for entry in pool:
        t = entry.get("tokens") or entry
        token = t.get("access_token") or t.get("token") or entry.get("access_token")
        if token:
            return token
    raise SystemExit("No xai-oauth access_token found in auth.json")


def http_json(method: str, url: str, token: str, body: dict | None = None, timeout: float = 60.0):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "hermes-xai-hello-probe",
        },
        method=method,
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
            return True, resp.status, time.time() - t0, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        try:
            ej = json.loads(err)
            msg = ej.get("error", ej)
            if isinstance(msg, dict):
                msg = msg.get("message") or str(msg)
        except Exception:
            msg = err[:300]
        return False, e.code, time.time() - t0, {"error": str(msg)}
    except Exception as e:
        return False, type(e).__name__, time.time() - t0, {"error": str(e)[:300]}


def list_models(token: str) -> list[dict]:
    ok, status, _, payload = http_json("GET", f"{BASE}/models", token, timeout=30)
    if not ok:
        raise SystemExit(f"GET /models failed: {status} {payload}")
    return list(payload.get("data") or [])


def chat_hello(token: str, model: str, timeout: float = 60.0) -> dict:
    ok, status, lat, payload = http_json(
        "POST",
        f"{BASE}/chat/completions",
        token,
        {
            "model": model,
            "messages": [{"role": "user", "content": "Say hello in exactly 3 words."}],
            "max_tokens": 32,
            "temperature": 0,
        },
        timeout=timeout,
    )
    if ok:
        choice = (payload.get("choices") or [{}])[0]
        msg = choice.get("message") or {}
        text = (msg.get("content") or "").strip().replace("\n", " ")
        return {"model": model, "ok": True, "status": status, "latency_s": round(lat, 2), "text": text[:120], "api": "chat"}
    return {"model": model, "ok": False, "status": status, "latency_s": round(lat, 2), "text": str(payload.get("error", payload))[:200], "api": "chat"}


def responses_hello(token: str, model: str, timeout: float = 180.0) -> dict:
    ok, status, lat, payload = http_json(
        "POST",
        f"{BASE}/responses",
        token,
        {
            "model": model,
            "input": "Say hello in exactly 3 words.",
            "max_output_tokens": 64,
        },
        timeout=timeout,
    )
    if ok:
        text = (payload.get("output_text") or "").strip()
        if not text:
            chunks = []
            for item in payload.get("output") or []:
                if item.get("type") == "message":
                    for c in item.get("content") or []:
                        if c.get("type") in ("output_text", "text"):
                            chunks.append(c.get("text") or "")
            text = "".join(chunks).strip()
        return {"model": model, "ok": True, "status": status, "latency_s": round(lat, 2), "text": text[:120].replace("\n", " "), "api": "responses"}
    return {"model": model, "ok": False, "status": status, "latency_s": round(lat, 2), "text": str(payload.get("error", payload))[:200], "api": "responses"}


def main() -> int:
    token = load_token()
    models = list_models(token)
    print(f"catalog_count={len(models)} base={BASE}")
    text_ids = []
    non_text = []
    for m in models:
        mid = m.get("id") or ""
        if mid.startswith("grok-imagine") or "video" in mid or "image" in mid:
            non_text.append(mid)
        else:
            text_ids.append(mid)
            for a in m.get("aliases") or []:
                if a not in text_ids:
                    text_ids.append(a)

    # Always include multi-agent responses path explicitly
    multi = [m for m in text_ids if "multi-agent" in m]
    chat_targets = [m for m in text_ids if "multi-agent" not in m]

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(chat_hello, token, m) for m in chat_targets]
        futs += [ex.submit(responses_hello, token, m) for m in multi]
        for f in concurrent.futures.as_completed(futs):
            r = f.result()
            results.append(r)
            flag = "OK  " if r["ok"] else "FAIL"
            print(f"{flag} {r['model']:<40} api={r['api']:<9} status={r['status']} {r['latency_s']:>6}s  {r['text']}")

    print("\nNON_TEXT_SKIPPED:", ", ".join(non_text) or "(none)")
    ok = sum(1 for r in results if r["ok"])
    print(f"\nsummary ok={ok} fail={len(results) - ok} probed={len(results)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

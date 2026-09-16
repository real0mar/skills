# xAI live model probe

Use when the user asks which Grok/xAI models actually exist or respond.

## Auth token (never print)

Resolve in order:

1. `~/.hermes/auth.json` → `providers["xai-oauth"].tokens.access_token`
2. `credential_pool["xai-oauth"][*].tokens.access_token` (or entry-level `access_token`)
3. env `XAI_API_KEY`

Base URL: `https://api.x.ai/v1` (Hermes default for xAI / xAI OAuth).

## Catalog

```bash
curl -sS -H "Authorization: Bearer $TOKEN" https://api.x.ai/v1/models
```

Parse `data[].id` and `data[].aliases`. Expect a mix of text, image, and video IDs.

Canonical text families observed (verify live; catalogs change):

- `grok-4.5` — aliases often include `grok-4.5-latest`, `grok-build-latest`
- `grok-4.3` — aliases often include `grok-4.3-latest`, `grok-latest`
- `grok-4.20-0309-reasoning` — aliases often include `grok-4.20`, `grok-4.20-reasoning`
- `grok-4.20-0309-non-reasoning` — aliases often include `grok-4.20-non-reasoning`
- `grok-4.20-multi-agent-0309` — aliases often include `grok-4.20-multi-agent`
- `grok-build-0.1` — aliases often include `grok-code-fast`, `grok-code-fast-1`

Non-text (skip for hello probes): `grok-imagine-image*`, `grok-imagine-video*`.

## Text hello (chat completions)

```http
POST /v1/chat/completions
Authorization: Bearer <token>
Content-Type: application/json

{
  "model": "<id>",
  "messages": [{"role": "user", "content": "Say hello in exactly 3 words."}],
  "max_tokens": 32,
  "temperature": 0
}
```

Parallelize (~6 workers). Timeouts: ~60s normal, longer for heavy reasoning.

## Multi-agent requires Responses API

`grok-4.20-multi-agent*` returns HTTP 400 on chat completions:

```text
Multi Agent requests are not allowed on chat completions
```

Probe with:

```http
POST /v1/responses
{
  "model": "grok-4.20-multi-agent-0309",
  "input": "Say hello in exactly 3 words.",
  "max_output_tokens": 64
}
```

Extract text from `output[]` message content blocks (`output_text` / `text`) or `output_text`.

Hermes xAI paths generally use Responses-style transport, so multi-agent can still be usable inside Hermes even when a naive chat-completions probe fails.

## Reasoning effort (Grok 4.5)

Supported: `low` | `medium` | `high` (API default **high** if omitted).
Cannot disable. `none` is rejected.

## Retired names

Hermes maps several old IDs → `grok-4.3` in `hermes_cli/xai_retirement.py` (e.g. `grok-4-0709`, `grok-4-fast-*`, `grok-code-fast-1`, `grok-3`).

Live API may still accept some retired names as aliases. For config, prefer **canonical current IDs** from `/v1/models`.

Names that hard-failed in a 2026-07 probe (re-check): `grok-2`, `grok-beta`.

## Reporting format

Keep it terminal-scannable:

- table or bullets: model, ok/fail, status, latency, short reply
- separate sections: working canonical, working aliases/redirects, dead, non-text
- recommend canonical IDs for config

## Script

See `scripts/xai_hello_probe.py` for a re-runnable concurrent probe.

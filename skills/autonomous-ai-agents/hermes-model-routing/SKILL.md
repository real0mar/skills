---
name: hermes-model-routing
description: "Use when configuring Hermes primary models, fallback chains, reasoning effort, or live-probing provider model catalogs (xAI/Codex/Nous)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, models, providers, fallbacks, reasoning-effort, xai, openai-codex, routing]
    related_skills: [hermes-agent, hermes-feature-triage, provider-usage-auditing, codex]
---

# Hermes Model Routing

Class-level skill for choosing, verifying, and changing which model Hermes uses — primary, fallback chain, reasoning effort, and live provider catalog checks.

Protected hub skill `hermes-agent` owns general setup. This skill owns the model-routing subclass: commands, config shape, provider-specific effort knobs, and probe workflows.

## When to load

- "what model are we using"
- set / reorder fallbacks
- switch primary provider (Codex, xAI OAuth, Nous, OpenRouter, …)
- reasoning / thinking level for a model family
- "which models from provider X actually work"

## Quick status

```bash
hermes status                 # Model + Provider lines
hermes config get model       # default + provider (+ base_url if set)
hermes fallback list          # primary + ordered fallback chain
```

Session footer/system metadata may still show the *session-start* model after a config change. Config changes apply to **new sessions** (`/new`, new gateway chat, new CLI). In-session switch: `/model <name>` (add `--global` to also pin default when supported).

## Primary model

Interactive picker (OAuth, keys, catalog):

```bash
hermes model
```

Non-interactive pin (prefer `hermes config set`, not hand-edited YAML for scalar keys):

```bash
hermes config set model.default gpt-5.6-sol
hermes config set model.provider openai-codex
hermes config unset model.base_url    # drop stale endpoint when leaving xAI/custom
```

Common pairings observed:

| Intent | provider | model |
|--------|----------|--------|
| Codex GPT-5.6 Sol | `openai-codex` | `gpt-5.6-sol` (also terra/luna, `*-pro`) |
| Grok SuperGrok OAuth | `xai-oauth` | `grok-4.5` |
| Nous Portal | `nous` | portal slug e.g. `deepseek/deepseek-v4-flash` |
| OpenRouter | `openrouter` | `vendor/model` slug |

Codex family IDs live in installed source `hermes_cli/codex_models.py` — check there before inventing slugs.

## Fallback chain

Yes — multi-entry ordered fallbacks are first-class.

```bash
hermes fallback list
hermes fallback add       # interactive picker (same as hermes model)
hermes fallback remove
hermes fallback clear
```

Config shape (`~/.hermes/config.yaml` top-level):

```yaml
fallback_providers:
  - provider: xai-oauth
    model: grok-4.5
  - provider: nous
    model: deepseek/deepseek-v4-flash
```

Each entry needs both `provider` and `model`. Custom endpoints may add `base_url` + `key_env`.

`hermes fallback add/remove` are interactive-only; for non-interactive multi-entry writes, set `fallback_providers` via a careful YAML update (documented path) then verify with `hermes fallback list`. Prefer not rewriting the whole config file if a targeted edit is enough.

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers

### Fallback behavior (do not mis-sell)

- Triggers: rate limit, 5xx after retries, auth 401/403, 404, repeated invalid responses.
- **Turn-scoped**: each new user message starts on primary again; within a turn walks the chain.
- Swapping models resets prompt cache → full-history re-read cost on the next request.
- Subagents/cron inherit the configured chain unless overridden.
- No env-var override for the primary fallback chain — config only.

## Reasoning effort

Global:

```bash
hermes config set agent.reasoning_effort medium
```

Hermes-valid levels (parser): `none|minimal|low|medium|high|xhigh|max|ultra` — **provider/model may reject some**.

### Grok 4.5 (xAI)

API-supported: **`low` | `medium` | `high`** only.
- Default if omitted: **high**
- Reasoning **cannot be disabled** (`none` is rejected)
- Wire forms: chat `reasoning_effort`, Responses `reasoning.effort`

Docs: https://docs.x.ai/developers/model-capabilities/text/reasoning

### Codex / OpenAI reasoning models

Often accept a wider set including `minimal` and `xhigh` depending on model — verify against current OpenAI/Codex docs when user asks for an exotic level.

### Per-model overrides

If present in config schema for this install, prefer `agent` per-model override keys from `cli-config.yaml.example` over inventing new keys. Always `hermes config get agent` / example file before asserting.

## Live provider model probes

When the user doubts a catalog ("do all these models exist?"), **probe the live API** — do not answer from memory or stale Hermes pickers alone.

### xAI (API key or OAuth)

1. Resolve token from `~/.hermes/auth.json` (`providers.xai-oauth.tokens.access_token` or `credential_pool.xai-oauth`) or `XAI_API_KEY`. Never print the token.
2. `GET https://api.x.ai/v1/models` → canonical IDs + aliases.
3. Text hello probe via `POST /v1/chat/completions` with a tiny prompt and low `max_tokens`.
4. **Multi-agent** (`grok-4.20-multi-agent*`) fails on chat completions (`Multi Agent requests are not allowed on chat completions`). Probe those on `POST /v1/responses` instead.
5. Image/video IDs (`grok-imagine-*`) are not text chat — skip or use their media APIs.
6. Some retired names may still answer (aliases/redirects) even when absent from `/v1/models`. Hermes `hermes_cli/xai_retirement.py` may still want them mapped to current IDs — prefer canonical current IDs in config.

Reusable notes + script outline: `references/xai-live-model-probe.md`.

### General probe rules

- Parallelize with a small worker pool; longer timeout for multi-agent / heavy reasoning.
- Report: ok/fail, HTTP status, latency, short reply snippet, and whether the ID is canonical vs alias.
- Prefer canonical IDs from `/v1/models` when writing config.
- Redact tokens and account identifiers always.

## Workflow checklist

1. `hermes status` + `hermes fallback list` (current truth).
2. Confirm credentials: `hermes status` Auth Providers / `hermes auth`.
3. Set primary with `hermes config set` or `hermes model`.
4. Clear stale `model.base_url` when changing provider families.
5. Write `fallback_providers` ordered list; verify with `hermes fallback list`.
6. Set `agent.reasoning_effort` appropriate for the **primary** (and note fallback model constraints).
7. Tell the user: **new session required** for default primary change; this open session may still be on the old model.
8. If existence is questioned, live-probe before recommending a model ID.

## Pitfalls

- Answering "current model" from conversation kickoff text after a config change without re-running `hermes status`.
- Leaving `model.base_url: https://api.x.ai/v1` after switching to Codex/Nous.
- Assuming `hermes fallback add` accepts non-interactive CLI args — it does not.
- Claiming Grok 4.5 supports `none` / `xhigh` — it does not.
- Probing multi-agent only via chat completions and concluding the model is dead.
- Treating Hermes retirement maps as "API hard-deleted"; verify live.
- Hand-editing large swaths of `config.yaml` and risking YAML corruption — prefer `hermes config set` for scalars.
- Dumping raw `auth.json` or bearer tokens into the user-visible reply.

## Related

- `hermes-agent` — general Hermes config/setup (protected; load for command index).
- `hermes-feature-triage` — verify whether a Hermes feature exists before asserting.
- `provider-usage-auditing` — quota/remaining limits (Codex WHAM, etc.), not model routing.
- `codex` — standalone Codex CLI delegation, not Hermes `openai-codex` provider config.

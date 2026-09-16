---
name: provider-usage-auditing
description: "Audit LLM provider usage/quota from CLI-accessible local telemetry and provider-specific authenticated endpoints."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [usage, quota, rate-limits, providers, codex, openai, telemetry, audit]
    related_skills: [hermes-agent, codex]
---

# Provider Usage Auditing

Use this skill when the user asks how much model/provider usage they have left, what an interactive status command is showing, whether quota is nearly exhausted, or how to preflight long agent runs against provider limits.

## Principles

1. Distinguish local telemetry from official quota.
   - Local telemetry (`hermes insights`, session DB token counts, CLI history files) is useful for trend analysis.
   - Official remaining allowance comes from the provider's authenticated usage/quota endpoint when one is available.
   - Do not present local token totals as the provider's billing/quota truth.

2. Prefer non-interactive, scriptable checks.
   - Interactive TUI commands such as Codex `/status` or `/statusline` are useful clues, but a future agent should look for the underlying API/request path when the user needs automation.
   - If a provider lacks a supported command, inspect source/docs or use documented/observed authenticated endpoints carefully and label them as internal/undocumented when appropriate.

3. Redact account identity and secrets.
   - Never print access tokens, refresh tokens, cookies, raw auth files, account emails, or user IDs in the final answer unless explicitly needed and user-approved.
   - It is fine to report plan tier, remaining percentages, reset times, and whether a limit is reached.

4. Report reset times clearly.
   - Include percent used and/or remaining.
   - Include reset timestamp with timezone.
   - Include relative time-to-reset when possible.

## Workflow

1. Identify active provider/model and relevant credential store.
   - Hermes provider config is usually in `~/.hermes/config.yaml`.
   - Hermes OAuth/API-key pools are usually in `~/.hermes/auth.json`.
   - Standalone CLIs may have separate stores, e.g. `~/.codex/auth.json` for Codex CLI.

2. Gather local telemetry.
   - For Hermes, run `hermes insights --days N` to see local sessions, token totals, model mix, tool use, and loaded skills.
   - Treat this as local accounting only.

3. Find the official quota source.
   - Check provider docs/source when the UI/TUI has a status display.
   - Search for statusline/status/usage/rate-limit code paths, not just CLI help.

4. Query official usage if credentials are available and the user asked for the answer.
   - Use the credential already configured for the provider.
   - Do not log or display secret-bearing headers.
   - Save raw response only in a private temp file if needed for parsing; do not persist secrets.

5. Summarize concisely.
   - State source: local telemetry vs provider endpoint.
   - Give current remaining/used and reset times.
   - Call out uncertainty if endpoint is undocumented/internal.

## OpenAI Codex / ChatGPT Codex usage endpoint

Detailed session notes live in `references/openai-codex-usage-endpoint.md`.
For threshold-based monitoring / Telegram watchdogs, see `references/codex-limit-watchdog.md`.

When Hermes is using the `openai-codex` provider with ChatGPT OAuth, Codex quota is exposed through the same backend family used by Codex CLI statusline rate-limit items.

Source-code path observed in OpenAI Codex CLI:

- UI/app-server request: `account/rateLimits/read`
- Account processor calls `get_account_rate_limits_response()`
- Backend client calls `get_rate_limits_with_reset_credits()`
- That calls `GET {base}/wham/usage` for ChatGPT-style base URLs

For ChatGPT-hosted Codex, the normalized base is:

```text
https://chatgpt.com/backend-api
```

So the effective endpoint is:

```text
GET https://chatgpt.com/backend-api/wham/usage
Authorization: Bearer <access_token>
```

Important fields commonly returned:

- `plan_type`
- `rate_limit.limit_reached`
- `rate_limit.primary_window.used_percent`
- `rate_limit.primary_window.limit_window_seconds` (typically 18,000 seconds / 5 hours)
- `rate_limit.primary_window.reset_at` (Unix timestamp)
- `rate_limit.secondary_window.used_percent`
- `rate_limit.secondary_window.limit_window_seconds` (typically 604,800 seconds / weekly)
- `rate_limit.secondary_window.reset_at` (Unix timestamp)
- `rate_limit_reset_credits.available_count`

Interpretation:

- Primary window is the short rolling window, usually the 5-hour Codex limit.
- Secondary window is the weekly limit.
- Remaining percent is `100 - used_percent`.
- Convert `reset_at` from Unix seconds to local or UTC time and include the timezone.

Pitfalls:

- `codex --help` may not list a non-interactive quota command even though the TUI/statusline can show quota.
- Codex session JSONL `rate_limits` fields may be `null`; do not rely on local rollout files as the authoritative source when the usage endpoint is available.
- `https://chatgpt.com/backend-api/codex/usage` is not the same as the ChatGPT WHAM path and may be rejected; for ChatGPT OAuth use `/backend-api/wham/usage`.
- The endpoint is internal/undocumented behavior and may change; describe it as observed from current Codex source, not a stable public API contract.

## Example Python probe pattern

Use this pattern only after locating a valid access token in the configured credential store. Redact all identity fields before showing output.

```python
import json, urllib.request
from datetime import datetime, timezone

url = "https://chatgpt.com/backend-api/wham/usage"
req = urllib.request.Request(url, headers={
    "Authorization": f"Bearer {access_token}",
    "User-Agent": "provider-usage-audit",
})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.load(r)

rl = data["rate_limit"]
for label, window in [("5h", rl["primary_window"]), ("weekly", rl["secondary_window"])] :
    used = window["used_percent"]
    reset = datetime.fromtimestamp(window["reset_at"], tz=timezone.utc)
    print(label, "used", used, "remaining", 100 - used, "reset_utc", reset.isoformat())
```

## Nous Portal and combined spend audits

For questions like “how much did we spend today, everything combined?”, load `references/nous-portal-and-daily-spend.md`. It documents live Nous billing helpers, OpenRouter checks, subscription-vs-metered separation, timezone handling, and why billing-period counters or cross-midnight session aggregates must not be presented as exact daily spend.

## Relationship to other skills

- `hermes-agent` covers Hermes configuration, auth, `hermes insights`, and provider setup.
- `codex` covers using the standalone Codex CLI for coding tasks.
- This skill covers the cross-provider class of quota/usage auditing and the distinction between local telemetry and provider-authoritative limits.

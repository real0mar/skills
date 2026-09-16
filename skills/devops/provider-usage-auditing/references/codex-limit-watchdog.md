# Codex usage watchdog pattern

Use when the user wants to keep an eye on Codex/ChatGPT OAuth limits without opening the Codex TUI.

## Source of truth

For ChatGPT-backed Codex OAuth, query:

```text
GET https://chatgpt.com/backend-api/wham/usage
Authorization: Bearer <Codex access token>
```

Do not print or persist access tokens, account emails, user IDs, or raw credential files. Report only plan, used/remaining percentages, reset times, and whether the limit is reached.

## Useful alert shape

For a gateway-first Hermes install, prefer a script-only cron/watchdog that stays quiet unless a threshold is crossed. Example thresholds:

- 5h primary window >= 80% used: warning
- 5h primary window >= 95% used or `limit_reached=true`: urgent
- Weekly secondary window >= 80% used: warning

The script should print a short message only when alerting; empty stdout means silent when used with `cronjob(no_agent=True)`.

Suggested message format:

```text
Codex usage: 5h window 87% used / 13% left; resets 06:22 UTC (~1.4h). Weekly 10% used. Limit reached: no.
```

## Delivery note

In CLI-only Hermes sessions, cron default/origin delivery is local-only and will not actively notify the terminal. For a Telegram-first VPS, create the watchdog with explicit gateway delivery such as `deliver='telegram:<chat_id>'` or another configured platform target.

## Implementation notes

- Reuse configured Hermes/Codex OAuth credentials when available.
- Treat the WHAM endpoint as internal/observed, not a stable public API.
- If multiple access tokens are present, try them without printing source identities; stop at the first successful usage response.
- Include reset time both absolute UTC and relative when possible.

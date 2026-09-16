# OpenAI Codex usage/rate-limit endpoint notes

This reference captures a session discovery about how Codex CLI obtains quota/rate-limit data and how Hermes can query it when `openai-codex` OAuth credentials are configured.

## Observed source path

In current OpenAI Codex CLI source, the quota/statusline path is:

- `account/rateLimits/read`
- `get_account_rate_limits_response()`
- `BackendClient::get_rate_limits_with_reset_credits()`
- `get_rate_limit_status()`
- `GET {base}/wham/usage` for ChatGPT-style base URLs

The backend client normalizes `https://chatgpt.com` / `https://chat.openai.com` bases to include `/backend-api`; a base containing `/backend-api` uses the ChatGPT/WHAM path style.

Effective ChatGPT OAuth endpoint:

```text
GET https://chatgpt.com/backend-api/wham/usage
Authorization: Bearer <access_token>
```

For Codex API-style bases, source maps to:

```text
GET {base}/api/codex/usage
```

## Response shape of interest

A successful ChatGPT OAuth response may include:

```json
{
  "plan_type": "plus",
  "rate_limit": {
    "allowed": true,
    "limit_reached": false,
    "primary_window": {
      "used_percent": 46,
      "limit_window_seconds": 18000,
      "reset_after_seconds": 15504,
      "reset_at": 1782714139
    },
    "secondary_window": {
      "used_percent": 7,
      "limit_window_seconds": 604800,
      "reset_after_seconds": 602304,
      "reset_at": 1783300939
    }
  },
  "rate_limit_reset_credits": {
    "available_count": 3
  }
}
```

Redact `user_id`, `account_id`, `email`, tokens, cookies, and any other account identifiers before presenting results.

## Interpretation

- `primary_window` is the short rolling window, commonly 5 hours.
- `secondary_window` is the weekly window.
- Remaining percent = `100 - used_percent`.
- `reset_at` is Unix seconds.
- `rate_limit_reset_credits.available_count` may indicate available reset credits.

## Pitfalls

- Codex `/statusline` can show quota even when `codex --help` has no non-interactive usage/quota command.
- Local Codex rollout JSONL may contain `rate_limits: null`; do not treat that as proof the quota cannot be queried.
- For ChatGPT OAuth, `https://chatgpt.com/backend-api/codex/usage` and double-prefixed Codex paths may return 403. Use `/backend-api/wham/usage`.
- This is an observed/internal endpoint, not a stable public API contract. Re-check Codex source if it fails.

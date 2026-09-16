# Nous Portal and combined daily-spend auditing

## Live Nous account and billing sources

Current Hermes releases expose authenticated Nous Portal data through existing OAuth credentials:

- `hermes_cli.nous_account.get_nous_portal_account_info(force_fresh=True)` calls `GET /api/oauth/account` and returns subscription state, purchased/subscription credits remaining, total usable credits, and `paid_service_access_info`.
- `hermes_cli.nous_billing.get_billing_state()` calls `GET /api/billing/state` and returns `balanceUsd` plus `monthlyCap.spentThisMonthUsd` when applicable.
- `hermes_cli.nous_billing.get_subscription_state()` calls `GET /api/billing/subscription` and returns plan/cycle details.
- `/credits`, `/usage`, and `/billing` are user-facing Hermes surfaces over these APIs.

Use the helper modules rather than hand-parsing `auth.json`; they refresh OAuth and normalize account state. Never print organisation IDs, emails, payment details, tokens, or raw account payloads.

## Critical time-scope rule

Do not call a balance, `member_spend_usd`, or `spentThisMonthUsd` value “today’s spend” unless the provider explicitly defines it as daily. These are current-balance or billing-period counters. Exact daily spend requires one of:

1. a provider daily-usage/history endpoint, or
2. a persisted balance/counter snapshot at the start of the requested day.

Without either, report a bound only. For example, a month-to-date spend is an upper bound on today’s spend, not today’s exact value. State the timezone and boundary (`America/Los_Angeles` vs UTC).

## Hermes telemetry caveats

`session_model_usage` is useful for model billing mode and cost fields:

- `billing_mode=subscription_included`, `cost_status=included` means zero incremental model charge.
- `actual_cost_usd` is preferable to `estimated_cost_usd` when present.
- Rows aggregate across the whole session. Filtering rows by `first_seen`/`last_seen` can overcount a session crossing midnight; it is not per-request daily accounting.
- Hermes session telemetry does not currently provide authoritative per-call Nous Tool Gateway cost. Tool-call counts plus public rates are only estimates because browser minutes/bandwidth and Firecrawl credits vary.

## Combined-provider checklist

For “everything combined,” separate and sum only compatible scopes:

1. Hermes model rows and billing modes.
2. OpenAI Codex/ChatGPT OAuth quota (`/backend-api/wham/usage`): quota, not dollar spend.
3. OpenRouter: `GET /api/v1/key` for daily/weekly/monthly key usage and `GET /api/v1/credits` for all-time balance/usage.
4. Nous Portal balance/billing counters and Tool Gateway charges.
5. Other fallback providers only if telemetry shows calls actually reached them.
6. Fixed subscription fees separately from incremental metered spend; do not silently amortize monthly fees into a daily number.

A good final answer gives: exact verified charges, subscription-included usage, current balances, the requested timezone, and any irreducible bound/uncertainty.
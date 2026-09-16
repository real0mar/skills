---
name: web-data-csv-reports
description: "Build verified CSV reports from web/API data and deliver them through Hermes messaging."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, data-extraction, csv, api, reporting, messaging]
---

# Web Data CSV Reports

Use this skill when the user asks for a CSV/export/report built from web data, APIs, scraped pages, rankings, counts, or time-windowed data, especially when they want the artifact delivered to Telegram/Discord/Slack/etc.

## Operating pattern

1. Clarify only if the target dataset or delivery destination is genuinely ambiguous. Otherwise choose the obvious default and act.
2. Establish the exact time window with a real clock command when the request is relative (e.g. "last 365 days", "this week"). Record UTC start/end in metadata.
3. Prefer official or quasi-official APIs over scraping when available. Inspect API limits before bulk collection. For market/job-count reports, prefer current indexed-job APIs or SSR data over ad-hoc web-search snippets; verify that the returned page/API echoes the intended filters before trusting counts.
4. If collection requires an authenticated browser session, treat exported cookies exactly like passwords:
   - prefer a site-scoped Netscape `cookies.txt` rather than account credentials,
   - never print cookie values, account identifiers, or request headers containing them,
   - load them with `http.cookiejar.MozillaCookieJar`,
   - keep the cookie file outside the deliverable directory,
   - delete the upload and clear any imported browser cookies after collection,
   - advise the user to revoke the session after delivery.
5. Write a deterministic script that:
   - retries transient HTTP failures and 429s with bounded exponential backoff and jitter,
   - logs page-level progress without logging credentials,
   - preserves provenance fields,
   - paginates until the source reports no next page,
   - deduplicates stable IDs/usernames while preserving source order,
   - writes a CSV with explicit column names,
   - writes JSON or a metadata sidecar with source, time window, normalization rules, displayed totals, retrieved totals, and API-call counts.
6. Verify the artifact before delivery:
   - row count matches the requested shape when the source exposes every record,
   - file exists and has nonzero size,
   - CSV and JSON counts agree,
   - stable IDs/usernames are unique,
   - first rows look plausible,
   - any known API cap was handled, not silently truncated,
   - when a displayed count differs from retrievable records, repeat a full pagination pass or use an independent endpoint before reporting the discrepancy plainly.
7. Deliver via `hermes send` when the user asks for a messaging-platform delivery. For attachments, put `MEDIA:/absolute/path/to/file.csv` in the message body.
8. Final response should be concise: provide the artifact, verification facts, method, any source-count discrepancy, and credential-cleanup status.

## CSV quality defaults

- Include rank/count/share fields for ranking reports.
- Include raw aggregation fields that help the user interpret dominance, such as total points/comments if available.
- Use stable, lowercase, snake_case headers.
- Avoid over-normalizing unless the user asked: document normalization choices clearly.
- Keep local copies under `/home/ubuntu/outputs/` or a task-specific output directory, not `/tmp` or the credential/cache directory.

## Pitfalls

- A 429 can be endpoint-specific. Probe the exact collection endpoint with the authenticated session before concluding the whole workflow is blocked; use bounded retries rather than tight loops.
- Relationship-list counters may include unavailable records. Never invent rows to match a displayed total; verify with a second full pass and report displayed versus retrievable counts.
- Cookie exports are live credentials. Do not log them, copy them into output artifacts, or retain them after the verified export.
- Search APIs often report large `nbHits` but cap retrievable pages/results. Do not trust `nbHits` alone; page through or split the time range until each query is below the retrievable cap.
- If using relative time windows, do not compute dates mentally. Use a tool and include exact UTC bounds in metadata.
- If a platform send command supports home-channel shorthand, verify targets with `hermes send --list <platform>` when practical.
- Do not promise CLI-origin cron delivery; CLI cron output is local-only unless a gateway target is specified.

## References

- `references/authenticated-social-relationship-exports.md` — secure cookie intake, cursor pagination, repeated-pass verification, count discrepancies, and cleanup for authenticated social-platform exports.
- `references/hacker-news-algolia-domain-counts.md` — HN Algolia pattern for capped time-window collection and domain aggregation.
- `references/hiringcafe-ssr-job-market-counts.md` — HiringCafe Next.js SSR pattern for current job-market counts by salary threshold, metro radius, and remote category.

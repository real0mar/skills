---
name: web-release-monitoring
description: "Use when monitoring an official site for a price, release, availability, or other one-time event."
version: 1.0.0
---

# Web Release Monitoring

Build quiet, deterministic monitors for one-time events such as a product price appearing, preorders opening, specifications being published, or an official release becoming available.

## Choose the Monitoring Strategy

1. **RSS/feed available:** use a feed monitor and filter article titles/content.
2. **Structured endpoint available:** prefer product JSON, sitemap, API, or embedded structured data.
3. **Static official page:** fetch and parse narrowly around event-specific text.
4. **Dynamic or social-only announcement:** use an agent-driven scheduled research job only when deterministic extraction is insufficient.

Prefer official first-party sources. A search-engine result or social post can reveal an event, but verify against the official source before alerting whenever possible.

## Deterministic Silent-Watcher Pattern

For recurring checks where nothing should be sent until the condition is met:

- Use a script-only/no-agent scheduled job.
- Print **nothing** while the condition is false.
- Print the exact user-facing alert when the condition becomes true.
- Persist a notified-state file so a one-time event does not alert repeatedly.
- Treat transient fetch/parse errors as retryable and silent, unless the user explicitly asks for monitor-health alerts.
- Include the detected value and official URL in the alert.

See `templates/one-shot-web-watcher.py` for a reusable skeleton.

## Detection Design

- Search structured product entries by stable title/handle identifiers before scraping page text.
- Reject placeholder or zero prices.
- When scraping HTML, remove scripts/styles and require event language near the extracted value—for example `price`, `preorder`, or `order now` near a nonzero currency amount.
- Avoid broad page-wide currency matching because carts, unrelated products, and footer metadata create false positives.
- Combine independent official signals with `structured_result OR page_result`, ordered from most reliable to least reliable.

## Verification

Before scheduling:

1. Run the watcher manually against the current page.
2. Confirm exit status is zero.
3. Confirm stdout is empty while the event is absent.
4. Confirm no notified-state file was created.
5. Test the positive branch with a local fixture or injected parser input when practical.
6. Confirm delivery targets the user’s actual chat/channel rather than local-only output.

## Pitfalls

- Do not use an LLM job for a condition that can be expressed deterministically; it costs more and may emit unwanted “nothing yet” messages.
- Do not alert on search snippets alone when the official page can be checked.
- Do not swallow permanent parser breakage forever. For important long-running monitors, add a separate low-frequency health check after repeated failures.
- Do not hardcode session-specific absolute script paths into scheduler configuration when the scheduler expects paths relative to its scripts directory.
- Do not mark the event notified before the alert text has been constructed successfully.

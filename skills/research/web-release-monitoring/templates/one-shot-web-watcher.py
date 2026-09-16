#!/usr/bin/env python3
"""One-shot official-web event watcher. Silent until detection, then alerts once."""

import json
import urllib.request
from pathlib import Path

EVENT_NAME = "Example product event"
OFFICIAL_URL = "https://example.com/product"
STATE = Path.home() / ".local/share/agent-skills" / "cron" / "state" / "example-event-notified.json"
USER_AGENT = "Mozilla/5.0 (compatible; release-watch/1.0)"


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", "ignore")


def detect() -> str | None:
    """Return a concise detected value, or None while the event is absent.

    Prefer parsing an official JSON/API endpoint here. If HTML parsing is
    necessary, remove scripts/styles and match narrowly around event-specific
    language. Never treat unrelated cart/footer values as a detection.
    """
    body = fetch(OFFICIAL_URL)
    marker = "REPLACE_WITH_STABLE_EVENT_MARKER"
    if marker in body:
        return marker
    return None


def main() -> None:
    if STATE.exists():
        return

    value = detect()
    if value is None:
        return

    message = f"{EVENT_NAME} is now available: {value}\n{OFFICIAL_URL}"
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        json.dumps({"event": EVENT_NAME, "value": value, "url": OFFICIAL_URL}),
        encoding="utf-8",
    )
    print(message)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Silent retry on the next tick. For critical monitors, pair this with a
        # separate repeated-failure health check rather than noisy per-tick errors.
        pass

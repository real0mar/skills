# Authenticated Instagram-style following export

Use this note for public relationship-list exports that require a logged-in browser session. Endpoint names and query identifiers are volatile; discover and validate them at runtime rather than treating the examples as permanent API contracts.

## Credential intake

1. Ask for a site-scoped Netscape `cookies.txt`, not a password. For Chrome, the open-source **Get cookies.txt LOCALLY** extension by `kairi003` can export Netscape format; verify the exact store listing rather than recommending similarly named extensions.
2. Warn that the file is equivalent to a temporary login credential.
3. Parse with `http.cookiejar.MozillaCookieJar`; do not display cookie values in logs or final responses.
4. Keep credentials in the upload/cache location and outputs under `/home/ubuntu/outputs/<task>/`.

## Collection pattern

- Resolve the target's numeric ID from public profile bootstrap data or an authenticated profile endpoint.
- Prefer the authenticated relationship GraphQL endpoint used by the web client. A profile-info endpoint may be rate-limited independently while the relationship query still succeeds, so probe the exact required endpoint before concluding collection is blocked.
- Send browser-like headers, the platform web app ID when required, and a target-profile Referer.
- Cursor-paginate using `page_info.has_next_page` and `end_cursor` until exhausted.
- Sleep a few seconds with jitter between pages; retry 429/5xx with bounded exponential backoff.
- Save username, full name, privacy/verification flags, and canonical profile URL when available.
- Deduplicate by username or stable numeric ID while preserving returned order.

## Verification pattern

- Compare the displayed aggregate count with retrieved edge count and unique output count.
- Run a second complete pagination pass and union by stable key when the counts differ.
- If both complete passes return the same smaller set, report both numbers. Disabled, deleted, restricted, or otherwise unavailable accounts can remain in the displayed counter without appearing as retrievable nodes; do not fabricate rows to force equality.
- Verify CSV/JSON parse successfully, counts agree, keys are unique, and files are non-empty.

## Cleanup

- Delete the uploaded cookie file after collection.
- Clear cookies imported into any automation browser.
- Tell the user to revoke the exported session in the platform's login/security settings.
- Do not include cookies, session IDs, email addresses, or the authenticated account identity in artifacts or summaries.

---
name: dynamic-web-catalog-research
description: "Use when extracting current catalogs from JavaScript apps."
version: 1.0.0
metadata:
  hermes:
    tags: [research, javascript, spa, api, catalogs, recommendations]
    related_skills: [blocked-page-recovery, grounded-citations]
---

# Dynamic Web Catalog Research

Use this skill when the user asks what is available **right now** in a web-backed catalog—entertainment, products, events, transport amenities, menus, or similar—and the public page is a JavaScript application whose initial HTML contains little or no data.

The objective is not merely to recover titles. Produce a dated, scope-aware catalog and turn it into a practical answer grounded in the user's constraints or tastes.

## Workflow

1. **Define freshness and scope**
   - Resolve the current date with a tool.
   - Distinguish network-wide, regional, device-specific, route-specific, account-specific, and inventory-specific availability.
   - Use the user's exact date, route, model, venue, or device when supplied; do not silently downgrade a specific question to a global catalog.

2. **Inspect the public source directly**
   - Fetch the canonical page before searching secondary sources.
   - If it is an app shell, enumerate its environment scripts, main bundle, module chunks, and configuration files.
   - Prefer current first-party data over search snippets, old listicles, or archives.

3. **Recover the read-only data surface**
   - Search client bundles for API base URLs, `/api/`, `/graphql`, `.json`, `catalog`, `items`, `programs`, `search`, pagination, date parameters, and public application/host identifiers.
   - Reproduce only anonymous/public browser requests. A short-lived anonymous token may be used if the site's own client obtains it without user credentials.
   - Never bypass user authentication, reuse private cookies, probe write endpoints, or expose tokens in output.

4. **Query narrowly, then expand if results look incomplete**
   - Preserve date, locale, content-system/platform, category, pagination, and filtering parameters explicitly.
   - If a count is suspiciously small, inspect service/program metadata, section relationships, pagination, and hidden content-system filters before accepting it.
   - Retrieve item details where summaries omit nested fields such as duration, year, genres, compatibility, or synopsis.

5. **Verify programmatically**
   - Parse, deduplicate, count, and sort in code.
   - Confirm the active program or effective date covers the requested date.
   - Cross-check declared totals against enumerated items.
   - Treat a successful app-shell fetch or HTTP 200 as insufficient verification.

6. **Personalize with explicit evidence**
   - Build a compact taste/constraint model from repeated user signals, not a single keyword.
   - Rank recommendations by overlap and quality, not merely by literal title/genre matches.
   - Give one decisive first choice, a short ranked list, and a practical sequence when time allows multiple selections.
   - Use spoiler-free, title-specific reasons tied to both the catalog metadata and the user's stated preferences.

7. **State confidence and residual scope limits**
   - Cite the public front-end page and label API-derived data as a live first-party catalog result.
   - If per-device, per-flight, per-store, or account-level verification was unavailable, say so plainly and tell the user how to confirm on the actual interface.
   - Never claim exact availability from a broad catalog when compatibility metadata only suggests it.

## Output pattern

- **Start with:** “Choose **X** first.”
- **Then:** 3–7 ranked alternatives with runtime/price/other decision-critical metadata.
- **Optional:** a double feature, basket, itinerary, or fallback sequence.
- **End with:** one concise provenance/scope note.

## Quality checks

- [ ] Canonical first-party source inspected.
- [ ] Effective date/program verified.
- [ ] Requested scope distinguished from broader catalog scope.
- [ ] Counts and deduplication checked in code.
- [ ] No tokens, account identifiers, or private headers exposed.
- [ ] Recommendation order reflects both user fit and intrinsic quality.
- [ ] First choice is decisive; caveats do not bury the answer.

## Pitfalls

- **Shell-as-content:** treating `<app-root>` or a loading page as an empty catalog.
- **Catalog-scope laundering:** presenting network-wide availability as exact vehicle/store/device inventory.
- **Token leakage:** printing an anonymous session token while debugging.
- **Premature narrowness:** accepting a small result without checking pagination, active programs, nested sections, and platform filters.
- **Keyword-only personalization:** recommending a mediocre literal match over a much better thematic fit.
- **Unverified totals:** quoting counts that disagree with the enumerated result.

## References

- See `references/js-spa-api-recovery.md` for a validated extraction pattern and an airline-entertainment example.

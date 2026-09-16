# Hacker News Algolia domain-count reports

Use this reference when asked to rank publications/domains linked from Hacker News over a time window.

## Source

HN Algolia API endpoint:

```text
https://hn.algolia.com/api/v1/search_by_date
```

Typical parameters:

```text
tags=story
numericFilters=created_at_i>=START,created_at_i<END
hitsPerPage=1000
page=0
```

Important behavior observed: the API can report a large `nbHits`, but retrievable results are capped. If `nbHits > hitsPerPage`, split the interval recursively (daily windows are often a good first pass; split days further when over cap). Do not assume `nbPages` gives access to all matches for broad queries.

## Counting method

For "most linked domains" reports:

1. Use `tags=story` and only count hits with a non-empty `url`.
2. Deduplicate by `objectID`/`story_id`.
3. Parse `urlparse(url).hostname`.
4. Normalize conservatively:
   - lowercase host,
   - strip one leading `www.`, `m.`, `mobile.`, or `amp.`,
   - preserve other subdomains unless the user asks for registrable-domain folding.
5. Aggregate counts by normalized host.
6. Useful CSV columns:
   - `rank`
   - `domain`
   - `linked_story_count`
   - `share_of_linked_stories_pct`
   - optional engagement totals: `total_hn_points`, `total_hn_comments`

## Metadata to write alongside CSV

Write a `.metadata.json` sidecar with:

- `generated_at_utc`
- `window_start_utc`
- `window_end_utc`
- source/API description
- normalization rule
- total linked stories counted
- unique domains
- unique HN stories seen
- API calls
- intervals processed
- recursive splits
- max interval hit count

## Delivery

When the user asks for Telegram delivery and Hermes gateway is configured:

```bash
hermes send --list telegram
hermes send --to telegram "Short description. MEDIA:/absolute/path/report.csv"
```

Verify success from `hermes send` stdout before telling the user it was sent.

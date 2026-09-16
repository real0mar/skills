# Reddit Archive Recovery

Use this when Reddit HTML, `.json`, `old.reddit.com`, or `api.reddit.com` is blocked but the user needs actual thread content rather than links.

## Discover thread IDs

Search indexes can expose canonical Reddit URLs even when Reddit itself is inaccessible. One validated fallback is DuckDuckGo HTML through Jina Reader:

```text
https://r.jina.ai/http://html.duckduckgo.com/html/?q=<URL-ENCODED QUERY>
```

Extract canonical URLs shaped like:

```text
https://www.reddit.com/r/<subreddit>/comments/<post_id>/<slug>/
```

Anonymous Jina access may succeed for a search-result page while a direct Jina fetch of Reddit still reproduces Reddit's 403 block. Validate page content, not HTTP status alone.

## Retrieve archived comments with Arctic Shift

Arctic Shift is a public historical Reddit archive. The validated workflow required no authentication.

Comment tree:

```text
GET https://arctic-shift.photon-reddit.com/api/comments/tree?link_id=t3_<post_id>&limit=5000
```

Chronological comment slice:

```text
GET https://arctic-shift.photon-reddit.com/api/comments/search?link_id=t3_<post_id>&limit=100&sort=desc
```

Operational details:

- Prefix post IDs with `t3_`; the unprefixed form may time out on some threads.
- `/comments/search` sorts by `created_utc`, not score. Never describe its first results as “top comments.”
- `/comments/tree` retains Reddit-style nesting and archived `score` fields. Recursively walk top-level `data[]` and each `data.replies.data.children[]`, then rank locally by `score`.
- Large threads may time out at high limits. Reduce the limit or retrieve a smaller related thread instead of repeatedly hammering the service.
- Filter `[deleted]`, `[removed]`, AutoModerator, duplicates, and reply fragments that make no sense alone.
- Favor top-level stories. Add replies only when they provide an outcome, correction, or necessary context.

## Reading packets

If the user cannot open links:

- Deliver the selected material in chat, not as a URL list.
- Faithfully paraphrase and condense repetitive setup; retain material facts, chronology, outcomes, and punchlines.
- Clearly label the packet as paraphrased archived anecdotes.
- State that Reddit stories are not independently verified.
- Target approximately 180–220 words per requested reading minute.

## Provenance

Arctic Shift is an archive, not proof of current Reddit state. Preserve post IDs and comment IDs during selection so the source can be audited later.
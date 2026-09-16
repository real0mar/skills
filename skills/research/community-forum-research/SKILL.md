---
name: community-forum-research
description: "Use when finding, recovering, and packaging forum threads."
version: 1.0.0
metadata:
  hermes:
    tags: [forums, reddit, archives, thread-research, offline-delivery]
    category: research
    related_skills: [blocked-page-recovery, grounded-citations]
---

# Community Forum Research

Use this skill to find relevant discussion threads, recover their actual posts and comments when the live site is obstructed, distinguish popular material from merely recent material, and package the useful content for the user's access constraints.

## Principles

- Inspect the original forum when accessible; use archives and search indexes only as fallbacks.
- A thread title or search snippet proves existence, not the contents of the full discussion.
- Forum anecdotes are user reports, not independently verified facts.
- Preserve provenance: forum, community, thread ID, comment ID, archive source, and whether the copy is live or historical.
- Validate response bodies. HTTP 200 can contain a block page, consent interstitial, or redirect shell.
- Match the deliverable to the user's connectivity. If they cannot open links, bring the content into the chat instead of handing them a bibliography.

## Workflow

1. **Clarify the target implicitly when possible**
   - Infer whether the user wants one remembered thread, several related threads, raw links, representative answers, or a reading packet.
   - When the request has an obvious interpretation, proceed without asking.

2. **Discover candidate threads**
   - Search exact phrasings, paraphrases, community names, and title fragments.
   - Record canonical URLs and stable post IDs.
   - Prefer threads with visible engagement evidence and substantive answers over duplicate low-activity prompts.

3. **Retrieve actual content**
   - Try the live page or official API first.
   - If blocked, use the `blocked-page-recovery` ladder and forum-specific archives.
   - For Reddit-specific recovery, read `references/reddit-archive-recovery.md`.

4. **Rank and filter programmatically**
   - Do not infer “top” from API order unless the endpoint explicitly sorts by score.
   - When archived score fields are available, sort locally.
   - Prefer top-level, self-contained responses; include replies only when they supply an outcome, correction, or essential context.
   - Remove deleted/removed entries, bot comments, duplicates, and contextless one-liners.

5. **Package for the requested experience**
   - **Link list:** titles, communities, engagement if verified, and direct canonical URLs.
   - **Summary:** thematic synthesis with representative examples.
   - **Reading packet:** vivid but faithful paraphrases, arranged for pacing and variety.
   - Label paraphrase versus quotation. Never invent connective details to make an anecdote more satisfying.

## Offline or chat-only delivery

When the user says they lack web access or only have the current messaging channel:

- Do not make links the primary deliverable.
- Include the recovered substance directly in the message.
- For a requested reading time, budget approximately 180–220 words per minute.
- Respect platform message limits and allow the connector to split a long packet cleanly at headings.
- Put the strongest item first and mix long stories with short palate cleansers.

## Verification checklist

- [ ] Candidate thread URLs and IDs were found from an inspectable source.
- [ ] Actual comment bodies—not only snippets—were retrieved for any detailed retelling.
- [ ] Claimed rankings or engagement numbers are backed by metadata.
- [ ] Archive provenance and anecdotal uncertainty are disclosed.
- [ ] The final format is usable under the user's connectivity constraints.
- [ ] No deleted, duplicated, or contextless entries were presented as complete stories.

## Pitfalls

- **Links-only response to an offline user:** technically sourced, practically useless.
- **Search snippets as full evidence:** snippets may be stale, generated, or context-stripped.
- **Chronological order presented as popularity:** many archive search endpoints sort only by creation time.
- **Over-quoting:** condense and paraphrase unless exact wording is the point.
- **Anecdote laundering:** high score does not establish truth.
- **Retry loops:** after repeated blocks, pivot to an archive or data endpoint rather than changing only the user agent.

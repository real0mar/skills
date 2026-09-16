---
name: conversation-analysis
description: "Analyze long private chats and message exports with evidence-backed extraction, timelines, interpersonal-pattern assessment, and scoped quotation inventories."
version: 1.0.0
metadata:
  hermes:
    tags: [conversation-analysis, chat-logs, whatsapp, evidence-extraction, relationship-analysis, timelines]
    category: research
    requires_toolsets: [file, delegation]
---

# Conversation Analysis

Use this skill when a user supplies a long chat/message export and asks for exhaustive comments, a timeline, tone or relationship analysis, recurring patterns, contradictions, or evidence-backed interpretation.

## Core principles

- Treat private conversations as sensitive source material. Analyze only what the user requests; do not expose unrelated details.
- Separate **what was said** from **what it suggests**. Quote first; interpret second.
- Define ambiguous scope before extraction, or state a reasonable interpretation explicitly. For example, “comments about bodies” can mean appearance only or the broader set of anatomy, grooming, hygiene, health, sensations, and sexual functions.
- Preserve exact wording, speaker, timestamp, and source line numbers when the request asks for “every,” “all,” or an audit trail.
- Do not infer the contents of deleted messages or `<Media omitted>` entries. Text reactions to missing media may be included only when their subject is clear from surrounding context.

## Workflow

1. **Inspect source size and format**
   - Determine line count and message format before reading the whole file.
   - Identify message boundaries, multiline messages, edited/deleted markers, and omitted media.

2. **Operationalize the request**
   - Write inclusion and exclusion rules before extraction.
   - For an ambiguous category, use tiers rather than silently choosing one:
     - narrow: direct appearance/body evaluation;
     - broad: anatomy, grooming, hygiene, health, bodily sensation/function, sexual references;
     - contextual: reported third-party comments or implications.

3. **Extract in parallel for long logs**
   - Split by non-overlapping line ranges.
   - Give each worker the absolute path, exact range, shared inclusion/exclusion rules, and required output schema.
   - Require exact quote, speaker, timestamp, line number(s), and referent.
   - Independently run a broad keyword/regex screen as a recall check; treat it as candidate generation, not final classification.

4. **Wait for all extraction workers before answering**
   - Do not publish an “exhaustive” result while delegated chunk reviews are still running.
   - Read every full worker artifact, not only truncated summaries.
   - Merge, deduplicate, resolve boundary/context errors, and normalize labels.

5. **Present results at the requested granularity**
   - For short inventories, use a chronological table.
   - For large inventories, provide a concise in-chat summary plus a Markdown/CSV artifact containing the complete evidence list.
   - Clearly state source limitations and the interpretation used.

6. **Interpret dynamics only after extraction**
   - Distinguish ordinary friendship, flirtation, friends-with-benefits, romantic attachment, and boundary ambiguity based on repeated behavioral evidence.
   - Calibrate language: “consistent with,” “reads as,” or “more accurately described as” is preferable to unsupported certainty.
   - Separate mutual/consensual sexual behavior from possible boundary complications involving current or future partners.

## Quality checks

- [ ] Every source range was reviewed.
- [ ] All delegated results completed before the final claim of exhaustiveness.
- [ ] Full worker outputs were read despite summary truncation.
- [ ] Exact quotes match the source.
- [ ] Speaker, timestamp, line number, and referent are present.
- [ ] Third-party and participant comments are not mixed unintentionally.
- [ ] Appearance-only and broader bodily references are labeled separately when relevant.
- [ ] Missing media/deleted-message limitations are disclosed.
- [ ] Interpretive conclusions cite multiple concrete patterns, not one isolated line.

## Pitfalls

- **Premature completion:** answering from keyword candidates while deeper chunk reviews are still running. This creates an incomplete “every comment” list and forces a correction.
- **Silent scope narrowing:** interpreting “body comments” as appearance-only without saying so.
- **Regex-as-verdict:** keyword searches produce false positives and miss euphemisms, replies, and context-dependent references.
- **Generic-attractiveness drift:** decide explicitly whether standalone “hot/cute/beautiful” remarks count.
- **Third-party leakage:** reported comments by dates/friends must be labeled as reported speech or excluded according to scope.
- **Media hallucination:** never infer what an omitted photo/video depicted beyond surviving textual context.

## References

- See `references/large-chat-evidence-extraction.md` for a proven chunking, recall-check, and merge procedure for multi-thousand-line exports.

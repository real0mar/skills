# Large-chat evidence extraction

## Trigger

Use this procedure for multi-thousand-line WhatsApp, SMS, Telegram, Slack, Discord, or email-thread exports when the user asks for every instance of a category or wants an evidence-backed interpersonal analysis.

## Extraction contract

Give every chunk reviewer the same contract:

```text
Read only lines START–END from ABSOLUTE_PATH.
Extract every message matching CATEGORY.
Return: line number(s), timestamp, sender, exact quote, referent, and a one-line classification.
Include: [explicit rules].
Exclude: [explicit rules].
Do not paraphrase quotes. Do not infer omitted/deleted media.
```

Good body-comment categories illustrate why scope must be tiered:

1. **Appearance/anatomy:** face, hair, height, body shape, skin, genitals, explicit attractiveness tied to appearance.
2. **Grooming/hygiene:** shaving, haircuts, showers, cleanliness.
3. **Health/sensation/function:** lungs, teeth, pain, temperature, menstruation, orgasm, physical stress reactions.
4. **Sexual bodily references:** nudity, touching, penetration, ejaculation, sexual photos/videos.
5. **Reported speech:** a third party's quoted assessment of either participant; label separately.

## Parallelization

- Split on message boundaries when possible.
- Use non-overlapping ranges and record exact endpoints.
- Three chunks is usually a good starting point for roughly 6k–10k lines.
- Require all workers to finish before claiming completeness.
- If a worker result is truncated in the parent context, read its saved full summary artifact.

## Independent recall check

Run a broad lexical screen across the entire source. Include direct nouns, euphemisms, grooming terms, appearance adjectives, and phrases such as `you look`, `your body`, `I feel`, `shaved`, `hair`, `inside you`, and `fit check`.

Use the screen to:

- find likely misses;
- inspect context windows around candidates;
- verify cross-chunk consistency.

Do **not** use keyword matches as the final list: words such as “hot,” “body,” “hard,” “fit,” and “ass” have many non-bodily meanings, while euphemisms may contain none of the expected terms.

## Merge and validation

1. Concatenate chunk results.
2. Sort by source line and timestamp.
3. Deduplicate grouped exchanges and repeated reported speech.
4. Confirm ambiguous replies against nearby source lines.
5. Separate direct comments, self-comments, reported third-party comments, and bodily events.
6. Produce a narrow answer in chat and a broad appendix when the user's wording is ambiguous.
7. State that deleted messages and omitted media are unavailable.

## Lesson captured

In a 6,853-line WhatsApp export, an initial manual/regex pass found the most obvious appearance comments but missed hygiene, grooming, health, contextual replies, reported speech, and euphemistic sexual references. Parallel full-range review plus a keyword recall check produced the complete textual inventory. The key procedural lesson is to wait for the complete merge before using words such as “every” or “exhaustive.”

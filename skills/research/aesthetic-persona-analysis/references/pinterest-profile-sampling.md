# Pinterest public-profile sampling

## Validated inspection pattern

1. Open the user-supplied short link and record the canonical profile URL.
2. Capture the profile overview: avatar, visible board titles, cover images, pin counts, and update recency.
3. If accessibility snapshots omit board URLs, inspect public anchor `href` values in the DOM rather than guessing URL slugs.
4. Sample boards from distinct domains:
   - home/environment;
   - clothing, beauty, or self-presentation;
   - crafts, possessions, or collecting.
5. For each board, combine the accessibility text/alt labels with a screenshot. Text supplies searchable cultural labels; vision supplies palette, texture, density, and composition.
6. When a sign-in modal obscures already-public content, remove only the fixed visual overlay from the local DOM view, restore scrolling if needed, and take a fresh screenshot. Do not claim access to unloaded or private material.
7. Stop when motifs converge across domains; additional near-duplicate boards add little confidence.

## Evidence-to-inference example

The following map illustrates the level of grounding expected; it is not a reusable verdict for every pastel profile.

| Repeated observation | Supported interpretation | Avoid |
|---|---|---|
| Compartmentalized drawers, tidy small rooms, restricted cream/blush palette | Visual order may serve a regulating or reassuring function | “The person has OCD” |
| Plush animals, dollhouses, character goods, bows, tiny charms | Projects nostalgia, playfulness, or a desire for tangible comfort | “Emotionally regressed” |
| Shōjo/coquette/kawaii clothes, doe-eye makeup, soft silhouettes | Idealized social presentation is delicate, approachable, and low-aggression | Guessing gender, age, or sexuality |
| Journals, handmade bracelets, decorated ceramics, customized devices | Values personalization, ritual, and emotionally charged small objects | Assuming the person actually makes or owns every item |
| Bedrooms, pajamas, crafts, gaming, baking dominate over travel/status imagery | The aspirational world is private, domestic, and sanctuary-oriented | Claiming the person is antisocial |
| Dense decoration contained within a narrow palette | Useful tension: expressive maximalism constrained by strong coherence needs | Flattening the collection to “just cute” |

## Output calibration

- Lead with a sharp thesis, but make the following bullets show the evidence.
- Say **projected self**, **ideal self**, or **aesthetic persona** when behavior is not directly observed.
- A “shadow side” should describe a plausible risk—such as perfectionistic escapism—not a diagnosis.
- End with a short scope note: curated collections usually reveal aspiration more reliably than biography.

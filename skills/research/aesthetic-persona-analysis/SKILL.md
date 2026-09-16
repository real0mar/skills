---
name: aesthetic-persona-analysis
description: "Use when inferring persona from curated visual collections."
version: 1.0.0
metadata:
  hermes:
    tags: [visual-analysis, aesthetic-analysis, persona, pinterest, moodboards, identity]
    category: research
    requires_toolsets: [web]
---

# Aesthetic Persona Analysis

Use this skill when a user asks to “psychoanalyze,” profile, or interpret someone from a Pinterest profile, moodboard, saved-image collection, room inspiration, wardrobe board, playlist artwork, or similar curated visual corpus.

The target is the **projected or aspirational persona expressed by the collection**, not a clinical diagnosis or a claim that the collection reveals the whole person.

## Principles

- Inspect the supplied source directly before using search results or prior conversation context.
- Separate **observation** (visible patterns) from **inference** (possible emotional or identity function).
- Prefer repeated motifs across multiple boards over one striking image.
- Treat titles, board sizes, and recency as supporting metadata, not personality proof.
- Distinguish aesthetic coding from demographics: “feminine-coded,” “youth-coded,” or “modest styling” is safer than guessing gender, age, religion, or ethnicity.
- Do not diagnose disorders, trauma, attachment style, or sexuality from aesthetic material.
- Calibrate claims with “suggests,” “projects,” “may function as,” and confidence labels when evidence is thin.
- A playful “armchair psychoanalysis” tone is acceptable when requested, but it must remain grounded and non-clinical.

## Workflow

1. **Resolve the target, ownership, and scope**
   - Follow short links to the canonical destination; determine whether it is a profile, board, or single pin.
   - Until the user identifies the owner, say **the curator** or **the board owner** rather than assuming the collection belongs to the user.
   - State whether the eventual read is profile-wide or board-specific. Do not generalize a fashion board into claims about domestic habits, work competence, or relationship functioning.
   - Record profile name, visible boards, pin counts, and update recency.
   - Use a screenshot or vision pass to capture the profile-level palette and board-cover motifs when the target is a profile.

2. **Sample across psychological domains**
   Select several high-signal boards rather than analyzing only the first visible page:
   - **environment/home:** safety, order, privacy, sensory preferences;
   - **self-presentation/fashion/beauty:** desired social impression and identity performance;
   - **crafts/objects/collections:** agency, ritual, sentimentality, and personalization;
   - optionally food, relationships, travel, work, humor, or text boards when prominent.

3. **Gather evidence from each board**
   Note repeated:
   - palette, contrast, lighting, texture, and shape language;
   - objects, characters, brands, eras, and subcultures;
   - silhouettes, styling, tidiness, density, and spatial arrangement;
   - activities and implied setting: public/private, solitary/social, active/restful;
   - contradictions, such as maximal decoration inside a highly restricted palette.

4. **Handle obstructive web UI pragmatically**
   - If sign-in overlays obscure a public board, use browser DOM inspection to identify canonical board links and remove only visual overlays from the local page view when permitted.
   - Re-capture the page after the obstruction is removed.
   - Never represent hidden or unloaded pins as inspected.

5. **Build interpretations from converging evidence**
   Useful interpretive axes include:
   - control ↔ spontaneity;
   - sanctuary/private world ↔ public display;
   - nostalgia/play ↔ status/adulthood;
   - personalization/maximalism ↔ visual restraint;
   - approachability/softness ↔ intimidation/edge;
   - aspiration ↔ documentation of current life.

   Require at least two independent visual patterns before making a personality inference. Phrase the mechanism explicitly, e.g. “compartmentalized storage plus a tightly restricted palette suggests that visual order may be emotionally regulating.”

6. **Quantify thematic prevalence when asked**
   - Sample visible pins across every accessible board and deduplicate repeated accessibility descriptions.
   - Define explicit coding separately from broad compatibility (for example, hijab imagery versus generally modest fashion).
   - Report inspected sample size, total visible corpus size, approximate coverage, and a bounded estimate rather than false precision.
   - Keyword matching is only a floor; use screenshots to catch visual themes absent from labels.

7. **Present a concise, layered read**
   Recommended structure:
   - one-sentence core thesis;
   - 4–7 evidence-backed projected traits or needs;
   - one tension or “shadow side” framed as a risk, not a diagnosis;
   - one-line synthesis;
   - brief scope note that curated aesthetics reveal an ideal self more reliably than the whole person.

## Quality checks

- [ ] The original source was opened and visually inspected.
- [ ] More than one board or content domain was sampled when available.
- [ ] Every major inference is tied to repeated visible evidence.
- [ ] Observation and interpretation are distinguishable.
- [ ] No demographic or clinical conclusion is presented as fact.
- [ ] Aspirational identity is not confused with current living conditions, practical competence, family dynamics, or behavior.
- [ ] Ownership was not assumed before the user disclosed it.
- [ ] A board-specific analysis is not presented as profile-wide.
- [ ] The answer is specific enough that it could not fit any generic pastel/cute profile.

## Pitfalls

- **Single-image overreading:** one pin may be accidental, algorithmic, or merely practical.
- **Aesthetic-to-diagnosis leap:** nostalgia does not prove regression; tidiness does not prove OCD; dark imagery does not prove depression.
- **Identity guessing:** cultural or modest-fashion references do not establish the curator’s identity.
- **Generic Barnum language:** “sensitive but strong” is meaningless without concrete visual evidence.
- **Flattening subcultures:** name recognizable influences—such as shōjo, coquette, kawaii, Wonyoungism, cottagecore, brutalism—only when the images or metadata support them.
- **Ignoring contradictions:** tensions often reveal more than the dominant palette does.
- **False exhaustiveness:** state which visible boards were sampled and do not imply the entire corpus was reviewed.
- **Ownership assumption:** a shared link may belong to a partner or third party; use neutral ownership language until told otherwise.
- **Biography laundering:** do not use aesthetics plus a thin biographical proxy (distance from family, living arrangement, job prestige) to manufacture claims about competence, enmeshment, or relationship readiness. Analyze concrete behavior separately and update immediately when counterevidence appears.
- **Scope drift:** do not turn a requested aesthetic read into unsolicited marital risk assessment.

## References

- See `references/pinterest-profile-sampling.md` for a validated public-profile inspection pattern and an example evidence-to-inference map.
- See `references/relationship-context-guardrails.md` for ownership, partner-analysis, behavioral-scope, and thematic-quantification guardrails.

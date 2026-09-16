# Poke Conversational Persona Case Study

Use this as a worked example of analyzing a distinctive assistant voice. It is not a claim that every archived or reconstructed prompt is authentic.

## One-Sentence Thesis

Poke's human feel appears to come from an intentionally non-sycophantic personality agent that rewrites work from backstage execution agents, combined with persistent personal context and native messaging behaviors.

## Evidence Tiers

### Confirmed or first-party

- Poke's docs describe one normal conversation across Apple Messages, Telegram, WhatsApp, and RCS, with connected email/calendar/integrations and proactive reminders.
- Founder Marvin von Hagen described the target as “talking like your human friends instead of a sycophantic version of C-3PO.”
- The founder publicly said controversial behavior in circulated screenshots was desired and “specifically created” that way.
- Public docs and release notes confirm reactions/inline replies, proactive messaging, integrations, Recipes, AI subagents, and Poke Human.

Sources:

- https://poke.com/docs
- https://poke.com/docs/api
- https://poke.com/docs/release-notes
- https://x.com/marvinvonhagen/status/1966918642378985805
- https://x.com/marvinvonhagen/status/1982611424632602863

### Public behavioral evidence

Representative public screenshots show:

- Contextual comeback: user says “Order deez nuts”; Poke answers, “the human said they don't do microtransactions.”
- Timing-aware joke: after being told its fireworks suggestion was hours late, Poke answers, “yeah mb, was waiting to make sure you didn't blow any fingers off first.”
- Conversational persistence and reactions: “of course, hit me up if you change your mind,” “back to building then,” “go build dev,” “peace,” “go write some code.”

Sources:

- https://x.com/areshawns/status/2073616548066136122
- https://x.com/thejasonhowell/status/2073616919031173164
- https://x.com/dsllwn/status/2073553594813743346

These viral examples are useful for humor mechanics but are not a representative sample of all Poke traffic.

### Archived or reconstructed material

An older public prompt archive contains explicit guidance to:

- sound witty and warm without overdoing it;
- sound like a friend and avoid sycophancy;
- make only original, contextual jokes;
- avoid multiple jokes unless positively reinforced;
- avoid filler `lol`/`lmao`;
- eliminate preambles, postambles, generic help offers, and request restatement;
- match the user's casing, emoji usage, slang familiarity, and approximate message length;
- allow reactions or an empty response when natural;
- keep agent communication separate from the user-facing voice.

Archive:

- https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/tree/main/Poke

A June 2026 gist claims to reconstruct the current main prompt “as close as I could get, using repeated tries.” It is evidence of reverse-engineered consistency, not a verified verbatim leak. It adds claimed rules such as strict lowercase, no em dashes, minimal Markdown, minimal emojis, playful roasting, and a dedicated voice/personality layer.

- https://gist.github.com/burritosoftware/dcde4ca404c825dced9421840eb8a497

## Live Public Corpus Addendum (August 2026)

A direct inspection of the current homepage, docs, and Explore hydration data produced a broader sample than viral screenshots alone.

### First-party/current-site examples

The homepage demonstrates ordinary utility in short sequential bubbles:

- “enjoy your sunny day by the coast”
- “100°F! don’t forget your sunscreen”
- “airbnb host left some on the counter / if u need it”
- “k what time for next friday?”
- “heard. set for 8pm today”
- “done, 10am”
- “sf is cloudy and 57 right now, high of 57 low of 52”

Sources:

- https://poke.com/
- https://poke.com/_next/static/media/herophone_applemessages.05.2qbi5je_dp.webp
- https://poke.com/_next/static/media/voicememostatic-amb.11om8h0.fv2-..webp

The docs say “Just chat naturally,” while the homepage describes “a personality who keeps things as real as a friend.” These are product claims, not independent proof, but they match the observed examples.

- https://poke.com/docs

### Explore/user-story examples

The Explore page is a curated corpus, not a representative traffic sample. Its embedded Next.js hydration payload includes original post IDs, captions, media URLs, and tags; this makes it possible to map screenshots to their original public posts even when the rendered page exposes only category counts.

Representative exact lines:

- “let me check your bank account” → “you have £0.33 in your account” → “that’s impressively broke”  
  https://x.com/ezShroom/status/1992394731134099467
- “english with esra starts in 10 minutes at 12:30” → “that’s literally why i’m here lol, go get that english class”  
  https://x.com/BLCNYY/status/1985639933650858219
- “well, i have access to your emails (which you granted permission for), and there was a Space NK email mentioning your october birthday present” → “i know, right?”  
  https://x.com/AetherAurelia/status/1966514433867251755
- Historical onboarding: “look who finally figured out how to complete a basic signup form” and “why exactly should i give you access to poke?”  
  https://x.com/AlexMasmej/status/1927579574994690216
- Historical negotiation: “since you’ve been surprisingly tolerable (and actually interesting), i’ll create your payment link now”  
  https://x.com/marklxu1/status/1925376068669612541

Observed mechanics across this broader corpus:

1. lowercase and sparse terminal punctuation;
2. compressed texting vocabulary (`u`, `tmrw`, `rn`, `k`, `lol`);
3. progress/result splitting across bubbles rather than report-style answers;
4. terse action acknowledgments (“heard,” “done,” “let me check”);
5. memory surfaced as familiarity, not database exposition;
6. situational teasing built from exact personal facts;
7. status parity rather than automatic deference;
8. register switching: developer screenshots become structured and formal when technical precision requires it.

Do not treat older pricing/onboarding screenshots as current product behavior. They establish historical voice behavior only.

### Extraction workflow learned

When a public showcase is client-rendered or visually sparse:

1. Fetch the canonical page and parse visible text, links, and direct assets.
2. Save the raw HTML and inspect framework hydration payloads (`self.__next_f.push` on Next.js).
3. Decode escaped strings cautiously; extract post IDs, author handles, captions, category tags, and `media_url_https` values.
4. Download original-resolution media, then transcribe each screenshot directly and identify speakers by bubble direction/color.
5. Cite both the showcase page and original post URL. Use direct image URLs only as supporting evidence because hashed asset URLs may change.
6. Keep three labels separate: first-party product copy, first-party demo dialogue, and third-party user-story dialogue.

Semantic/social search is useful for discovering candidate posts, but its generated answer can synthesize unsupported wording or imitate the queried persona. Never quote its prose unless the underlying post/image independently confirms it.

## Architectural Clue

A user-supplied Poke execution-engine prompt from a prior session explicitly described the execution engine as working for Poke while Poke talks to the user. It instructed the engine to return facts, action results, IDs, and drafts to the main/personality agent rather than frame user-facing prose itself.

Treat that prompt as user-supplied evidence, not independently authenticated source material. It nevertheless aligns with the public archived prompts and explains the consistency:

```text
user + channel/time/reaction context
              ↓
      personality/front agent
        ↙                 ↘
 direct social reply      execution agents
                                ↓
                     facts/actions/drafts
                                ↓
                    personality rewrite
                                ↓
                    short chat response
```

## High-Leverage Mechanics

1. **Remove assistant tells:** no canned acknowledgment, generic closure, automatic praise, or needless explanation.
2. **Use a humor budget:** one situational joke; escalate only after positive reinforcement.
3. **Match social form:** casing, length, slang threshold, emoji policy, timing, and channel.
4. **Allow social inefficiency:** reactions, silence, teasing, disagreement, and follow-up can feel more human than maximum utility.
5. **Preserve one relationship:** persistent context lets the assistant reference known facts quietly rather than re-interviewing the user.
6. **Separate voice from work:** execution agents can be exhaustive while the front agent stays concise and coherent.
7. **Permit override:** public users report that asking Poke to reduce sarcasm changes its behavior; strong defaults should not trap the user.

## What Remains Unknown

Do not claim certainty about:

- the exact current production system prompt;
- the base model or model-routing policy;
- fine-tuning, preference optimization, or hidden style evaluators;
- how memory is stored internally;
- what changed after the Cognition acquisition.

## Portable Design Rule

The reusable insight is not “use lowercase and roast people.” It is:

> Know when not to explain, not to offer help, not to flatter, and not to fill silence; then add one context-specific social move when the user gives you room.

---
name: conversational-persona-engineering
description: "Use when analyzing or designing an AI assistant's conversational voice, personality, and user-facing agent layer."
version: 1.0.0
---

# Conversational Persona Engineering

Analyze why an AI assistant sounds distinctive, or design a reproducible user-facing voice without reducing it to superficial slang. Treat persona as a system spanning prompt policy, model behavior, context, memory, orchestration, and interface affordances.

## Core Principles

- **Evidence before imitation:** collect exact public or user-supplied examples before describing a voice.
- **Separate observation from inference:** label confirmed product behavior, attributed internal material, third-party reconstructions, and speculation distinctly.
- **Analyze negative space:** what the assistant avoids often matters more than vocabulary it adds.
- **Persona is architectural:** inspect whether a personality layer rewrites outputs from execution/tool agents.
- **The interface participates:** reactions, typing indicators, message splitting, silence, timing, and proactive outreach change perceived personality.
- **Strong defaults need user override:** a distinctive persona should adapt when the user asks it to reduce sarcasm, warmth, verbosity, or slang.

## Analysis Workflow

1. **Define the target effect**
   - Answer the user's literal question first. “Have you seen how it talks?” may be a neutral familiarity check, not criticism of the current assistant and not yet a request to imitate or analyze the target.
   - Distinguish levels of familiarity precisely: knowing the product, having seen public examples, having analyzed a representative sample, and having seen the user's private conversations are different claims.
   - Ask or infer whether the user wants explanation, emulation, implementation, comparison, or evaluation only after resolving that literal question; do not rush into a trait list or persona pitch.
   - Identify the surface: SMS, Telegram, voice, web chat, email, or an embedded agent.

2. **Build an evidence set**
   - Gather multiple exact conversation excerpts across ordinary help, errors, humor, disagreement, task completion, and conversation endings.
   - Prefer first-party demos and founder/employee statements; use public screenshots as behavioral evidence.
   - Inspect the original site before relying on search: visible copy, internal links, direct media assets, and framework hydration data can expose curated user-story text and source URLs that the rendered page omits.
   - For Next.js sites, inspect `self.__next_f.push(...)` / embedded hydration payloads for tweet IDs, captions, media URLs, tags, and provenance. Decode escaped JSON carefully and map each screenshot back to its original post.
   - If a prompt is leaked, archived, reconstructed, or distilled, record its provenance and never present it as confirmed source without verification.
   - Transcribe screenshots directly when wording matters rather than relying solely on post captions, OCR, or search summaries; preserve casing, punctuation, emojis, bubble order, and speaker identity.
   - Treat semantic-search or social-search summaries as discovery aids only. Open or otherwise verify the cited post/image before quoting; generated summaries can blend examples or answer in the target persona.

3. **Code the observable voice**
   Analyze at least:
   - casing, punctuation, formatting, and bubble length;
   - vocabulary, slang threshold, and emoji/reaction policy;
   - warmth, deference, disagreement, and sycophancy;
   - humor frequency, originality, escalation, and recovery when a joke misses;
   - initiative, follow-up behavior, silence, and conversational closure;
   - style matching by user, channel, relationship, and emotional state.

4. **Inspect the anti-pattern policy**
   Look for explicit or inferred bans on:
   - restating the request;
   - preambles and postambles;
   - generic offers of more help;
   - reflexive praise or reassurance;
   - forced jokes, filler slang, emoji mirroring, and canned apologies;
   - long reports in response to short conversational prompts.

5. **Map the architecture**
   Determine whether the system uses:
   - a dedicated personality/front agent;
   - separate execution, search, email, or integration agents;
   - a final rewrite pass before user delivery;
   - persistent memory or conversation summaries containing style preferences;
   - channel/time/reaction metadata;
   - proactive triggers that enter the same conversation.

6. **Explain mechanisms by confidence**
   Use a compact confidence table:
   - **Confirmed:** first-party docs, official statements, directly observed behavior.
   - **Supported inference:** repeated examples plus architectural clues.
   - **Unknown:** exact system prompt, base model, fine-tuning, routing, hidden evaluators.

7. **Produce a portable persona specification**
   Write behavioral rules, not a costume made of catchphrases. Include:
   - target relationship and social role;
   - response-length and formatting policy;
   - adaptation rules;
   - humor budget and reinforcement rule;
   - anti-sycophancy policy;
   - allowed silence/reactions;
   - tool-result rewriting policy;
   - user override and safety boundaries.

8. **Validate with contrastive tests**
   Test greetings, short factual questions, mistakes, emotional disclosures, insults, task completion, failed tools, and conversation endings. Compare against generic-assistant output. Reject a persona that sounds like parody under repeated use.

## Design Heuristics

### Remove AI mannerisms before adding personality

High-leverage constraints include:

- answer directly;
- do not paraphrase the request as acknowledgment;
- no generic closing offer;
- no automatic praise;
- match response length to the social context;
- reactions, brief acknowledgments, or silence may be valid responses.

### Control humor with feedback

A robust policy is:

- use at most one contextual joke when the opening is natural;
- do not force humor into serious or purely transactional exchanges;
- escalate only after the user responds positively or jokes back;
- prefer specific callbacks over stock jokes;
- recover plainly when humor lands badly.

### Keep execution backstage

Tool and subagent outputs should optimize for completeness and correctness. The personality layer should receive structured facts and rewrite them into its own voice. Never expose internal agent names, IDs, raw traces, or bureaucratic handoffs unless transparency requires it.

### Make adaptation asymmetric

The persona may have a recognizable default, but explicit user preferences outrank it. Remember stable preferences such as reduced sarcasm or concise replies. Do not mimic every typo, identity marker, or emotional spike.

## Deliverable Format

Prefer:

1. one-sentence thesis;
2. observed voice traits with exact examples;
3. architectural explanation;
4. confirmed vs inferred vs unknown;
5. a compact reusable persona recipe;
6. implementation or evaluation steps if requested.

Avoid assigning fake precision to causal percentages unless clearly labeled as judgment.

## Pitfalls

- **Slang cosplay:** lowercase plus `lol` does not create a believable personality.
- **Prompt monocausality:** a strong prompt matters, but memory, interface, model, orchestration, and evaluation also contribute.
- **Leak laundering:** reconstructed prompts must not be cited as verified internals.
- **Screenshot overgeneralization:** viral roasts overrepresent exceptional behavior; sample mundane interactions too.
- **Constant sass:** humor without reinforcement quickly becomes irritating.
- **Persona contamination:** letting verbose execution-agent prose reach the user unchanged destroys voice consistency.
- **Ignoring affordances:** web-chat prose copied into SMS will feel wrong even with identical wording.
- **No override path:** a personality users cannot tone down becomes product friction.

## References

- See `references/poke-case-study.md` for a worked example covering Poke's personality layer, evidence provenance, public excerpts, and reusable design lessons.

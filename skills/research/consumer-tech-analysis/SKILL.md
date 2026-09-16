---
name: consumer-tech-analysis
description: "Analyze consumer technology tradeoffs using web-verified facts, practitioner consensus, and matched-condition reasoning."
version: 1.0.0
license: MIT
platforms: [linux, macos, windows]
---

# Consumer Tech Analysis

Use this skill when the user asks for practical judgment about consumer tech: phones, cameras, laptops, displays, peripherals, local AI hardware, hosted AI services, smart home devices, subscriptions, or everyday hardware/software features. The user prefers concise, high-signal, technically correct answers with current web verification for fast-moving products.

## Core workflow

1. **Verify current product facts.** Use official support/spec pages and credible review outlets for model-specific behavior. Treat Reddit/forums as practitioner-consensus signals, not authoritative specs.
2. **Separate objective constraints from workflow preferences.** Example: storage and processing time are objective; whether Motion Photos matter depends on shooting style.
3. **Reason at matched output conditions.** If the question is about a 12MP display/export, compare 12MP-native output against 50MP downsampled to 12MP, not 100% crops from different resolutions.
4. **Name the hidden pipeline assumptions.** For computational photography, distinguish sensor readout, binning, demosaicing, HDR/multi-frame merge, denoise, sharpening, feature availability, and UI latency.
5. **Give a default plus exceptions.** The user wants direct judgment: e.g. “12MP for people/moments; 50MP for bright static detail/cropping.”

## PC-to-console game graphics comparisons

When the user asks for console-equivalent PC settings:

1. Start with the frame-rate mode they care about (especially 60+ fps), not the highest-fidelity 30 fps mode.
2. Verify official targets and retained rendering technologies, then use measured technical analysis for internal resolution and per-setting matches.
3. Treat console presets as bespoke. Explicitly mark settings that sit between or below selectable PC levels; do not imply a whole PC preset is an exact match.
4. Convert measured internal resolution to the game's actual percentage/quality labels rather than assuming standard DLSS/FSR naming.
5. Separate native rendered FPS, dynamic resolution, reconstruction, and frame generation. Mention fixed-rate cutscenes separately.
6. Provide both a strict console-equivalent profile and a PC-optimized profile when they materially differ.

See `references/pc-console-graphics-equivalence.md` for the workflow and a sourced Halo: Campaign Evolved example.

## Third-party camera ports and device-specific mods

For GCam ports, camera apps, ROM-specific integrations, and similar device mods:

1. **Lock the exact device identity first.** Closely named models (for example, OnePlus 11 vs 11R, or 13 vs 13R) can use different sensors, camera IDs, configs, and package variants. If the user corrects the model, discard the prior model-specific recommendation and redo the device lookup rather than merely renaming the answer.
2. **Separate four kinds of freshness:** active modder, actively updated base/branch, current device-specific config, and compatibility with the phone's current OS. Do not call an old known-good APK “current” only because its developer still releases other branches.
3. **Prefer an exact known-good pair over the newest APK:** device + OS + package variant + APK version + matching config/library. Configs can depend on processing behavior from a specific release and may regress or crash on newer builds.
4. **Verify package-name requirements.** OEMs may expose auxiliary lenses only to package names such as `aweme` or `snapcam`; “the app installs” does not prove all lenses work.
5. **Rank by the user's actual criterion.** “Best image quality,” “easiest,” and “non-abandonware” may point to different builds. State the tradeoff instead of silently treating them as equivalent.
6. **Use stock camera fallbacks explicitly.** A GCam port may be strongest for stills/Night Sight while stock remains safer for video, slow motion, high-frame-rate modes, or OEM-only computational features.
7. **Treat community claims as compatibility evidence, not controlled image-quality proof.** Prefer official mod repositories/config pages for exact files and use XDA/Telegram/Reddit to establish practitioner consensus and OS-specific breakage.

## Messaging-native AI and consumer subscription reuse

When evaluating LLM assistants on Telegram, SMS/RCS, WhatsApp, iMessage, Discord, or similar channels, distinguish first-party hosted bots, official subscription-backed self-hosted channels, independent agents with their own plans, and unofficial API wrappers. Never assume a web/app subscription carries into a messaging bot: verify account linking, entitlement source, region/rollout constraints, and whether linking applies paid-plan limits or merely raises a free allowance. Also distinguish SMS from WhatsApp, RCS, iMessage, and voice calling.

See `references/messaging-native-ai-subscription-reuse.md` for the research order, subscription-reuse checklist, answer format, and privacy guardrails.

## Local AI hardware vs hosted inference economics

When comparing a local GPU against API inference, do not default to the API price of the same local model. Compare against the **best realistically substitutable hosted model** the user would actually choose, accounting for both quality and price. A cheaper, stronger hosted model can make same-model API pricing irrelevant.

1. **Separate sunk and incremental costs.** If the GPU is already owned, exclude purchase price unless the user explicitly asks for total cost of ownership. Compare electricity, cooling, and other marginal operating costs against API usage. Include hardware amortization only for a prospective purchase.
2. **Use measured workload variables when available:** wall power during inference, sustained decode tokens/s, prompt/prefill throughput, input:output token ratio, cache-hit rate, quantization, context length, and backend. Do not substitute GPU TGP for wall power without labeling it a conservative assumption.
3. **Price input and output separately.** Local decode is often the expensive phase while local prompt ingestion may be cheap. Hosted APIs may have very low output prices but meaningful uncached-input charges; input-heavy agent or repository workloads can reverse a conclusion based on output tokens alone.
4. **Compare equivalent utility, not just token cost.** Include model quality, tool calling, context limits, privacy, offline availability, latency, reliability, and quantization loss. If the hosted model is materially better, say so rather than treating one million local and hosted tokens as interchangeable.
5. **Give break-even conditions.** Report the local tokens/s or input:output ratio required to match the API—not merely a single point estimate. Use current official/API pricing and a live electricity rate, and flag supply-only rates that may exclude delivery charges.
6. **Answer in this order:** direct verdict → assumptions → marginal-cost table → break-even conditions → exceptions. Do not lead with capital-cost analysis after the user has said the hardware is already owned.

## Dropship, white-label, and original-R&D assessment

When evaluating whether a consumer device is generic dropshipping, customized ODM hardware, or genuinely original engineering, avoid a binary verdict based on storefront polish.

1. **Inspect the original product page first.** Record concrete specifications, launch status, price/deposit structure, technical claims, regulatory language, and whether imagery shows shipping hardware or only renders.
2. **Trace the company’s product stack.** Look for prior shipped products, a product-specific companion app, app-store seller identity and version history, firmware-update support, independent owner reports, warranty/support infrastructure, and regulatory filings under the seller’s own grantee name.
3. **Search for exact hardware reuse.** Use reverse-image search, exact dimensions, sensor/case geometry, charger shape, model numbers, manuals, Bluetooth names, and distinctive marketing phrases across Alibaba, Global Sources, Amazon, FCC/device databases, and other brands. An absent clone is evidence against literal dropshipping, not proof of deep R&D.
4. **Separate the engineering layers:** industrial design/tooling; PCB/reference platform; sensors and algorithms; low-level firmware; companion app/cloud; validation/regulatory work. State which layers appear custom, commissioned, ODM-supplied, or unproven.
5. **Use regulatory evidence correctly.** A company-owned FCC filing with internal photos supports real product integration and market preparation, but does not establish proprietary sensor science. For prelaunch radio products, note when no public filing is discoverable without claiming one cannot exist under confidentiality, another model name, or a pending application.
6. **Audit technical disclosure.** Missing SoC, display type/resolution, battery capacity, sensor vendors, GPS/runtime details, memory, OS/API, and accuracy validation are strong signals that marketing is outrunning demonstrated engineering.
7. **Interrogate novelty claims.** Undefined phrases such as “proprietary 3D technology,” “AI health intelligence,” or “medical-grade insights” need a mechanism, patent/publication, validation study, or working demonstration. Do not count branding, UI presentation, or ordinary shaders as deep R&D by default.
8. **Classify rather than caricature.** Default output categories: literal reseller/dropship; private-label OEM; customized ODM; custom industrial design plus ODM electronics; substantially original platform. Give confidence and distinguish company legitimacy from product maturity.
9. **End with a purchase threshold.** Identify the evidence that should exist before preorder or full-price purchase: certification, named components, uncut prototype footage, teardown, independent accuracy testing, shipping history, and enforceable refund terms.

See `references/dropship-vs-original-rd.md` for a compact evidence matrix, search workflow, and wording guardrails.

## Digital-wellbeing and behavior-change interventions

When evaluating ways to reduce smartphone use, distinguish **awareness tools** from **commitment devices**. A usage dashboard or instantly editable timer may inform the user without materially constraining behavior.

1. Identify the actual failure mode first: forgetting, automatic app opening, impulsive override, nighttime proximity, or legitimate work requirements.
2. Rank interventions by how reversible they are during an urge. Prefer externally enforced approval, delayed overrides/cooldowns, recurring locked schedules, uninstall protection, or physical separation over notifications and self-administered timers.
3. Match the mechanism to the behavior:
   - Hard blocker for clearly unwanted apps/times.
   - Per-opening friction for apps that remain legitimately useful.
   - Physical separation or a timed lockbox for bedroom/evening use.
   - Grayscale, launcher cleanup, and notification removal only as supporting cue reduction.
4. For users who repeatedly override limits, do not recommend a PIN they know as the primary intervention. Use trusted-person approval or a delay that makes changes apply only after the urge has passed. A useful policy is: changes may affect tomorrow, never today.
5. Prefer recurring schedules/allowances over ad-hoc daily values that remain altered after an exception.
6. Verify anti-bypass details on the current Android version: rule-edit locking, uninstall protection, Settings blocking, reinstalled-app handling, website/domain coverage, and emergency allowlists.
7. Separate evidence quality. Label randomized trials, longitudinal field studies, and vendor claims distinctly; disclose relevant conflicts of interest. Report measured behavioral outcomes (minutes, openings, compliance, rebound), not merely self-reported satisfaction.
8. Warn that no user-administered phone app is truly uncheatable. External control or physical separation is stronger when bypass resistance is the core requirement.

See `references/digital-wellbeing-interventions.md` for evidence notes, intervention ranking, and an Android configuration pattern.

## Style expectations for this user

- Be direct and avoid hand-wavy consumer-review filler.
- Do not over-explain basics the user clearly understands.
- If challenged, correct the technical point plainly; do not defend a bad framing.
- Avoid misleading pixel-count intuition. Always convert claims to same final viewing size/output resolution before judging quality.
- Prefer compact tables and bullets only when they clarify; avoid padding.

## Camera Mode Comparison Scope

This skill incorporates `smartphone-camera-analysis`. Before comparing modes, establish whether the output is a native 100% crop, matched-size display/export, print, or crop; check whether storage, latency, burst, RAW, and capture-assist features matter. Prefer high resolution for bright static detail and deliberate crops/prints; favor the default/binned mode for motion, quick people/pet photos, and computational features, subject to device-specific verification.

See `references/pixel-high-resolution-mode.md` for the preserved Pixel case notes. Treat model-specific feature availability as historical observations requiring current verification.

## Smartphone camera resolution pitfalls

- **Do not claim higher resolution inherently creates more motion blur at matched output size.** A 50MP frame with blur spanning twice as many pixels as a 12MP frame can be equivalent after downsampling if exposure/stabilization/scene motion are identical.
- **Do not reduce 12MP-vs-50MP to “more noise.”** Downsampling 50MP to 12MP averages random noise; native 12MP can still win only if the capture pipeline/readout/HDR/multi-frame processing is better.
- **Feature loss can dominate image-quality deltas.** On Pixel-class phones, high-res modes may disable or limit capture-assist features such as Top Shot, Motion Photos, Auto Best Take, special portrait/tele modes, or burst behavior. Treat that as a significant workflow tradeoff.
- **Quad Bayer high-res is not the same as a true conventional Bayer 50MP capture.** Full-res output may involve interpolation/reconstruction and may not preserve all color/detail information implied by the megapixel count.

## Useful reference files

- `references/smartphone-camera-resolution-modes.md` — session-derived notes on Pixel-style 12MP vs 50MP tradeoffs, matched-output reasoning, Top Shot/Motion Photos, and power-user sentiment.
- `references/gcam-device-port-selection.md` — durable GCam selection workflow plus dated OnePlus 11/13 examples showing package, config, OS, and branch-freshness pitfalls.

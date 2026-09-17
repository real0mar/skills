---
name: headphone-iem-peq
description: >-
  Use when creating or explaining parametric EQ for headphones or IEMs from
  public FR measurements and published targets (Harman OE, Diffuse Field, JM-1 /
  IEF-style). Covers target choice, measurement-rig caveats, and FR → PEQ bands.
---
# Headphone / IEM Parametric EQ Cookbook

Generic skill for designing **parametric EQ** from **public** FR data and well-known preference / research targets. Audience: any agent or user. No personal gear, serials, or private addresses.

---

## When to use

- User wants PEQ bands (frequency / gain / Q) so a headphone or IEM tracks a published target.
- User asks which target fits open-ear (OE) headphones vs IEMs.
- User has (or links) a public FR and needs a safe workflow from curve → bands.
- User needs caveats about measurement rigs, seating variance, or AutoEQ-derived files.

**Out of scope:** speaker/room correction, hearing-aid fitting, medical claims, reverse-engineering paywalled proprietary measurement dumps.

---

## Safety and refusal (light)

**Allowed**

- Public FR graphs/CSVs (Crinacle Graph Comparison Tool exports, RTINGS, manufacturer public charts when clearly free to use, community EARS posts with public data).
- Targets that are published research or community standards (Harman OE 2018 family, Diffuse Field, JM-1 / IEF-style IEM targets, etc.).
- EQ derived from those public sources (including explaining AutoEQ outputs as *derivative*, not new measurements).

**Refuse or redirect**

- Helping circumvent paywalls or redistribute closed measurement packs the user does not have a legitimate right to use.
- Claiming medical / hearing-restoration outcomes.
- Mixing incompatible rigs into one “truth” FR (see below).

Keep refusals short: decline the piracy/paywall step, then offer the same workflow with a public source.

---

## Step 0 — Clarify the product class

| Class | Typical fit | Default target family |
|--------|-------------|------------------------|
| Over-ear / on-ear (OE) | Pads seal around or on the pinna | Harman OE 2018 (or bass-tilted variants) |
| IEM / earbud in-canal | Tip seal in ear canal | JM-1 / IEF-style or similar IEM preference curves |
| Semi-open / unusual form | Ambiguous | Ask OE vs IEM seal; do not guess from marketing alone |

If the user only names a model, classify OE vs IEM first. Never invent a “house default” headphone.

---

## Step 1 — Choose a target

### Over-ear / on-ear

1. **Harman OE 2018** — Common starting point for pads that seal reasonably. Strong bass shelf relative to diffuse field; many listeners like it “as is.”
2. **Harman with less bass** — Same mid/treble shape, reduced low-shelf (often −2 to −6 dB vs full Harman bass, or a published “less bass” variant). Use when the user reports boom, fatigue, or prefers leaner bass.
3. **Diffuse Field (DF)** — Flatter bass than Harman OE; useful as a neutral-ish reference or when Harman bass is unwanted. Not interchangeable with IEM DF without checking the exact DF definition used.

### IEMs

1. **JM-1 / IEF-style** (and closely related community IEM preference targets) — Prefer these over raw Harman OE for in-canal products; canal coupling and target definitions differ.
2. Avoid blindly applying **Harman OE 2018** to IEMs unless the user explicitly wants that experiment and understands the mismatch.
3. If the user cites a named IEM target (e.g. a specific IEF revision), stick to that revision’s published curve—do not silently substitute another.

### Quick chooser

```
Is it an IEM / deep-seal earbud?
  yes → JM-1 / IEF-style (or user-named IEM target)
  no  → OE path:
          wants Harman bass? → Harman OE 2018
          wants less boom?   → Harman less-bass / tilted
          wants DF-neutral?  → Diffuse Field
```

Document the **exact target name + revision/year** in the EQ notes.

---

## Step 2 — Get a public FR (and keep the rig honest)

### Source hygiene

1. Prefer one primary public measurement set with a known coupler/rig.
2. Record: measurer, date if available, **rig**, tip/pad used, and whether raw or compensated.
3. Prefer CSV / numeric export over eyeballing a screenshot when possible.

### Never mix these as if they were the same FR

Do **not** average, splice, or “trust the midpoint” across:

| Rig / coupler family | Note |
|----------------------|------|
| GRAS (e.g. 43AG / RA040x-style headphone setups) | Common industry headphone coupler family |
| HMS II.3 (HEAD acoustics) | Different geometry / transfer |
| miniDSP E.A.R.S. | Hobby / different compensation; useful but not GRAS-equivalent |
| B&K / GRAS 5128 (ear simulator) | Different standard; not drop-in with older 711-style workflows |

**Rule:** One product → one rig family for the EQ chain. Comparing *shapes* across rigs for curiosity is fine; feeding mixed CSVs into one PEQ solver is not.

### Seating / seal variance

- Pad rotation, clamp, hair, glasses, and tip insertion depth move bass and lower midrange several dB.
- Treat a single trace as **one seating**, not absolute truth.
- If two public traces on the **same** rig disagree mainly below ~200 Hz, prefer a mild bass correction or ask the user to A/B shelf gain rather than chasing every wiggle.

### AutoEQ and similar libraries

- AutoEQ (and clones) produce **EQ that aims a given measurement at a given target**. The result is **derivative**, not a new FR measurement.
- Prefer stating: measurement source + target + tool/version when known.
- Do not present AutoEQ’s “corrected” curve as an independent lab FR.

---

## Step 3 — Optional short example (illustration only)

**Example model:** Razer BlackShark V2 X (generic illustration—not a recommended default).

1. Classify: over-ear gaming headset → OE target path (e.g. Harman OE 2018 or less-bass).
2. Find public FR:
   - **Crinacle** (or similar graph DB) — if listed; note coupler.
   - **RTINGS** — if listed; note their methodology differs from hobby 711/GRAS dumps.
   - **Hobby miniDSP E.A.R.S.** posts — fine for a rough DIY chain, but **do not** merge with GRAS/HMS/5128 CSVs.
3. Pick **one** source. If only E.A.R.S. exists publicly, say so and keep expectations modest.
4. Proceed to Step 4 with that single FR + chosen OE target.

No serial numbers, no “user’s unit,” no shipping addresses—ever.

---

## Step 4 — From FR to parametric bands

### 4.1 Align units

- Work in dB SPL (or relative dB) vs frequency (Hz), log-x mentally or in tools.
- Ensure FR and target share the same compensation philosophy (raw vs ear-compensated). If one is compensated and one is not, stop and fix that first.

### 4.2 Form an error curve

```
error(f) = target(f) − measurement(f)
```

Positive error ⇒ need boost at `f`; negative ⇒ cut.

Optional: smooth lightly (e.g. fractional-octave) before fitting to avoid fitting mic noise and one-off seating spikes.

### 4.3 Fit PEQ bands

Common practical pattern:

1. **Low shelf** (~40–105 Hz hinge) for overall bass vs target.
2. **High shelf** or broad bell in presence/treble for tilt.
3. **3–8 peaking filters** for narrower mismatches (200 Hz–8 kHz).
4. Prefer **cuts** for sharp peaks when possible (headroom / harshness).
5. Keep Q moderate unless a real narrow resonance is visible on the **same** rig repeatedly.
6. Stay within sane gain (often ±6 dB per band unless the FR clearly needs more); warn if preamp negative gain is required to avoid digital clipping.

**Minimum band report fields**

| Field | Meaning |
|--------|---------|
| Type | peak / lowshelf / highshelf / etc. |
| Fc (Hz) | Center or shelf frequency |
| Gain (dB) | Signed |
| Q or S | Bandwidth control (state which) |

Also state: **preamp / input gain** if peak positive sum risks clipping.

### 4.4 Tooling options (generic)

- Spreadsheet or script: error curve → manual or optimizer-placed bands.
- Established open tools/libraries that take measurement + target → Peace/Equalizer APO, CamillaDSP, Wavelet, etc. export.
- Manual “cookbook” placement: shelves first, then largest error humps, then fine peaks.

Do not require a specific proprietary app.

### 4.5 Verify

1. Re-apply bands to the measurement; overlay vs target.
2. Check 100–200 Hz (seal) and 2–6 kHz (harshness) carefully.
3. Tell the user to trim **global** bass/treble by ear ±1–2 dB after the cook—targets are averages, not law.

---

## Step 5 — Deliverable template

Use this structure in replies:

```markdown
## Product class
OE | IEM

## Measurement
- Source: [public link or database name]
- Rig: [GRAS | HMS II.3 | E.A.R.S. | 5128 | other—pick one]
- Notes: tip/pad, raw vs compensated

## Target
- Name + revision: [e.g. Harman OE 2018 | Harman less-bass | DF | JM-1 / IEF-style]
- Why: [one line]

## PEQ
| Type | Fc (Hz) | Gain (dB) | Q |
|------|---------|-----------|---|
| ...  | ...     | ...       | ... |

Preamp: [dB]

## Caveats
- Single-rig only; seating variance; not medical advice
```

---

## Step 6 — Quality checklist

- [ ] OE vs IEM target matches product class
- [ ] Single measurement-rig family end-to-end
- [ ] Target named with revision/year when applicable
- [ ] AutoEQ/derivative outputs labeled as such
- [ ] No paywalled dump redistribution
- [ ] No personal serials, private addresses, or “default” user headphones
- [ ] Preamp / clipping mentioned if boosts exist
- [ ] User told to fine-tune bass/treble by ear

---

## Short refusal examples

- **Paywalled FR pack:** “I can’t help extract or share that paywalled measurement set. If you have a public FR (same model, one rig), we can cook PEQ from that.”
- **Mixed rigs:** “Those CSVs are from different couplers. Pick one rig’s curve and we’ll target from there.”
- **IEM + Harman OE without caveat:** “For IEMs, JM-1 / IEF-style is the usual starting family; Harman OE is an OE preference curve—use only if you explicitly want that mismatch.”

---

## One-page flow

1. Classify OE vs IEM → pick target family.
2. Grab **one** public FR; lock the rig; don’t mix GRAS / HMS II.3 / E.A.R.S. / 5128.
3. error = target − measurement; fit shelves + peaks; set preamp.
4. Label derivatives (AutoEQ, etc.); refuse paywall piracy; scrub personal gear.
5. Hand off bands + caveats; user trims by ear.

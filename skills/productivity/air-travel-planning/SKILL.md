---
name: air-travel-planning
description: Use when assessing flight feasibility around hard events or deadlines.
version: 1.0.0
license: MIT
---

# Air Travel Planning

## Overview

Assess whether a trip can satisfy fixed commitments using live itineraries, local calendar dates, ground-transfer time, sleep constraints, and disruption risk. The useful output is not merely “a flight exists”; it is a realistic door-to-door plan with a clear recommendation and fallback posture.

## When to Use

Use for:

- Weddings, conferences, work shifts, exams, or other hard commitments around air travel
- “Can this work?” questions involving different time zones
- Choosing between a humane itinerary and a more disruption-resistant one
- Determining whether the traveler can reach home, sleep, and function before the next obligation

Do not use this skill alone for visa, entry-rule, or medical-fitness questions; verify those from authoritative sources separately.

## Core Workflow

### 1. Normalize the calendar

Write down every fixed event with its **local date, local time, and place**:

- Last event at origin
- Earliest plausible airport departure
- Flight arrival at destination
- Required arrival at home/hotel
- Next hard obligation

Check the weekday against the year when the user gives weekday plus month/day. Never infer that an overnight flight arrives on the same calendar date. Completion criterion: each hard boundary is attached to a location and local date.

### 2. Search the actual travel date

Use a live flight-search source and inspect individual itineraries. Capture:

- Departure and arrival local times and dates
- Total duration
- Number of stops
- Connection airports and layover lengths
- Operating/marketing carriers
- Whether it can be booked as one protected ticket

Search results that silently assume a round trip may show a dummy return date and round-trip price. Do not present that price as the requested fare unless the user's full trip matches it. The outbound schedule can still establish feasibility.

For browser-based Google Flights extraction and consent handling, see `references/google-flights-browser-workflow.md`.

### 3. Add the missing door-to-door legs

A runway arrival is not “home.” Add realistic allowances for:

- Hotel/venue to origin airport
- Check-in and security
- Immigration and baggage claim
- Destination airport to bed or commitment

Use maps or official airport/transit sources when those legs materially affect feasibility. Distinguish a sourced duration from a planning allowance.

### 4. Separate feasibility from resilience

Classify each viable option on two axes:

- **Human cost:** sleep lost, post-event departure time, total duration, jet lag
- **Operational margin:** arrival buffer, number of stops, layover tightness, last useful connection, and recovery options after disruption

A later departure may preserve sleep but place the traveler one missed connection away from missing work. An early departure may be miserable but leave an entire afternoon for recovery or reaccommodation. State this tradeoff explicitly.

Prefer:

- One protected through-ticket over separate tickets
- One stop over two when timing is comparable
- Earlier same-day arrival when the next commitment is non-negotiable
- A connection long enough to be legal and plausible, while recognizing that a legal connection is not a guarantee

### 5. Recommend by consequence of failure

Give a direct recommendation conditioned on stakes:

- **Balanced option:** preserves the event and some sleep while still arriving in time
- **Safety-first option:** larger arrival margin, even if unpleasant
- **Reject option:** arrives after the deadline or depends on an implausible transfer

Avoid vague “it depends” endings. If one missing fact would change the decision—such as the exact Thursday start time—state the assumed default and name that fact.

## Output Pattern

Lead with the verdict:

> **Yes, this is feasible**, assuming the next commitment is ordinary daytime work.

Then provide:

1. **Best-balance itinerary** — local times, stops, arrival, why it works
2. **Safety-first itinerary** — larger buffer and its human cost
3. **Door-to-door reality** — likely airport departure and bed-arrival window
4. **Judgment** — which option to book based on failure consequences
5. **Risk note** — one ticket, delay/misconnect exposure, and any assumption

Keep the response decision-oriented. The user generally needs a recommendation, not an exhaustive dump of every flight.

## Common Pitfalls

1. **Ignoring the date line/time-zone advantage.** Show local departure and arrival dates; westbound long-haul travel can return the traveler surprisingly early on the same date.
2. **Treating airport arrival as bedtime.** Include immigration, baggage, and the final ground leg.
3. **Optimizing only for sleep.** A humane late departure may have little recovery margin if a connection fails.
4. **Optimizing only for reliability.** A pre-dawn departure after a late event may technically work but leave the traveler unsafe or nonfunctional.
5. **Quoting misleading prices.** A search engine's default return date can make the displayed round-trip fare irrelevant.
6. **Listing options without judgment.** Name the balanced and safety-first choices and explain which stakes justify each.
7. **Assuming separate tickets are protected.** Verify through-ticket status or clearly label self-transfer risk.
8. **Overstating certainty.** Schedules and fares can change; ground the current answer in the live result and label planning allowances.

## Verification Checklist

- [ ] Weekday, year, and local dates are consistent
- [ ] At least one live itinerary arrives before the true door-to-door deadline
- [ ] Arrival date is explicit, including any `+1` day
- [ ] Ground transfer and airport processing are accounted for
- [ ] Sleep/human-cost tradeoff is stated
- [ ] Disruption margin and ticket protection are considered
- [ ] Displayed price is not misrepresented because of a dummy return date
- [ ] Final answer gives a direct recommendation, not just options

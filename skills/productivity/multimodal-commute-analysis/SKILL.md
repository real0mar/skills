---
name: multimodal-commute-analysis
description: Use when comparing transit-plus-walk/bike commute options. Build schedule-aware, station-to-door estimates from official transit data and routed last-mile legs.
version: 1.0.0
license: MIT
---

# Multimodal Commute Analysis

## Overview

Compare commute options as complete chains rather than quoting a single map-app duration. Separate scheduled transit, transfer/egress, and walking or cycling; then distinguish **moving time**, **realistic platform-to-door time**, and **wait-sensitive time**.

This complements `maps`: use `maps` for geocoding and street routing, and this skill for schedule extraction, multimodal composition, frequency effects, and decision-quality comparison.

## When to Use

Use for questions such as:

- “Train A plus bike versus Train B plus walk?”
- “Which commute is faster if I time the departure?”
- “How much does frequency change the answer?”
- “Compare station-to-office or door-to-door transit options.”

Do not use for a simple walking, cycling, or driving route with no scheduled service; load `maps` alone.

## Required Output Model

For each option, identify:

1. **Declared origin and destination** — preserve exactly what the user specified.
2. **Transit leg** — scheduled departure/arrival and in-vehicle minutes.
3. **Last-mile leg** — routed distance and time for the requested mode.
4. **Mechanical total** — transit minutes + routed last-mile minutes.
5. **Realistic total** — add a clearly labeled practical allowance for station exit, stairs, bike unlocking/parking, or transfer movement.
6. **Schedule sensitivity** — frequency, service window, and relevant disruptions.

Never silently compare different origins as if they were door-to-door equivalents. Call out an apples-to-oranges origin mismatch and, when useful, explain what extra access leg would be required for a same-origin comparison.

## Workflow

### 1. Lock the comparison scope

Extract:

- exact start point for each option;
- exact destination;
- weekday/weekend and time-of-day, if given;
- transit service class (local, limited, express);
- last-mile mode for each option;
- whether the user is asking station-to-door or true door-to-door.

If time/date is omitted, use the current normal weekday schedule as the default when the question names a commuter express service, and label that assumption. Completion criterion: every option has a defined origin, transit service, endpoint, and last-mile mode.

### 2. Use official transit data first

Preferred evidence order:

1. Transit agency timetable or trip planner.
2. Transit agency GTFS or public endpoint.
3. A reputable journey planner as cross-check.
4. Search snippets only as discovery, not final evidence.

For a web timetable rendered as a matrix:

- identify the correct direction table;
- extract the header row of train/run IDs;
- locate origin and destination station rows;
- compare cells in the **same column**;
- classify runs from the agency legend rather than guessing from elapsed time.

For a dynamic planner in an iframe, use accessibility-tree controls where possible. Select the station suggestions rather than leaving free text unresolved. Preserve the planner’s displayed departure, arrival, and total duration.

Completion criterion: transit time is backed by one matching scheduled run or an official planner result, not inferred from distance.

### 3. Route the last mile independently

Use `maps` or a public routing engine with the exact station entrance/coordinates and destination address. Record:

- mode;
- distance;
- routed time;
- source.

If name geocoding fails, recover coordinates from an authoritative station page, OpenStreetMap object, agency station page, or a well-sourced encyclopedia page, then route by coordinates. Do not replace a failed bike route with straight-line distance.

Completion criterion: last-mile time follows a street/path network and uses the requested mode.

### 4. Compute totals with a tool

Use Python or another calculation tool; do not mentally add or subtract travel times.

Report:

```text
mechanical_total = scheduled_transit + routed_last_mile
realistic_total = mechanical_total + practical_egress_allowance
```

The allowance is not fake precision. Present it as a range and say what it covers. Typical contributors include platform egress, fare gates, stairs, unlocking a bike, and parking it at the destination.

Completion criterion: all totals reproduce from the listed components.

### 5. Analyze frequency separately from speed

A faster scheduled run may be worse for an untimed arrival. Show both:

- **Timed trip:** assumes the user arrives to catch the selected run.
- **Random arrival:** discusses headway and expected wait qualitatively or quantitatively.

If using an expected random wait, state the assumptions; `headway / 2` applies only to approximately regular, uncorrelated arrivals. Do not add that expectation to a timed commuter trip.

Also identify limited service windows. An express that runs only during peaks is not a general all-day option.

Completion criterion: the recommendation says whether it assumes schedule alignment.

### 6. Check alerts and operational constraints

Look for official alerts affecting the route or time window. Include only alerts that materially change the comparison. Also note mode constraints such as bike restrictions, inaccessible platforms, transfer construction, or late-night service changes when relevant.

Completion criterion: either a relevant alert is stated with scope, or the answer avoids implying that live service was checked.

## Presentation Format

Lead with a compact table:

| Option | Transit | Last mile | Mechanical total |
|---|---:|---:|---:|
| Route A | X min | Y min / distance | Z min |
| Route B | X min | Y min / distance | Z min |

Then provide:

- **Difference:** one sentence with the tool-computed delta.
- **Realistic range:** one short bullet per option.
- **Decision:** timed-departure winner versus frequency-sensitive caveat.
- **Scope warning:** only if origins or endpoints differ.

Avoid drowning a simple commute decision in every departure time. List exact departures only when sparse service or peak-only operation materially affects the answer.

## Common Pitfalls

1. **Comparing unlike origins.** “Station A versus Station B” is not a true door-to-door comparison. Preserve the requested comparison, then flag the mismatch.

2. **Using a timetable cell from the wrong run.** Match origin and destination by the same train/run column.

3. **Calling every fast train an express.** Use the agency’s legend or run numbering.

4. **Treating map-app transit totals as pure in-vehicle time.** Inspect the itinerary; it may include access walking or waiting.

5. **Ignoring frequency.** Separate run time from expected wait and service span.

6. **Using straight-line last-mile estimates.** Route on the actual pedestrian or bicycle network.

7. **False precision.** Preserve exact source values internally, but present sensible rounded minutes and a practical range.

8. **Overstating live status.** Static schedules answer normal travel time; alerts and real-time feeds answer current operations.

## Consolidated Transit Coverage

This skill also covers non-commute transit comparisons with walking or cycling legs, formerly handled by `multimodal-transit-comparison`. Route access as well as egress when claiming true door-to-door time; keep waiting separate from timed movement and practical station-exit allowances.

- `references/bay-area-transit-sources.md` — Caltrain/BART entry points, timetable matching, and Valhalla routing examples. Reverify dated station IDs and service classes before use.

## Reference Files

- `references/source-playbook.md` — extraction patterns for agency timetable matrices, iframe trip planners, coordinate fallback, and last-mile routing.

## Verification Checklist

- [ ] Exact origin and destination for every option are explicit.
- [ ] Transit duration comes from an official matching itinerary or timetable column.
- [ ] Last-mile distance/time is network-routed in the requested mode.
- [ ] Totals and differences were calculated with a tool.
- [ ] Timed travel and frequency/wait effects are not conflated.
- [ ] Peak-only or sparse service is identified.
- [ ] Relevant alerts are scoped by time and segment.
- [ ] Different origins are called out rather than hidden.
- [ ] Final answer starts with the comparison, not the research process.

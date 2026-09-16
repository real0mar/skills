# Timed Road-Trip Stop Selection

Use when the user gives a departure time and a desired stopping/bedtime rather than a fixed lodging corridor.

## Decision model

1. Resolve the departure to an explicit date and local time.
2. Use a traffic-aware routing source with **Depart at**, not a static no-traffic router alone.
3. Identify lodging clusters that bracket the cutoff:
   - **Conservative stop:** expected arrival before the cutoff even near the slow end of the typical range.
   - **Target stop:** expected arrival at or just after the cutoff, if the user accepts a small overrun.
   - **Too far:** slow-end arrival materially exceeds the cutoff.
4. Verify lodging and vehicle constraints only for the bracketed clusters; avoid researching destinations the driver is unlikely to reach.
5. Give a live fallback rule tied to the navigation ETA at the last practical decision point.

## Google Maps browser pattern

1. Open directions from the real origin (not merely a region) to a candidate property.
2. Select **Leave now → Depart at**.
3. Set the explicit departure time and calendar date.
4. Read the displayed typical duration range and arrival time.
5. Repeat by replacing only the destination, preserving the departure settings.
6. Treat the upper end of the typical range as the planning value when the user has a hard fatigue/bedtime cutoff.

Google Maps may initially default to the current date or time. Confirm the rendered date and time after every destination change.

## Ranking operational lodging

A hotel exactly at the nominal cutoff is not automatically best. Rank the full overnight operation:

- route detour and re-entry cost;
- expected arrival against the fatigue cutoff;
- room availability and real all-in price;
- charging reliability and connector compatibility;
- whether charging requires staying awake after arrival;
- next-morning departure friction.

When overnight Level 2 is sparse or unreliable, an on-property bank of reliable DC fast chargers can be the better road-trip choice. Say explicitly that this substitutes a short arrival/morning charging session for passive overnight charging; do not describe DCFC as Level 2.

## Output pattern

- **Primary stop:** one property and why.
- **Expected arrival:** traffic-aware range for the stated departure.
- **Vehicle operation:** connector, count, reliability, and whether charging happens overnight or before bed.
- **Fallback rule:** “At [decision point], continue if ETA is ≤ X; otherwise stop at Y.”
- Mention one rejected tempting option only when its failure explains the recommendation (for example, offline charging or a route detour).

## Pitfalls

- Static OSRM/no-traffic duration can misplace a Friday-evening stop by an entire lodging cluster.
- A midpoint or fixed-mile stop is inferior to a departure-time/arrival-cutoff calculation.
- Do not recommend driving beyond the user's fatigue cutoff merely to maximize next-day progress without clearly labeling the overrun.
- Do not let a nominal charger count outrank recent operational status.
- If the exact vehicle/connector is unknown, state connector assumptions or favor a site with broad fast-charging compatibility; ask only if the ambiguity changes the recommendation materially.

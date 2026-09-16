---
name: road-trip-lodging-research
description: Use for route-corridor lodging with vehicle constraints.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [travel, lodging, road-trip, hotels, ev-charging, price-comparison]
    related_skills: [maps, grounded-citations, purchase-deal-comparison]
---

# Road-Trip Lodging Research

## Overview

Use this skill to find and price lodging along a driving corridor when the stay has operational constraints such as overnight EV charging, trailer access, secure parking, late arrival, or proximity to a route. The result should be a short, ranked recommendation backed by current hotel inventory and constraint-specific evidence—not a generic hotel list.

## When to Use

Use for requests such as:

- “Find lodging between A and B, inclusive.”
- “Which hotel has enough reliable overnight Level 2 charging?”
- “Price the smallest room this Friday for one adult.”
- “Find a route hotel with trailer-friendly parking or another vehicle constraint.”

For flights around hard events, use `air-travel-planning`. For generic directions or POIs, use `maps`.

## Procedure

### 1. Normalize the corridor and stay

Record:

- Corridor endpoints and whether they are inclusive
- Direction of travel and acceptable detour from the route
- Stay date as explicit check-in and check-out dates
- Number of adults/rooms
- Smallest acceptable room and cancellation preference
- Vehicle and connector requirements

If “this Friday” is unambiguous, resolve it to dates and proceed. Do not ask a low-value clarification.

### 2. Convert a bedtime cutoff into reachable lodging clusters

When the user gives a departure time and says to stop around a particular time, do not assume a geographic midpoint or reuse an earlier corridor. Use a traffic-aware **Depart at** estimate for the explicit date and time, then bracket the cutoff with:

- a conservative cluster whose slow-end arrival remains before the cutoff;
- a target cluster around the cutoff;
- the next cluster only if a small, clearly labeled overrun is acceptable.

Use the upper end of the typical travel-time range for a hard fatigue cutoff. A static no-traffic route is useful for distance and sanity checks, but not as the final stop selector for Friday-evening traffic. Give a live fallback rule at the last practical decision point: continue only if navigation ETA remains below a stated threshold.

See `references/timed-stop-selection.md` for the traffic-aware browser workflow, ranking model, and fallback format.

### 3. Enumerate plausible lodging clusters

Use the route and settlements/exits between the endpoints to identify candidate clusters. Search the full corridor, not merely the named endpoints or one metro area. Keep only properties within the user’s detour tolerance. If a timed cutoff was provided, research only the bracketed reachable clusters rather than the entire route.

### 4. Translate amenities into measurable requirements

Avoid treating a hotel’s “EV charging available” badge as sufficient. For overnight Level 2 charging, verify:

- Connector type (J1772, NACS, or outlet)
- Number of plugs versus number of physical stations
- Rated and recently observed power
- Whether plugs can charge simultaneously
- 24/7 and overnight access rules
- Guest-only versus public access
- Energy, session, idle, and parking fees
- ICEing, shared-breaker, outage, or access-gate reports
- Distance from the actual lodging property

Interpret “ample” as both enough connectors and a credible chance of simultaneous overnight use. A nominal five-plug installation with recurrent breaker trips is not ample in practice.

### 5. Triangulate each serious candidate

Use at least:

1. Official hotel page for lodging identity, amenities, parking, and direct rate
2. PlugShare or equivalent community source for plug count, current status, and recent check-ins
3. ChargePoint/ChargeHub/ChargeFinder or another network/source for connector, power, live availability, and pricing when available

Search snippets are discovery evidence. Open the serious candidates and read recent check-ins before ranking. Prefer recent operational evidence over old amenity badges.

### 6. Stop searching once the decision is supported

Set an evidence budget: enumerate the corridor, verify the top 2–4 plausible properties, and synthesize once one clear winner and credible backups are established. Do not keep issuing near-duplicate searches after the requested comparison is answerable.

### 7. Price the exact stay configuration

For each finalist, set:

- Explicit check-in/check-out dates
- One room
- Actual traveler count
- Smallest available room
- A price display that includes taxes and mandatory booking fees when possible

Verify the date and traveler fields in the rendered booking UI. Do not assume URL query parameters were honored. Hotel pages may label a room “2 guests” because that is its capacity even when the search correctly has one traveler; room pricing usually does not fall for solo occupancy.

Record separately:

- Direct/official or major-OTA total
- Cheapest surfaced third-party total
- Room type
- Cancellation terms
- Mandatory parking/resort/destination fees
- Charging cost, which is normally separate from the room total

Treat unusually cheap minor-OTA rates as a separate risk tier rather than calling them the default winner.

### 8. Deliver a compact result

Use this order:

1. **Verdict** — best operational match
2. **Comparison table** — hotel, room total, room type, verified constraint capacity/reliability
3. **Material caveats** — only property-specific issues
4. **Recommendation** — direct/major-site versus cheapest minor OTA if they differ

Do not lead with the research diary or a tool-limit explanation. If enough evidence exists, answer despite a late research-tool failure.

## Consolidated Planning Guidance

- Separate the literal cheapest property, a practical cleanliness/reliability floor, and the trip-optimal stop. Flag severe room-quality tradeoffs rather than optimizing only for price.
- Establish whether charging must be overnight Level 2 or whether DC fast charging before bed/after waking is acceptable. Onsite or nearby DCFC is a fallback, not fulfillment of an explicit overnight-L2 requirement.
- Lead with the recommended stop, expected arrival range, room total and booking channel, charging reality, and an en-route fallback rule. Explicitly disclose any sleep-cutoff overrun.
- See `references/hotel-price-and-ev-verification.md` for the consolidated traffic, pricing, room-quality, and charger-verification playbook formerly in `road-trip-lodging-planning`.

## Google Hotels Browser Pattern

When Google Travel is the practical live-pricing source:

1. Open the hotel or a tightly scoped hotel search.
2. Set check-in and check-out in the visible UI.
3. Set travelers to the requested count.
4. Confirm all three rendered fields after the page refreshes.
5. Set price display to “nightly price with fees” when offered.
6. Read the official-site room type/price and the “All options” list separately.
7. Report the cheapest minor-OTA listing as an alternative, not as equivalent to direct booking.

See `references/ev-corridor-hotel-example.md` for a worked evidence pattern and UI verification notes.

## Common Pitfalls

1. **Counting stations instead of plugs.** Dual-head stations may expose more connectors than station objects.
2. **Equating advertised count with usable capacity.** Shared breakers and outages can erase nominal abundance.
3. **Using a hotel amenity badge as operational evidence.** Verify connector, access, power, and current check-ins.
4. **Ignoring overnight pricing mechanics.** Hourly parking or idle fees can dominate the charging bill.
5. **Trusting date parameters without checking the UI.** Booking pages may reset dates or traveler count.
6. **Mixing room and charging totals.** State clearly what the hotel total includes.
7. **Promoting a suspiciously cheap OTA without qualification.** Show direct/major-site and minor-OTA prices separately.
8. **Continuing research after reaching a supported answer.** Synthesize rather than exhausting search calls.

## Verification Checklist

- [ ] Corridor endpoints and intermediate lodging clusters covered
- [ ] If departure/cutoff times were given, traffic-aware date/time and slow-end ETA verified
- [ ] A conservative fallback stop or live ETA threshold provided when useful
- [ ] Exact stay dates and traveler count confirmed in rendered UI
- [ ] Smallest available room identified
- [ ] Taxes and mandatory booking fees included or clearly labeled
- [ ] Direct/major-site price separated from minor-OTA price
- [ ] Connector type, plug count, and power verified
- [ ] Recent reliability and simultaneous-use evidence reviewed
- [ ] Parking and charging fees separated from room total
- [ ] One clear recommendation given

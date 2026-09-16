# EV Corridor Hotel Worked Example

## Scenario

Find lodging along California I-5 between Tejon Ranch and Santa Clarita, inclusive, with ample overnight Level 2 charging; then price Friday night for one adult in the smallest room.

This is a worked evidence pattern from August 2026, not a durable inventory or price list. Re-check all operational and price facts before reuse.

## Candidate verification pattern

### Best Western Liberty Inn, Lebec

- Official hotel sources advertised onsite EV charging.
- PlugShare identified four ChargePoint charging stations at the hotel.
- This was the strongest corridor match because the charging count was meaningful and directly associated with the lodging property.
- Exact current power, fees, and overnight access should still be rechecked before recommending.

### Homewood Suites Santa Clarita

- Network/community sources showed three physical ChargePoint stations exposing five J1772 plugs, nominally up to 6.48 kW, open 24/7.
- ChargeHub listed energy pricing plus a per-hour parking charge.
- Recent PlugShare check-ins materially changed the ranking: one reported breaker trips whenever two cars charged, and another reported only one working plug despite five installed.
- Lesson: five advertised plugs did not equal ample simultaneous overnight capacity.

### SpringHill Suites Valencia

- Three J1772 ChargePoint plugs were visible at the hotel, nominally 6.48 kW and open 24/7.
- Recent users reported roughly 3 kW actual charging and high effective pricing.
- Lesson: count, observed power, and cost all matter; an amenity badge alone is weak evidence.

## Live pricing pattern that worked

Google Travel did not reliably honor dates embedded in the initial URL. The working sequence was:

1. Open the specific hotel or tightly scoped hotel search.
2. Open its Prices view when needed.
3. Type check-in and check-out into the visible fields.
4. Change travelers from the default two adults to one.
5. Refresh/snapshot and confirm the rendered fields show the requested dates and one traveler.
6. Confirm the display says “nightly price with fees.”
7. Read the official-site room name and total separately from the “All options” aggregator list.
8. If accessibility snapshots truncate the rate list, inspect rendered `document.body.innerText` around “Official Site”; use this only to read the already-rendered page, not to invent missing data.

A room line may still say “2 guests” after the traveler control is set to one because that line describes room capacity. Confirm the traveler control itself rather than treating room capacity as proof that the search is wrong.

## Delivery lesson

Once one winner and two credible backups were verified, the correct action was to synthesize. Continuing near-duplicate searches exhausted the per-turn search budget and produced an irrelevant blocker message even though enough evidence already existed. Use a candidate/evidence budget and answer when the requested decision is supported.

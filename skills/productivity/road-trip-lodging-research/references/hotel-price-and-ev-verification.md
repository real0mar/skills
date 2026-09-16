# Hotel Price and EV Verification

## Evidence hierarchy

### Routing and arrival
1. Traffic-aware route planner with the trip's future departure date/time.
2. Live traffic on departure day.
3. Traffic-free routing only as a distance and lower-bound check.

Use the planner's typical range. A displayed midpoint such as “arrive around 10:00” can hide a 30–60 minute upper bound.

### Room price
1. Hotel's official booking flow for the exact dates.
2. Major OTA with an explicit total and cancellation policy.
3. Metasearch listing used only to discover candidates.
4. Obscure resellers treated as a separate risk tier, never as interchangeable with direct booking.

Record:
- Check-in/out dates
- One room and actual guest count
- Smallest available room type
- Total including taxes/mandatory fees
- Refundability cutoff
- Parking or destination fees
- Seller/merchant of record

If a metasearch page advertises an unusually low price, open the property-price panel and identify the seller. A low teaser from a subscription-linked or wholesale OTA may have stricter support and refund paths.

## Dynamic Google workflow

### Historical traffic
1. Open Google Maps directions for origin → candidate hotel.
2. Select **Leave now → Depart at**.
3. Enter the actual departure time and date.
4. Capture the typical travel-time range and stated arrival time.
5. Repeat for the early fallback and stretch target.

### Hotel pricing
1. Open Google Hotels for the town or exact property.
2. Set exact dates and guest count; interfaces often retain or reset stale dates, so verify the visible fields after every navigation.
3. Select “nightly price with fees” when available.
4. Open **View prices**, then capture room type and direct/OTA totals.
5. If the page still labels the room “2 guests” after selecting one traveler, interpret it as room capacity unless the search control itself reverted.

## EV station verification

Cross-check operator/hotel data with a community station page. Capture:

| Field | Why it matters |
|---|---|
| Plug count | Better measure than pedestal/station count |
| Connector | J1772, NACS, CCS, CHAdeMO, outlet |
| Power | Determines whether an overnight fill is realistic |
| Simultaneous capacity | Shared breakers/load management may cut reliability |
| Access | Guests only, public, valet, gated, 24/7 |
| Price | Energy, session, parking, and idle fees can dominate |
| Recent check-ins | Reveals outages, derating, ICEing, breaker trips |
| Alternatives | Nearby DCFC can rescue a failed hotel charger |

Do not call a property “ample overnight L2” merely because it advertises several ports. Recent reports of only one working plug or breakers tripping under two-car load defeat the nominal count.

## Decision framing

Present three concepts separately when useful:

- **Literal cheapest:** lowest displayed room price, with seller and quality warning.
- **Practical floor:** lowest property that meets basic cleanliness/reliability expectations.
- **Trip-optimal:** best combination of cutoff-compatible arrival, room quality, and charging certainty.

A good final recommendation is operational: target one hotel, state the expected arrival range, and provide a point on the route where the user should switch to the fallback if ETA slips.
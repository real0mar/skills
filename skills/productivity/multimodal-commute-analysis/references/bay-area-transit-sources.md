# Bay Area transit source notes

Use these as source-entry points; schedules and advisories are time-sensitive and must be rechecked.

## Caltrain

- Official site and schedule table: <https://www.caltrain.com/>
- On the homepage, open the **Schedules** tab and select weekday/weekend as appropriate.
- Station IDs observed in the schedule controls:
  - San Francisco: `7001`
  - 22nd Street: `7002`
  - Millbrae: `7006`
  - San Mateo: `7009`
- Train-number families shown by Caltrain:
  - `1XX` local
  - `4XX` limited
  - `5XX` express
  - `6XX` weekend local
  - `8XX` South County Connector
- For precise runtime, inspect the northbound or southbound timetable DOM. Pair the origin and destination cells using the same column index and train number. This avoids visually misaligning a very wide table.
- 22nd Street station location reference: 1149 22nd Street, San Francisco; approximately `37.7572, -122.3925`. Reverify before routing.

## BART

- Official trip planner: <https://www.bart.gov/planner>
- The planner is commonly embedded in an iframe. Accessibility snapshots can still expose the origin/destination textboxes, station suggestions, search button, and result cards.
- Select exact station suggestions rather than submitting free text. Result cards provide departure, arrival, and total travel time.
- Official schedule page: <https://www.bart.gov/schedules>
- Check the service-alert banner, especially for planned work affecting SFO, Millbrae, Daly City, or late-night service.

## First/last mile

- Valhalla public routing can estimate pedestrian and bicycle legs when a maps client cannot geocode a transit station:

```text
https://valhalla1.openstreetmap.de/route?json=<URL-encoded JSON>
```

Example request body:

```json
{
  "locations": [
    {"lat": 37.7572, "lon": -122.3925},
    {"lat": 37.7647, "lon": -122.4136}
  ],
  "costing": "bicycle",
  "units": "miles"
}
```

Use `"pedestrian"` for walking. Convert returned seconds to minutes with a calculation tool, and retain the returned distance for a plausibility check.

## Interpretation pattern

Report:

1. Scheduled station-to-station ride time
2. Independently routed last-mile time and distance
3. Sum of the two
4. A realistic range allowing for platform exit and bike handling
5. Service frequency and expected-wait implications
6. Any mismatch in the routes’ true starting points

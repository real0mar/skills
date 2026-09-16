# Source and Extraction Playbook

Load this reference when official transit pages are dynamic, timetable-shaped, or difficult to query directly.

## Official timetable matrix

Many commuter-rail pages expose one table per direction:

- first row: train/run IDs;
- first columns: zone and station;
- remaining cells: scheduled times or a bypass marker;
- nearby legend: service class encoded in run numbers or colors.

Reliable extraction:

1. Choose direction from table context, not station order alone.
2. Read header IDs and station rows from the DOM/accessibility tree.
3. Locate the exact origin and destination rows.
4. For each requested service class, compare times at the same column index.
5. Parse AM/PM explicitly and account for midnight rollover.
6. Verify at least one result against the visible page.

A browser-console extraction can return a compact matrix without copying a huge page:

```js
Array.from(document.querySelectorAll('table')).map((table, index) => ({
  index,
  header: Array.from(table.rows[0]?.cells || []).map(c => c.innerText.trim()),
  rows: Array.from(table.rows)
    .filter(r => /ORIGIN|DESTINATION/.test(r.innerText))
    .map(r => Array.from(r.cells).map(c => c.innerText.trim()))
}))
```

Replace `ORIGIN|DESTINATION` with escaped station names. Keep DOM extraction read-only unless normal controls cannot expose the needed data.

## Iframe trip planner

Agency planners often embed a cross-origin journey-planner iframe. Parent-page JavaScript may not access the iframe DOM, but browser accessibility snapshots can still expose its controls.

Procedure:

1. Navigate to the official planner.
2. Type the origin.
3. Refresh the snapshot and select the exact station suggestion.
4. Repeat for destination.
5. Set departure/arrival mode and date when the question requires it.
6. Submit and capture the result card’s departure, arrival, duration, route, and date.
7. Expand itinerary details if total duration may include walking or transfers.

Pitfall: free text that looks correct may remain unresolved; select the suggestion before submitting.

## Coordinate fallback

When station-name geocoding fails:

1. Try the agency’s station detail page.
2. Query OpenStreetMap/Nominatim with shorter variants.
3. Query an OSM object by station tags and a city bounding box.
4. Use a well-sourced station page that publishes coordinates.
5. Verify the address/coordinates correspond to the correct entrance or platform area.

Store coordinates at enough precision for routing, but do not clutter the final answer with them.

## Last-mile routing

Use a pedestrian or bicycle network router, not aerial distance. If the preferred maps helper cannot geocode the station, route by verified coordinates with another public engine.

Capture the raw response values, then convert and round with a calculation tool. Keep source precision for arithmetic; present whole minutes or a short range.

## Frequency-aware comparison

Extract or infer headway only from multiple official departures. Distinguish:

- scheduled run time;
- service headway;
- peak-only span;
- live delays or planned disruptions.

For regular service and random arrivals, expected wait may be approximated as half the headway. Label this assumption and never add it to a trip where the rider plans around a specific departure.

## Minimal evidence record

For each option, retain:

```text
origin:
destination:
date/service day:
run/line:
departure:
arrival:
transit minutes:
last-mile mode:
last-mile distance:
last-mile minutes:
alert checked/source:
```

This is enough to reproduce the comparison without preserving a full scraped page or a one-off commute narrative.

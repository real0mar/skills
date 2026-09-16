# Google Flights Browser Workflow

Use this reference when ordinary web search is unavailable or when precise schedule extraction requires a dynamic flight-results page.

## Natural-language deep link

Google Flights accepts a readable query URL:

```text
https://www.google.com/travel/flights?q=Flights%20from%20<ORIGIN>%20to%20<DESTINATION>%20on%20<DATE>&hl=en&curr=USD&gl=US
```

Example shape:

```text
https://www.google.com/travel/flights?q=Flights%20from%20BLQ%20to%20SFO%20on%20September%209%202026&hl=en&curr=USD&gl=US
```

After load, verify the origin, destination, and departure-date fields in the accessibility snapshot. Natural-language parsing may default to **round trip** and invent a return date; outbound schedules remain useful, but its displayed prices are round-trip prices for that default return.

## Consent-page recovery

A browser click on “Accept all” or “Reject all” may report success without navigating. If the page remains on `consent.google.com`:

1. Inspect `document.forms` in the page context.
2. Identify the form by its visible text or hidden fields:
   - Reject form commonly includes `set_eom=true`.
   - Accept form commonly includes `set_sc=true`, `set_aps=true`, and `set_eom=false`.
3. Submit the selected form directly with `document.forms[index].submit()`.
4. Refresh the accessibility snapshot and confirm the flight-search page loaded.

This is a recovery pattern, not a permanent assumption about Google; first try the normal button interaction.

## Extracting itineraries

The full accessibility snapshot often exposes each itinerary as a descriptive link containing:

- Fare basis shown by the page
- Stop count and airlines
- Departure airport/date/time
- Arrival airport/date/time
- Total duration
- Connection airport and layover length

Prefer the descriptive link text over visually inferring times. Save or page through the full snapshot when compact output truncates the “other flights” section.

## Interpretation rules

- Treat every displayed time as local to the associated airport.
- Preserve explicit next-day markers (`+1`) and spell out the arrival date.
- Do not quote a round-trip fare when the user's return date was not entered.
- Compare one-stop options by both arrival buffer and human cost.
- A single late connection can be technically feasible but brittle; identify an earlier-arriving safety-first option.

## Session-derived example

For a Tuesday-night event in Bologna followed by Thursday work near San Francisco, live Wednesday results demonstrated the useful comparison pattern:

- A midday one-stop departure preserved Wednesday-morning sleep and arrived SFO Wednesday evening.
- Several pre-dawn one-stop departures arrived around midday Wednesday, sacrificing sleep for a much larger disruption buffer.
- A Wednesday-evening departure arrived Thursday and failed the “sleep at home Wednesday night” constraint.

The durable lesson is to report **balanced**, **safety-first**, and **reject** categories rather than dumping all results.

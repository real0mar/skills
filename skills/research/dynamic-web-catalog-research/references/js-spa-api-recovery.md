# JavaScript SPA API Recovery Pattern

Use this reference when the canonical page returns a valid HTML shell but no catalog rows.

## Extraction recipe

1. Fetch the HTML and list all `<script src>`, module-preload, environment, and configuration assets.
2. Download the smallest config/environment files first, followed by the main bundle and relevant imported chunks.
3. Search bundle text for API hosts and read-only route strings: `/api/`, `/graphql`, `.json`, `items`, `catalog`, `service`, `programs`, `search`, date arguments, filters, and pagination.
4. Reproduce the site's anonymous browser flow only. If its client exchanges a public application/host ID and empty credentials for a short-lived session token, keep that token in memory and out of logs.
5. Call the narrowest read-only endpoint with explicit date, locale, category, page, and platform/content-system arguments.
6. Parse responses in code. Compare declared counts with enumerated items and inspect representative full objects for nested metadata.
7. Cite the canonical public page, record the effective date/program, and state any gap between catalog-wide and exact device/vehicle/store availability.

## Validated airline-entertainment example

A United Private Screening page exposed only an Angular app shell. Its current client bundles revealed a public Airtime/Anuvu data flow:

- a production API base and public application host ID in the compiled configuration;
- an anonymous session request at `/api/v3/account/session` returning a short-lived `auth_token`;
- read-only content requests authenticated with the client's `Auth-Token` header;
- `/api/v3/content/programs?staging=false` for monthly effective-date validation;
- `/api/v3/content/items` with `flight_date=YYYY-MM-DD` and a movie-template filter for the dated catalog.

Item metadata was nested under fields including `duration_minute`, `year`, `director_list`, `long_description`, `attributes`, and `content_systems`. The broad catalog token did not authorize every flight-schedule query, so the defensible result was a current network catalog—not guaranteed inventory for one aircraft. The final recommendation therefore led with a decisive choice while advising confirmation on the seatback interface.

## Reliability and safety

- Never print or persist session tokens.
- Do not attempt authenticated-account or write operations.
- Do not hard-code public application IDs; deployments can rotate.
- Treat HTTP 200 plus an app shell as incomplete recovery.
- Re-discover routes from the current client when the schema changes.
- A compatibility/content-system field is evidence, not proof of exact installed availability.

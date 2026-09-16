# HiringCafe SSR job-market counts

Use when the user wants current job counts by metro, remote category, salary threshold, role/title, or market snapshot and HiringCafe is an appropriate source.

## Source pattern

HiringCafe exposes enough data in server-rendered Next.js pages to collect aggregate counts without browser automation:

1. Build a `searchState` JSON object and URL-encode it into `https://hiring.cafe/?searchState=<json>`.
2. Fetch the page with a normal browser User-Agent.
3. Parse `<script id="__NEXT_DATA__" type="application/json">...</script>`.
4. Read:
   - `props.pageProps.ssrTotalCount`
   - `props.pageProps.ssrCompanyCount`
   - `props.pageProps.ssrHits` for samples/provenance checks
   - `props.pageProps.initialSearchState` to verify filters were accepted/normalized
5. For city/metropolitan anchors, call `https://hiring.cafe/api/searchLocation?query=<city>` and use the first `placeDetail`; for locality locations add:
   ```json
   {"options":{"radius":50,"radius_unit":"miles","ignore_radius":false},"workplace_types":[]}
   ```
6. For US remote, use `workplaceTypes:["Remote"]` with a US country location object or the site may default/normalize unexpectedly.

## Useful searchState fields

```json
{
  "jobTitleQuery": "engineer",
  "restrictJobsToTransparentSalaries": true,
  "calcFrequency": "Yearly",
  "dateFetchedPastNDays": 121,
  "sortBy": "date",
  "maxCompensationLowEnd": 300000,
  "locations": [/* placeDetail + options */]
}
```

Salary filters observed in the UI/source:

- `maxCompensationLowEnd`: "Salary upper range over X" — good for *range touches $X* counts, e.g. a posting with `$180k–$300k` qualifies.
- `minCompensationLowEnd`: "Salary lower range over X" — stricter *floor starts at/above $X* counts.
- `restrictJobsToTransparentSalaries:true`: avoid opaque/estimated salary pollution.
- `calcFrequency:"Yearly"`: normalize threshold interpretation.

## Recommended report framing

For compensation-market reports, include both columns when possible:

- **tail_count_ge_threshold**: upper end/range touches threshold — larger but noisy.
- **floor_count_ge_threshold**: lower end starts at threshold — smaller, cleaner signal for truly high-comp roles.

State the caveats directly: HiringCafe counts are current indexed postings, city anchors are radius searches rather than official CBSA definitions, parsing depends on the site’s current SSR shape, and salary fields are advertised/parsed not guaranteed offers.

## Minimal Python sketch

```python
import html, json, re, requests
from urllib.parse import quote

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0'})

state = {
    'jobTitleQuery': 'engineer',
    'restrictJobsToTransparentSalaries': True,
    'maxCompensationLowEnd': 300000,
    'calcFrequency': 'Yearly',
    'dateFetchedPastNDays': 121,
    'sortBy': 'date',
}
url = 'https://hiring.cafe/?searchState=' + quote(json.dumps(state, separators=(',', ':')))
text = s.get(url, timeout=35).text
m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', text)
data = json.loads(html.unescape(m.group(1)))
pp = data['props']['pageProps']
print(pp['ssrTotalCount'], pp['ssrCompanyCount'])
print(pp['initialSearchState'])
```

---
name: purchase-deal-comparison
description: Use when comparing purchase deals and landed costs.
version: 1.0.0
license: MIT
---

# Purchase Deal Comparison

## Overview

Use this skill to answer “Can you find a better deal than this?” for physical goods. The job is not to collect lower sticker prices; it is to find purchasable alternatives that are genuinely comparable after variant, shipping, taxes/fees, location, condition, warranty, and fulfillment risk.

A strong result names the best verified option, shows the landed-cost arithmetic, distinguishes exact matches from compromises, and gives the user a short buying recommendation.

## When to Use

Use for:

- Comparing a linked product against other retailers
- Finding local pickup or delivery alternatives
- Evaluating new versus used, marketplace, refurbished, or open-box offers
- Checking whether a promotion, coupon, membership price, or bundle is actually cheaper
- Comparing live goods where size, condition, shipping stress, or guarantees materially affect value

Do not use for broad product-category recommendations where the user has not anchored the comparison to a specific item; use the relevant domain-analysis skill instead.

## Core Comparison Model

Define the target before searching:

| Field | Examples |
|---|---|
| Identity | manufacturer/model, species/cultivar, exact SKU |
| Variant | size, color, capacity, configuration, condition |
| Quantity | single, pack, subscription quantity |
| Included items | pot, stand, charger, accessories, installation |
| Fulfillment | shipped, delivered, pickup |
| Destination | ZIP code or local search radius |
| Time constraint | arrival date, pickup window |
| Risk protections | returns, warranty, live-arrival guarantee |

An alternative is an **exact match** only if its load-bearing fields match. Otherwise label the difference explicitly: “same product, smaller size,” “darker cultivar,” “used,” “unbraided,” “no pot,” or similar. Never let a lower price hide a material mismatch.

## Procedure

### 1. Inspect the anchor listing

Retrieve the linked page rather than relying on its URL or search snippet. Record:

- Selected variant, not merely the page’s default or starting price
- Current sale price and coupon terms
- Shipping threshold and destination restrictions
- Included accessories or container
- Warranty/returns
- Stock and estimated fulfillment

Completion criterion: the comparison baseline is one concrete purchasable configuration with a pre-tax delivered price or a clearly marked unknown.

### 2. Establish destination early

If the user gives a city, region, or ZIP, immediately re-run local and shipping searches for that destination. Do not continue optimizing for an inferred location after the user corrects it.

If the user says only a metro subregion (for example, “West County”), search the practical local radius without blocking on an exact ZIP. Use a representative ZIP only for a shipping-rate probe and say which one was used.

Completion criterion: every recommendation is deliverable to or collectible within the user’s stated area.

### 3. Search in parallel across channels

Search independent channels concurrently:

1. Major retailers and the manufacturer
2. Specialist online sellers
3. Local stores, nurseries, dealers, or florists
4. Local marketplaces and classifieds when used goods are acceptable
5. Alternate variants only when the compromise could improve value

Search exact phrases for model/spec/size and include the location. Search snippets are discovery evidence, not final price verification.

Completion criterion: at least one specialist, one mainstream, and one local channel were checked when those channels plausibly exist.

### 4. Verify the candidate listing

Open every serious candidate and confirm:

- Exact variant and stock
- Price shown on the product page
- Shipping restrictions
- Return/warranty language
- Material caveats buried in fulfillment text

For local listings with missing height, configuration, or inventory, present them as “call to confirm,” not as a verified winner. Provide the exact question to ask.

Completion criterion: the winning claim rests on the listing body or checkout, not only a search snippet.

### 5. Compute landed cost

Use:

`landed cost = item price - discounts + mandatory shipping + mandatory fees`

Treat tax separately when two sellers would charge comparable destination tax and the exact amount is unavailable. Include tax if checkout exposes it.

For coupon prices, verify code, minimum spend, end date, exclusions, and whether the discounted item still qualifies for free shipping.

When shipping is “calculated at checkout,” continue to checkout far enough to obtain the rate without placing the order. A public business address in the destination ZIP can be used solely as a rate probe; do not enter payment details or submit the order. See `references/landed-cost-checkout.md` for a tested Shopify pattern.

Completion criterion: the winner has a numeric pre-tax landed cost, or is explicitly conditional on an unknown fee.

### 6. Adjust for value and risk

Price alone is not always the best deal. Compare:

- Exactness of match
- Condition and ability to inspect before purchase
- Warranty/return window
- Shipping damage or trimming risk
- Delivery speed and handling time
- Seller reputation and review volume
- Missing accessories, containers, soil, installation, or setup work

Quantify the premium when possible: “Seller A costs $29 more but adds a one-year guarantee and intact-pot shipping.” This lets the user decide whether risk reduction is worth the premium.

Completion criterion: the recommendation states both the cheapest option and the best-value option if they differ.

### 7. Deliver a compact recommendation

Use this order:

1. **Verdict** — one sentence
2. **Best verified alternative** — item, match differences, item price, shipping, landed cost, savings
3. **Best local lead** — location, price, and what must be confirmed
4. **Why the anchor may still be worth it** — only material protections or quality differences
5. **Action** — exact purchase link or concise call script
6. **Sources** — grounded citations

Avoid leading with a long research diary. The user asked for a buying decision, not a browsing transcript.

## Live Goods and Condition-Sensitive Products

Plants, animals, food, vintage goods, and fragile items require additional checks:

- Measurement basis: pot-to-top, floor-to-top, nominal pot size, weight, maturity
- Exact cultivar/breed/model, not merely common name
- Whether the pictured item is representative or the actual item
- Whether shipping may trim, bare-root, remove soil, substitute, or delay fulfillment
- Temperature/weather restrictions
- Live-arrival versus long-term guarantee
- Local inspection advantage

For plants, pot diameter and gallon rating are not reliable substitutes for height or fullness. Call local inventory a better deal only when the relevant size/form is confirmed.

## Evidence and Citation Discipline

Load `grounded-citations` when producing a researched answer.

- Cite current prices, availability, shipping policies, and warranty claims.
- A checkout-observed shipping rate may be described as verified for the ZIP/address used; note the destination.
- Do not cite a marketplace category page as proof that one specific listing remains active unless the item page is accessible.
- State “inventory/price may change” once if needed; do not repeat generic caveats.

## Common Pitfalls

1. **Comparing against the wrong variant.** Product pages often show a starting price while the URL selects a larger option. Record the selected configuration first.

2. **Calling a sticker-price winner.** “Shipping calculated at checkout” is unfinished work. Probe checkout or label the result conditional.

3. **Ignoring a location correction.** Once the user provides a destination, discard earlier local findings and search the corrected area.

4. **Treating close substitutes as identical.** Cultivar, size, braid/form, color, capacity, accessories, and condition can be load-bearing.

5. **Overweighting search snippets.** Snippets may be stale, omit stock, or combine prices from multiple variants.

6. **Claiming local availability from a catalog page.** “Check store for availability” is a lead, not stock confirmation.

7. **Ignoring fulfillment damage.** Trimming, bare-root shipping, soil removal, long handling time, and weak return terms can erase apparent savings.

8. **Hiding the risk premium.** If the safer seller is only modestly more expensive, quantify that premium rather than declaring the cheapest seller best.

9. **Overloading the answer.** Keep rejected candidates out unless they explain why the apparent lower price is misleading.

## Verification Checklist

- [ ] Anchor listing’s selected variant and effective price verified
- [ ] Destination/location applied to all serious candidates
- [ ] Exact-match differences labeled
- [ ] Shipping and mandatory fees included or marked unknown
- [ ] Coupon requirements verified
- [ ] Stock/availability not inferred from snippets alone
- [ ] Return, warranty, and fulfillment risks compared
- [ ] Arithmetic checked with a tool
- [ ] Cheapest and best-value options distinguished when necessary
- [ ] Final answer gives one clear recommended next action
- [ ] External claims carry grounded citations

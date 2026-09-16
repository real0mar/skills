# Verifying “Calculated at Checkout” Shipping

Use this when a candidate appears cheaper but its product page omits shipping. The goal is to verify landed cost without placing an order or using the user’s personal data.

## Shopify storefront pattern

1. Open the exact product and verify variant/availability.
2. Add one unit to the cart.
3. Open `/cart`, confirm the intended variant and item price, then choose checkout.
4. Enter only enough destination information to calculate shipping:
   - a neutral rate-check email such as `ratecheck@example.com`
   - a public business address in the destination ZIP
   - city, state, and ZIP
5. Do not enter payment data and do not click the final payment/order button.
6. Record the shipping method, rate, destination ZIP, item price, and total before tax.
7. Close or abandon the checkout.

If the checkout’s address autocomplete does not commit typed state/region values, select the region normally. In browser automation, changing the underlying `select[name="zone"]` value and dispatching bubbling `change` and `input` events can trigger recalculation:

```javascript
const state = document.querySelector('select[name="zone"]');
state.value = 'MO';
state.dispatchEvent(new Event('change', {bubbles: true}));
state.dispatchEvent(new Event('input', {bubbles: true}));
```

Then blur the field or press Tab and refresh the snapshot. A successful probe shows a concrete shipping method and price.

## Why this matters

A low item price is not a deal until mandatory shipping is known. In the validated example that motivated this reference, a $69.99 item had $27.99 economy shipping to ZIP 63011, producing a $97.98 pre-tax landed cost. The checkout rate changed the comparison from conditional to verified.

## Boundaries

- Use a public business address only for a rate estimate; never submit the order.
- Do not use or fabricate payment credentials.
- Do not claim the rate applies nationally; tie it to the probed ZIP.
- If checkout requires a phone number or other unnecessary personal data before showing rates, stop and label shipping unverified rather than inventing personal information.
- Taxes may remain unknown until later checkout stages; compare pre-tax landed costs and say so.
- A verified lower landed cost can still be worse value if the seller trims, bare-roots, removes accessories, has weak returns, or takes much longer to fulfill.

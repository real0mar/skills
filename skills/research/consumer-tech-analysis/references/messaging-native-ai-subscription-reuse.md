# Messaging-native AI and subscription reuse

Use this workflow when comparing LLM assistants available through Telegram, SMS/RCS, WhatsApp, iMessage, Discord, or similar channels—especially when the user wants to reuse an existing consumer subscription.

## Separate four product shapes

1. **First-party native assistant:** The model vendor operates the messaging bot/integration. Verify the exact handle or phone number from the vendor’s own site.
2. **Subscription-backed self-hosted channel:** An official CLI/agent runs on the user’s machine and receives messages through a channel plugin. This may consume an existing Pro/Max-style subscription even though there is no public hosted bot.
3. **Independent agent with its own plan:** A service may route among several models but bills its own Free/Pro/Ultra allowance. It does not thereby inherit upstream ChatGPT, Claude, Gemini, or Grok subscriptions.
4. **Third-party API wrapper:** A Telegram bot may advertise many models but normally uses its operator’s API accounts and billing. Treat model/version, retention, and privacy claims as unverified unless documented.

## Subscription-reuse checklist

For each candidate, verify independently:

- Is account linking supported on this exact messaging surface?
- Does linking merely raise a free usage limit, or actually apply paid-plan entitlements?
- Is access tied to the model vendor’s subscription, the messaging platform’s premium tier, or a separate bot subscription?
- Does the integration run on the vendor’s servers or on the user’s own persistent machine?
- Is the feature general chat, search/answer engine, or a coding/agent session with narrower behavior?
- Are availability and limits region-, phone-number-, account-, or rollout-dependent?

Do not infer that a web/app subscription applies to a bot just because both use the same brand. Consumer subscriptions and API billing are separate unless official documentation explicitly says otherwise.

## Research order

1. Vendor help center, release notes, pricing, and official integration docs.
2. Messaging platform announcement or verified bot landing page.
3. Current reputable reporting for rollout history and account/region caveats.
4. Search snippets and community posts only as leads.

Record the exact verification date because messaging integrations change quickly.

## Recommended answer format

Use a compact table:

| Existing subscription | Reusable on channel? | Exact mechanism | Important limitation |
|---|---:|---|---|

Then provide a short verdict distinguishing:

- **Direct reuse** of an existing subscription
- **Separate paid entitlement**
- **Free bot with no account linking**
- **Unofficial wrapper—not recommended for sensitive prompts**

If a self-hosted official channel is the only direct-reuse path, say so plainly and include the minimal setup command only after verifying current official docs.

## Privacy and wording guardrails

- Verify bot handles from first-party pages; impersonator bots are common.
- Do not recommend sending private documents to an unofficial multi-model bot.
- Say “no documented account linking found” rather than asserting linking is impossible.
- Distinguish SMS from WhatsApp/iMessage/RCS and voice calling; users often group them together, but providers do not.
- Distinguish a Telegram Premium entitlement from an xAI/Perplexity/etc. subscription.

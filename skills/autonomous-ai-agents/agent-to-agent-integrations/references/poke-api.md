# Poke API Integration

Authoritative documentation: `https://poke.com/docs/api`

## Capability

Poke exposes an inbound API that lets scripts and automation tools send a message into the user's normal Poke conversation. Poke processes the message with access to the user's enabled Poke integrations. The API response is a delivery/acceptance result; Poke's conversational reply appears through the user's configured Poke messaging surface rather than in the HTTP response.

## Current Endpoint

```http
POST https://poke.com/api/v1/inbound/api-message
Authorization: Bearer <V2_POKE_API_KEY>
Content-Type: application/json

{"message":"<instruction>"}
```

The body may be any JSON object; it is forwarded to Poke as context. Prefer a clear `message` field for interoperability.

## Authentication

- Create a **V2 API key** in Poke Kitchen.
- Store it as `POKE_API_KEY` in the active Hermes profile's secret environment file.
- Do not expose the key while testing configuration; report only whether it exists.
- Treat it as high authority: anyone holding it can send instructions to the user's Poke, which may have access to email, calendar, reminders, and other connected services.

### Legacy incompatibility

The deprecated endpoint is:

```text
POST /api/v1/inbound-sms/webhook
```

It uses legacy `pk_`-prefixed V1 keys. Those keys do **not** work with `/api/v1/inbound/api-message`; create a V2 key in Kitchen instead.

## Minimal Test

```bash
curl --fail-with-body --silent --show-error \
  -X POST https://poke.com/api/v1/inbound/api-message \
  -H "Authorization: Bearer $POKE_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"message":"Hello Poke — this is Hermes acting for the user. This is a connectivity test. Please acknowledge receipt in the normal Poke conversation and take no other action."}'
```

Expected acceptance shape:

```json
{"success":true,"message":"Message sent successfully"}
```

## Verification Checklist

1. Confirm the API returned HTTP 2xx and `success: true`.
2. Describe that result as **accepted/sent**, not as proof Poke completed a task.
3. Ask the user to check their normal Poke conversation for the asynchronous acknowledgement.
4. If no message appears, refresh the Poke conversation and retry with `{"message":"test"}`.
5. For `401`, verify the Bearer header, that the key is V2, that it was not revoked, and that no whitespace was introduced.
6. If the credential was pasted into chat, recommend creating a replacement key and updating the stored secret.

## Integration Pattern

Hermes → Poke is directly supported through the inbound API. A genuinely bidirectional automated loop additionally needs a return path from Poke to Hermes, such as a Hermes webhook, supported recipe, email gateway, or messaging-channel bridge. Without that return path, the human-visible Poke conversation is the response channel.

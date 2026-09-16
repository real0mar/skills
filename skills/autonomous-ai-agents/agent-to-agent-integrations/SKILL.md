---
name: agent-to-agent-integrations
description: "Use when connecting external AI assistants via API, webhook, MCP, email, or chat."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [agents, integrations, api, webhooks, mcp, delegation, security]
---

# Agent-to-Agent Integrations

Connect Hermes to an external AI assistant or automation agent through a supported machine interface. The goal is a verified message path with explicit identity, scope, delivery semantics, and credential hygiene—not merely proof that the other product exists.

## Workflow

1. **Inspect the authoritative interface**
   - Prefer the product's current developer documentation over search snippets or remembered behavior.
   - Look for API, webhook, MCP, email, bot/chat, and callback interfaces.
   - Distinguish a user-facing chat surface from a programmatic ingress endpoint.

2. **Determine directionality**
   - Establish whether the interface is Hermes → external agent, external agent → Hermes, or bidirectional.
   - Identify whether the API returns the agent's answer synchronously, only acknowledges delivery, or sends the answer through another channel.
   - Do not call a delivery acknowledgement a completed conversation.

3. **Check authentication and authority**
   - Identify key version/type, endpoint compatibility, required headers, and scopes.
   - Warn when possession of the credential permits actions through connected email, calendar, files, or other integrations.
   - Never quote credentials in the final response, memory, skills, logs, examples, or support files.

4. **Configure securely**
   - Put secrets in the profile's credential store or `.env`, never in `config.yaml` or source control.
   - Preserve existing environment-file contents and use restrictive permissions (`0600` where applicable).
   - Record only the non-secret fact that the integration is configured.
   - If a credential was pasted into chat, recommend rotation after setup because it remains in chat/provider history.

5. **Run a minimal delivery test**
   - Send a harmless, uniquely identifiable message stating the sender and purpose.
   - Ask the external agent to acknowledge through the expected return channel.
   - Avoid granting a first test broad or destructive authority.

6. **Verify precisely**
   - Capture the real HTTP/status response.
   - Report separately: credential saved, request accepted, message delivered (if guaranteed), and reply observed.
   - If the API only returns an acceptance flag, say the reply is expected asynchronously and where to look for it.

7. **Operationalize only after the test**
   - Add reusable scripts, recipes, webhooks, or scheduled jobs after the manual test succeeds.
   - Include timeouts, bounded retries for transient failures, rate-limit handling, and secret-safe diagnostics.

## Safe Test Message

Use a message similar to:

> Hello — this is Hermes, acting for <user>. This is a direct agent-to-agent connectivity test. Please acknowledge receipt through <expected channel>; take no other action.

## Pitfalls

- A public website or chat UI does not prove a programmatic interface exists.
- An HTTP `200` may mean only “queued” or “accepted,” not that the agent completed the task.
- API-key generations may be endpoint-specific; do not assume legacy keys work with newer endpoints.
- Never expose credentials while checking whether they are configured; print only a boolean/status.
- Do not persist a credential for an unrelated service merely because it appeared in conversation.
- Agent identity is informational unless cryptographically authenticated; phrase introductions accordingly.

## Provider References

- **Poke:** See `references/poke-api.md` for its programmatic inbound-message API, V2 key requirements, asynchronous reply semantics, and verification checklist.

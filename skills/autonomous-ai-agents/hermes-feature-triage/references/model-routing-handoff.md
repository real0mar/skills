# Model / fallback / reasoning handoff

When triage hits questions about:

- current Hermes model/provider
- fallback chains (`hermes fallback`)
- `agent.reasoning_effort` / thinking levels
- whether a provider model ID actually exists/responds

**Load and follow `hermes-model-routing`.** Do not answer those from memory alone.

Minimum commands:

```bash
hermes status
hermes config get model
hermes fallback list
hermes config get agent.reasoning_effort
```

xAI note: `grok-4.20-multi-agent*` fails on chat completions; probe via `/v1/responses`. See `hermes-model-routing` → `references/xai-live-model-probe.md` and `scripts/xai_hello_probe.py`.

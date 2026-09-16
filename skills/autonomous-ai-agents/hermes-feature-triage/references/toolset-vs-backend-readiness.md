# Toolset enablement vs backend readiness

Use this when Hermes lists a toolset as enabled but the user asks whether the capability is actually usable.

## Three-layer check

1. **Tool schema enabled for the platform**
   - Run `hermes tools list`.
   - This only proves the toolset is exposed to that platform; it does not prove credentials, managed entitlement, binaries, or runtime dependencies are ready.
2. **Backend/provider selected and ready**
   - Run `hermes status` for the configured provider and Nous Tool Gateway state.
   - Run `hermes doctor` for missing runtime dependencies.
3. **Real smoke test**
   - Exercise the smallest harmless operation through the actual tool, then report the observed result. For browser automation, navigate to `https://example.com` and confirm the title/accessibility snapshot.

## Browser automation on a Nous subscription

A common valid configuration is:

- browser toolset enabled;
- `browser.cloud_provider` set to `browser-use`;
- `browser.use_gateway` set to `true`;
- Nous Portal authenticated and entitled;
- browser bootstrap dependency installed.

If `hermes status` says browser automation is included but not selected, while `hermes tools list` says browser is enabled, inspect `hermes doctor`. When the browser bootstrap dependency is missing, run the supported non-interactive setup hook:

```bash
hermes tools post-setup agent_browser
```

Then verify all three layers again. Do not ask for a separate Browser Use API key when the managed Nous gateway is active.

## Reporting rule

Say **enabled** only for layer 1. Say **active/working** only after layers 2 and 3 pass. Keep ordinary web research distinct from browser automation: `web_search`/`web_extract` can work through managed web tooling even when interactive browser automation is not ready.

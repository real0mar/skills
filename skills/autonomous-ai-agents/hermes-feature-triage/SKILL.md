---
name: hermes-feature-triage
description: Verify Hermes Agent feature-support questions against docs, CLI help, and source before answering; distinguish built-in behavior from quick commands, platform aliases, and feature requests.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, cli, troubleshooting, feature-verification, source-inspection]
---

# Hermes Feature Triage

Use this skill when the user asks whether Hermes supports a specific behavior, CLI shortcut, slash command, passthrough, integration, or configuration knob.

## Workflow

1. Load the protected `hermes-agent` skill first for current command/docs pointers.
2. Check the live docs when the question is about public behavior. Prefer the official docs at `https://hermes-agent.nousresearch.com/docs` over memory.
3. Check the installed CLI/source when the question is about exact local behavior:
   - `hermes --help`
   - `hermes chat --help`
   - `hermes <subcommand> --help`
   - Diagnostic commands such as `hermes prompt-size --platform <platform>` when the user asks what is taking up context.
   - Source locations such as `hermes_cli/commands.py`, `cli.py`, `hermes_cli/config.py`, `hermes_cli/prompt_size.py`, gateway adapters, or tool implementations.
4. For tool-capability questions, distinguish three layers: (a) toolset enabled for the platform, (b) provider/backend and dependencies ready, and (c) a real smoke test succeeds. Use `hermes tools list`, `hermes status`, and `hermes doctor` respectively, then exercise the smallest harmless real operation. See `references/toolset-vs-backend-readiness.md`.
5. When the user asks for *the command*, lead with the exact command before summarizing concepts. If they are frustrated, skip defensive framing and verify the command from help/source immediately.
6. Separate similar-looking mechanisms:
   - Slash commands (`/...`) handled by the CLI/gateway registry.
   - User-defined `quick_commands` in config that bypass the agent for configured shell snippets.
   - Messaging-platform aliases such as Matrix/Slack `!command` handling.
   - Natural-language requests that invoke the terminal tool through the agent.
   - True shell passthrough where user input is executed directly without an LLM call.
7. If evidence is partial, say what was checked and what remains unverified. Avoid broad negative claims from memory.
8. Answer directly and briefly. If the feature is absent, state the closest supported alternatives and whether it looks like a feature request.

## Pitfalls

- Do not infer absence from docs alone; verify the installed source or CLI help when feasible.
- Do not confuse gateway `!command` aliases with local CLI bash passthrough.
- Do not describe a command as supported merely because the agent can run terminal tools after natural-language prompting.
- Do not answer Hermes introspection questions from high-level memory when a local diagnostic command exists; look up and run the command.
- Do not equate an enabled toolset with a usable backend. Check provider selection, entitlement/credentials, runtime dependencies, and perform a real smoke test before saying the capability works.
- If a tool call hangs or is interrupted, do not leave the user wondering; continue with another verification path or state the interruption plainly.

## References

- `references/bang-passthrough.md` records a concrete triage example for Codex/Claude-style `!<bash>` passthrough in Hermes CLI.
- `references/prompt-size-skill-index.md` records the prompt-size / skills-index commands and a pattern for reporting skills-index bloat by category.
- `references/toolset-vs-backend-readiness.md` records the enabled → backend-ready → smoke-tested verification ladder, including managed browser automation setup.

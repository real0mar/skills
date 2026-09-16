# Bang passthrough triage (`!<bash>` in Hermes CLI)

Session learning: a user asked whether Hermes supports Codex/Claude-style bash passthrough using a leading exclamation mark, e.g. `!ls` or `!git status`.

Verification path used:

- Loaded `hermes-agent` for CLI/slash-command context.
- Checked `hermes --help` and `hermes chat --help`; no bang-passthrough flag or command was listed.
- Searched source for bang handling and quick commands.
- Found `quick_commands` support in `hermes_cli/config.py` and execution handling in `cli.py`, but those are configured slash commands, not arbitrary `!<command>` passthrough.
- Found Matrix/Slack bang normalization/aliases for messaging platforms, but that is not local CLI shell passthrough.

Conclusion at time of triage:

- The Hermes CLI does not appear to have a built-in Codex/Claude-style arbitrary `!<bash>` passthrough.
- `!…` in local CLI should be treated as normal user input unless a surface-specific adapter rewrites it.
- Closest current alternatives are asking naturally for a command to be run via the terminal tool, or defining fixed slash-based `quick_commands` in config.
- If the user wants exact `!<bash>` behavior, frame it as a small CLI feature request: detect a leading `!`, strip it, execute the remainder through the configured terminal backend, and print stdout/stderr without invoking the model.

Caveat: re-check current docs/source before repeating this as a durable product fact; Hermes may add the feature later.

# Prompt-size and skills-index diagnostics

Use when a user asks what is taking up Hermes context, wants to inspect the system prompt/tool payload, or wants to prune skills-index noise.

## Commands verified in-session

```bash
hermes prompt-size --platform telegram
hermes prompt-size --platform telegram --json
hermes skills list
hermes skills config
```

`hermes prompt-size` reports an offline fresh-session breakdown: system prompt total, skills index, memory, user profile, prompt tiers, and tool-schema JSON. Use `--platform telegram` (or the current platform) to match gateway sessions. Use `--json` for scriptable measurements.

`/usage` is the in-session slash command for live session token usage.

`hermes skills list` shows installed/enabled skills. `hermes skills config` opens the interactive enable/disable UI. Skill disablement affects fresh sessions / after `/reset`, not the already-built prompt.

## Useful inspection pattern

For a quick category-level skills-index bloat report, build an offline inspection agent and parse the `<available_skills>` block from the stable prompt tier. Count bytes per category and per skill line; this shows what categories are likely noise before changing config.

## User-facing answer style

When the user asks for a command, give the exact command first. Avoid defending hidden prompt boundaries or giving only a conceptual summary. After the command, add the shortest necessary explanation and any reset/restart caveat.

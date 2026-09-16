# skills

Personal [Agent Skills](https://agentskills.io) library for Claude Code, OpenAI Codex, Cursor, Grok Build, Google Antigravity, and other agents that speak the Agent Skills format.

## Install

```bash
npx skills add real0mar/skills
```

Target specific agents:

```bash
npx skills add real0mar/skills \
  -a claude-code -a codex -a cursor -a grok -a antigravity -y
```

Prefer symlink installs when prompted so one copy can feed multiple agents.

## Update

Agents do not pull this repo on their own. Refresh with:

```bash
npx skills update -y
```

Or, with GitHub CLI 2.90+:

```bash
gh skill update --all
```

### Antigravity

Prefer a **project** install (commands above). For a global install across Antigravity hub, IDE, and CLI, place skills under `~/.gemini/config/skills/<name>/` until the skills CLI’s Antigravity global path is fixed.

## Layout

```text
skills/
  <category>/
    <skill-name>/
      SKILL.md
      scripts/       # optional
      references/    # optional
      assets/        # optional
```

Each `SKILL.md` needs `name` and `description` frontmatter. Folder name should match `name`.

## Notes

- Some skills originated in a Hermes Agent environment. Replace Hermes-specific tool names with your agent’s equivalents where needed.
- Scripts may assume Linux paths; adapt before running.
- No credentials are included. Configure integrations yourself.
- `manifest.json` is an inventory of the packaged skills.

## License

MIT

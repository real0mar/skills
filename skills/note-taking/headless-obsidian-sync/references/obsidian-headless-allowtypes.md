# Obsidian Headless `allowTypes` notes

Session learning from setting up the user's `Notes` vault on a headless Linux VPS with `obsidian-headless` / `ob` 0.0.12.

## Observed behavior

`ob sync-config --path /home/ubuntu/ob --file-types ""` printed `Configuration updated`, but `ob sync-status --path /home/ubuntu/ob` still showed:

```text
File types: image, audio, pdf, video
```

Trying placeholder values failed as invalid:

```text
Invalid file type: "none". Valid values: image, audio, video, pdf, unsupported
Invalid file type: "markdown". Valid values: image, audio, video, pdf, unsupported
```

## Source-code cause

The installed bundled `cli.js` defines:

```js
rs = ["image","audio","video","pdf","unsupported"]
Le = ["image","audio","pdf","video"]
```

The `sync-config` handler contains logic equivalent to:

```js
if (s.fileTypes !== undefined) {
  if (s.fileTypes === "") delete t.allowTypes
  else t.allowTypes = Rr(s.fileTypes)
}
```

The sync filter initializes with:

```js
this.allowTypes = new Set(e || Le)
```

So deleting `allowTypes` makes the client fall back to default attachment types, not to no attachments.

## Working representation

For markdown-only sync, the local headless sync config needs:

```json
"allowTypes": []
```

in:

```bash
~/.config/obsidian-headless/sync/<vault-id>/config.json
```

This is local Obsidian Headless client config, not a vault note edit. Stop the continuous sync service before patching it, then start it again.

## Safety note

The user's concern was “don't write to the vault” while still allowing setup/config changes. Be explicit about this distinction before changing local sync config:

- Avoid note/content writes inside `/home/ubuntu/ob` unless explicitly authorized.
- Updating `~/.config/obsidian-headless/.../config.json` controls the sync client and is not writing a vault note.

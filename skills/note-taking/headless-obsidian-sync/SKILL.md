---
name: headless-obsidian-sync
description: Set up and troubleshoot official Obsidian Headless Sync mirrors on a headless VPS for read/search access from Hermes.
version: 1.0.0
author: Hermes Agent
platforms: [linux]
metadata:
  hermes:
    tags: [obsidian, obsidian-sync, headless, systemd, vps, notes]
    related_skills: [obsidian, hermes-agent]
---

# Headless Obsidian Sync

Use this when configuring a headless Linux/VPS mirror of an Obsidian Sync vault for Hermes to read/search via the filesystem-first `obsidian` skill.

## Core model

- Official desktop `obsidian` CLI controls a running desktop app; it is not the right fit for a headless VPS.
- Official `obsidian-headless` exposes the `ob` CLI and can sync Obsidian Sync vaults without the desktop app.
- For agent access, prefer a local mirror with `mirror-remote` mode: remote Obsidian Sync is source of truth; local changes are reverted.
- The filesystem path is what the bundled `obsidian` skill consumes through `OBSIDIAN_VAULT_PATH`.

## Preferred user setup on this VPS

The user's single vault is intentionally short-path:

```bash
/home/ubuntu/ob
```

Hermes env should contain:

```bash
OBSIDIAN_VAULT_PATH=/home/ubuntu/ob
```

For this user, keep paths short when choosing local vault/mirror paths; short paths are easier to type and token-cheaper.

## Setup sequence

```bash
mkdir -p /home/ubuntu/ob
ob login
ob sync-list-remote
ob sync-setup --vault "Notes" --path /home/ubuntu/ob --device-name hermes-host
ob sync-config --path /home/ubuntu/ob --mode mirror-remote
ob sync --path /home/ubuntu/ob
```

Then set Hermes env:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/home/ubuntu/.hermes/.env')
p.parent.mkdir(parents=True, exist_ok=True)
line = 'OBSIDIAN_VAULT_PATH=/home/ubuntu/ob'
lines = p.read_text().splitlines() if p.exists() else []
out, done = [], False
for l in lines:
    if l.startswith('OBSIDIAN_VAULT_PATH='):
        out.append(line); done = True
    else:
        out.append(l)
if not done:
    out.append(line)
p.write_text('\n'.join(out) + '\n')
PY
```

## systemd user service

Use a user service and ensure lingering is enabled so sync survives SSH logout and VPS reboot:

```bash
sudo loginctl enable-linger ubuntu
loginctl show-user ubuntu -p Linger
```

Template:

```ini
[Unit]
Description=Obsidian Headless Sync - Notes vault
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/ubuntu/ob
Environment=PATH=/home/ubuntu/.local/bin:/home/ubuntu/.hermes/node/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/home/ubuntu/.local/bin/ob sync --path /home/ubuntu/ob --continuous
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

Install/verify:

```bash
systemctl --user daemon-reload
systemctl --user enable --now obsidian-sync.service
systemctl --user status obsidian-sync.service
journalctl --user -u obsidian-sync.service -n 50 --no-pager
```

## Read-only / read-mostly behavior

When the user asks for a read-only mirror, distinguish two scopes clearly:

- Vault content writes: do not create/edit/delete notes or attachments unless explicitly authorized.
- Local sync config writes: commands like `ob sync-config` and systemd service edits are not note edits; they are setup/configuration changes.

`mirror-remote` is the main safety mechanism: if local vault content changes, the remote remains source of truth and the local mirror is reverted.

## Markdown-only / attachment sync pitfall

`ob sync-config --file-types ""` in `obsidian-headless` 0.0.12 does not produce markdown-only sync. It deletes the custom `allowTypes` key, which makes the client fall back to default attachment types: `image,audio,pdf,video`.

To make attachment types empty, set local headless config to:

```json
"allowTypes": []
```

The config file lives under:

```bash
~/.config/obsidian-headless/sync/<vault-id>/config.json
```

Procedure:

```bash
systemctl --user stop obsidian-sync.service
python3 - <<'PY'
import json
from pathlib import Path
p = Path.home() / '.config/obsidian-headless/sync/<vault-id>/config.json'
data = json.loads(p.read_text())
data['allowTypes'] = []
p.write_text(json.dumps(data, indent=2) + '\n')
PY
ob sync-status --path /home/ubuntu/ob
systemctl --user start obsidian-sync.service
```

Expected status after patch:

```text
File types: none
```

See `references/obsidian-headless-allowtypes.md` for the source-code reasoning and verification notes.

## Verification checklist

```bash
ob sync-list-local
ob sync-status --path /home/ubuntu/ob
systemctl --user is-enabled obsidian-sync.service
systemctl --user is-active obsidian-sync.service
grep '^OBSIDIAN_VAULT_PATH=' /home/ubuntu/.hermes/.env
python3 - <<'PY'
from pathlib import Path
print(sum(1 for _ in Path('/home/ubuntu/ob').rglob('*.md')))
PY
```

Only use `read_file` / `search_files` for vault content unless the user explicitly authorizes vault edits.
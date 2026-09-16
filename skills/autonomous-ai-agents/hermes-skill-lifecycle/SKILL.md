---
name: hermes-skill-lifecycle
description: "Audit, maintain, and package Hermes skills by provenance."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, skills, provenance, audit, packaging, curator]
    related_skills: [hermes-agent, hermes-agent-skill-authoring, session-librarian]
---

# Hermes Skill Lifecycle

Audit the lifecycle of Hermes skills: identify what is bundled, hub-installed,
local, externally owned, curator-managed, user-owned, created or modified in a
session, and safe to package. This skill is for provenance and lifecycle
questions, not for editing protected skills or blindly archiving every local
skill.

Use the linked reference for the evidence hierarchy and command recipes:
`references/provenance-audit.md`.

## When to Use

- The user asks which skills are non-default, custom, created, modified, or ours.
- The user asks to audit, export, zip, share, or email a set of Hermes skills.
- A skill appears local but its origin is unclear.
- A bundled skill has a local diff and the user asks what changed.
- A curator review needs to distinguish agent-created skills from user-owned skills.

Don't use this for ordinary skill authoring, editing an in-repo Hermes checkout,
or deleting/archive-pruning skills without a separate explicit request.

## Ownership and Safety Boundaries

1. Treat bundled, hub-installed, external-directory, pinned, and user-owned
   skills as protected from autonomous edits.
2. A skill being loaded or consulted does not make it agent-owned.
3. A local skill is a storage classification, not proof that the current agent
   created it.
4. If a protected skill needs improvement, report the issue and recommend the
   appropriate foreground adoption/edit path; do not bypass the guard.
5. Do not include credentials, `.env` files, auth stores, session databases, or
   the entire Hermes home directory in a skill archive.

## Evidence Hierarchy

Use evidence in this order:

1. Hermes source classification: `hermes skills list` with `--source` filters.
2. Bundled manifest and `hermes skills list-modified`/`hermes skills diff` for
   default-skill tracking and local diffs.
3. Curator ledger entries, especially their actor, action, skill, and evidence
   session ID.
4. Session history showing a skill-management action or an explicit explanation
   of origin.
5. File timestamps and frontmatter as corroboration only.

Never turn a timestamp, `author: Hermes Agent`, or `source: local` alone into a
claim that a skill was created in a particular conversation. Report confidence
when evidence is indirect.

## Procedure

1. Define the requested scope. Separate “all non-default skills,” “skills
   created/modified in our sessions,” and “all skills currently present.”
   Completion criterion: the final scope has one explicit inclusion rule.
2. Enumerate current skills with Hermes' skills listing and classify each as
   bundled, hub, local, or disabled. Completion criterion: the claimed total
   matches the enumerated names.
3. Inspect bundled modifications with `list-modified` and `diff`; do not call
   those skills newly created merely because they differ from stock. Completion
   criterion: each modified bundled skill has a named diff or is excluded.
4. Check curator provenance and session history for creation/edit evidence.
   Record direct evidence separately from inference. Completion criterion: every
   included skill has a confidence label and an evidence reason.
5. Consolidate overlapping skills conceptually before packaging. Prefer the
   class-level umbrella and its `references/` files; flag overlap for the
   background curator rather than creating a narrow duplicate.
6. Package only the selected skill directories, preserving their category paths.
   Exclude caches and compiled files such as `__pycache__/` and `*.pyc`.
   Completion criterion: the archive listing contains exactly the selected
   skill directories and no secrets.
7. Verify the archive with a test extraction/listing, compare the selected count
   with the archive count, and report the absolute archive path and checksum.
   Completion criterion: archive integrity and scope both pass.
8. For email or messaging delivery, verify the actual outbound effect by reading
   back the sent record or obtaining a provider-confirmed message ID before
   claiming delivery.

## Quick Reference

```text
hermes skills list
hermes skills list --source local
hermes skills list --source builtin
hermes skills list --source hub
hermes skills list-modified
hermes skills diff <name>
```

Use `session_search` for historical evidence. Use `skill_manage` for skill
writes, and respect its ownership/provenance refusal messages.

## Pitfalls

- “Local” does not mean “created by me”; optional skills may have been seeded
  during setup or copied from another source.
- `list-modified` reports bundled skills whose current copies differ from stock;
  it does not establish who made each hunk.
- Linux ctime is metadata-change time, not reliable authorship evidence; mtime
  is only corroboration.
- Session search is historical context, not proof that the live file is still
  unchanged. Reconcile history with the current filesystem classification.
- Do not report a total until the names have been deduplicated and counted in
  code or by a verified listing.
- Do not email an archive before resolving the recipient and verifying the
  attachment and sent message.

## Verification

A completed lifecycle audit should state:

- the scope definition;
- counts by source and status;
- names created/modified with confidence and evidence;
- protected or uncertain items excluded;
- archive path, member count, and integrity result if packaging was requested;
- delivery ID/read-back evidence if it was sent.

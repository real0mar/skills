# Skill Provenance Audit Reference

Use this as the evidence worksheet for Hermes skill-origin questions. It is a
recipe, not a claim that any one current profile has a particular count.

## 1. Establish the live classification

Run through the `terminal` tool:

```bash
hermes skills list
hermes skills list --source local
hermes skills list --source builtin
hermes skills list --source hub
hermes skills list-modified
```

Record names from the rendered output, not only the summary line. The summary
is an assertion that must agree with a deduplicated name count.

Interpretation:

- `builtin`: shipped/bundled; protected from autonomous edits.
- `hub`: installed from a registry/source; protected unless explicitly adopted
  in a foreground workflow.
- `local`: present in the profile's local skills directory; origin remains
  unresolved until corroborated.
- `disabled`: still installed; do not silently omit it when the user asks for
  all installed skills.

## 2. Inspect bundled tracking

The profile's bundled manifest is an implementation detail, but it is useful
corroboration when the CLI classification needs explanation. `list-modified`
and `diff <name>` identify bundled copies with local changes.

Treat these as two separate questions:

- “Does this copy differ from stock?” — answered by `diff`.
- “Who made the difference and in which session?” — answered by the curator
  ledger or session history, not by the diff alone.

## 3. Inspect curator provenance

When available, read the curator ledger with the `read_file` tool. Each JSONL
entry may include:

- `actor` — for example `curator`, `agent`, or `user`;
- `action` — `create`, `patch`, `write_file`, etc.;
- `skill` — the affected skill;
- `evidence.session_id` — the session that motivated the mutation;
- `before` and `after` manifests — files and content hashes.

A curator `create` record with an evidence session is direct creation evidence.
A `write_file` record for a reference file proves a file mutation, not that the
whole skill was newly created.

## 4. Correlate with session history

Use `session_search` for historical messages and tool-call context. Search in
several forms:

```text
"skill_manage" "<skill-name>"
"created skill" "<skill-name>"
"modified skill" "<skill-name>"
"<skill-name>" "where did" OR "came from"
```

Prefer an actual `skill_manage` create/patch record or an explicit assistant
explanation grounded in a file/ledger inspection. A session that merely calls
`skill_view` proves consultation, not authorship.

Report confidence explicitly:

- **Confirmed** — direct mutation record or ledger entry names the skill and
  session.
- **Strongly indicated** — creation timestamp aligns with a session and the
  session contains the relevant workflow, but no direct mutation record is
  available.
- **Uncertain/pre-existing** — the skill was already present during setup or
  evidence only shows that it was loaded.

## 5. Package an approved set

After the user defines the inclusion rule, create a staging directory containing
only the selected skill directories. Preserve category/name paths so collisions
and provenance remain visible. Use `terminal` to create the archive, for
example:

```bash
zip -r /home/ubuntu/outputs/hermes-skills.zip \
  autonomous-ai-agents/hermes-skill-lifecycle \
  ... \
  -x '*/__pycache__/*' '*.pyc'
```

Run the command from the skills root, or use absolute paths consistently. Do
not archive `.env`, `auth.json`, `state.db`, sessions, logs, or the whole
`$HERMES_HOME`.

Verify before delivery:

```bash
unzip -t /home/ubuntu/outputs/hermes-skills.zip
unzip -Z1 /home/ubuntu/outputs/hermes-skills.zip
sha256sum /home/ubuntu/outputs/hermes-skills.zip
```

Parse the archive listing and compare its distinct top-level skill directories
with the approved set. Never claim “all N skills” until the counts agree.

## 6. Delivery evidence

For email, use the configured email workflow and attach the verified archive.
Resolve the recipient before sending. After sending, read back the sent record
or capture the provider's message ID and attachment metadata. A successful CLI
exit alone is not delivery proof.

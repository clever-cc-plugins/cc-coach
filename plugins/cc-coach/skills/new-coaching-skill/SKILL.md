---
name: new-coaching-skill
description: >
  Use this skill when building a new coaching skill for a specific domain. Invoke
  when the user says "create a new coaching skill", "build a coach for [domain]",
  "new coaching skill", "synthesize research into a coaching skill", or "create a
  [domain] coach skill".
allowed-tools: Read, Write, Bash
argument-hint: "<domain-name> [--plugin] (e.g., negotiation-coach, sales-coach --plugin)"
---

# New Coaching Skill

This meta-skill turns external research reports into a fully structured coaching
skill. It reads research files from the staging folder, assesses coverage across the
areas a coaching skill needs, synthesizes a `coaching-framework.md` shared reference,
and generates a `SKILL.md` skeleton ready for customization — following the
conversational shape every cc-coach skill uses (see `../_shared/skill-contract.md`).

## Step 0: Recall learnings

If `.claude/learnings.md` exists, read it silently. Apply relevant entries — such as
prior skill-creation observations or project-level defaults that would affect how this
skill is structured. Do not announce this step. If the file is absent, continue normally.

## Step 1: Determine the domain name and mode

If the user passed a domain name as `$ARGUMENTS`, use it. Normalize to kebab-case
(e.g., "Negotiation Coach" → `negotiation-coach`). Strip the `--plugin` flag from
`$ARGUMENTS` before deriving the domain name — it is not part of the name.

If no argument was passed, ask:

> "What coaching domain is this skill for? Provide a short kebab-case name — for
> example: `negotiation-coach`, `sales-coach`, `interview-coach`, `writing-coach`."

Wait for the answer before proceeding.

**Determine the mode.** After resolving the domain name, check whether `$ARGUMENTS`
contains the flag `--plugin`.

- If `--plugin` is present: you are in **plugin-dev mode**. The output will go into
  the `cc-coach` plugin repository at `plugins/cc-coach/skills/<domain-name>/`.
- If `--plugin` is absent: ask once:

  > "Where should this skill be created? Reply `project` for a project-local custom
  > skill, or `plugin` to contribute it to the cc-coach plugin."

  Wait for the answer. `project` → **end-user mode**; `plugin` → **plugin-dev mode**.

Store the mode — it controls output paths and @-imports in all subsequent steps.

## Step 2: Find research files

Check whether the staging folder exists and contains `.md` files:

```bash
ls .claude/skill-drafts/<domain-name>/ 2>/dev/null && echo "found" || echo "missing"
```

**If missing or empty:** respond with the following and stop:

> "No research files found at `.claude/skill-drafts/<domain-name>/` (your consuming
> project's local `.claude/` folder, not a folder inside the plugin repository).
>
> To get started, run `/research-prompt` for this domain — it generates a
> ready-to-paste deep-research prompt.
>
> Save each research response as a `.md` file under
> `.claude/skill-drafts/<domain-name>/`, then invoke this skill again. If you were
> running in plugin-dev mode, remember to include `--plugin` again."

**If found:** list the files and read all of them:

```bash
ls .claude/skill-drafts/<domain-name>/*.md 2>/dev/null
```

Read every file listed. Note which files appear to cover which research areas (by
content, not filename).

## Step 3: Assess research coverage

Semantically assess the research files across four coverage areas. Match on meaning,
not filenames.

| #   | Coverage area                                                                         | Maps to                                    |
| --- | ------------------------------------------------------------------------------------- | ------------------------------------------ |
| 1   | Core framework(s)/model(s) named in this domain                                       | `coaching-framework.md` main sections      |
| 2   | Step-by-step application guidance for each framework                                  | `coaching-framework.md` "How to apply"     |
| 3   | Common pitfalls / anti-patterns specific to this domain                               | `coaching-framework.md` pitfalls note      |
| 4   | Existing cc-career/cc-concept context artifacts this domain could enrich from, if any | `SKILL.md` Step 1's enrichment-source list |

Present a coverage summary like:

```
Coverage assessment for [DOMAIN]:

✓ 1. Core framework(s) — [names found]
✓ 2. Application guidance — covered
✗ 3. Common pitfalls — not found
✓ 4. Enrichment candidates — [none apply / candidate named]

Gaps: area 3.
```

For each gap, ask once:

> "Area [N] — [name] — is not covered by the research files. Choose:
> a) I synthesize this section from general knowledge (flag it for review)
> b) Pause — you run `/research-prompt` for this domain and we resume
>
> Reply with the area numbers you want me to synthesize (e.g., `3`), or `pause` to
> stop."

- If the user replies `pause`: stop and remind them to save the research under
  `.claude/skill-drafts/<domain-name>/` before invoking the skill again.
- If the user accepts knowledge-based synthesis for any gaps: note which areas will
  be marked `⚠ KNOWLEDGE-BASED` in the output and proceed.

## Step 4: Synthesize coaching-framework.md

Create the skill folder.

**End-user mode:**

```bash
mkdir -p .claude/skills/<domain-name>
```

**Plugin-dev mode:** the shared contract already exists in the repo at
`plugins/cc-coach/skills/_shared/skill-contract.md`. Only create the new skill
folder:

```bash
mkdir -p plugins/cc-coach/skills/<domain-name>
```

Write `coaching-framework.md` to:

- **End-user mode:** `.claude/skills/<domain-name>/coaching-framework.md`
- **Plugin-dev mode:** `plugins/cc-coach/skills/<domain-name>/coaching-framework.md`

Base every claim on the research files; use knowledge-based synthesis only for
user-approved gaps, and mark those sections with
`⚠ KNOWLEDGE-BASED — verify before treating this skill as production-ready`.

The file must include, per named framework: a short "What it is" paragraph, a "Best
for" / "Avoid" pair, and a numbered "How to apply" sequence — the same shape as
`career-coaching-framework.md` and `presentation-coaching-framework.md` in this
plugin. Follow with a **Common Pitfalls** section listing domain-specific
anti-patterns from the research.

Confirm when written:

- **End-user mode:** "✓ Written: `.claude/skills/<domain-name>/coaching-framework.md`"
- **Plugin-dev mode:** "✓ Written: `plugins/cc-coach/skills/<domain-name>/coaching-framework.md`"

## Step 5: Generate SKILL.md skeleton

Write the `SKILL.md` to:

- **End-user mode:** `.claude/skills/<domain-name>/SKILL.md`
- **Plugin-dev mode:** `plugins/cc-coach/skills/<domain-name>/SKILL.md`

Required YAML frontmatter — the `name:` field is the same in both modes:
`<domain-name>`. Plugin skills are namespaced automatically as
`cc-coach:<domain-name>`, so the skill's own `name:` field must never repeat the
`cc-coach-` prefix.

```yaml
---
name: <domain-name>
description: >
  Use this skill for a live coaching conversation on [DOMAIN]. Invoke when the user
  says "[TRIGGER PHRASES]". Works standalone with a generic [FRAMEWORK NAME]
  session[; enriches from <context need> when registered, if area 4 found a
  candidate].
allowed-tools: Read, Write, Bash
argument-hint: "[optional: the situation to start with]"
---
```

**End-user mode:** leave `[TODO: add trigger phrases for this domain]` in place of
`[TRIGGER PHRASES]`.

**Plugin-dev mode:** do not leave a TODO here — write 3-5 concrete, natural-sounding
trigger phrases directly, derived from the domain name itself.

Required @-import at the top of the body (after frontmatter):

**End-user mode:** `@.claude/skills/<domain-name>/coaching-framework.md **Read
when:** starting this skill`

**Plugin-dev mode:** `@./coaching-framework.md **Read when:** starting this skill`

Then this line, verbatim, matching every other cc-coach skill:

`This skill follows the shared step sequence in ../_shared/skill-contract.md (or
../../.claude/skills/_shared — adjust the relative path to match end-user mode's
actual layout). Steps below add only <domain-name>-specific behavior.`

Required skill steps — write each as a level-2 heading, following the shape of
`career-coach/SKILL.md` and `presentation-coach/SKILL.md` in this plugin exactly:

- **Step 0-1: Recall learnings and load context (enrichment only)** — if area 4
  found a candidate enrichment source, name it here and state it is optional, never
  gated. If no candidate exists (as with `life-coach`), state this step is a no-op.
- **Step 2: Session framing** — one line stating personalized vs. generic (or, if no
  enrichment source exists, just what the session will do).
- **Step 3: Coaching conversation** — apply the framework(s) from
  `coaching-framework.md`, one question at a time, waiting for each answer.
- **Step 4: Delimited reply** — reference the contract's delimiter format directly
  rather than restating it.
- **Step 5: Session-wrap save-prompt** — reference the contract's save-prompt
  directly, with tag `[cc-coach:<domain-name>]` and
  `context/<domain-name>-session-<YYYY-MM-DD>.md`, plus two example learnings
  entries specific to this domain.

Confirm when written:

- **End-user mode:** "✓ Written: `.claude/skills/<domain-name>/SKILL.md`"
- **Plugin-dev mode:** "✓ Written: `plugins/cc-coach/skills/<domain-name>/SKILL.md`"

## Step 6: Report and next steps

Present a completion summary:

```
✓ New skill created: <domain-name>

Files written:
  <path>/coaching-framework.md
  <path>/SKILL.md
```

If any areas were synthesized from general knowledge:

```
⚠ Sections synthesized from general knowledge (verify before shipping):
  - [list the affected area names]
```

**Plugin-dev mode next steps:**

```
Next steps:
1. Review coaching-framework.md — especially any ⚠ KNOWLEDGE-BASED sections.
2. Add the skill to CLAUDE.md's Key Config Files table description (the pre-commit
   hook will add the row; pre-populate the description so it doesn't land as TODO).
3. Add the skill to .claude-plugin/marketplace.json if it's a new plugin entry.
4. Test the skill in a target project.
```

**End-user mode next steps:**

```
Next steps:
1. Open SKILL.md and replace [TODO: ...] markers with domain-specific content.
2. Review coaching-framework.md — especially any ⚠ KNOWLEDGE-BASED sections.
3. Test the skill.
```

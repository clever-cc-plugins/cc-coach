# networking-coach: design

## Context

The user's personal network has shrunk to near zero and they want coaching support
for rebuilding it. `cc-coach:life-coach` already covers this via its
Wheel-of-Life-plus-GROW session (relationships is one of its life domains). But the
user pointed out that the _tactical_ mechanics of networking — starting
conversations, follow-up cadence, where to meet people, maintaining contact over
time, overcoming approach anxiety — are largely domain-agnostic: the same mechanics
apply whether the goal is professional (career-coach's territory) or personal
(life-coach's territory). Only the framing/purpose differs.

This design adds a fourth coaching skill, `networking-coach`, that owns the tactical
playbook, and a hand-off mechanism so `career-coach` and `life-coach` can bring it in
mid-session when the conversation turns operational — "let's bring in networking
expertise for this part" — without losing session context or breaking conversational
flow.

## Scope

`networking-coach` owns tactics only: how to start conversations, follow-up cadence,
maintaining a network over time, where/how to find people, overcoming approach
anxiety, reciprocity norms. It stays silent on _why_ the user is networking — that
purpose/framing stays with whichever skill brought it in (or, when invoked directly,
with the user's own stated goal).

## Creating the skill

No new mechanism needed here — this follows the plugin's existing, already-designed
path for adding a coaching skill:

1. `/cc-coach:research-prompt` generates a deep-research prompt for the networking
   domain.
2. The user runs that research externally and saves results under
   `.claude/skill-drafts/networking-coach/`.
3. `/cc-coach:new-coaching-skill networking-coach --plugin` synthesizes
   `plugins/cc-coach/skills/networking-coach/coaching-framework.md` and `SKILL.md`,
   following the same shape as `career-coaching-framework.md` and
   `presentation-coaching-framework.md`.

`networking-coach` is directly invocable on its own (trigger phrases + slash
command), exactly like the other three skills — it does not require being invoked
via a hand-off.

## The hand-off mechanism

This is the one genuinely new pattern in the plugin: a skill referencing another
skill's framework mid-session. It is added narrowly — only to `career-coach/SKILL.md`
and `life-coach/SKILL.md` — not to the shared `_shared/skill-contract.md`, since it
is specific to these two skills' relationship with `networking-coach`, not a general
capability every cc-coach skill needs.

Both files gain a new **Step 3a: Networking hand-off**, inserted between Step 3
(coaching conversation) and Step 4 (delimited reply):

> When the conversation turns operational/tactical on networking specifically (how
> to start conversations, follow-up cadence, where to meet people, maintaining
> contact) — not before, and not for networking framed only as a goal or motivation
> — say one line bringing in the expert, e.g. "This is networking-coach's
> territory — let's bring that expertise in for this part." Then read
> `../networking-coach/coaching-framework.md` and apply it for that portion of the
> conversation. Once the tactical question is resolved, return to the parent
> skill's own framework (GROW / Wheel of Life) to keep the session moving.

Mechanics:

- No literal nested `Skill` tool invocation — `networking-coach`'s
  `coaching-framework.md` is read directly, the same way `career-coach` already
  reads its own framework file. This avoids nesting `networking-coach`'s own
  session-framing/save-prompt steps inside the parent's.
- The hand-off is a framework swap within the same session. Step 4 (delimited
  reply) and Step 5 (session-wrap save-prompt) continue to apply across the whole
  conversation, including the hand-off portion — there is no separate save-prompt
  or session-wrap fired when the hand-off starts or ends.
- The hand-off can happen more than once in a session if operational questions
  resurface after moving back to the parent framework.

## Files touched

- New: `plugins/cc-coach/skills/networking-coach/coaching-framework.md` (via
  `new-coaching-skill`)
- New: `plugins/cc-coach/skills/networking-coach/SKILL.md` (via `new-coaching-skill`)
- Edited: `plugins/cc-coach/skills/career-coach/SKILL.md` (add Step 3a)
- Edited: `plugins/cc-coach/skills/life-coach/SKILL.md` (add Step 3a)
- Edited: `CLAUDE.md` Key Config Files table (new skill row — handled by the
  pre-commit sync hook, description pre-populated to avoid a TODO landing)
- Edited: `.claude-plugin/marketplace.json` — **not** touched by this work; the
  plugin is still unregistered in the catalog per the existing design doc, and this
  addition doesn't change that status.

## Testing and validation

Same as the rest of the plugin: no automated tests (prompt-engineering artifacts),
validated via the existing `.githooks/pre-commit` (gitleaks + CLAUDE.md table sync)
and manual review against the
[repo guideline](https://github.com/clever-cc-plugins/marketplace/blob/main/docs/cc-plugin-repo-guideline.md)
checklist. Additionally, before considering this done: a live trial conversation in
each of the three entry points — standalone `networking-coach`, hand-off from
`career-coach`, hand-off from `life-coach` — to confirm the framing lands and the
session resumes cleanly afterward.

## Out of scope for this design

- The actual research content and framework text for `networking-coach` (produced by
  the `research-prompt` → `new-coaching-skill` pipeline, not authored here).
- Registering `cc-coach` in the marketplace catalog — still deferred per the
  original plugin design doc.
- A general cross-skill hand-off pattern in `skill-contract.md` for future skills —
  YAGNI until a second case beyond networking-coach shows up.

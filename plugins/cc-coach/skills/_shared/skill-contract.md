# cc-coach Skill Contract — Shared Reference

Every cc-coach skill follows the same step sequence. A SKILL.md **references this
file** rather than restating the sequence — this is the single source of truth, so
the steps cannot drift skill to skill. A coaching skill is a live, multi-turn
conversation, not a single-shot document generator — Steps 3–5 re-run on each
substantive exchange within the same invocation rather than firing once. A skill
documents only its own specifics: its named coaching framework, which sibling-plugin
context file (if any) it opportunistically enriches from, and its session-wrap
save-prompt wording.

## The sequence

0. **Recall learnings** (silent) — read `.claude/learnings.md` if present, across
   all plugin tags. Apply relevant observations. Never announce this step; surface
   nothing unless it changes behavior.
1. **Load context — enrichment, never gating** — read the `## Context files` table
   in `CLAUDE.md`. Check for the skill's own named enrichment source(s) by semantic
   Summary match, never by label or filename. This skill never blocks or asks an
   ask-once question if the enrichment source is absent — it proceeds with its
   generic baseline framework instead.
2. **Session framing** — before the first substantive question, state in one line
   whether this session is running personalized (enrichment source loaded, name it)
   or generic (no matching context found), and name the coaching framework being
   applied. Example: `"Running with your career plan loaded — coaching against the
milestones in context/career-plan.md, using the GROW model."` or `"No career plan
on file yet, so this is a generic GROW-model session — happy to load one if you
register `/career-plan`'s output partway through."`
3. **Coaching conversation** — apply the skill's named framework as a structured
   conversation, not a form to fill in silently. Ask one question at a time; wait
   for the answer before the next. No fixed section skeleton — pace and depth follow
   the conversation.
4. **Delimited reply** — every substantive reply, even a short one, is wrapped in a
   delimiter block with a topic header:

   ```
   ─────────────────────────────────────────────────────────────────
   ## [Topic Header]
   ─────────────────────────────────────────────────────────────────

   [Coaching reply here]

   ─────────────────────────────────────────────────────────────────
   ```

5. **Session-wrap save-prompt** — after a reply that surfaces a decision, an action
   item, or a commitment worth keeping, offer to persist it — do not wait for an
   explicit "end session" signal a coaching conversation may never reach:

   1. Ask: `"Worth saving this? I can add it to .claude/learnings.md (lightweight,
for future sessions to recall) or write a session summary to
context/<skill-name>-session-<date>.md (for you to revisit, not auto-loaded by
other skills). Which, or neither?"`
   2. If **learnings**: append to `.claude/learnings.md` tagged
      `[cc-coach:<skill-name>]`.
   3. If **session summary**: write to `context/<skill-name>-session-<YYYY-MM-DD>.md`
      with a collision-check suffix (`-2`, `-3`, ...) if that exact date's file
      already exists. Do **not** register it in the `## Context files` table — it's
      a personal record, not input another skill should auto-load.
   4. If **neither**: continue without saving.

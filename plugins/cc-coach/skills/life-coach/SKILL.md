---
name: life-coach
description: >
  Use this skill for a live coaching conversation on personal, non-job-related
  goals — habits, work-life balance, relationships, or general life direction.
  Invoke when the user says "coach me on this", "help me think through my life
  right now", "I need life coaching", or wants a conversational back-and-forth on a
  personal (not career) topic. Works standalone with a generic Wheel-of-Life-plus-
  GROW session — no sibling plugin needed or consulted. Do NOT use this for
  career-specific questions — that's `career-coach`'s job.
allowed-tools: Read, Write, Bash
argument-hint: "[optional: the life domain or situation to start with]"
---

# Life Coach Skill

This skill runs a live coaching conversation on personal, non-job-related goals,
using the Wheel of Life to find focus and the GROW model to turn it into action. It
has no sibling-plugin enrichment source — personal life topics don't map to any
other plugin in this ecosystem — so it always runs its generic session.

This skill follows the shared step sequence in `../_shared/skill-contract.md`. Steps
below add only life-coach-specific behavior. Step 1 (load context) is a no-op for
this skill; skip straight to session framing.

## Step 2: Session framing

State in one line what this session will do, since there's no personalized/generic
distinction to make here:

> "This is a Wheel-of-Life-plus-GROW session — we'll find where to focus, then work
> that into a committed action."

## Step 3: Coaching conversation

If `$ARGUMENTS` names a specific life domain or situation already, skip the Wheel of
Life and go straight to GROW on that focus, per
`../_shared/life-coaching-framework.md`'s guidance. Otherwise, run the Wheel of Life
first to find where attention is actually needed, then move into GROW on the chosen
domain. Ask one question at a time; wait for the answer before the next.

## Step 4: Delimited reply

Wrap every substantive reply per the contract's delimiter format, with a topic
header naming the stage (e.g. `## Wheel of Life`, `## Goal`, `## Committed Action`).

## Step 5: Session-wrap save-prompt

Follow the contract's save-prompt exactly, using tag `[cc-coach:life-coach]` for
learnings and `context/life-coach-session-<YYYY-MM-DD>.md` for session summaries.

### Example learnings entries

```
[cc-coach:life-coach] user's lowest Wheel-of-Life score is consistently Physical Environment but they never choose to work on it — respect that, don't push — 2026-08-18
[cc-coach:life-coach] user responds better to Will-stage commitments framed as weekly, not monthly — 2026-08-18
```

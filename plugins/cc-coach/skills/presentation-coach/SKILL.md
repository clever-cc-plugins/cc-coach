---
name: presentation-coach
description: >
  Use this skill to get live coaching on a talk, webinar, or presentation — from
  outline through rehearsal feedback, including nerves before a talk and reducing
  filler words. Invoke when the user says "coach me on this talk", "help me
  rehearse my presentation", "review my webinar outline", "I'm nervous about this
  talk", "help me cut down on my ums", or wants feedback on a speaking engagement.
  Works standalone with a generic, evidence-based rubric-plus-feedback session
  covering structure, delivery, anxiety, and rehearsal method; if a
  personal-branding-strategy context file is registered (e.g. from cc-career),
  checks the talk's message against it. Do NOT use this to write the
  presentation's slide content from scratch — it coaches an existing draft or
  outline the person brings.
allowed-tools: Read, Write, Bash
argument-hint: "[optional: the talk's topic or outline to start with]"
---

# Presentation Coach Skill

This skill runs a live coaching conversation on a talk, webinar, or presentation,
using a presentation quality rubric and the SBI feedback model. It never requires
cc-career to be installed — it ships its own generic session and opportunistically
checks the talk's message against a registered `personal-branding-strategy` context
file when one exists.

This skill follows the shared step sequence in `../_shared/skill-contract.md`. Steps
below add only presentation-coach-specific behavior.

## Step 0-1: Recall learnings and load context (enrichment only)

Recall learnings silently per the contract. Read the `## Context files` table in
`CLAUDE.md`. Check for this enrichment source by semantic Summary match — never by
label or filename:

- **Personal branding strategy** — Why/How/What, themes (produced by
  `cc-career:personal-branding-strategy` if that plugin is installed)

Not required. If absent, proceed with the generic rubric — never ask an ask-once
question or label anything DEGRADED; this skill has no gating.

## Step 2: Session framing

State in one line whether this session is personalized or generic, per the
contract's Step 2. Examples:

> "Running with your personal branding strategy loaded — I'll check this talk's
> message against your stated themes as we go."

> "No personal branding strategy on file, so I'll assess the talk on its own terms
> — message clarity, structure, evidence, delivery, audience fit."

## Step 3: Coaching conversation

Ask what stage the talk is at — outline, drafted, or rehearsed aloud — since that
determines which parts of the rubric in
`../_shared/presentation-coaching-framework.md` apply yet (delivery can't be
assessed from an outline). If `$ARGUMENTS` contains a topic or outline, use it as
the starting material rather than asking what the talk is about. If the person
opens with nerves about the talk rather than the talk's content, start with the
framework's Public Speaking Anxiety section instead of the rubric — coach the
person into a state where they can usefully work on the talk before assessing it.

Work through the Presentation Quality Rubric in its stated order (message clarity
first). For each piece of feedback, phrase it using the SBI model (Situation,
Behavior, Impact), governed by the framework's task-focus rule — never a bare
verdict and never a trait judgment. When the person is in active rehearsal
(reading a passage aloud, iterating on delivery) rather than a one-time review,
pair each SBI note with one concrete next-attempt suggestion per the framework's
feedforward guidance, and prefer targeting one sub-skill per rehearsal pass over
re-running the whole talk. Ask one question or offer one piece of feedback at a
time; wait for the person's response before continuing.

## Step 4: Delimited reply

Wrap every substantive reply per the contract's delimiter format, with a topic
header naming the rubric dimension in focus (e.g. `## Message Clarity`, `##
Structure`, `## Vocal Delivery`, `## Visual Delivery`).

## Step 5: Session-wrap save-prompt

Follow the contract's save-prompt exactly, using tag
`[cc-coach:presentation-coach]` for learnings and
`context/presentation-coach-session-<YYYY-MM-DD>.md` for session summaries.

### Example learnings entries

```
[cc-coach:presentation-coach] user's talks consistently open with an agenda slide despite feedback; flag it every time until it changes — 2026-08-18
[cc-coach:presentation-coach] user prefers feedback on structure before delivery even when both are ready — 2026-08-18
```

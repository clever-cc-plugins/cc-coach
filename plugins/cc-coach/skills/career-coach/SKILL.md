---
name: career-coach
description: >
  Use this skill for a live coaching conversation on a career question or decision.
  Invoke when the user says "coach me on this career decision", "I need career
  coaching", "help me think through this career situation out loud", or wants a
  conversational back-and-forth rather than a document. Works standalone with a
  generic GROW-model session; if a career-plan or personal-branding-strategy context
  file is registered (e.g. from cc-career), coaches against that specific plan
  instead. Do NOT use this to build or revise a career plan document — that's
  cc-career's job; this skill only coaches the conversation.
allowed-tools: Read, Write, Bash
argument-hint: "[optional: the career situation or question to start with]"
---

# Career Coach Skill

This skill runs a live, multi-turn coaching conversation on a career question or
decision, using the GROW model. It never requires cc-career to be installed — it
ships its own generic GROW session and opportunistically enriches from a registered
`career-plan` or `personal-branding-strategy` context file when one exists.

This skill follows the shared step sequence in `../_shared/skill-contract.md`. Steps
below add only career-coach-specific behavior.

## Step 0-1: Recall learnings and load context (enrichment only)

Recall learnings silently per the contract. Read the `## Context files` table in
`CLAUDE.md`. Check for these two enrichment sources by semantic Summary match —
never by label or filename:

- **Career plan** — direction, Career Anchor, prioritized skills, milestones
  (produced by `cc-career:career-plan` if that plugin is installed)
- **Personal branding strategy** — Why/How/What, themes (produced by
  `cc-career:personal-branding-strategy` if that plugin is installed)

Neither is required. If absent, proceed with the generic framework — never ask an
ask-once question or label anything DEGRADED; this skill has no gating.

## Step 2: Session framing

State in one line whether this session is personalized or generic, per the
contract's Step 2. Examples:

> "Running with your career plan loaded — coaching against the milestones in
> context/career-plan.md, using the GROW model."

> "No career plan on file yet, so this is a generic GROW-model session. If you want
> it grounded in a specific plan, run cc-career's `/career-plan` first — or we can
> just start with what's on your mind."

## Step 3: Coaching conversation

Apply the GROW model from `../_shared/career-coaching-framework.md`. If
`$ARGUMENTS` names a starting situation, open with it as the Goal-stage question
rather than asking what to talk about. Follow the framework's guidance on when to
ground Goal/Reality in loaded context vs. asking directly, and on letting the person
generate Options before adding any.

## Step 4: Delimited reply

Wrap every substantive reply per the contract's delimiter format, with a topic
header naming the stage or sub-topic (e.g. `## Goal`, `## Options`, `## Committed
Action`).

## Step 5: Session-wrap save-prompt

Follow the contract's save-prompt exactly, using tag `[cc-coach:career-coach]` for
learnings and `context/career-coach-session-<YYYY-MM-DD>.md` for session summaries.

### Example learnings entries

```
[cc-coach:career-coach] user consistently under-scopes the Will stage, needs a second push for a specific date — 2026-08-18
[cc-coach:career-coach] user's Career Anchor (Technical/Functional) means management-track Options should be offered but not pushed — 2026-08-18
```

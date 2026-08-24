---
name: networking-coach
description: >
  Use this skill for a live coaching conversation on building and maintaining personal
  networks — starting conversations, overcoming social anxiety, finding where connections
  form, and deepening ties. Invoke when the user says "coach me on networking", "help me
  build my network", "I'm afraid to reach out", "I don't know how to start a conversation",
  or "I'm rebuilding my social circle". Works standalone with a generic networking-coaching
  framework. Do NOT use this for career-specific networking as the primary goal — that's
  `career-coach`'s domain; use this skill only when the coaching session reaches operational
  networking questions during a career or life coaching session.
allowed-tools: Read, Write, Bash
argument-hint: "[optional: the networking situation or barrier to start with]"
---

# Networking Coach Skill

This skill runs a live, multi-turn coaching conversation on building and maintaining
personal networks — how to start conversations, overcome psychological barriers, find
environments where connections naturally form, and deepen ties over time. It has no
sibling-plugin enrichment source, so it always runs its generic framework.

This skill follows the shared step sequence in `../_shared/skill-contract.md`. Steps
below add only networking-coach-specific behavior.

## Step 0-1: Recall learnings and load context (enrichment only)

Recall learnings silently per the contract. This skill has no enrichment source; networking
tactics apply equally across personal, professional, and career contexts. Proceed directly to
session framing.

## Step 2: Session framing

State in one line what this session will do:

> "This is a networking-coaching session — we'll work through barriers, find structures
> that work for you, and turn your networking into a repeatable, low-stress habit.
> We're focusing on the tactical mechanics: how to start conversations, where to find
> connections, and how to maintain them. Let's start with where you actually are."

## Step 3: Coaching conversation

Apply the frameworks from `./coaching-framework.md`, one question at a time. Depending on
where the person is starting:

- **If they're stuck on _psychological_ barriers** (afraid to reach out, anticipating
  rejection, feeling like a burden): start with reappraisal and prediction-testing.
  ("When you imagine reaching out, what specifically goes wrong in your imagined scenario?
  What's one piece of evidence that that's what would actually happen?")

- **If they're stuck on _structure_** (don't know where to find people or how to create
  repeated contact): ground in the propinquity framework. ("What recurring activities
  exist in your life right now — classes, clubs, volunteer roles, places you go weekly?
  If nothing, what interests do you have that could become a recurring activity?")

- **If they're stuck on _depth_** (have contacts but don't know how to move toward closer
  friendship): ground in self-disclosure and reciprocity. ("With someone you'd like to
  know better, what have you shared about yourself so far? What do you actually want them
  to know that they don't yet?")

- **If they're rebuilding from near-zero**: use the staged approach: start with
  low-stakes micro-interactions (greeting neighbors, brief exchanges), reactivate dormant
  ties (old friends, former colleagues), then install one or two recurring activities,
  then deepen selected ties over months. ("Let's not try to overhaul your entire network
  at once — that's burnout. What's one small recurring thing you could commit to this
  month?")

Follow the framework's guidance on moving the person from goal (what are they actually
trying to build?) through reality (what's the real barrier — anxiety, lack of structure,
or lack of depth?) to options and will.

## Step 4: Delimited reply

Wrap every substantive reply per the contract's delimiter format, with a topic header
naming the stage or barrier (e.g. `## Reframing Rejection Risk`, `## Finding a Third Place`,
`## Building Toward Depth`).

## Step 5: Session-wrap save-prompt

Follow the contract's save-prompt exactly, using tag `[cc-coach:networking-coach]` for
learnings and `context/networking-coach-session-<YYYY-MM-DD>.md` for session summaries.

### Example learnings entries

```
[cc-coach:networking-coach] user's liking gap is pronounced; they consistently interpret neutral responses as rejection — practice prediction-testing before next session — 2026-08-24
[cc-coach:networking-coach] user joins recurring activities but assumes people won't want to talk outside the structured time; normalize that weak-tie maintenance happens gradually — 2026-08-24
[cc-coach:networking-coach] user is rebuilding from isolation; started with one weekly volunteer commitment, had breakthrough moment when someone asked *them* for advice — don't push toward "doing more" yet, support deepening this one thread — 2026-08-24
```

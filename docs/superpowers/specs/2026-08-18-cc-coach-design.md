# cc-coach: design

## Context

The clever-cc-plugins ecosystem has a marketing-focused strategy/execution split:
`cc-concept` (positioning, GTM, campaign concepting) produces planning artifacts;
`cc-content` (LinkedIn posts, blog articles, etc.) consumes them to produce finished
content. `cc-coach` extends this pattern into live coaching: it plays the cc-content
role — a bundle of small, independent skills, each producing/facilitating one thing —
for coaching conversations across job-related and personal-life domains.

Its sibling plugin, [`cc-career`](https://github.com/clever-cc-plugins/cc-career),
plays the cc-concept role for the user's own career: it owns the career plan and
personal-branding strategy that cc-coach's `career-coach` skill can read as context.

The open design question this doc resolves: where a domain that spans both plugins —
career coaching — belongs, and whether cc-coach skills should require their matching
domain plugin to be installed.

## Role

cc-coach owns live coaching sessions: a bundle of independent coaching-persona skills
(career, presentation, life, ...), each producing/facilitating one type of session. It
does not maintain long-lived plans — that's cc-career's (or, for marketing-adjacent
coaching, cc-concept's) job.

## Cross-plugin context sharing

cc-coach skills never require a sibling plugin (cc-career, cc-concept, ...) to be
installed. Each ships a generic, domain-general coaching framework as its baseline
(e.g. `career-coach` ships a goal-clarification / gap-analysis / action-planning
framework that works standalone).

If the loaded CLAUDE.md's `## Context files` table lists a matching file (e.g.
`career-plan.md` from cc-career, `positioning.md` from cc-concept), the skill reads it
and coaches against that specific plan. If not, it proceeds with the generic
framework and notes it's running without personalized context.

This is the same pattern `cc-content:linkedin-post` already uses for brand-voice and
positioning context (see
[`cc-content/plugins/cc-content/skills/linkedin-post/SKILL.md`](https://github.com/clever-cc-plugins/cc-content/blob/main/plugins/cc-content/skills/linkedin-post/SKILL.md))
— reused here, not invented. It resolves three concerns raised during brainstorming:

- **No install dependency.** cc-coach installs and works standalone, same experience
  as every other plugin in this marketplace today. No plugin in this ecosystem
  currently declares a hard dependency on another, and this design doesn't start.
- **No knowledge duplication drift.** The baseline framework in cc-coach is
  methodology-level (how to structure a session, what questions to ask). cc-career's
  planning logic is a different layer (what a good career plan contains, how to build
  one). There's little surface area for the two to duplicate or drift apart.
- **No future migration pain.** Because cc-coach never depended on cc-career's files
  existing, adding cc-career later just switches a skill from generic to
  context-aware — nothing is removed or replaced, so there's nothing to migrate.

### The career-coaching ambiguity, resolved

A "career coach" skill is not duplicated between the two plugins:

- `cc-career:career-plan` is where the plan gets built and revised.
- `cc-coach:career-coach` is where a live coaching conversation happens, using that
  plan as context if it's registered, generic framework if not.

Same relationship as `cc-concept:positioning` → `cc-content:linkedin-post`.

## v1 skill set

| Skill                | Purpose                                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `career-coach`       | Live coaching conversation on career questions. Reads `career-plan.md` / `personal-branding-strategy.md` when registered as context; generic career-coaching framework otherwise. |
| `presentation-coach` | Coaches on talks, webinars, and presentations — e.g. for marketing-strategy-driven speaking engagements.                                                                          |
| `life-coach`         | Broader personal-life coaching (not job-related): goal-setting, habits, work-life balance.                                                                                        |
| `new-coaching-skill` | Meta-skill for scaffolding a new coach skill. Mirrors `cc-content:new-content-skill`.                                                                                             |
| `research-prompt`    | Generates deep-research prompts for a coaching domain — feeds both live sessions and `new-coaching-skill` authoring. Mirrors `cc-content:research-prompt`.                        |

## Testing and validation

No automated tests for skill content — consistent with cc-content and cc-concept,
since these are prompt-engineering artifacts, not code. Validation is the existing
`.githooks/pre-commit` (gitleaks + CLAUDE.md table sync) plus manual review against
the [repo guideline](https://github.com/clever-cc-plugins/marketplace/blob/main/docs/cc-plugin-repo-guideline.md)'s
checklist.

## Out of scope for this design

- The exact SKILL.md content for each skill (written during implementation, following
  existing skills of the same shape as templates — `new-coaching-skill` and
  `research-prompt` follow their cc-content namesakes; `career-coach` /
  `presentation-coach` / `life-coach` are a new shape with no direct precedent).
- Additional cc-coach domains beyond the v1 three (e.g. negotiation-coach) — added
  later via `new-coaching-skill` without a design change.
- Registering this plugin in the marketplace catalog (`marketplace.json`) — deferred
  until skills exist.

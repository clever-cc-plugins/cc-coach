<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/clever-cc-plugins/.github/main/assets/logo-dark.svg" />
    <img src="https://raw.githubusercontent.com/clever-cc-plugins/.github/main/assets/logo.svg" width="220" alt="clever [cc] plugins" />
  </picture>
</p>

# cc-coach

A [Claude Code](https://claude.ai/code) plugin bundling live-coaching skills across job-related and personal-life domains.

---

## Plugin: `cc-coach`

`cc-coach` owns live coaching sessions — a bundle of independent coaching-persona skills, each producing/facilitating one type of conversation. It doesn't maintain long-lived plans; that's its sibling plugin [`cc-career`](https://github.com/clever-cc-plugins/cc-career)'s job for career direction, or [`cc-concept`](https://github.com/clever-cc-plugins/cc-concept)'s for marketing strategy.

Every coaching skill works standalone with a generic, domain-general framework — no sibling plugin required. If your project has a matching context file registered (e.g. `career-plan.md` from `cc-career`), the skill reads it and coaches against that specific plan instead.

| Skill                          | What it does                                                                                                                                              |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/cc-coach:career-coach`       | Live GROW-model coaching conversation on a career question or decision — coaches against your `cc-career` plan when one is registered, generic otherwise  |
| `/cc-coach:life-coach`         | Live coaching on personal, non-job-related goals — habits, work-life balance, relationships, general life direction                                       |
| `/cc-coach:networking-coach`   | Live coaching on building and maintaining personal networks — starting conversations, overcoming social anxiety, deepening ties                           |
| `/cc-coach:presentation-coach` | Live coaching on talks, webinars, and presentations — outline through rehearsal feedback, using a rubric plus SBI feedback                                |
| `/cc-coach:research-prompt`    | Generates a vendor-neutral deep-research prompt for a coaching domain or methodology, ready to paste into Claude, ChatGPT, Gemini, Perplexity, or similar |
| `/cc-coach:new-coaching-skill` | Builds a new coaching skill for a specific domain from research notes                                                                                     |

---

## Installation

Open Claude Code in any project and run:

```
/plugin marketplace add clever-cc-plugins/marketplace
/plugin install cc-coach@clever-cc-plugins
```

This makes all skills immediately available.

### Keeping Skills Current

Auto-update is disabled by default for third-party marketplaces. To enable it:

1. Run `/plugin` in Claude Code
2. Go to the **Marketplaces** tab
3. Toggle auto-update for `clever-cc-plugins/marketplace`

Once enabled, skills update automatically on startup when new versions are available.

---

## Getting Started

Just invoke the coaching skill that matches what you want to talk through — there's no onboarding step required:

```
/cc-coach:career-coach
```

```
/cc-coach:presentation-coach
```

Each skill runs a live, conversational session rather than producing a document. If the domain needs research first (a coaching methodology you want grounded in evidence, say), start with:

```
/cc-coach:research-prompt
```

and paste the resulting prompt into a deep-research tool before your session.

Want a coach for a domain that isn't covered yet? Build one:

```
/cc-coach:new-coaching-skill
```

---

## Working with cc-career

Installing [`cc-career`](https://github.com/clever-cc-plugins/cc-career) is optional, not required. `career-coach` runs a standalone GROW-model session by default; if `cc-career` is installed and has produced a `career-plan.md` or `personal-branding-strategy.md` registered in your project's `## Context files` table, `career-coach` reads it and coaches against that specific plan instead of the generic framework. Neither plugin depends on the other being installed.

---

## License

[MIT](LICENSE) — Copyright (c) 2026 Michael van Laar

---

<p align="center">
  Part of the <a href="https://github.com/clever-cc-plugins">clever-cc-plugins</a> family · <a href="https://github.com/clever-cc-plugins/marketplace">marketplace</a> · <a href="https://github.com/clever-cc-plugins/cc-config">cc-config</a> · <a href="https://github.com/clever-cc-plugins/cc-concept">cc-concept</a> · <a href="https://github.com/clever-cc-plugins/cc-content">cc-content</a> · <a href="https://github.com/clever-cc-plugins/cc-career">cc-career</a> · <a href="https://github.com/clever-cc-plugins/cc-handoff">cc-handoff</a> · <a href="https://github.com/clever-cc-plugins/cc-chime">cc-chime</a>
</p>

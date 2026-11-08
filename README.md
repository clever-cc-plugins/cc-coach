<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/clever-cc-plugins/.github/main/assets/logo-dark.svg" />
    <img src="https://raw.githubusercontent.com/clever-cc-plugins/.github/main/assets/logo.svg" width="220" alt="clever [cc] plugins" />
  </picture>
</p>

# <img src="assets/icon.svg" width="40" height="40" align="top" alt="" />&nbsp;cc-coach

A [Claude Code](https://claude.ai/code) plugin that bundles live-coaching skills for job-related and personal-life topics. Every session starts on time, and nobody bills by the hour.

---

## At a Glance

`cc-coach` owns live coaching sessions. It's a bundle of independent coaching-persona skills, and each one facilitates one type of conversation. It doesn't maintain long-lived plans. Its sibling plugin [`cc-career`](https://github.com/clever-cc-plugins/cc-career) handles career direction, and [`cc-concept`](https://github.com/clever-cc-plugins/cc-concept) handles marketing strategy.

Every coaching skill works standalone with a generic framework for its domain, so no sibling plugin is required. If your project has a matching context file registered (for example `career-plan.md` from `cc-career`), the skill reads it and coaches against that specific plan instead.

| Skill                          | What it does                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `/cc-coach:career-coach`       | Coaches you live on a career question or decision with the GROW model, against your `cc-career` plan when one is registered and with the generic framework otherwise                                                                                                                                                                 |
| `/cc-coach:life-coach`         | Coaches you live on personal, non-job-related goals: habits, work-life balance, relationships, general life direction                                                                                                                                                                                                                |
| `/cc-coach:networking-coach`   | Coaches you live on building and maintaining personal networks: starting conversations, overcoming social anxiety, deepening ties                                                                                                                                                                                                    |
| `/cc-coach:presentation-coach` | Coaches you live on talks, webinars, and presentations, from outline to rehearsal feedback, using a rubric plus SBI feedback and a built-in devil's advocate pass that anticipates audience objections. On request, it builds a new PowerPoint deck from your template or revises an existing deck, changing only what you asked for |
| `/cc-coach:productivity-coach` | Coaches you live on task overwhelm, procrastination, focus, and habit-building. It checks popular productivity-book claims (GTD, The 4-Hour Work Week, A Perfect Mess) against the research and corrects the myths                                                                                                                   |
| `/cc-coach:research-prompt`    | Generates a vendor-neutral deep-research prompt for a coaching domain or methodology, ready to paste into Claude, ChatGPT, Gemini, Perplexity, or similar                                                                                                                                                                            |
| `/cc-coach:new-coaching-skill` | Builds a new coaching skill for a specific domain from research notes                                                                                                                                                                                                                                                                |

---

## Installation

Open Claude Code in any project and run:

```
/plugin marketplace add clever-cc-plugins/marketplace
/plugin install cc-coach@clever-cc-plugins
```

All skills are available immediately.

### Keeping Skills Current

Auto-update is off by default for third-party marketplaces. To switch it on:

1. Run `/plugin` in Claude Code
2. Open the **Marketplaces** tab
3. Toggle auto-update for `clever-cc-plugins/marketplace`

Once it's on, Claude Code updates the skills on startup whenever a new version is available.

### Uninstalling

```
/plugin uninstall cc-coach@clever-cc-plugins
```

To remove the marketplace as well (this uninstalls every plugin you installed from it):

```
/plugin marketplace remove clever-cc-plugins
```

---

## Getting Started

Invoke the coaching skill that matches what you want to talk through. There's no onboarding step:

```
/cc-coach:career-coach
```

```
/cc-coach:presentation-coach
```

Each skill runs a live conversation and doesn't produce a document. If a domain needs research first (a coaching methodology you want grounded in evidence, say), start with:

```
/cc-coach:research-prompt
```

Paste the resulting prompt into a deep-research tool before your session.

Want a coach for a domain that isn't covered yet? Build one:

```
/cc-coach:new-coaching-skill
```

---

## Working with cc-career

Installing [`cc-career`](https://github.com/clever-cc-plugins/cc-career) is optional. `career-coach` runs a standalone GROW-model session by default. If `cc-career` has produced a `career-plan.md` or `personal-branding-strategy.md` that is registered in your project's `## Context files` table, `career-coach` reads it and coaches against that specific plan instead of the generic framework. Neither plugin needs the other.

---

## Contributing

Issues and pull requests are welcome. If you've spotted a gap or a rough edge, please open an issue first so we can agree on the approach.

---

## License

[MIT](LICENSE), Copyright (c) 2026 Michael van Laar

---

<p align="center">
  Part of the <a href="https://github.com/clever-cc-plugins">clever-cc-plugins</a> family · <a href="https://github.com/clever-cc-plugins/marketplace">marketplace</a> · <a href="https://github.com/clever-cc-plugins/cc-config">cc-config</a> · <a href="https://github.com/clever-cc-plugins/cc-concept">cc-concept</a> · <a href="https://github.com/clever-cc-plugins/cc-content">cc-content</a> · <a href="https://github.com/clever-cc-plugins/cc-career">cc-career</a> · <a href="https://github.com/clever-cc-plugins/cc-handoff">cc-handoff</a> · <a href="https://github.com/clever-cc-plugins/cc-chime">cc-chime</a> · <a href="https://github.com/clever-cc-plugins/cc-chef">cc-chef</a>
</p>

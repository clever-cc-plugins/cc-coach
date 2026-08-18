# Research Prompts

Ready-to-paste deep-research prompts to strengthen this plugin's skills with
scientific background and best practices, beyond what was available from
general knowledge and practitioner books when each skill was built.

## Scope

Only skills that apply a named framework to run a coaching conversation get a
research prompt — a research prompt doesn't attach usefully to a pure
meta/process skill, since there's no framework to validate or deepen.

| Skill                | Research prompt                                | Why / why not                                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `career-coach`       | [career-coach.md](career-coach.md)             | GROW + networking domain, sourced from practitioner books; no peer-reviewed backing yet                                                                                                                                                        |
| `presentation-coach` | [presentation-coach.md](presentation-coach.md) | Rubric + SBI model, general knowledge; the Cialdini portion already has research backing via `cc-content`, but not re-verified for live delivery specifically                                                                                  |
| `life-coach`         | [life-coach.md](life-coach.md)                 | Wheel of Life + GROW + follow-through + resilience + perfectionism domains, all practitioner-book sourced; also the skill closest to mental-health-adjacent territory, so this prompt explicitly asks for coaching-vs-treatment scope guidance |
| `new-coaching-skill` | —                                              | Meta-skill for scaffolding new coach skills; no framework of its own to research                                                                                                                                                               |
| `research-prompt`    | —                                              | Meta-skill for generating research prompts; no framework of its own to research                                                                                                                                                                |

## Using a prompt

1. Open the prompt file for the skill you want to strengthen.
2. Paste the delimited prompt block into a "deep research" AI tool (Claude,
   ChatGPT, Gemini, Perplexity, or similar).
3. Save the response as Markdown under `docs/research/<skill-name>.md`
   (matching the convention `cc-concept` already uses for its researched
   skills).
4. Use the research to refine the skill's `_shared/*-framework.md` file —
   validate the frameworks already in use, add any well-evidenced ones the
   research surfaces, correct anything the current version got wrong, and
   for `life-coach` specifically, tighten the non-clinical boundary language
   against whatever the research turns up.

---
name: research-prompt
description: >
  Use this skill when the owner wants a ready-to-paste research prompt for a "deep
  research" AI tool (Claude, ChatGPT, Gemini, Perplexity, DeepSeek, or similar) to
  investigate a coaching domain or methodology before a session or before building a
  new coach skill. Invoke when the user says "give me a research prompt for X
  coaching", "write me a deep research prompt on this coaching methodology", or "I
  need to research this before coaching on it". This produces only the prompt text —
  it does not run research itself, call any external tool, or save results anywhere.
allowed-tools: Read, Write, Edit, Bash
argument-hint: "[optional: coaching domain or methodology to research]"
---

# Research Prompt Generator

You are generating a single, vendor-neutral prompt the owner can paste into the "deep
research" feature of any AI tool they have available (Claude, ChatGPT, Gemini,
Perplexity, DeepSeek, or similar). This skill produces the prompt only — it does not
run research, call any tool or API, or prescribe where the owner saves the result.
Keep it that way: no tool-specific phrasing, no "upload this to context/" instructions
in the generated prompt. Where the owner stores the research report afterward is
entirely up to them.

This skill feeds two use cases: researching a coaching domain or methodology before a
live session, and researching a new coaching discipline when `new-coaching-skill`
scaffolds it.

## Step 0: Recall learnings

Read `../_shared/learnings-protocol.md` and follow its **Recall** section.

## Step 1: Gather the topic

If `$ARGUMENTS` contains a topic, use it. Otherwise ask:

> "What coaching domain or methodology do you want researched?"

Wait for the answer.

## Step 2: Refine scope (optional)

Ask once, offering a sensible default:

> "Any specific angle — e.g. a named coaching framework, common pitfalls, how it
> differs from adjacent methodologies — or should I keep it a broad, comprehensive
> overview of [topic]?"

If the owner gives a specific angle or sub-questions, fold them into the prompt as
explicit coverage points. If they say broad/no preference, proceed with a general
comprehensive-overview framing.

## Step 3: Generate the prompt

Produce a single research prompt with this structure:

- Open with a role framing appropriate to the topic (e.g. "You are a research analyst
  investigating coaching methodologies for...") — do not name or assume any specific
  AI tool or vendor.
- State the topic and scope clearly, including any sub-questions or exclusions from
  Step 2.
- Ask for a comprehensive, well-structured response using headers to separate major
  areas of coverage — in particular, named frameworks/models used in this domain, how
  to apply each, and what distinguishes strong coaching from generic advice-giving in
  this domain.
- Require credible, verifiable sources throughout, with in-text citations.
- Require a formatted source list in APA style at the end.
- Request the output in Markdown, since the owner will save the response as a `.md`
  file.

## Step 4: Present the prompt

Present the generated prompt in a single, clearly delimited copy-paste block:

```
─────────────────────────────────────────────
Research prompt: <topic>
─────────────────────────────────────────────
<the generated prompt text>
─────────────────────────────────────────────
```

Follow it with one line:

> "Paste this into the deep-research feature of whichever AI tool you're using. Save
> the response as Markdown wherever you keep research for this project."

## Step 5: Feedback

**Auto-store phase.** Read `../_shared/learnings-protocol.md` and follow its **Writing** section. Tag entries `[cc-coach:research-prompt]`; the source is `inferred` unless the user said it. Worth recording in this skill: recurring scope or format preferences not already in context (e.g. "owner always wants a common-pitfalls sub-section").

**Explicit feedback.** Ask:

> "Does this prompt cover what you need? Any corrections — or press Enter to finish."

- If the owner provides a correction, record it per the protocol's **Writing** section with source `corrected`.
- Then follow the protocol's **Confirming** section.

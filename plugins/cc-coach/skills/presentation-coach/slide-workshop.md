# Slide Workshop — presentation-coach Reference

How `presentation-coach` creates or revises a PowerPoint file when — and only when —
the person explicitly asks for it. The workshop serves the talk: slides are built
or changed so they carry the message the coaching worked out, not as a separate
design service. Coaching stays the default mode; this file applies only after the
mode switch described in `SKILL.md`.

## 1. Permission model

The person owns the deck's content and design. The coach changes either only when
asked, and only as far as asked.

- **Feedback is not a work order.** "Review my deck", "what do you think of slide
  4?", or a coaching finding the person agreed with does not authorize a file
  change. Offer once ("Want me to apply that to slide 4?") and wait.
- **Scope is what was named.** "Rework slides 4–7" covers slides 4–7. A problem
  spotted on slide 9 gets mentioned in the hand-off, not fixed.
- **Content and design are separate permissions.** "Tighten the wording on slide
  4" doesn't authorize a new layout, colors, or reordering. "Clean up the layout
  of slide 4" doesn't authorize rewording. A request that clearly implies both
  ("make slide 4 readable for non-experts") covers both — for that slide.
- **Broad requests get a plan first.** "Make the deck better", "rework the whole
  thing", or anything that touches more than a handful of slides: propose a
  slide-by-slide change plan (slide, what changes, content or design, why) and
  wait for a go. For a new deck or a broad rework, the plan also carries the
  devil's advocate pass from `SKILL.md` Step 3c — the kept objections and where
  the deck answers each — so the go covers those slides, notes, and backup slides
  too. A narrow, unambiguous request ("add speaker notes to every
  slide", "retitle slide 3 to X") can go straight to work.
- **The template is read-only.** A registered template is never edited, renamed,
  or overwritten — new decks are built from a copy.
- **The original deck is not overwritten** unless the person asks for in-place
  editing. Default output: a new file next to the original,
  `<name>-revised.pptx` (`-revised-2`, `-revised-3`, ... if that exists). Even in
  a git repo — a binary `.pptx` diff is unreadable, so a side-by-side file is the
  reviewable version.
- **No invented material.** No made-up statistics, quotes, sources, customer
  names, or images presented as real. Where the content needs a fact the person
  hasn't supplied, put a visible placeholder (`[source needed]`, `[Q3 figure]`)
  and list it in the hand-off.

## 2. Inputs

| Input                                            | Role                                         | Typical request                        |
| ------------------------------------------------ | -------------------------------------------- | -------------------------------------- |
| Registered template (`.potx` or `.pptx`)         | Design source: masters, layouts, theme       | "Build the deck from our template"     |
| Working deck (`.pptx` in the repo)               | Content source and, usually, design source   | "Revise slides 4–7", "add notes"       |
| Working deck + registered template               | Content from the deck, design from template  | "Move this deck onto the new template" |
| Outline, script, or notes (file or conversation) | Content for new slides                       | "Turn this outline into slides"        |
| Nothing but an idea                              | Coaching first; then an outline, then slides | —                                      |

When both a deck and a template are in play and the request doesn't say which file
contributes what, ask that one question. A template is not an instruction to keep
its sample slides; an existing deck is not a license to redesign it.

**Macro-enabled files** (`.pptm`, `.potm`) and password-protected files: don't
edit. Ask the person to save a plain `.pptx` copy from PowerPoint.

## 3. Tooling

Everything runs locally through Bash. Check what's available before promising
anything:

```bash
python3 -c "import pptx; print(pptx.__version__)"   # python-pptx: creating/editing
command -v soffice libreoffice pdftoppm               # rendering for visual checks
```

- **`scripts/pptx_tool.py`** (in this skill's base directory, standard library
  only — always works): `inventory`, `potx-to-pptx`, `diff`, `render`. Run it with
  `python3` and the full path.
- **python-pptx** does the actual slide work. If it's missing, say so and ask
  before installing it (`pip install python-pptx`, ideally into a virtualenv) —
  installing packages into someone's environment is their call. If they decline,
  fall back to section 9.
- **LibreOffice + pdftoppm** for rendering. If missing, the hand-off says the
  visual check wasn't done; don't install system packages unasked.
- If another PPTX-capable skill is available in the session (e.g. a dedicated
  `pptx` skill), its tooling advice may be used for the mechanics. This file's
  permission model still governs — and nothing here requires such a skill.

Scratch files (converted templates, renders, build scripts) go in a temp directory
(`mktemp -d`), never into the person's repo. Only the finished deck is written
there.

## 4. Inventory before touching anything

Run `pptx_tool.py inventory <file>` on every input file. It reports format (real
`.pptx` vs `.potx`), slide size, theme fonts and colors, every master with its
layouts and placeholder indices, every slide with layout, title, text, notes, and
risky objects (charts, tables, SmartArt, OLE, media, animations, hyperlinks), plus
package-level warnings (embeddings, macros, embedded fonts, external links,
corruption).

Read the result before planning:

- **Which layouts exist** — new slides must use them, not hand-placed text boxes on
  a blank layout.
- **Sample slides in a template** — usually to be removed from the new deck, never
  edited into content.
- **Risky objects on slides in scope** — SmartArt, OLE, media, animations, and
  linked charts don't round-trip reliably through python-pptx edits. Leave them
  alone where possible; if the requested change requires touching them, say so
  before starting.
- **Theme fonts** not installed locally will render with substitutes — the visual
  check is then an approximation; note it.

For a template, render it once (`render`) and look at the layouts so the build uses
them as the designer intended.

## 5. Working with a `.potx` template

python-pptx refuses `.potx` files (wrong content type). Convert a copy:

```bash
python3 <skill-dir>/scripts/pptx_tool.py potx-to-pptx template.potx "$TMP/base.pptx"
```

This changes the package's main content type — renaming the extension is not a
conversion. Masters, layouts, theme, and placeholders stay intact; the script
reports their counts so you can compare against the inventory. Never write back to
the `.potx`.

## 6. Building and editing with python-pptx

Write the edit as a short Python script in the temp directory and run it; keep the
script so a follow-up request can rerun it with changes.

**New deck from a template**

```python
from pptx import Presentation
prs = Presentation(base_path)            # template, or converted .potx copy
layouts = {l.name: l for m in prs.slide_masters for l in m.slide_layouts}
s = prs.slides.add_slide(layouts["Title and Content"])
s.shapes.title.text = "Half of new users never finish setup"
s.placeholders[1].text_frame.text = "..."  # placeholder idx from the inventory
s.notes_slide.notes_text_frame.text = "..."
```

- `prs.slide_layouts` only covers the first master — collect layouts across
  `prs.slide_masters` as above when the template has several. If two masters
  share a layout name, pick by master explicitly.
- Fill placeholders by the indices the inventory reported. Add free shapes only
  where no layout fits, and then align them to the layout's placeholder geometry.
- Keep the slide size. Don't change theme colors or fonts.
- Remove the template's sample slides at the end (see structural edits).

**Revising an existing deck**

- Edit text at run level to keep formatting. `text_frame.text = ...` wipes
  run-level formatting — use it only on slides you're rebuilding anyway.

  ```python
  para = shape.text_frame.paragraphs[0]
  para.runs[0].text = "New wording"
  for r in para.runs[1:]:
      r._r.getparent().remove(r._r)
  ```

- Change only the shapes the request covers. Don't re-save images, touch charts,
  or "normalize" anything on the side.
- Chart data: `chart.replace_data(...)` keeps the chart editable; never swap a
  chart for a picture of one.

**Structural edits** (python-pptx has no API for delete/reorder/duplicate):

```python
lst = prs.slides._sldIdLst
# reorder: move an element
el = list(lst)[from_idx]; lst.remove(el); lst.insert(to_idx, el)
# delete: drop the relationship, then the list entry
el = list(lst)[idx]; prs.part.drop_rel(el.rId); lst.remove(el)
```

**Order matters: add all new slides first, then reorder, then delete.** Deleting
before adding makes python-pptx reuse a part name and write a corrupt file with
duplicate entries — `inventory` and `diff` flag that as `CORRUPT`. Don't duplicate
slides by copying XML; build the new slide from its layout instead.

**Answering objections** (when the approved plan places them in the deck):

- **In-talk pre-emption** — the slide title states the answer, not the objection
  ("Payback in 14 months, including migration"), and the objection itself is
  named in the body or the spoken line. Never put an objection on a slide without
  its answer on the same slide.
- **Backup slides** — after the closing slide, under a divider titled `Backup`
  (or the template's section-divider layout), one objection per slide, titled
  with the answer. They don't count toward the talk's time.
- **Notes** — the prepared line goes into the speaker notes of the slide where
  the objection is most likely to come up, prefixed `If asked:`.

**Speaker notes**: one per slide on request — the slide's point in a sentence, 2–4
spoken beats, the transition to the next slide, an estimated time. Mark times as
estimates and check that they add up to the talk's slot. Notes say what the slide
doesn't; they never contradict it.

## 7. Verification before hand-off

1. **Integrity** — `inventory` on the output: real `.pptx`, expected slide count,
   no `CORRUPT` flag.
2. **Scope** — `diff <original> <output>` (or `diff <converted template>
<output>` for a new deck). Every `CHANGED`/`NEW` slide must be one the person
   asked for; design must read `unchanged` unless a design change was requested.
   A `CHANGED` slide that wasn't in scope is a bug: fix it before handing over. Slides
   are matched by slide ID, so a replaced slide shows as `NEW` plus a removed
   entry, and a moved slide says where it was.
3. **Visual** — `render <output> "$TMP/render"` and look at every changed slide
   (Read the PNGs): overflowing or cut-off text, overlaps, leftover placeholder
   prompts ("Click to add text"), contrast, legibility at the back of the room.
   Fix and re-render. LibreOffice approximates PowerPoint — say so if fonts were
   substituted.
4. **Talk fit** — titles carry the message the coaching settled on, one
   communicative job per slide, nothing the speaker will read aloud verbatim, the
   slide count fits the slot (backup slides excluded).
5. **Objections** — if the plan placed objections, each one is answered where
   planned, none is raised without its answer, and in-talk pre-emptions stay
   within the airtime budget from the framework.

## 8. Hand-off

A short delimited reply under `## Slide Workshop`:

- Path of the file written (and that the original/template is untouched).
- What changed, per slide, straight from the `diff` result.
- Placeholders left for missing facts.
- What was not verified (no render available, substituted fonts, risky objects on
  changed slides, animations or links not checked).
- **Objections** (when the pass ran): where each kept objection is answered, a
  one-sentence answer for each Q&A-prep objection, and any objection still open
  with the evidence that would close it. After a narrow request: at most one line
  on an obvious objection the changed slides invite.
- One coaching offer tied to the change — e.g. "Want to rehearse the transition
  from slide 3 into the new slide 4?", or, when the pass ran, "Want to practice
  answering the payback question aloud?" — not a list of further edits.

## 9. When the tooling isn't there

Without python-pptx (and no permission to install it), don't simulate a file.
Deliver a slide-by-slide spec instead: slide number, layout name from the
inventory, title, body text, visual, speaker note. The inventory still works, so
the spec can name the template's real layouts. Say plainly that no file was
written.

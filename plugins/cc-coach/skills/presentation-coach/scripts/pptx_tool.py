#!/usr/bin/env python3
"""Deterministic helpers for presentation-coach's slide workshop.

Standard library only, so inspecting and checking a deck never requires an
install. Creating and editing slides is done separately (python-pptx); these
commands cover the parts that must not depend on judgment:

  inventory FILE            What's in a .pptx/.potx: size, theme, masters,
                            layouts + placeholders, slides, notes, risky objects.
  potx-to-pptx IN OUT       Turn a .potx template into a real .pptx package
                            (content type, not just the extension). Never
                            overwrites OUT.
  diff BEFORE AFTER         Which slides changed, were added or removed, and
                            whether masters/layouts/theme/slide size changed.
                            Proves untouched slides stayed untouched.
  render FILE OUTDIR        PNG per slide via LibreOffice + pdftoppm, for
                            visual checks. An approximation of PowerPoint.
"""

import argparse
import hashlib
import json
import posixpath
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
R_ID = "{%s}id" % NS["r"]

CT_PRESENTATION = "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"
CT_TEMPLATE = "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml"
CT_MACRO = ("application/vnd.ms-powerpoint.presentation.macroEnabled.main+xml",
            "application/vnd.ms-powerpoint.template.macroEnabled.main+xml")

REL_SUFFIX = {
    "slide": "/slide",
    "layout": "/slideLayout",
    "master": "/slideMaster",
    "notes": "/notesSlide",
    "theme": "/theme",
}

GRAPHIC_KINDS = {
    "http://schemas.openxmlformats.org/drawingml/2006/chart": "chart",
    "http://schemas.openxmlformats.org/drawingml/2006/table": "table",
    "http://schemas.openxmlformats.org/drawingml/2006/diagram": "SmartArt",
    "http://schemas.openxmlformats.org/presentationml/2006/ole": "OLE object",
}


class Package:
    """Read-only view of an OPC zip package."""

    def __init__(self, path):
        self.path = Path(path)
        try:
            self.zip = zipfile.ZipFile(self.path)
        except (zipfile.BadZipFile, FileNotFoundError) as exc:
            sys.exit(f"error: {path} is not a readable Office package ({exc})")
        all_names = self.zip.namelist()
        self.names = set(all_names)
        # python-pptx can write two parts under one name (e.g. add_slide after a
        # delete); PowerPoint then refuses or "repairs" the file.
        self.duplicates = sorted({n for n in all_names if all_names.count(n) > 1})
        if "[Content_Types].xml" not in self.names:
            sys.exit(f"error: {path} has no [Content_Types].xml — not an Office Open XML file")
        self.content_types = self._content_types()
        self.main = self._main_part()

    def _content_types(self):
        root = ET.fromstring(self.zip.read("[Content_Types].xml"))
        return {o.get("PartName").lstrip("/"): o.get("ContentType")
                for o in root.findall("ct:Override", NS)}

    def _main_part(self):
        for rel in self.rels(""):
            if rel["type"].endswith("/officeDocument"):
                return rel["target"]
        sys.exit(f"error: {self.path} has no main document relationship")

    def read(self, name):
        return self.zip.read(name)

    def xml(self, name):
        return ET.fromstring(self.zip.read(name))

    def rels(self, part):
        """Relationships of a part, targets resolved to package paths."""
        base_dir, base_name = posixpath.split(part)
        rels_name = posixpath.join(base_dir, "_rels", base_name + ".rels")
        if rels_name not in self.names:
            return []
        out = []
        for r in ET.fromstring(self.zip.read(rels_name)).findall("rel:Relationship", NS):
            target = r.get("Target")
            external = r.get("TargetMode") == "External"
            if not external:
                if target.startswith("/"):
                    target = target.lstrip("/")
                else:
                    target = posixpath.normpath(posixpath.join(base_dir, target))
            out.append({"id": r.get("Id"), "type": r.get("Type"),
                        "target": target, "external": external})
        return out

    def rel_targets(self, part, kind):
        return [r["target"] for r in self.rels(part)
                if r["type"].endswith(REL_SUFFIX[kind]) and not r["external"]]

    def kind(self):
        ct = self.content_types.get(self.main, "")
        if ct == CT_TEMPLATE:
            return "potx"
        if ct == CT_PRESENTATION:
            return "pptx"
        if ct in CT_MACRO:
            return "macro-enabled"
        return f"unknown ({ct or 'no content type'})"

    def slides(self):
        """Slide part names in presentation order."""
        pres = self.xml(self.main)
        rid_to_target = {r["id"]: r["target"] for r in self.rels(self.main)}
        lst = pres.find("p:sldIdLst", NS)
        return [rid_to_target[s.get(R_ID)] for s in (lst if lst is not None else [])]

    def slide_ids(self):
        """Presentation slide IDs in order. PowerPoint and python-pptx keep a
        slide's ID across saves, so it identifies the same slide in two files."""
        lst = self.xml(self.main).find("p:sldIdLst", NS)
        return [s.get("id") for s in (lst if lst is not None else [])]

    def masters(self):
        pres = self.xml(self.main)
        rid_to_target = {r["id"]: r["target"] for r in self.rels(self.main)}
        lst = pres.find("p:sldMasterIdLst", NS)
        return [rid_to_target[m.get(R_ID)] for m in (lst if lst is not None else [])]


def text_of(el):
    paras = []
    for p in el.iter("{%s}p" % NS["a"]):
        t = "".join(x.text or "" for x in p.iter("{%s}t" % NS["a"]))
        if t.strip():
            paras.append(t.strip())
    return paras


def shorten(s, n=90):
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def placeholder_info(sp):
    ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
    if ph is None:
        return None
    name = sp.find("p:nvSpPr/p:cNvPr", NS)
    return {"type": ph.get("type", "body"), "idx": ph.get("idx", "0"),
            "name": name.get("name") if name is not None else ""}


def special_objects(root):
    found = {}

    def bump(k):
        found[k] = found.get(k, 0) + 1

    for gd in root.iter("{%s}graphicData" % NS["a"]):
        kind = GRAPHIC_KINDS.get(gd.get("uri"))
        if kind:
            bump(kind)
    for _ in root.iter("{%s}pic" % NS["p"]):
        bump("picture")
    for tag in ("videoFile", "audioFile"):
        for _ in root.iter("{%s}%s" % (NS["a"], tag)):
            bump("media")
    if root.find("p:timing", NS) is not None:
        bump("animations")
    if root.find("p:transition", NS) is not None:
        bump("transition")
    for _ in root.iter("{%s}hlinkClick" % NS["a"]):
        bump("hyperlink")
    return found


def notes_text(pkg, slide):
    """Speaker-notes paragraphs of a slide (body placeholder of its notes page)."""
    notes = (pkg.rel_targets(slide, "notes") or [None])[0]
    if not notes:
        return []
    out = []
    for sp in pkg.xml(notes).iter("{%s}sp" % NS["p"]):
        ph = placeholder_info(sp)
        if ph and ph["type"] == "body":
            out.extend(text_of(sp))
    return out


def layout_name(pkg, layout):
    cSld = pkg.xml(layout).find("p:cSld", NS)
    return cSld.get("name", posixpath.basename(layout)) if cSld is not None else layout


def inventory(pkg):
    data = {"file": str(pkg.path), "format": pkg.kind()}
    pres = pkg.xml(pkg.main)
    sz = pres.find("p:sldSz", NS)
    if sz is not None:
        cx, cy = int(sz.get("cx")), int(sz.get("cy"))
        ratio = cx / cy
        label = {round(16 / 9, 2): "16:9", round(4 / 3, 2): "4:3", round(16 / 10, 2): "16:10"}.get(round(ratio, 2), f"{ratio:.2f}:1")
        data["slide_size"] = {"cm": [round(cx / 360000, 2), round(cy / 360000, 2)], "ratio": label}

    masters = []
    for m in pkg.masters():
        theme = (pkg.rel_targets(m, "theme") or [None])[0]
        theme_info = {}
        if theme:
            t = pkg.xml(theme)
            fonts = {}
            for which in ("majorFont", "minorFont"):
                latin = t.find(f".//a:fontScheme/a:{which}/a:latin", NS)
                if latin is not None:
                    fonts["heading" if which == "majorFont" else "body"] = latin.get("typeface")
            colors = {}
            scheme = t.find(".//a:clrScheme", NS)
            for c in (scheme if scheme is not None else []):
                val = c.find("a:srgbClr", NS)
                sys_c = c.find("a:sysClr", NS)
                colors[c.tag.split("}")[1]] = (val.get("val") if val is not None
                                               else sys_c.get("lastClr") if sys_c is not None else "?")
            theme_info = {"name": t.get("name"), "fonts": fonts, "colors": colors}
        layouts = []
        for lay in pkg.rel_targets(m, "layout"):
            root = pkg.xml(lay)
            phs = [placeholder_info(sp) for sp in root.iter("{%s}sp" % NS["p"])]
            layouts.append({"part": lay, "name": layout_name(pkg, lay),
                            "placeholders": [p for p in phs if p]})
        masters.append({"part": m, "theme": theme_info, "layouts": layouts})
    data["masters"] = masters

    slides = []
    for i, s in enumerate(pkg.slides(), 1):
        root = pkg.xml(s)
        lay = (pkg.rel_targets(s, "layout") or [None])[0]
        title, body = "", []
        for sp in root.iter("{%s}sp" % NS["p"]):
            ph = placeholder_info(sp)
            paras = text_of(sp)
            if ph and ph["type"] in ("title", "ctrTitle") and paras:
                title = " / ".join(paras)
            else:
                body.extend(paras)
        slides.append({
            "n": i, "part": s, "hidden": root.get("show") == "0",
            "layout": layout_name(pkg, lay) if lay else None,
            "title": title, "text": body, "notes": notes_text(pkg, s),
            "objects": special_objects(root),
        })
    data["slides"] = slides

    pkg_flags = []
    if pkg.duplicates:
        pkg_flags.append("CORRUPT: duplicate part names " + ", ".join(pkg.duplicates)
                         + " — rebuild the file, do not hand it over")
    if any(n.startswith("ppt/embeddings/") for n in pkg.names):
        pkg_flags.append("embedded files present (chart data workbooks or OLE objects)")
    if any(n.lower().endswith(".bin") and "vba" in n.lower() for n in pkg.names):
        pkg_flags.append("VBA macros present")
    if any(n.startswith("ppt/fonts/") for n in pkg.names):
        pkg_flags.append("embedded fonts present")
    externals = {r["target"] for s in pkg.slides() for r in pkg.rels(s) if r["external"]}
    if externals:
        pkg_flags.append(f"{len(externals)} external link target(s)")
    data["package_flags"] = pkg_flags
    return data


def print_inventory(d):
    print(f"File:    {d['file']}")
    print(f"Format:  {d['format']}")
    if "slide_size" in d:
        w, h = d["slide_size"]["cm"]
        print(f"Size:    {w} x {h} cm ({d['slide_size']['ratio']})")
    for mi, m in enumerate(d["masters"], 1):
        t = m["theme"]
        print(f"\nMaster {mi} ({m['part']}) — theme {t.get('name')!r}")
        if t.get("fonts"):
            print("  Fonts:  " + ", ".join(f"{k}={v}" for k, v in t["fonts"].items()))
        if t.get("colors"):
            print("  Colors: " + ", ".join(f"{k}={v}" for k, v in t["colors"].items()))
        print("  Layouts:")
        for lay in m["layouts"]:
            phs = ", ".join(f"{p['type']}#{p['idx']}" for p in lay["placeholders"]) or "no placeholders"
            print(f"    - {lay['name']!r}: {phs}")
    print(f"\nSlides: {len(d['slides'])}")
    for s in d["slides"]:
        flags = []
        if s["hidden"]:
            flags.append("HIDDEN")
        flags += [f"{v}x {k}" if v > 1 else k for k, v in s["objects"].items()]
        print(f"  {s['n']:>3}. [{s['layout']}] {shorten(s['title']) or '(no title)'}"
              + (f"  {{{', '.join(flags)}}}" if flags else ""))
        if s["text"]:
            print(f"       text:  {shorten(' | '.join(s['text']), 110)}")
        if s["notes"]:
            print(f"       notes: {shorten(' '.join(s['notes']), 110)}")
    if d["package_flags"]:
        print("\nHandle with care: " + "; ".join(d["package_flags"]))


def cmd_inventory(args):
    d = inventory(Package(args.file))
    if args.json:
        json.dump(d, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        print_inventory(d)


def cmd_potx_to_pptx(args):
    src, dst = Path(args.src), Path(args.dst)
    if dst.exists():
        sys.exit(f"error: {dst} already exists — pick a new name, nothing was written")
    pkg = Package(src)
    kind = pkg.kind()
    if kind == "pptx":
        sys.exit(f"error: {src} is already a .pptx package — open it directly")
    if kind != "potx":
        sys.exit(f"error: {src} is {kind}, not a plain .potx — ask the person to save it "
                 "as .pptx from PowerPoint desktop instead")
    ct = pkg.read("[Content_Types].xml").decode("utf-8")
    patched = ct.replace(CT_TEMPLATE, CT_PRESENTATION)
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as out:
        for info in pkg.zip.infolist():
            data = patched.encode("utf-8") if info.filename == "[Content_Types].xml" else pkg.read(info.filename)
            out.writestr(info, data)
    check = Package(dst)
    print(f"wrote {dst}: {check.kind()}, {len(check.masters())} master(s), "
          f"{sum(len(check.rel_targets(m, 'layout')) for m in check.masters())} layout(s), "
          f"{len(check.slides())} slide(s)")


def canonical(pkg, name):
    data = pkg.read(name)
    if name.endswith(".xml") or name.endswith(".rels"):
        try:
            return ET.canonicalize(data.decode("utf-8"), strip_text=True).encode("utf-8")
        except ET.ParseError:
            pass
    return data


def digest(pkg, part, seen=None):
    """Hash of a part plus everything it references, except navigation links
    (layout/master/notes are compared separately) so a slide's hash only moves
    when the slide itself, its media, charts, or embeddings change."""
    seen = seen if seen is not None else set()
    seen.add(part)
    h = hashlib.sha256(canonical(pkg, part))
    for r in sorted(pkg.rels(part), key=lambda r: r["id"]):
        h.update(f"{r['id']}|{r['type']}".encode())
        if r["external"]:
            h.update(r["target"].encode())
            continue
        if any(r["type"].endswith(REL_SUFFIX[k]) for k in ("layout", "master", "notes", "slide", "theme")):
            continue
        if r["target"] in pkg.names and r["target"] not in seen:
            h.update(digest(pkg, r["target"], seen).encode())
    return h.hexdigest()


def slide_signature(pkg, part):
    lay = (pkg.rel_targets(part, "layout") or [None])[0]
    return {
        "content": digest(pkg, part),
        "layout": layout_name(pkg, lay) if lay else None,
        "notes": notes_text(pkg, part),
    }


def design_parts(pkg):
    out = {}
    for m in pkg.masters():
        out[f"master {m}"] = digest(pkg, m)
        for t in pkg.rel_targets(m, "theme"):
            out[f"theme {t}"] = digest(pkg, t)
        for lay in pkg.rel_targets(m, "layout"):
            # Layout names repeat across masters; the part path keeps keys unique.
            out[f"layout {layout_name(pkg, lay)!r} ({lay})"] = digest(pkg, lay)
    return out


def cmd_diff(args):
    a, b = Package(args.before), Package(args.after)
    sa = [slide_signature(a, s) for s in a.slides()]
    sb = [slide_signature(b, s) for s in b.slides()]

    ida, idb = a.slide_ids(), b.slide_ids()

    # Pass 1: the same slide ID in both files is the same slide, edited or not.
    pair = {j: ida.index(sid) for j, sid in enumerate(idb) if sid in ida}
    # Pass 2: slides without a shared ID (rebuilt or re-imported) pair only by
    # identical content, preferring the same position. Anything left over is
    # reported as NEW/removed rather than guessed to be an edit.
    for j, sig in enumerate(sb):
        if j in pair:
            continue
        same = [i for i, x in enumerate(sa) if x["content"] == sig["content"] and i not in pair.values()]
        if same:
            pair[j] = j if j in same else same[0]

    report, changed = [], 0
    for j, sig in enumerate(sb):
        i = pair.get(j)
        if i is None:
            report.append(f"  {j + 1:>3}. NEW")
            changed += 1
            continue
        notes = sa[i]["notes"] != sig["notes"]
        layout = sa[i]["layout"] != sig["layout"]
        content = sa[i]["content"] != sig["content"]
        what = [w for w, hit in (("content", content), ("notes", notes), ("layout", layout)) if hit]
        if layout:
            what[-1] = f"layout {sa[i]['layout']!r} -> {sig['layout']!r}"
        moved = f" (was slide {i + 1})" if i != j else ""
        if what:
            changed += 1
            report.append(f"  {j + 1:>3}. CHANGED: {', '.join(what)}{moved}")
        else:
            report.append(f"  {j + 1:>3}. unchanged{moved}")
    removed = [i + 1 for i in range(len(sa)) if i not in pair.values()]

    for pkg in (a, b):
        if pkg.duplicates:
            print(f"WARNING: {pkg.path} is corrupt — duplicate part names: {', '.join(pkg.duplicates)}")
    print(f"Before: {a.path} ({len(sa)} slides)   After: {b.path} ({len(sb)} slides)")
    print("Slides (after-numbering):")
    print("\n".join(report))
    if removed:
        print(f"Removed or replaced from before: slide(s) {', '.join(map(str, removed))}")

    da, db = design_parts(a), design_parts(b)
    design = [f"  {k}: {'changed' if k in db else 'removed'}" for k in da if da[k] != db.get(k)]
    design += [f"  {k}: added" for k in db if k not in da]
    size_a = a.xml(a.main).find("p:sldSz", NS)
    size_b = b.xml(b.main).find("p:sldSz", NS)
    if size_a is not None and size_b is not None and size_a.attrib != size_b.attrib:
        design.append("  slide size: changed")
    print("Design (masters, layouts, theme, size): " + ("unchanged" if not design else "CHANGED"))
    if design:
        print("\n".join(design))
    print(f"Summary: {changed} slide(s) new/changed, {len(removed)} removed, "
          f"{len(sb) - changed} unchanged, design {'changed' if design else 'unchanged'}")


def cmd_render(args):
    src, outdir = Path(args.file).resolve(), Path(args.outdir)
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    pdftoppm = shutil.which("pdftoppm")
    if not soffice:
        sys.exit("error: LibreOffice (soffice) not found — visual check unavailable; say so in the hand-off")
    outdir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        # Isolated profile so a running LibreOffice instance doesn't swallow the job.
        profile = Path(tmp, "profile").as_uri()
        subprocess.run([soffice, f"-env:UserInstallation={profile}", "--headless",
                        "--convert-to", "pdf", "--outdir", tmp, str(src)],
                       check=True, capture_output=True, timeout=300)
        pdf = Path(tmp, src.stem + ".pdf")
        if not pdf.exists():
            sys.exit("error: LibreOffice produced no PDF")
        if not pdftoppm:
            shutil.copy(pdf, outdir / pdf.name)
            print(f"pdftoppm not found — wrote {outdir / pdf.name} instead of PNGs")
            return
        subprocess.run([pdftoppm, "-png", "-r", str(args.dpi), str(pdf), str(outdir / "slide")],
                       check=True, timeout=300)
    for png in sorted(outdir.glob("slide*.png")):
        print(png)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("inventory")
    p.add_argument("file")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_inventory)
    p = sub.add_parser("potx-to-pptx")
    p.add_argument("src")
    p.add_argument("dst")
    p.set_defaults(func=cmd_potx_to_pptx)
    p = sub.add_parser("diff")
    p.add_argument("before")
    p.add_argument("after")
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser("render")
    p.add_argument("file")
    p.add_argument("outdir")
    p.add_argument("--dpi", type=int, default=60)
    p.set_defaults(func=cmd_render)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

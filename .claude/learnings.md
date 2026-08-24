# Learnings

Corrections and observations collected during configuration sessions.
Entries are tagged by skill and dated.

---

[cc-config:auditing-config] sync-config-table.sh v6 duplicates a row if the `last-optimize-run` marker comment is placed immediately after the Key Config Files table (blank line, comment, blank line, then a stray old row reappears on the next commit-time run) — place the marker elsewhere in CLAUDE.md (e.g. end of file) instead. — 2026-08-25

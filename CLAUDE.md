# WilliamButcherBot (Fuzzybutt)

Pyrogram-based Telegram group-management bot with a companion userbot session. Bot commands (`app`, `/` prefix) live in `wbb/modules/*.py`, plus `/start` and `/help` in `wbb/__main__.py`. Userbot-only commands (`app2`, `.` prefix by convention) run through the operator's personal account and are gated to `SUDOERS`.

## Command reference

There are two synced copies of the same catalog at the repo root — every end-user-facing command (bot and userbot), grouped by category with access-level badges (Open / Admin / Sudo / Userbot) and usage syntax:
- `command-reference.html` — standalone, browsable, searchable. No build step, open it directly in a browser.
- `command-reference.md` — plain-Markdown mirror of the same categories/rows, for viewing on GitHub or in an editor without opening a browser.

**Whenever you add, remove, rename, or change the behavior/access-level/usage of a command in `wbb/modules/` or `wbb/__main__.py`, update BOTH files in the same change.** This includes:
- New command handlers (`filters.command(...)` or equivalent) — add a row to the relevant category (or a new category if none fits) in both files.
- Removed handlers — delete the row from both files.
- Changed aliases, usage syntax, or access restriction (admin-only vs sudo-only vs open) — update that row's fields in both files.
- Renamed/restructured plugin files — sanity-check the category it landed in still makes sense in both files.

In `command-reference.html`, each row lives in the `DATA` array as `[commandOrAliases, description, accessTier, usage]`:
- `commandOrAliases`: comma-separated, e.g. `"/ban, /dban, /tban"`.
- `accessTier`: one of `open`, `admin`, `sudo`, `userbot` — drives the colored badge.
- `usage`: a usage string; append `" — "` followed by a short note for things like "reply required", "PM only", "group only" (rendered as a muted caption under the usage code).

The category count and total command count in the HTML page header are computed automatically from `DATA` — no manual counters to maintain there. `command-reference.md`'s header line (`**N commands · N categories · N tiers**`) is NOT automatic — update that count by hand to match.

In `command-reference.md`, each row is a Markdown table row under the matching `## Category` heading, in the same order and with the same wording as the HTML's `DATA` entries — keep the two in lockstep rather than letting one drift into a paraphrase of the other.

If a change is large enough that the category structure no longer fits well, restructure the categories rather than force-fitting — but keep the same visual/token system already in the HTML file (it intentionally matches a sibling bot's reference page), and mirror the restructuring into the Markdown file's headings.

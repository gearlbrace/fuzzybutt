# WilliamButcherBot (Fuzzybutt)

Pyrogram-based Telegram group-management bot with a companion userbot session. Bot commands (`app`, `/` prefix) live in `wbb/modules/*.py`, plus `/start` and `/help` in `wbb/__main__.py`. Userbot-only commands (`app2`, `.` prefix by convention) run through the operator's personal account and are gated to `SUDOERS`.

## Command reference

`command-reference.html` at the repo root is a standalone, browsable catalog of every end-user-facing command (bot and userbot), grouped by category with access-level badges (Open / Admin / Sudo / Userbot) and usage syntax. It has no build step — open it directly in a browser.

**Whenever you add, remove, rename, or change the behavior/access-level/usage of a command in `wbb/modules/` or `wbb/__main__.py`, update the matching entry in `command-reference.html`'s `DATA` array in the same change.** This includes:
- New command handlers (`filters.command(...)` or equivalent) — add a row to the relevant category (or a new category if none fits).
- Removed handlers — delete the row.
- Changed aliases, usage syntax, or access restriction (admin-only vs sudo-only vs open) — update that row's fields.
- Renamed/restructured plugin files — sanity-check the category it landed in still makes sense.

Each `DATA` row is `[commandOrAliases, description, accessTier, usage]`:
- `commandOrAliases`: comma-separated, e.g. `"/ban, /dban, /tban"`.
- `accessTier`: one of `open`, `admin`, `sudo`, `userbot` — drives the colored badge.
- `usage`: a usage string; append `" — "` followed by a short note for things like "reply required", "PM only", "group only" (rendered as a muted caption under the usage code).

The category count and total command count in the page header are computed automatically from `DATA` — no manual counters to maintain.

If a change is large enough that the category structure no longer fits well, restructure the categories rather than force-fitting — but keep the same visual/token system already in the file (it intentionally matches a sibling bot's reference page).

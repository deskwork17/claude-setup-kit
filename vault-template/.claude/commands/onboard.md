Run onboarding for this vault: learn what the user wants Claude for, suggest a setup to match, and build only what they approve. The start-up hook triggers this automatically until `.claude/onboarding.md` exists. The user can also run `/onboard` any time to revisit it.

## 1. Interview

Ask these in one message, conversationally, and let the user answer as briefly as they like:

1. What will you mostly use Claude and this wiki for? For example: school, a job, a side business, creative writing, a game or campaign, personal notes, coding, research, life admin.
2. What projects or areas are active right now? Name a few.
3. Where does your information come from now? Phone notes, email, Google Docs, PDFs, websites, meetings?
4. Anything repetitive you'd like handed off? Summarizing, filing notes, drafting emails, tracking tasks, reminders.
5. Which services do you use that Claude could connect to? Gmail, Google Calendar or Drive, GitHub, Notion, and so on.

Ask one round of follow-ups only if the answers are too thin to tailor suggestions.

## 2. Suggest a setup

Give one concise proposal. Group it under the headings below, give each item a single-line reason tied to what the user said, and mark the 2–3 you'd do first. Only suggest what fits their answers; don't dump the whole catalogue.

**Vault layout.** Propose folders and page types for their actual projects and areas, as a short tree. For each page type, give the sections a page should have (e.g. `Projects/<name>/` with an overview page, `Meetings/`, `Tasks.md`). Starting points:

| Use case | Typical layout |
|---|---|
| School | `Courses/<course>/` (syllabus, lecture notes, assignments), `Readings/`, `Deadlines.md` |
| Work / projects | `Projects/<project>/` (overview, decisions log, meeting notes), `People/`, `Tasks.md` |
| Creative writing | `Stories/<title>/` (outline, chapters, characters), `Worldbuilding/`, `Ideas/` |
| Game / campaign | `Characters/`, `Locations/`, `Factions/`, `Sessions/`, `Lore/`, `Tools & Tables/` |
| Personal knowledge | `Notes/<topic>`, `Reading list.md`, `Journal/YYYY-MM-DD` |
| Coding | `Projects/<repo>/` (architecture notes, TODO, decisions), `Snippets/` |
| Life admin | `Home/`, `Finances/` (no account numbers or passwords), `Health/`, `Travel/` |

**Skills** (`.claude/skills/<name>/SKILL.md`). These are repeatable procedures Claude follows when a task matches. Examples:
- `file-note`: sort a pasted note into the right page and link it.
- `meeting-notes`: turn rough notes into a dated page with decisions and action items.
- `weekly-review`: summarize the week's session notes and open to-dos.
- `new-project`: create a project folder from a template.

Skills you write yourself go in the vault's `.claude/skills/`. The built-in document skills (Word, Excel, PowerPoint, PDF) already exist, so don't recreate them.

**Slash commands** (`.claude/commands/<name>.md`). These are short prompts the user triggers by name. For example: `/inbox` sorts the Inbox, `/today` builds a daily page, `/todo` lists open tasks across the vault.

**Hooks** (in `.claude/settings.json`). These are automatic actions the harness runs. For example:
- a SessionStart reminder of upcoming deadlines from a `Deadlines.md`;
- a check after each edit that new pages are linked from somewhere;
- a Stop hook that warns about uncommitted vault changes.

Hooks are Python or PowerShell scripts in `.claude/hooks/`. Keep them fast, under a few seconds.

**Connectors and MCP servers.** These are claude.ai connectors (Gmail, Google Calendar, Google Drive, and others, turned on in claude.ai settings), GitHub through `gh`, and any service the user named. The user does every sign-in themselves.

**Tools.** Suggest anything their use case needs that isn't in `~/.claude/machine_setup.md` yet. For example: pandas for data, Zotero for citations, ffmpeg for media. Check that file first.

## 3. Build what's approved

- Ask which items to set up. Build only those.
- Create the folders and template pages. Add the new layout and page rules to `CLAUDE.md` under **Conventions**, and update `Home.md`.
- Write skills, commands and hooks in the vault's `.claude/` folder so they travel with the vault's git repo.
- Record any installed tool in `~/.claude/machine_setup.md`.
- Never ask for or handle the user's passwords, API keys or tokens. The user does every sign-in and key entry personally.

## 4. Record it

Write `.claude/onboarding.md` with the date, the user's use cases and active projects in a line or two each, what was set up, and what was suggested but declined or deferred. This file stops the start-up prompt from running again. Future sessions can read it for context.

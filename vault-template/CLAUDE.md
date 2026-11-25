# <VAULT NAME>

This folder is an Obsidian vault used as a personal wiki. Claude reads and writes it through the `obsidian` MCP tools, which need Obsidian open. If they aren't connected, say so, then fall back to editing the Markdown files directly.

## Structure
- `Home.md`: the front page, with links to the main areas. Keep it current when a new top-level folder or major page is added.
- `Inbox/`: quick captures and unsorted notes. Pasted notes land here unless the user says where they go.
- `Notes/`: general topic pages, one page per topic, named after the topic.
- `People/`: one page per person.
- `Projects/`: one page (or subfolder) per project.
- `Session notes/`: one file per Claude session, `YYYY-MM-DD.md`, written by `/end`.
- `Templates/`: page templates. Don't add content here.

The user sets the organization as they go. When they settle on a new folder or page convention, record it in this file under **Conventions** so future sessions follow it.

## Working conventions
- **Keep the user's words.** When turning pasted notes into pages, tidy the formatting and keep the user's wording and ideas. Don't rewrite.
- **One page per thing.** Before creating a page, search the vault for an existing one (including near-duplicate names) and update it instead.
- **Link generously.** Whenever a page mentions a person, place, project or topic that has its own page, link it with `[[wikilinks]]`. Use `[[Page|display text]]` to keep the original wording. When creating a page, also add links to it from existing pages that mention it.
- **Mark what Claude adds.** Anything Claude invents or infers (suggestions, summaries not from the user, guesses) goes in a `> [!note] Claude suggestion` callout until the user approves it.
- **Ask before deleting, moving or renaming pages.** Renaming breaks links unless it's done through Obsidian.

## Formatting
- Start pages with `# Title`. Use `##` sections below that.
- Tables must start at column 0 with a blank line before them (never indented inside a list item). Otherwise Obsidian shows them as raw text.
- Use Obsidian callouts (`> [!info]`, `> [!todo]`, `> [!warning]`) for asides and to-dos.
- Dates are `YYYY-MM-DD`.

## Conventions
<!-- Add folder and page rules here as the user decides them. -->

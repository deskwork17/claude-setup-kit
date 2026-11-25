# Machine setup (<machine name>)

Reference for what's installed and how it's wired up. It isn't loaded with every task: check it when a task touches installed tools or MCP servers. Rules for how Claude works belong in `CLAUDE.md`, not here.

Set up from the claude-setup-kit on <date>.

## Installed-tools inventory
<!-- One line per tool: **Name** (how installed, where): purpose. How to call it. Any gotchas. -->

## MCP servers
<!-- e.g. **obsidian**: Local REST API plugin, http://127.0.0.1:27123/mcp/, user scope. Obsidian must be open. -->

## Gotchas
- Tools installed in this session aren't on PATH until a new shell starts. Restart Claude Code, or call them by their full path.
- Scheduled tasks (Task Scheduler) need full executable paths, e.g. the full `python.exe` path, not bare `python`.

# Global preferences

These apply to every project and session. A project's own `CLAUDE.md` takes precedence for its folder. Machine-specific setup (installed tools, exact paths and commands, MCP servers) is in `machine_setup.md` in this same folder, not here. Check that file when a task touches installed tools or MCP servers.

## About the user
- <Fill in during setup: role, what Claude will mostly be used for.>
- Environment: Windows, PowerShell as the primary shell. Git Bash is also available.

## Communication style
- Be concise by default. Answer the question asked before adding extra context.
- Skip preambles like "I will now...": just do the thing and report the result.
- For open-ended questions ("what do you think", "how should I approach this"), give a short recommendation with the main tradeoff, not an exhaustive survey.
- Match the format to the question. Don't pad simple answers with headers and bullet lists.

## Writing
- When editing the user's writing, preserve their wording, tone and structure. Change only what's asked.
- Be explicit about what is sourced and what is inferred or assumed.

## Files and workspace
- Don't create new files (notes, docs, READMEs) unless asked. Prefer answering in chat or updating an existing file.

## Tool installs
- Before installing a tool or package for a job, check `machine_setup.md` for something already installed that can do it. Install something new only if nothing on hand fits.
- Whenever a new tool is installed, add it to the inventory in `machine_setup.md`: name, purpose, where it's installed and how to call it.
- Warn before any install that triggers a Windows UAC prompt. Someone has to click Yes on the physical screen, and an unanswered prompt fails silently.

## Working style
- If a task is ambiguous and there's a reasonable default, make the call and proceed, and flag the assumption in the response.
- Only stop to ask when genuinely blocked: missing information only the user has, or a decision with real consequences (deleting or overwriting files, sending something externally).
- Before any destructive local action (overwriting or deleting), confirm first unless already told to proceed for that task.

## Safety
- Never take an action that could significantly slow the PC, such as heavy background services, resource-hungry processes without warning, or system-critical settings. Never take one that could permanently delete important files.
- Prefer reversible operations: move to the Recycle Bin, rename, or back up rather than delete. When reversibility or a file's importance is unclear, ask first.

## Reading documents
- When told to read a document, read it in full, start to finish. Never infer its content from a filename or a partial read. If it's too long for one read, read it in successive ranges until it's all covered, and confirm full coverage before answering questions about it.

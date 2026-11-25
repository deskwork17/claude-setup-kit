Wrap up this session in the wiki vault. Do these steps in order:

1. **Tidy the vault** for anything changed this session:
   - New pages are linked from at least one existing page (or from `Home.md`).
   - Pages that mention a new page link to it.
   - Nothing is left in `Inbox/` that the user asked to have sorted.

   If the `obsidian` MCP server isn't connected, say so explicitly and work on the files directly.
2. **Update `CLAUDE.md`** if the user settled on any new folder or page convention this session. Record it under **Conventions**. Delete rules that are no longer true.
3. **Write a session note** at `Session notes/YYYY-MM-DD.md` covering what was done and anything left open. If today's file exists, append a new section rather than overwriting.
4. **Commit and push** if the vault is a git repo with a remote:
   - Review `git status` first, and stage specific files rather than blindly running `git add -A`.
   - Never commit `.obsidian/plugins/*/data.json` (it holds the plugin API key).
   - Then commit with a short message and `git push`.
   - If there's no repo or remote, skip this step and say so.
5. **Report back** briefly: what changed, what was committed and pushed, and what's left for next time.

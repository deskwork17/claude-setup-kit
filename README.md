# Claude setup kit

A general-purpose Claude Code setup for Windows: Python, Node.js, Git and GitHub, document tools, and an Obsidian vault used as a personal wiki that Claude can read and write.

## How to use it

1. Install Claude Code and sign in, if you haven't already (https://claude.com/claude-code).
2. Open Claude Code in any folder and say:

   > Clone https://github.com/deskwork17/claude-setup-kit into my home folder, read SETUP.md in full, and set me up. Ask me anything you need as you go.

3. Claude walks through `SETUP.md`. A few steps need you personally:
   - clicking **Yes** on Windows install prompts (UAC);
   - signing in to GitHub (`gh auth login`);
   - turning on the Obsidian plugin;
   - running one script that connects Claude to Obsidian.

   Claude will tell you when each one comes up.

Nothing in this kit holds anyone's passwords, keys or personal details. You'll set up your own.

## What's in here

| Path | What it is |
|---|---|
| `SETUP.md` | Step-by-step instructions for Claude to follow |
| `global/CLAUDE.md` | Your preferences that apply to every Claude session; edit freely |
| `global/machine_setup.md` | A running inventory of installed tools, which Claude keeps updated |
| `vault-template/` | A starter Obsidian wiki: its `CLAUDE.md` rules, a Home page, folders, a `/end` command and a git sync hook |
| `scripts/register_obsidian_mcp.ps1` | Connects Claude to your vault (you run it yourself, since it handles the plugin's API key) |

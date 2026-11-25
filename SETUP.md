# SETUP.md: instructions for Claude

You are setting up a fresh Windows machine with a general-purpose Claude Code environment and an Obsidian wiki. Work through the steps below in order.

- Report progress briefly as you go.
- Ask the user whenever a step needs their decision or their hands. Do not guess at personal details such as names, emails or folder locations.
- `KIT` means the folder this file is in.

## Ground rules for this setup

- **Never handle secrets.** Never type, paste, read aloud or store any password, API key or token, including the Obsidian plugin's API key. The user runs `scripts/register_obsidian_mcp.ps1` themselves for that step.
- **Warn before any install that triggers a UAC prompt.** winget installs of system software usually do. The user has to click Yes on the physical screen, and an unanswered prompt fails silently (winget exit code 1602).
- **Skip what's already there.** Check each tool before installing it (`<tool> --version`, `winget list --id <id>`).
- **Don't change unrelated system settings**, and don't install background services or anything that autostarts.
- **Record every tool you install** in `~/.claude/machine_setup.md`, which you copy in step 2.

## 1. Ask the user first

Ask all of these at once:

1. Where should the wiki vault live? The default is `%USERPROFILE%\Documents\Wiki`. Also ask what to name it.
2. Do they have a GitHub account, and do they want the vault backed up to a **private** GitHub repo? This is recommended. It's what the session-start sync and `/end` use.
3. Anything to add to the "About the user" section of their global `CLAUDE.md` (role, what they'll mostly use Claude for)? Optional.

## 2. Global Claude config

1. Copy `KIT/global/CLAUDE.md` to `%USERPROFILE%\.claude\CLAUDE.md`. If that file already exists, show the user both versions and merge them rather than overwriting.
2. Fill in its "About the user" section from their answers.
3. Copy `KIT/global/machine_setup.md` to `%USERPROFILE%\.claude\machine_setup.md`. Fill in the machine name and today's date.

## 3. Core tools (winget)

Check each tool, then install whatever is missing:

| Tool | Check | winget id |
|---|---|---|
| Git (includes Git Bash, which Claude Code needs on Windows) | `git --version` | `Git.Git` |
| GitHub CLI | `gh --version` | `GitHub.cli` |
| Node.js LTS | `node -v` | `OpenJS.NodeJS.LTS` |
| Python 3.12 | `python --version` | `Python.Python.3.12` |
| uv (Python tool runner) | `uv --version` | `astral-sh.uv` |
| Obsidian | `winget list --id Obsidian.Obsidian` | `Obsidian.Obsidian` |

- Install with `winget install --id <id> -e --accept-source-agreements --accept-package-agreements`.
- Newly installed tools aren't on PATH in the current shell. Ask the user to restart Claude Code after this step if checks still fail. Or call the tool by its full path for now.
- Python's installer may leave the Microsoft Store `python` alias ahead of the real one. If `python --version` opens the Store, tell the user to turn off the aliases under **Settings > Apps > Advanced app settings > App execution aliases**.

Then tell the user to run `gh auth login` themselves (GitHub.com, HTTPS, login with a web browser). You can't do it for them. Confirm with `gh auth status`.

Set the git identity only with values the user gives you:

```
git config --global user.name "<name>"
git config --global user.email "<email>"
git config --global core.longpaths true
```

Suggest the user's GitHub no-reply address (`<id>+<username>@users.noreply.github.com`, shown at github.com/settings/emails) if they'd rather not publish their real email in commits.

## 4. Document and data tools

These are optional but recommended. Ask once, then install.

- **Python packages:**

  ```
  python -m pip install --user python-docx openpyxl matplotlib pypdf pymupdf pymupdf4llm
  ```

  They cover Word files, Excel files, charts as PNG (use `matplotlib.use("Agg")`), PDF handling, and PDF → Markdown.
- **Poppler** (`oschwartz10612.Poppler`) provides `pdftoppm` and `pdftotext`. Claude's PDF page reading uses them.
- **LibreOffice** (`TheDocumentFoundation.LibreOffice`, about 375 MB, UAC prompt) converts DOCX and other Office formats to PDF:

  ```
  "C:\Program Files\LibreOffice\program\soffice.exe" --headless --convert-to pdf <file>
  ```

After installing, add each tool to `machine_setup.md` with its name, purpose, install location and how to call it.

## 5. Create the wiki vault

1. Copy everything in `KIT/vault-template/` to the vault folder from step 1. That includes the hidden `.claude/` folder and `.gitignore`.
2. In the vault's `CLAUDE.md`, replace `<VAULT NAME>` with the vault's name.
3. Have the user open Obsidian, choose **Open folder as vault**, and pick that folder.

## 6. Connect Claude to Obsidian (MCP)

The user does these steps in Obsidian:

1. **Settings > Community plugins.** Turn off Restricted mode, then click **Browse**.
2. Search for **Local REST API**, by Adam Coddington, then **Install** it and **Enable** it.
3. In the plugin's settings, turn on **Enable Non-encrypted (HTTP) Server**. It runs on port 27123. Use HTTP rather than HTTPS, because Claude Code rejects the plugin's self-signed certificate (`DEPTH_ZERO_SELF_SIGNED_CERT`).

Then the user runs this in PowerShell:

```
powershell -ExecutionPolicy Bypass -File "<KIT>\scripts\register_obsidian_mcp.ps1" -Vault "<vault path>"
```

The script reads the API key from the plugin's `data.json` and registers an `obsidian` MCP server at user scope, so it's available in every folder. You don't see the key at any point.

The user then restarts Claude Code. Check that `/mcp` lists `obsidian` as connected. Obsidian must be open for it to work. Record the server in `machine_setup.md`: its name, port 27123, that Obsidian must be running, and that a second vault would need another port such as 27125.

## 7. Git backup for the vault

Do this step only if the user said yes in step 1.

1. In the vault folder, run `git init -b main`. Make a first commit of the template files.
2. Confirm the repo name with the user (default `wiki`), then run:

   ```
   gh repo create <name> --private --source . --push
   ```

   Always create it **private**.
3. The template's `.claude/settings.json` already registers `.claude/hooks/session_start_sync.py`. At every session start, that hook pulls new commits, but only fast-forwards, and it never overwrites local changes.
4. `/end` (`.claude/commands/end.md`) writes a session note, commits and pushes.

If the user said no, leave the hook in place. It reports "not a repo" and does nothing else. Tell the user that `/end` will skip the push.

## 8. Finish

1. Have the user restart Claude Code **inside the vault folder**. Run a quick test: create `Inbox/Test note.md` through the Obsidian MCP tools, then delete it.
2. Check `machine_setup.md` lists everything you installed.
3. Give the user a short summary:
   - what was installed;
   - where the vault is;
   - how to start a session: open Claude Code in the vault folder with Obsidian running;
   - what `/end` does;
   - anything they still need to do themselves.
4. Leave the kit folder in place, or ask before deleting it. Nothing in it is needed after setup.

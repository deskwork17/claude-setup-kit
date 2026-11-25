#!/usr/bin/env python3
"""SessionStart hook: fast-forward the vault from GitHub if it's behind.

Never merges, rebases or overwrites local work. If the vault has no git repo
or no remote, it just says so.
"""
import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent


def run(cmd):
    return subprocess.run(
        cmd, cwd=REPO, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )


def github_check():
    if run(["git", "rev-parse", "--is-inside-work-tree"]).returncode != 0:
        return "Git: not a repo (no sync)", None
    if not run(["git", "remote"]).stdout.strip():
        return "Git: no remote (no sync)", None
    fetch = run(["git", "fetch", "origin"])
    if fetch.returncode != 0:
        return "Git: fetch failed (offline?)", None
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip() or "main"
    upstream = f"origin/{branch}"
    if run(["git", "rev-parse", "--verify", upstream]).returncode != 0:
        return f"Git: no {upstream} yet", None
    behind = run(["git", "rev-list", "--count", f"HEAD..{upstream}"]).stdout.strip()
    ahead = run(["git", "rev-list", "--count", f"{upstream}..HEAD"]).stdout.strip()
    if behind == "0":
        note = f", {ahead} unpushed commit(s)" if ahead != "0" else ""
        return f"Git: up to date{note}", None
    if ahead != "0":
        return f"Git: diverged ({behind} behind, {ahead} ahead), not auto-pulling", (
            "The vault has diverged from GitHub. Tell the user before changing anything, "
            "and help them reconcile it (never force-push)."
        )
    pull = run(["git", "pull", "--ff-only", "origin", branch])
    if pull.returncode != 0:
        return f"Git: pull failed ({pull.stderr.strip()[:200]})", None
    return f"Git: pulled {behind} new commit(s)", (
        "This session just pulled new commits. Before other work, read the most recent "
        "file in 'Session notes/' to catch up on what changed."
    )


def onboarding_check():
    if (REPO / ".claude" / "onboarding.md").exists():
        return None
    return (
        "Onboarding hasn't been done for this vault yet (.claude/onboarding.md is missing). "
        "Before anything else, greet the user and run the onboarding procedure in "
        ".claude/commands/onboard.md: ask about their use case, suggest skills, commands, "
        "hooks, connectors and a vault layout for their projects, build only what they "
        "approve, then write .claude/onboarding.md. If the user wants to skip it for now, "
        "do their task instead and mention they can run /onboard later."
    )


def main():
    msg, git_context = github_check()
    contexts = [c for c in (git_context, onboarding_check()) if c]
    out = {"systemMessage": msg}
    if contexts:
        out["hookSpecificOutput"] = {
            "hookEventName": "SessionStart",
            "additionalContext": "\n\n".join(contexts),
        }
    print(json.dumps(out))


if __name__ == "__main__":
    main()

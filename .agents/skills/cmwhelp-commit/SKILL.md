---
name: cmwhelp-commit
description: Apply this rule to git commit messages.
---
This rule applies to git commit messages in the version control pane and in the terminal.

Generate the commit message text, but do no add files, stage or push the commit.

# Commit Message Rule

**Important requirement:**

- Always start the commit message with the ticket/issue number.
- **Always ask the user for the ticket number first.** Do not infer from branch names or previous commits unless the user explicitly asks you to.
- Format:
  `[#XXXXX] Concise description of the change`
  where `XXXXX` is the ticket number provided by the user.

**Algorithm:**

1. **Ask the user for the ticket number.** Branch names and previous commits can contain stale or irrelevant numbers, so always confirm with the user before committing. Do not commit without a ticket id.
2. If the user provides a number, use it directly as `[#<number>]`.
3. If the user says there is no ticket, fall back to inferring:
   - Check if a previous commit in the current task/session already uses a `[#XXXXX]` pattern — reuse it.
   - Otherwise extract from the branch name: `platform_v6` → `6`, `platform_v5` → `5`, `12345_branch_name` → `12345`.
4. Only if the user explicitly asks you to infer without asking, use the fallback from step 3. Otherwise, always ask first.
5. Use the issue number in square brackets with a `#` at the start of the commit message (no spaces inside the brackets).
6. Generate a concise description by analyzing the changes:
   - **Check staging status**: Use `git status` to see what's staged vs unstaged
   - **Prefer staged files only**: If there are staged files AND there are also unstaged files, use `git diff --cached` to analyze only staged changes
   - **Fallback to whole diff**: Only if no files are staged OR all files are staged (no unstaged changes exist), then use `git diff` to analyze all changes
   - Focus on the main change: what was added, fixed, or modified
   - Use imperative mood: "Add", "Fix", "Update", "Remove", etc.
   - Keep it to one short sentence (50-70 characters ideal)

**Correct examples:**

User provides `10622680`:
Commit message: `[#10622680] Add Funnel option to diagram widget docs`

User says "no ticket, it's a repo-level change" on `platform_v6`:
Commit message: `[#6] Set up PDF build toolchain`

**Incorrect examples:**

- `Add new documentation section` — no issue number
- `[12345] Fix bug` — no # symbol
- `[ #12345 ] Fix bug in module X, add tests, update docs` — spaces inside brackets
- Inferring from branch name without asking the user first

**Requirements:**

- The message must be concise, structured, and strictly relevant to the changes in the commit.
- Keep the length to the necessary minimum. Avoid blabber.
- Use imperative mood (e.g., "Add feature" not "Added feature" or "Adds feature").
- Focus on what the commit does, not why (unless critical context is needed).

**Note:** Git hooks in `.githooks/` automatically prepend `[#XXXXX]` if missing, but you should still follow this format when generating commit messages manually or via AI.

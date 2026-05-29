---
name: cmwhelp_commit
description: Apply this rule to git commit messages.
---
This rule applies to git commit messages in the version control pane and in the terminal.

Generate the commit message text, but do no add files, stage or push the commit.

# Commit Message Rule

**Important requirement:**

- Always start the commit message with the ticket/issue number.
- Take the issue number from the current branch name (eg., `12345_branch_name`) or from the previous commit message if the branch name does not have the issue number.
- Format:
  `[#XXXXX] Concise description of the change`
  where `XXXXX` is the number at the start of the branch name (up to the first `_` or other separator).

**Algorithm:**

1. Get current branch name, eg. `12345_branch_name`:

``` sh
git rev-parse --abbrev-ref HEAD
```

2. Extract the first sequence of digits (usually up to the `_` character), eg. `12345`.
3. If branch name has no issue number, find it from previous commits:
   - Check recent commit messages: `git log -n 20 --pretty=%B`
   - Look for the pattern `[#XXXXX]` in the most recent commits on this branch
   - Use the first matching issue number found
4. Use the issue number in square brackets with a `#` at the start of the commit message (no spaces inside the brackets).
5. Generate a concise description by analyzing the changes:
   - **Check staging status**: Use `git status` to see what's staged vs unstaged
   - **Prefer staged files only**: If there are staged files AND there are also unstaged files, use `git diff --cached` to analyze only staged changes
   - **Fallback to whole diff**: Only if no files are staged OR all files are staged (no unstaged changes exist), then use `git diff` to analyze all changes
   - Focus on the main change: what was added, fixed, or modified
   - Use imperative mood: "Add", "Fix", "Update", "Remove", etc.
   - Keep it to one short sentence (50-70 characters ideal)

**Correct examples:**

Branch name: `12345_branch_name`
Commit message: `[#12345] Add new documentation section`

Branch name: `67890_branch_name`
Commit message: `[#67890] Fix data processing bug`

Branch name: `branch_name`
Previous commit message: `[#67890] Previous bug fix`
Commit message: `[#67890] Fix data processing bug`

**Incorrect examples:**

- `Add new documentation section` — no issue number
- `[12345] Fix bug` — no # symbol
- `[ #12345 ] Fix bug in module X, add tests, update docs` — spaces inside brackets

**Requirements:**

- The message must be concise, structured, and strictly relevant to the changes in the commit.
- Keep the length to the necessary minimum. Avoid blabber.
- Use imperative mood (e.g., "Add feature" not "Added feature" or "Adds feature").
- Focus on what the commit does, not why (unless critical context is needed).

**Note:** Git hooks in `.githooks/` automatically prepend `[#XXXXX]` if missing, but you should still follow this format when generating commit messages manually or via AI.

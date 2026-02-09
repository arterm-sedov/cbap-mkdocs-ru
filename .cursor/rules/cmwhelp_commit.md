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
3. Find a previous commit message if the branch name has no issue number. Previous commit message might already contain the right [#XXXXX] pattern.
4. Use the issue number in square brackets with a `#` at the start of the commit message (no spaces inside the brackets).
5. After the brackets, provide a concise, to-the-point description of the change.

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

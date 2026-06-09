---
name: self-evolution
description: Use when you've completed a non-trivial task and need to document discoveries, patterns, or gotchas for future sessions. Also use to review the discovery log before starting similar work.
---

# Self-Evolution — Documenting Discoveries

After completing a non-trivial task, review what was learned and capture it so it benefits future sessions.

## When To Document

- A pattern that took debugging to figure out (e.g., silent macro errors, missing anchor warnings).
- A workflow step not covered by existing skills (e.g., which PHPKB category ID to use, which script signature fits which context).
- A recurring gotcha that cost time and would cost again.

## Where To Document

| Finding type | Destination |
|---|---|
| **Process/skill gap** | Update the matching skill under `.agents/skills/<name>/SKILL.md` |
| **Recurring authoring pitfall** | Add a concise rule to `AGENTS.md` under the relevant heading |
| **One-off context note** (category IDs, naming conventions) | Add to the relevant skill's `references/` folder |
| **Session discovery** (more than a one-off, not yet migrated) | Append to `references/discovery_log.md` (alongside this skill) |

## How

1. State the symptom and the fix in 1–2 lines.
2. Add it to the most specific skill or rule file — prefer updating existing docs over creating new ones.
3. Keep it agnostic: no absolute paths, no secrets, no machine-specific notes.
4. Append new entries to [references/discovery_log.md](references/discovery_log.md) with a date heading.

## Review Before Starting

When starting a non-trivial task, quickly scan `references/discovery_log.md` for recent entries relevant to the work at hand. Many gotchas are domain-specific and won't surface in generic search.

## Periodic Cleanup

Move entries from `references/discovery_log.md` into durable skill/rule files when they've proven useful across multiple sessions. Delete old log entries that have been fully absorbed into skills or rules.

# phase-meanings

What each of the five phases means, the one thing that changes in it, and how its illustration shows that. Text and image must say the same thing.

The author's framing: most teams are in phase 2 today, some reach phase 3, and phases 4 and 5 are where things are heading — the author has not yet seen them in practice. Present 4 and 5 as forward-looking recommendations ("I'd…", "my guess is…", "would"), never as observed fact.

Every illustration uses the same repository box so the reader sees its contents evolve. Section headings match the titles drawn in the images.

| # | Post heading | Image title | What changes | How the image shows it |
|---|---|---|---|---|
| 1 | Nothing added | Nothing added | Nothing — the baseline. The developer types all the code. | Developer typing at a keyboard → "types code" → repo with only `{ }` files. No AI. |
| 2 | The developer prompts an AI | The developer prompts an AI | An AI writes the code, but the project knowledge lives in the developer's head and is re-typed every session. | Thought cloud "in the developer's head" (React, tests in /spec, don't touch /legacy); "prompt + all of that, ↻ again, every session"; AI "starts empty each session". |
| 3 | AI context in the project | AI context in the project | The knowledge moves into the repo (`CLAUDE.md`, cards, project plan); the AI reads it every session; prompts get short. The same docs let parallel agents (one per git worktree) start from shared context. Unit and function tests arrive here, so the agent can check its own change. | Same chips now inside the repo under "AI context"; "reads" arrow to the AI; prompt is just "Add a login page."; a green "✓ unit + function tests" chip under the code files, with a "runs tests" arrow from the AI. |
| 4 | Architecture chosen for AI | Architecture chosen for AI | The developer actively picks designs that suit how an AI works, and starts measuring code quality (complexity, duplication, coverage, dependency rules) with thresholds the agent sees. | Whiteboard "architecture decisions": one big shared module → small features with clear hooks; rules written in docs → rules enforced by hooks; conventions in people's heads → explicit contract per feature; no quality measurement → code quality measured. Result: repo with hook slots, chips "contracts", "fast tests", "quality checks", inside "enforced rules". |
| 5 | Safe enough for stakeholders to drive | Safe enough for stakeholders to drive | Only once the project is fully set up, guarded and seen to hold (tests from phase 3, quality checks from phase 4) can stakeholders drive features; the developer stops adding features and maintains the system. Review scales by a second AI checking each change; humans step in only when it or a check flags something. | Repo fenced "guarded on every side"; stakeholder's change passes a "checks" gate (tests, hooks, review); developer's AI does "upkeep" on the foundation that "keeps it safe". |

## Rules of thumb

- Phase 1 is typing, never pen and paper ("by hand" was misread that way once).
- Phase 4 is about deliberate decisions, not just the resulting structure.
- Phase 5's precondition is safety; without it the phase does not work.
- When a phase's meaning changes, update in this order: diagram → illustration → heading, text and alt text in `blog-post.md` → the "Where is your project?" table row → `make check`.

# Project Plan: The Five Phases of AI Adoption — blog post

## Goal

Publish the post on the author's blog with text and illustrations that agree, so a reader understands what changes in each phase and leaves with one concrete next step (pointing their agent at ai.memention.net/setup).

## Non-goals

- Changing the five-phase model itself (the phases come from the author's brief).
- A new illustration concept unless the author asks; concept 2 is the current direction.
- A general static-site generator; at most a small markdown → HTML step for this one post.
- Claiming phases 4 and 5 are observed practice — they stay forward-looking.

## Milestones

- [x] M1 — Draft post in `blog-post.md` and `blog-post.html`
- [x] M2 — Concept 1 illustrations (comic) — committed, tagged `concept-1` / `style-1`
- [x] M3 — Concept 2: meaning diagrams + illustrations for all five phases (phases 1, 4, 5 redone on 2026-10-31)
- [x] M4 — Editorial review in `ASSESSMENT.md`
- [x] M5 — Project setup: `CLAUDE.md`, cards, this plan, `Makefile`
- [x] M6 — Apply the review (items below)
- [x] M7 — Single source: `blog-post.html` is generated from `blog-post.md` (`make html`, `scripts/build_html.py`)
- [x] M6b — Apply the round-2 review (items below)
- [x] M6c — Apply the round-3 review (items below)
- [ ] M8 — Optimise images (WebP, ~200 KB each instead of ~1.5 MB)
- [ ] M9 — Final proofread, `make check screenshot`, commit, merge `blog-post` into `main`
- [ ] M10 — Publish

### M6 — review items (numbers refer to ASSESSMENT.md)

- [x] R1 (issues 1–2) — Phase 4: make the bullets mirror the decision board (hooks/small features, rules enforced by hooks, contract per feature, fast tests); move skills to phase 3 or a tooling note; reframe "even if it's not the one you'd have picked for a human-only team" as "AI becomes the tie-breaker".
- [x] R2 (issue 3) — Phase 5: one sentence on what "review" means, so the developer isn't the bottleneck again. Author's answer: a second AI reviews each change alongside tests and hooks; humans step in only on a flag.
- [x] R3 (issue 4) — Cut one of the three "not yet seen" sentences (suggest the one in phase 4).
- [x] R4 (issue 5) — Align section headings with the image titles (or a blend, e.g. "Safe enough that the developer stops adding features").
- [x] R5 (issue 6) — Intro: "changes what the AI knows, who drives the changes, and what the developer spends their day on".
- [x] R6 (issue 7) — One line noting the examples use Claude Code; `AGENTS.md` plays the same role elsewhere.
- [x] R7 (issue 8) — Two or three sentences on cost and risk (setup and upkeep time, tokens, non-developers triggering changes).
- [x] R8 (issue 9) — Fix the markdown/HTML drift (phase 3 heading; decide on the callout and the "Here they are" line). Resolved by M7.
- [x] R9 (issue 10) — Phase 4 image draws the AI twice: regenerate or touch up (~655 credits; approved, regenerated with "exactly one robot" in the prompt).
- [x] R10 — The small line edits in ASSESSMENT.md ("Smaller line edits").

### M6b — round-2 review items (issue numbers refer to the round-2 ASSESSMENT.md)

- [x] R11 (issue 1) — Phase 5: drop "I think" after "my guess"; ease the six "would"s once the conditional frame is set.
- [x] R12 (issue 2) — Introduce the setup checker once: drop the phase 3 callout or the checker mention in "Getting started". Author's call: keep the callout; the checker mention left "Getting started".
- [x] R13 (issue 3) — Intro: add "how the code is shaped" so phase 4 is covered.
- [x] R14 (issue 4) — Phase 3: split the list intro; move the Claude Code naming note after the list.
- [x] R15 (issue 5) — Closing: soften "only holds up" and "have to be treated" to match phases 4–5.
- [x] R16 — Line edits: "few have tried it yet"; "an AI agent" once in phase 2.

### M6c — round-3 review items (issue numbers refer to the round-3 ASSESSMENT.md)

- [x] R17 (issue 1) — Phase 3: move "The application code itself hasn't changed yet…" before the tests paragraph.
- [x] R18 (issue 2) — Phase 3: tests "whether they're new or already there"; what's new is the agent running them.
- [x] R19 (issue 3) — Phase 5: split the two-colon opening sentence.
- [x] R20 — Phase 4 alt text: "“code quality measured” (replacing “no quality measurement”)".
- [ ] R21 (issues 4–5, optional) — Trim phase 3's last orchestration sentence; widen the phase 4 intro with "and measuring whether it holds". Author's call.

## Decisions

- 2026-10-30 — Markdown and a standalone HTML preview, both in the repo. HTML is hand-maintained for now.
- 2026-10-30 — Illustrations generated with ElevenLabs (`gpt-image-2`) via the MCP server; the author's account was upgraded on 2026-10-31.
- 2026-10-31 — Phases 4 and 5 are presented as forward-looking: most teams are in phase 2, some in 3.
- 2026-10-31 — Concept 2 (meaning-first diagrams, then soft hand-drawn illustrations) replaces concept 1 (comic panels). Concept 1 is archived in `images/concept-1/` and at tag `concept-1`.
- 2026-10-31 — Phase 1 shows typing, phase 4 shows deliberate architecture decisions, phase 5 shows a fully guarded project with a checks gate.
- 2026-10-31 — Generation needs the author's go-ahead with a stated cost; never retry a generate call.
- 2026-10-31 — `blog-post.md` is the single source; `blog-post.html` is generated by a stdlib-only script, with page chrome in `scripts/template.html`.
- 2026-10-31 — Section headings now match the titles drawn in the images.
- 2026-10-31 — Phase 5 review scales by an AI reviewer plus tests and hooks; humans step in only when something is flagged.
- 2026-10-31 — Phases 4 and 5 are written as recommendations ("I'd…", "would"), not facts; the setup page is presented as the author's own example and a starting point, not the answer.
- 2026-11-07 — Phase 3 also argues that in-repo context is what makes agent orchestration work: parallel agents in separate git worktrees all start from the same docs.
- 2026-11-07 — Tests split across phases: unit and function tests belong to phase 3, code-quality measurement to phase 4, and phase 5 starts once that setup has been validated. Kept five phases rather than adding a separate testing phase. Phase 3 and 4 illustrations updated to match by editing the current images (~840 credits); phase 5 kept, since its gate already reads "tests, hooks, review".

## Current state / handoff

M6, M6b, M6c and M7 are done: all three review rounds are applied (R21 optional, open) in `blog-post.md`, the HTML is generated from it, and `make check` passes. The post is ready to publish apart from the publishing steps. Next: M8–M10 (WebP, final proofread and merge, publish), which depend on where the post is published — see Open questions.

## Open questions

- Where will the post be published, and in what format (markdown with frontmatter, HTML, a CMS)? This decides M7 and M8.
- Keep the comic heading font (Bangers) on the HTML page, or switch to something calmer to match the concept-2 illustrations?
- Keep the title and subtitle drawn inside each illustration (good for sharing single images), or crop them out for the post?

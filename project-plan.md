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
- [ ] M6 — Apply the review (items below)
- [ ] M7 — Single source: generate `blog-post.html` from `blog-post.md` (`make html`), so they can't drift
- [ ] M8 — Optimise images (WebP, ~200 KB each instead of ~1.5 MB)
- [ ] M9 — Final proofread, `make check screenshot`, commit, merge `blog-post` into `main`
- [ ] M10 — Publish

### M6 — review items (numbers refer to ASSESSMENT.md)

- [ ] R1 (issues 1–2) — Phase 4: make the bullets mirror the decision board (hooks/small features, rules enforced by hooks, contract per feature, fast tests); move skills to phase 3 or a tooling note; reframe "even if it's not the one you'd have picked for a human-only team" as "AI becomes the tie-breaker".
- [ ] R2 (issue 3) — Phase 5: one sentence on what "review" means, so the developer isn't the bottleneck again. Needs the author's view (see Open questions).
- [ ] R3 (issue 4) — Cut one of the three "not yet seen" sentences (suggest the one in phase 4).
- [ ] R4 (issue 5) — Align section headings with the image titles (or a blend, e.g. "Safe enough that the developer stops adding features").
- [ ] R5 (issue 6) — Intro: "changes what the AI knows, who drives the changes, and what the developer spends their day on".
- [ ] R6 (issue 7) — One line noting the examples use Claude Code; `AGENTS.md` plays the same role elsewhere.
- [ ] R7 (issue 8) — Two or three sentences on cost and risk (setup and upkeep time, tokens, non-developers triggering changes).
- [ ] R8 (issue 9) — Fix the markdown/HTML drift (phase 3 heading; decide on the callout and the "Here they are" line). Superseded by M7 if that lands first.
- [ ] R9 (issue 10) — Phase 4 image draws the AI twice: regenerate or touch up (~655 credits; ask first).
- [ ] R10 — The small line edits in ASSESSMENT.md ("Smaller line edits").

## Decisions

- 2026-10-30 — Markdown and a standalone HTML preview, both in the repo. HTML is hand-maintained for now.
- 2026-10-30 — Illustrations generated with ElevenLabs (`gpt-image-2`) via the MCP server; the author's account was upgraded on 2026-10-31.
- 2026-10-31 — Phases 4 and 5 are presented as forward-looking: most teams are in phase 2, some in 3.
- 2026-10-31 — Concept 2 (meaning-first diagrams, then soft hand-drawn illustrations) replaces concept 1 (comic panels). Concept 1 is archived in `images/concept-1/` and at tag `concept-1`.
- 2026-10-31 — Phase 1 shows typing, phase 4 shows deliberate architecture decisions, phase 5 shows a fully guarded project with a checks gate.
- 2026-10-31 — Generation needs the author's go-ahead with a stated cost; never retry a generate call.

## Current state / handoff

All five concept-2 illustrations are in place and the post text matches them. `ASSESSMENT.md` lists the remaining editorial issues; none are applied yet. Everything is committed on `blog-post` (concept 2, the reorganised `images/concept-1/`, `ASSESSMENT.md`, this project setup). Next: work through M6, starting with R1–R3; R2 needs the author's answer first.

## Open questions

- Where will the post be published, and in what format (markdown with frontmatter, HTML, a CMS)? This decides M7 and M8.
- Phase 5: who reviews stakeholder changes — automated checks plus light human sign-off, stakeholders owning acceptance, or something else? (R2)
- Keep the comic heading font (Bangers) on the HTML page, or switch to something calmer to match the concept-2 illustrations?
- Keep the title and subtitle drawn inside each illustration (good for sharing single images), or crop them out for the post?

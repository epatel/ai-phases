# The Five Phases of AI Adoption — blog post

## About this project

A blog post by Edward Patel describing five phases a software project goes through as AI agents move in. `blog-post.md` is the source text; `blog-post.html` is a standalone preview page generated from it; each phase has an illustration in `images/concept-2/`, generated with ElevenLabs from SVG "meaning" diagrams. The post is published at https://epatel.github.io/ai-phases/ by GitHub Pages from `main` (repo `epatel/ai-phases`, public). There is no app to build: the work is writing, diagrams, illustrations and checks.

Always read @project-plan.md before starting — it holds the goal, the open review items and the current state.

## Commands

- `make` — list targets
- `make html` — build `blog-post.html` from `blog-post.md` and `scripts/template.html`
- `make jpg` — make the published JPGs from the PNG masters in `images/concept-2/` (run after replacing an illustration)
- `make site` — assemble the GitHub Pages site in `_site/` (`index.html` + the five JPGs); CI runs this on every push to `main`
- `make diagrams` — regenerate the SVG diagrams from `images/concept-2/diagrams/make_concept.py`
- `make previews` — render the diagrams to `build/previews/` to look at them
- `make refs` — render the diagrams at 1.6× to `build/refs/` for upload to ElevenLabs
- `make check` — rebuild the HTML, verify every image and local link resolves, then run the agent-docs checker
- `make screenshot` — desktop and phone-width screenshots of `blog-post.html` into `build/`
- `make open` — open the HTML preview in the browser
- `make clean` — remove `build/`

## Working rules

- Image generation spends the author's ElevenLabs credits. State the cost and get a go-ahead before generating, and never re-run a generate call to retry — it charges again.
- Edit `blog-post.md`, never `blog-post.html` — it is generated. Page styling and chrome live in `scripts/template.html`. Run `make html` (or `make check`) after editing.
- Look at every generated or rendered image before using it; check each label's spelling.

## Cards

### Architecture
- [architecture](cards/architecture.md) — finding a file, understanding how text, HTML and images connect, or onboarding

### Domains
- [phase-meanings](cards/phase-meanings.md) — writing or changing any phase's text, heading or illustration, or checking that text and image say the same thing
- [setup-site-links](cards/setup-site-links.md) — adding or checking links to ai.memention.net, or when that site is unreachable

### Features
- [illustration-pipeline](cards/illustration-pipeline.md) — making or regenerating an illustration with ElevenLabs, or editing a diagram
- [html-preview](cards/html-preview.md) — changing how the HTML page looks or is built, or adding markdown the generator doesn't handle yet

### Decisions
- [concept-2-over-concept-1](cards/concept-2-over-concept-1.md) — questions about the comic version, the old images, or changing the illustration style

When you commit a change that adds non-obvious logic, settles a choice, or makes a card above wrong, update or add the card in that commit and keep this index in sync. Proposed diffs and answers need no card edits. Cards stay self-contained: no card links to another.

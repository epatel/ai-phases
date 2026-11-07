# architecture

How the project's files fit together: the post text, the HTML preview, and where every image comes from.

## Files

| Path | What it is |
|---|---|
| `blog-post.md` | The post and the single source of truth. Frontmatter (title, date, author, page settings), five phase sections, a "Where is your project?" table, "Getting started". |
| `blog-post.html` | Generated preview page (`make html`); never edited by hand. |
| `scripts/build_html.py`, `scripts/template.html` | The markdown → HTML generator and the page template (head, CSS, header, footer). |
| `images/concept-2/phase-1..5.png` | The illustrations the post uses (1280×720, ElevenLabs `gpt-image-2`). |
| `images/concept-2/diagrams/` | `make_concept.py` and the SVG "meaning" diagrams it writes; the layout reference for each illustration. |
| `images/concept-2/first-take/` | Superseded versions of phases 1, 3, 4 and 5 (`phase-4-v2.png` drew the AI twice). |
| `images/concept-1/` | Archive of the first concept: `comic/` (ElevenLabs comic panels), `code-drawn/` (SVG-rendered comics), `style-2-phase-5.png` (a softer comic test). |
| `ASSESSMENT.md` | Editorial review of the post, with numbered issues. |
| `project-plan.md` | Goal, milestones, decisions and open items. |
| `Makefile`, `scripts/check_post.py` | HTML build, rendering, checks and screenshots. |
| `ai-phases.pdf`, `initial-idea.md` | The author's original hand sketches and brief. Git-ignored, local only. |
| `build/` | Generated previews, refs and screenshots. Git-ignored. |
| `.github/workflows/pages.yml`, `_site/` | GitHub Pages deploy: on push to `main`, CI runs `make site` and publishes `_site/` (git-ignored) — only `index.html` and the five illustrations, not the working files. |

## How an illustration gets made

```mermaid
flowchart LR
  A[make_concept.py] -->|make diagrams| B[phase-N.svg]
  B -->|make refs| C[build/refs/phase-N.png]
  C -->|upload + generate| D[ElevenLabs gpt-image-2]
  S[style reference image] --> D
  D -->|download, review labels| E[images/concept-2/phase-N.png]
  E --> F[blog-post.md]
  F -->|make html| H[blog-post.html]
  H -->|make check, make screenshot| G[verified page]
```

## Git

- `main` is what's published (https://epatel.github.io/ai-phases/); every push to it redeploys. Work can happen on `blog-post` and be fast-forwarded into `main`.
- Remote: `github.com/epatel/ai-phases` (public). Anything committed is public, so keep secrets and signed ElevenLabs URLs out of the repo.
- Tags `style-1` and `concept-1` both point at the commit with the comic (concept 1) version of the post.

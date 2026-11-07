# html-preview

`blog-post.html` is a standalone page showing how the published post could look. It is generated from `blog-post.md` by `scripts/build_html.py` (standard library only) — never edit it by hand.

## How the page is built

- `scripts/template.html` holds the `<head>`, all CSS, the site header (links to `/setup` and `cards/setup-changelog.md`) and the footer, with `{{title}}`, `{{description}}`, `{{article}}` and `{{footer}}` placeholders.
- Frontmatter in the markdown feeds the page: `title`, `date`, `author` (byline), `description` (meta tag), `kicker` (label above the title), `nav` (comma-separated pill labels, one per phase), `credit` (footer).
- Text before the first `---` becomes the lede under the title.
- `## Phase N: Title` becomes a numbered section with id `phase-N`; the nav pills link to these.
- Other `##` sections get a decorative break before them; `## Getting started` becomes the yellow call-to-action box with a "Have a look at the setup page →" button.
- A blockquote starting with bold text (`> **Try it on your repo** …`) becomes a callout box.
- Standalone images become `figure.panel` with the image's width and height read from the file (PNG or JPEG); every image after the first is lazy-loaded.

## Supported markdown

Paragraphs, `- ` lists, pipe tables, standalone `![alt](src)` images, blockquotes, `---`, `` `code` ``, `**bold**`, `*italic*`, `[links](url)`. Anything else (nested lists, numbered lists, headings below `##`, raw HTML) is not handled — extend the script before using it.

## Styling

- Colour tokens on `:root`, redefined for dark mode under `prefers-color-scheme: dark` and `[data-theme="dark"]`.
- Fonts from Google Fonts: Bangers (headings, comic accents), Literata (body), JetBrains Mono (code).
- `figure.panel img` has a thin rounded border and a soft shadow; links inside the yellow call-to-action box are dark for contrast.
- Layout: 760 px column, 16 px side gutter; works at 390 px phone width.

## Verify

`make check` rebuilds the page and checks every image and local link. `make screenshot` writes `build/page-desktop.png` and `build/page-phone.png` (the phone shot renders the page inside a 390 px iframe, because headless Chrome will not shrink its window that far). Look at both.

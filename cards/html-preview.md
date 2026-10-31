# html-preview

`blog-post.html` is a standalone page that shows how the published post could look. It is hand-maintained next to `blog-post.md`.

## Keeping it in sync

- Any text change goes into both files in the same edit; markdown `**x**` and `` `x` `` become `<strong>` and `<code>`.
- Intentional HTML-only parts: the site header (links to `/setup` and `cards/setup-changelog.md`), the kicker above the title, the phase nav pills, the "Try it on your repo" callout in phase 3, the "Set up your project →" button, and the footer credit.
- Known drift to fix: the phase 3 heading ("AI context is scaffolded…" in HTML vs "AI context engineering is scaffolded…" in markdown); the markdown's "Here they are, with an illustration for each." line has no HTML counterpart.
- Image `alt` text must match the markdown's image descriptions.

## Styling

- Colour tokens on `:root`, redefined for dark mode under `prefers-color-scheme: dark` and `[data-theme="dark"]`.
- Fonts from Google Fonts: Bangers (headings, comic accents), Literata (body), JetBrains Mono (code).
- `figure.panel img` has a thin rounded border and a soft shadow, suited to the concept-2 illustrations.
- Layout: 760 px column, 16 px side gutter; works at 390 px phone width.

## Verify

`make screenshot` writes `build/page-desktop.png` and `build/page-phone.png` (the phone shot renders the page inside a 390 px iframe, because headless Chrome will not shrink its window that far). Look at both.

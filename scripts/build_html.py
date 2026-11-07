#!/usr/bin/env python3
"""Build blog-post.html from blog-post.md and scripts/template.html.

Usage: python3 scripts/build_html.py [SOURCE.md] [OUT.html]

Standard library only. Handles the markdown this post uses: frontmatter,
## sections, paragraphs, "- " lists, pipe tables, standalone images,
"> " blockquotes, ---, `code`, **bold**, *italic* and [links](url).

Page structure comes from the source:
  - text before the first "---" becomes the lede under the title
  - "## Phase N: Title" becomes a numbered phase section with a nav pill
    (labels from the `nav:` frontmatter list)
  - a "> **Heading** text" blockquote becomes a callout box
  - "## Getting started" becomes the call-to-action box with a button
"""
import html
import re
import struct
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "blog-post.md"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "blog-post.html"
TEMPLATE = ROOT / "scripts" / "template.html"
CTA_URL = "https://ai.memention.net/setup"
CTA_LABEL = "Have a look at the setup page →"


def inline(text):
    """Escape, then apply code spans, links, bold and italic."""
    codes = []

    def keep_code(m):
        codes.append(f"<code>{html.escape(m.group(1), quote=False)}</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<em>\1</em>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)


def image_size(path):
    """(width, height) of a PNG or baseline/progressive JPEG, else (None, None)."""
    data = Path(path).read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w, h
            i += 2 + length
    return None, None


def frontmatter(text):
    meta = {}
    if text.startswith("---\n"):
        block, text = text[4:].split("\n---\n", 1)
        for line in block.splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
    return meta, text


def blocks(text):
    """Split markdown into (kind, lines) blocks."""
    out, cur, kind = [], [], None

    def flush():
        nonlocal cur, kind
        if cur:
            out.append((kind, cur))
        cur, kind = [], None

    for line in text.splitlines():
        if not line.strip():
            flush()
            continue
        if line.startswith("#"):
            flush()
            out.append(("heading", [line]))
            continue
        if line.strip() == "---":
            flush()
            out.append(("rule", [line]))
            continue
        k = ("list" if line.startswith("- ") else "table" if line.startswith("|")
             else "quote" if line.startswith(">") else "image" if line.startswith("![") else "para")
        if kind and k != kind and not (kind == "list" and k == "para"):
            flush()
        kind = kind or k
        cur.append(line)
    flush()
    return out


def render(kind, lines, first_image):
    if kind == "para":
        return f"<p>{inline(' '.join(lines))}</p>"
    if kind == "list":
        items, cur = [], []
        for line in lines:
            if line.startswith("- ") and cur:
                items.append(" ".join(cur))
                cur = []
            cur.append(line[2:] if line.startswith("- ") else line.strip())
        items.append(" ".join(cur))
        return "<ul>\n" + "\n".join(f"  <li>{inline(i)}</li>" for i in items) + "\n</ul>"
    if kind == "table":
        rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
        head, body = rows[0], [r for r in rows[2:]]
        th = "".join(f"<th>{inline(c)}</th>" for c in head)
        tb = "\n".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
        return f'<div class="table-wrap">\n<table>\n<thead><tr>{th}</tr></thead>\n<tbody>\n{tb}\n</tbody>\n</table>\n</div>'
    if kind == "quote":
        body = " ".join(l.lstrip(">").strip() for l in lines)
        m = re.match(r"\*\*(.+?)\*\*\s*(.*)", body)
        title, rest = (m.group(1), m.group(2)) if m else ("", body)
        strong = f"<strong>{inline(title)}</strong>\n" if title else ""
        return f'<div class="callout">\n{strong}<p>{inline(rest)}</p>\n</div>'
    if kind == "image":
        m = re.match(r"!\[([^\]]*)\]\(([^)\s]+)\)", lines[0])
        alt, src = m.group(1), m.group(2)
        w, h = image_size(SRC.parent / src)
        size = f' width="{w}" height="{h}"' if w else ""
        lazy = "" if first_image else ' loading="lazy"'
        return f'<figure class="panel"><img src="{src}"{size}{lazy} alt="{html.escape(alt)}"></figure>'
    raise ValueError(kind)


def build():
    meta, body = frontmatter(SRC.read_text())
    nav = [s.strip() for s in meta.get("nav", "").split(",") if s.strip()]
    parts = blocks(body)

    # Title and lede: everything before the first rule.
    title = meta.get("title", "")
    lede = []
    while parts and parts[0][0] != "rule":
        kind, lines = parts.pop(0)
        if kind == "heading" and lines[0].startswith("# "):
            title = title or lines[0][2:]
        elif kind == "para":
            lede.append(f'<p class="lede">{inline(" ".join(lines))}</p>')

    sections, cur, cur_kind = [], [], None
    image_seen = False

    def close():
        if cur_kind:
            sections.append((cur_kind, cur[:]))

    for kind, lines in parts:
        if kind == "rule":
            continue
        if kind == "heading" and lines[0].startswith("## "):
            close()
            cur.clear()
            cur_kind = lines[0][3:].strip()
            continue
        cur.append(render(kind, lines, not image_seen))
        image_seen = image_seen or kind == "image"
    close()

    out = []
    phase_ids = []
    for heading, content in sections:
        m = re.match(r"Phase (\d+):\s*(.+)", heading)
        if m:
            n, name = m.groups()
            phase_ids.append(n)
            out.append(f'<section class="phase" id="phase-{n}">\n<h2><span class="num">{n}</span>{inline(name)}</h2>\n'
                       + "\n".join(content) + "\n</section>")
        elif heading.lower() == "getting started":
            out.append(f'<aside class="cta">\n<h2>{inline(heading)}</h2>\n' + "\n".join(content)
                       + f'\n<a class="button" href="{CTA_URL}">{html.escape(CTA_LABEL)}</a>\n</aside>')
        else:
            slug = re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")
            if not out or not out[-1].startswith('<hr'):
                out.append('<hr class="break">')
            out.append(f'<section class="phase" id="{slug}">\n<h2>{inline(heading)}</h2>\n' + "\n".join(content) + "\n</section>")

    pills = "\n".join(f'  <li><a href="#phase-{n}">{n} · {html.escape(label)}</a></li>'
                      for n, label in zip(phase_ids, nav))
    when = meta.get("date", "")
    pretty = date.fromisoformat(when).strftime("%B %-d, %Y") if when else ""
    byline = " · ".join(x for x in [meta.get("author", ""), pretty] if x)
    hero = (f'<header class="hero">\n'
            + (f'<span class="kicker">{html.escape(meta["kicker"])}</span>\n' if meta.get("kicker") else "")
            + f"<h1>{inline(title)}</h1>\n"
            + (f'<p class="byline">{html.escape(byline)}</p>\n' if byline else "")
            + "\n".join(lede)
            + (f'\n<ul class="phase-nav">\n{pills}\n</ul>' if pills else "")
            + "\n</header>")

    page = TEMPLATE.read_text()
    year = when[:4] or str(date.today().year)
    footer = f"© {year} {meta.get('author', '')} · {meta.get('credit', '')}".rstrip(" ·")
    for key, value in {
        "title": html.escape(title),
        "description": html.escape(meta.get("description", ""), quote=True),
        "article": hero + "\n\n" + "\n\n".join(out),
        "footer": html.escape(footer),
    }.items():
        page = page.replace("{{" + key + "}}", value)
    OUT.write_text(page)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(sections)} sections)")


if __name__ == "__main__":
    build()

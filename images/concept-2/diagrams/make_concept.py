"""Concept diagrams for the five phases: one repo box per panel whose contents evolve."""
import os
import sys

OUT = sys.argv[1]
W, H = 800, 480

INK = "#1f2937"
MUTED = "#64748b"
LINE = "#94a3b8"
DEV = "#2563eb"
STAKE = "#db2777"
AI = "#7c3aed"
AI_TINT = "#ede9fe"
DOC = "#b45309"
DOC_TINT = "#fef3c7"
CODE = "#0f766e"
CODE_TINT = "#ccfbf1"
GUARD = "#ea580c"
FONT = 'font-family="-apple-system, \'Segoe UI\', Helvetica, Arial, sans-serif"'
MONO = 'font-family="\'SF Mono\', Menlo, Consolas, monospace"'


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, color=INK, weight=400, anchor="start", mono=False, italic=False):
    fam = MONO if mono else FONT
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" {fam} font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}"{st}>{esc(s)}</text>')


def frame(num, title, idea, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Phase {num}: {esc(title)}. {esc(idea)}">
<defs>
  <marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{MUTED}"/></marker>
  <marker id="ah-ai" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{AI}"/></marker>
  <marker id="ah-doc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DOC}"/></marker>
  <marker id="ah-dev" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DEV}"/></marker>
  <marker id="ah-stake" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{STAKE}"/></marker>
  <marker id="ah-code" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{CODE}"/></marker>
  <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="{GUARD}" stroke-opacity="0.25" stroke-width="3"/></pattern>
</defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
{text(32, 44, f"PHASE {num}", 12, MUTED, 700)}
{text(32, 72, title, 22, INK, 700)}
{text(32, 98, idea, 15, MUTED)}
{body}
</svg>
"""


def person(cx, cy, color, label):
    return (f'<g><circle cx="{cx}" cy="{cy-24}" r="15" fill="{color}"/>'
            f'<path d="M{cx-24},{cy+24} v-10 a24,22 0 0 1 48,0 v10 z" fill="{color}"/>'
            + text(cx, cy + 46, label, 13, INK, 600, "middle") + "</g>")


def ai(cx, cy, label=None, note=None):
    out = (f'<g><line x1="{cx}" y1="{cy-28}" x2="{cx}" y2="{cy-40}" stroke="{AI}" stroke-width="3"/>'
           f'<circle cx="{cx}" cy="{cy-43}" r="5" fill="{AI}"/>'
           f'<rect x="{cx-34}" y="{cy-28}" width="68" height="56" rx="14" fill="{AI}"/>'
           + text(cx, cy + 7, "AI", 20, "#ffffff", 700, "middle"))
    if label:
        out += text(cx, cy + 50, label, 13, INK, 600, "middle")
    if note:
        out += text(cx, cy + 68, note, 12, MUTED, 400, "middle", italic=True)
    return out + "</g>"


def chip(x, y, s, color, tint, mono=False, size=12):
    w = len(s) * (7.4 if mono else 6.9) + 20
    return (f'<g><rect x="{x}" y="{y}" width="{w:.0f}" height="26" rx="13" fill="{tint}" stroke="{color}" stroke-width="1.5"/>'
            + text(x + w / 2, y + 17.5, s, size, color, 600, "middle", mono) + "</g>"), w


def chips_row(x, y, labels, color, tint, gap=8, mono=False):
    out, cx = "", x
    for s in labels:
        g, w = chip(cx, y, s, color, tint, mono)
        out += g
        cx += w + gap
    return out


def code_file(x, y, w=46, h=56):
    f = 12
    return (f'<g><path d="M{x},{y} H{x+w-f} L{x+w},{y+f} V{y+h} H{x} z" fill="{CODE_TINT}" stroke="{CODE}" stroke-width="1.8"/>'
            + text(x + w / 2, y + h / 2 + 6, "{ }", 15, CODE, 700, "middle", True) + "</g>")


def code_grid(x, y, cols, rows, dx=60, dy=70):
    return "".join(code_file(x + c * dx, y + r * dy) for r in range(rows) for c in range(cols))


def repo(x, y, w, h, label="repository"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#f8fafc" stroke="{LINE}" stroke-width="2"/>'
            + text(x + 16, y + 24, label, 12, MUTED, 700))


def arrow(d, color=MUTED, marker="ah", width=2.5, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{da} marker-end="url(#{marker})"/>'


def bubble(x, y, s, color=INK):
    w = len(s) * 7.2 + 24
    return (f'<g><rect x="{x}" y="{y}" width="{w:.0f}" height="30" rx="8" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>'
            + text(x + 12, y + 20, s, 13, color, 500, italic=True) + "</g>")


def padlock(x, y, color=GUARD):
    return (f'<g><path d="M{x+4},{y+9} v-4 a5,5 0 0 1 10,0 v4" fill="none" stroke="{color}" stroke-width="2"/>'
            f'<rect x="{x}" y="{y+8}" width="18" height="13" rx="2" fill="{color}"/></g>')


def node(x, y, s, w=66, kind="code"):
    if kind == "slot":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="#ffffff" stroke="{AI}" stroke-width="2" stroke-dasharray="5 4"/>'
                + text(x + w / 2, y + 22, s, 12, AI, 600, "middle"))
    if kind == "new":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{AI_TINT}" stroke="{AI}" stroke-width="2"/>'
                + text(x + w / 2, y + 22, s, 12, AI, 700, "middle"))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{CODE_TINT}" stroke="{CODE}" stroke-width="1.8"/>'
            + text(x + w / 2, y + 22, s, 12, CODE, 600, "middle"))


def pipeline(x, y, items, w=66, gap=18):
    out = ""
    for i, (s, kind) in enumerate(items):
        nx = x + i * (w + gap)
        out += node(nx, y, s, w, kind)
        if i < len(items) - 1:
            out += f'<line x1="{nx+w+2}" y1="{y+17}" x2="{nx+w+gap-3}" y2="{y+17}" stroke="{CODE}" stroke-width="2" marker-end="url(#ah)"/>'
    return out


def cloud(x, y, w, h, tail_to):
    tx, ty = tail_to
    trail = "".join(
        f'<circle cx="{x + w * 0.3 + (tx - x - w * 0.3) * k}" cy="{y + h + (ty - y - h) * k}" r="{7 - k * 3}" fill="#ffffff" stroke="{LINE}" stroke-width="1.5"/>'
        for k in (0.35, 0.7))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="#ffffff" stroke="{LINE}" stroke-width="1.8" stroke-dasharray="6 5"/>' + trail


def keyboard(x, y, w=120, h=40):
    keys = "".join(
        f'<rect x="{x + 8 + c * ((w - 16) / 10)}" y="{y + 7 + r * 9}" width="{(w - 16) / 10 - 3:.1f}" height="6" rx="1.5" fill="{LINE}"/>'
        for r in range(3) for c in range(10))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#f1f5f9" stroke="{MUTED}" stroke-width="1.8"/>' + keys)


def mini_ai(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy}" r="17" fill="{AI}"/>'
            + text(cx, cy + 5, "AI", 13, "#ffffff", 700, "middle"))


def decision(x, y, old, new):
    return (text(x, y, "✗ " + old, 12, MUTED, 400)
            + f'<line x1="{x + 14}" y1="{y - 4}" x2="{x + 14 + len(old) * 6.3:.0f}" y2="{y - 4}" stroke="{MUTED}" stroke-width="1.2"/>'
            + text(x, y + 22, "✓ " + new, 14, CODE, 700))


def gate(x, y, w, h, items):
    rows = "".join(text(x + 12, y + 44 + i * 20, "✓ " + s, 12, CODE, 700) for i, s in enumerate(items))
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{CODE_TINT}" stroke="{CODE}" stroke-width="2"/>'
            + text(x + w / 2, y + 22, "checks", 12, CODE, 700, "middle") + rows)


panels = {}

# 1 — human writes everything
panels[1] = frame(1, "Nothing added", "The developer types every line of code themselves.",
    person(140, 290, DEV, "Developer")
    + keyboard(196, 300)
    + arrow("M326,320 H420", DEV, "ah-dev", 3)
    + text(372, 306, "types code", 13, DEV, 600, "middle")
    + repo(440, 140, 320, 300)
    + code_grid(480, 190, 4, 3)
)

# 2 — context lives in the dev's head, re-sent every prompt
panels[2] = frame(2, "The developer prompts an AI",
    "The project knowledge lives in the developer's head and is re-typed every time.",
    cloud(36, 126, 260, 120, (110, 290))
    + text(56, 150, "in the developer's head", 12, MUTED, 700)
    + chips_row(56, 162, ["React", "tests in /spec"], DOC, DOC_TINT)
    + chips_row(56, 196, ["don't touch /legacy"], DOC, DOC_TINT)
    + person(110, 350, DEV, "Developer")
    + arrow("M155,340 H335", DEV, "ah-dev", 3)
    + text(245, 314, "prompt + all of that", 13, DEV, 600, "middle")
    + text(245, 332, "↻ again, every session", 12, MUTED, 400, "middle", italic=True)
    + ai(390, 340, "AI", "starts empty each session")
    + arrow("M430,340 H525", AI, "ah-ai", 3)
    + repo(540, 150, 225, 290)
    + code_grid(570, 200, 3, 3)
)

# 3 — context moves into the repo
panels[3] = frame(3, "AI context in the project",
    "The knowledge and the tests move into the repo. The AI reads and runs them, every session.",
    person(100, 320, DEV, "Developer")
    + bubble(40, 150, "“Add a login page.”", DEV)
    + f'<path d="M100,180 L100,262" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="3 4"/>'
    + arrow("M145,310 H320", DEV, "ah-dev", 3)
    + text(232, 296, "short prompt", 13, DEV, 600, "middle")
    + ai(375, 310, "AI")
    + arrow("M415,292 C460,292 470,215 505,215", AI, "ah-ai", 3)
    + arrow("M520,375 C470,375 455,335 418,330", DOC, "ah-doc", 3)
    + text(468, 400, "reads", 12, DOC, 600, "middle")
    + repo(510, 135, 255, 310)
    + code_grid(535, 172, 4, 1, dx=56)
    + chips_row(535, 222, ["✓ unit + function tests"], CODE, CODE_TINT)
    + arrow("M410,300 C455,285 470,236 528,234", CODE, "ah-code", 2.5)
    + text(452, 262, "runs tests", 12, CODE, 600, "middle")
    + f'<line x1="525" y1="258" x2="750" y2="250" stroke="#e2e8f0" stroke-width="1.5"/>'
    + text(526, 274, "AI context", 12, DOC, 700)
    + chips_row(526, 286, ["CLAUDE.md", "cards/"], DOC, DOC_TINT, mono=True)
    + chips_row(526, 320, ["project-plan.md"], DOC, DOC_TINT, mono=True)
    + chips_row(526, 354, ["React", "tests in /spec"], DOC, DOC_TINT)
    + chips_row(526, 388, ["don't touch /legacy"], DOC, DOC_TINT)
)

# 4 — architecture chosen to suit how AI works
panels[4] = frame(4, "Architecture chosen for AI",
    "The developer actively picks designs that suit how an AI works.",
    person(64, 300, DEV, "Developer")
    + arrow("M100,290 H134", DEV, "ah-dev", 3)
    # decision board
    + f'<rect x="140" y="124" width="320" height="330" rx="12" fill="#ffffff" stroke="{DEV}" stroke-width="2"/>'
    + text(158, 152, "architecture decisions", 13, DEV, 700)
    + decision(158, 190, "one big shared module", "small features with clear hooks")
    + decision(158, 258, "rules written in docs", "rules enforced by hooks")
    + decision(158, 326, "conventions in people's heads", "explicit contract per feature")
    + decision(158, 394, "no quality measurement", "code quality measured")
    + arrow("M462,290 H492", DEV, "ah-dev", 3)
    # resulting repository inside guardrails
    + f'<rect x="498" y="124" width="282" height="330" rx="16" fill="none" stroke="{GUARD}" stroke-width="2.5" stroke-dasharray="9 6"/>'
    + f'<rect x="620" y="114" width="150" height="22" fill="#ffffff"/>'
    + padlock(626, 112)
    + text(652, 130, "enforced rules", 12, GUARD, 700)
    + repo(512, 140, 254, 300)
    + text(528, 198, "signup", 12, CODE, 700)
    + pipeline(584, 180, [("in", "code"), ("hook", "slot"), ("out", "code")], w=48, gap=12)
    + text(528, 248, "login", 12, CODE, 700)
    + pipeline(584, 230, [("in", "code"), ("hook", "slot"), ("out", "code")], w=48, gap=12)
    + text(528, 298, "billing", 12, CODE, 700)
    + pipeline(584, 280, [("in", "code"), ("+ new", "new"), ("out", "code")], w=48, gap=12)
    + mini_ai(668, 346)
    + arrow("M668,328 V318", AI, "ah-ai", 2.5)
    + text(690, 351, "plugs in", 11, AI, 600)
    + chips_row(528, 372, ["contracts", "fast tests", "quality checks"], CODE, CODE_TINT)
    + chips_row(528, 404, ["CLAUDE.md", "cards/"], DOC, DOC_TINT, mono=True)
)

# 5 — fully set up and safe, so stakeholders can drive
panels[5] = frame(5, "Safe enough for stakeholders to drive",
    "Fully set up and guarded, so stakeholders can drive features themselves.",
    # stakeholder lane, through the checks gate
    person(70, 200, STAKE, "Stakeholder")
    + bubble(22, 118, "“Dark mode, please.”", STAKE)
    + arrow("M108,190 H172", STAKE, "ah-stake", 3)
    + ai(222, 190)
    + arrow("M258,190 H394", AI, "ah-ai", 3)
    + text(326, 178, "change", 12, STAKE, 700, "middle")
    # guardrail fence around everything
    + f'<rect x="432" y="122" width="352" height="342" rx="18" fill="none" stroke="{GUARD}" stroke-width="2.5" stroke-dasharray="9 6"/>'
    + f'<rect x="572" y="112" width="200" height="22" fill="#ffffff"/>'
    + padlock(578, 110)
    + text(604, 128, "guarded on every side", 12, GUARD, 700)
    + gate(398, 140, 78, 108, ["tests", "hooks", "review"])
    + arrow("M478,190 H496", CODE, "ah", 2.5)
    + repo(500, 136, 272, 316)
    + text(516, 178, "features", 12, CODE, 700)
    + pipeline(516, 188, [("signup", "code"), ("login", "code"), ("search", "code")], w=72, gap=12)
    + pipeline(516, 230, [("export", "code"), ("billing", "code"), ("dark mode", "new")], w=72, gap=12)
    + f'<rect x="508" y="282" width="256" height="162" rx="10" fill="{DOC_TINT}" fill-opacity="0.45"/>'
    + text(522, 304, "foundation", 12, DOC, 700)
    + chips_row(522, 314, ["context: CLAUDE.md, cards"], DOC, DOC_TINT)
    + chips_row(522, 346, ["guardrails: hooks, permissions"], GUARD, "#ffedd5")
    + chips_row(522, 378, ["tests & checks", "skills"], CODE, CODE_TINT)
    + text(522, 428, "keeps it safe", 11, DOC, 600, italic=True)
    # developer lane, maintaining the foundation
    + person(70, 390, DEV, "Developer")
    + arrow("M108,380 H172", DEV, "ah-dev", 3)
    + ai(222, 380)
    + arrow("M258,380 H504", AI, "ah-ai", 3)
    + text(330, 368, "upkeep", 12, DEV, 700, "middle")
)

for n, svg in panels.items():
    with open(os.path.join(OUT, f"phase-{n}.svg"), "w") as fh:
        fh.write(svg)
print("ok")

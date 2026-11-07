# Assessment: "The Five Phases of AI Adoption in a Project" — round 2

Reviewed: `blog-post.md` (the source) and the generated `blog-post.html` with the concept-2 illustrations, 2026-10-31.
Length: about 1,400 words of body text (6 min read), five illustrations, one table, nine external links.
Mechanical checks: `make check` passes (every image and local link resolves; the agent-docs checker reports 0 errors and 0 warnings).

## Verdict

Ready to publish. The round-1 problems are fixed. The text and pictures now say the same thing, and phases 4 and 5 read as an honest forecast rather than a report. The setup page is offered as one example. What's left is polish: some stacked hedging in phase 5, one sentence in phase 3 that tries to do two jobs, and the number of links to your own site.

## Round 1: status

| # | Issue | Status |
|---|---|---|
| 1–2 | Phase 4's text and image listed different things, and the text contradicted itself | Fixed. The bullets now mirror the whiteboard, and "AI becomes the tie-breaker" removes the contradiction. |
| 3 | Phase 5 didn't say who does the reviewing | Fixed. A second AI reviews each change, with humans stepping in only on a flag. |
| 4 | "Not yet seen" said three times | Fixed. The intro says it once; phases 4 and 5 hedge in their own words. |
| 5 | Headings didn't match the image titles | Fixed. They now match exactly. |
| 6 | Intro overclaimed | Mostly fixed. See new issue 3. |
| 7 | Claude-specific terms never acknowledged | Fixed. Phase 3 now names them as Claude Code's. |
| 8 | Nothing on cost or risk | Fixed ("None of this is free…"). |
| 9 | Markdown and HTML had drifted apart | Fixed for good. The HTML is now generated from the markdown. |
| 10 | Phase 4 image drew the AI twice | Fixed by regenerating it. Image weight is still open (see new issue 6). |
| — | Line edits | All applied. |

## What works now

- **The forecast is credible.** The intro sets the frame: most teams are in phase 2, some in 3, and 4–5 are where things are heading. Phase 4 then opens with "read this as suggestions rather than a report", and phase 5 with "this is my guess at what it takes". Readers always know which parts are observation and which are opinion.
- **Phase 4 is actionable advice.** Each bullet starts with a verb (*Prefer*, *Enforce*, *Give*, *Invest in*), names what it replaces, and links to a pattern. It reads like a checklist someone could try.
- **Phase 5 has a mechanism.** The AI-reviewer paragraph answers the obvious objection ("isn't the developer still the bottleneck?") before the reader raises it.
- **The setup page reads as an offer, not a pitch.** "It's one way to do it, not the way… take what fits your project and change the rest", and the button now says "Have a look at the setup page →".
- **Every picture matches its text.** The phase 4 whiteboard lists the same four trades as the bullets, and the phase 5 checks gate matches the review paragraph.

## Remaining issues, most important first

### 1. Phase 5 hedges twice in a row

Line 80 says "this is my guess at what it takes. **I think** it only works once…". One hedge is enough. Cut "I think", so the sentence reads "My guess at what it takes: it only works once the project is…". Phase 5 also says "would" six times across four paragraphs. That's grammatically right but gets heavy. Once the conditional frame is set, the developer's upkeep list and the closing line can return to plain present tense without overclaiming.

### 2. Many links to your own site for a post that's meant to be modest

Eight of the nine links go to ai.memention.net:
- four in the phase 3 list
- the phase 3 callout
- three in phase 4
- "Getting started", which links to the setup page again

The setup page and its checker are introduced twice, in the callout and in "Getting started". Each link is useful on its own, but together they work against the humbler tone.

*Suggestion:* drop the phase 3 callout and keep the checker mention in "Getting started". Or keep the callout and cut "and a small read-only checker" from "Getting started".

### 3. The intro's list misses phase 4

"Each one changes what the AI knows, who drives the changes, and what the developer spends their day on." Phase 4 changes how the code is shaped, which isn't on that list.

*Suggestion:* "…what the AI knows, how the code is shaped, who drives the changes, and what the developer spends their day on."

### 4. Phase 3's list intro does two jobs in one sentence

"In my own projects this means files like these. It's one way to do it, and the names are Claude Code's; other agents read `AGENTS.md` and similar files:"

*Suggestion:* split it. "In my own projects that means files like these (one way to do it):" Then put the naming note after the list, e.g. "The names are Claude Code's; other agents use `AGENTS.md` and similar files."

### 5. The closing section speaks with more certainty than phases 4–5 do

Line 108, "Stakeholder-driven work only holds up on top of the context and guardrails that come before it", and line 110, "the guardrails have to be treated like security controls", state as fact what phase 5 presents as a guess.

*Suggestion:* "I'd expect stakeholder-driven work to hold up only on top of…" and "…would have to be treated like security controls…".

### 6. Not editorial, but needed before publishing

- **Images are about 7.5 MB in total** (about 1.5 MB each). Converting to WebP would bring that to about 1 MB. This is plan item M8, which waits on where the post will be published.
- **The date in the frontmatter** is 2026-10-30. Set it to the real publish date (plan item M10).
- **The titles drawn inside the images** state things plainly (phase 4: "The developer actively picks designs that suit how an AI works"), while the text now hedges. That's fine for a caption, but if the mismatch bothers you, a regeneration could change the subtitles to e.g. "Choosing designs that suit how an AI works".
- **The heading font on the HTML page** (Bangers, comic style) is louder than the soft illustrations. Whether to keep it is still an open question in the plan.

## Smaller line edits

- **Line 15:** "few dare to go there yet" implies teams are timid; "few have tried it yet" is more neutral and fits the humbler tone.
- **Line 33:** "the agent makes it". The post uses "AI" 15 times and "agent" 22 times for the same thing. That's fine, but it helps to tie them together once, in phase 2: "an AI agent".
- **Line 63:** "the pieces exist today" is a good, concrete hedge; keep it.
- **Line 92:** "In short, the developer would stop being the bottleneck…" still lands well as the section's last line.
- **Line 114:** "the patterns, files and skills I use myself" followed by "It's one way to do it, not the way" works. Don't add more hedging there.

## Suggested next steps

1. Apply issues 1, 3, 4 and 5. They're small text edits, about ten minutes.
2. Decide on issue 2: keep the callout or the checker mention, not both.
3. Then the plan's M8 to M10: WebP, final proofread and merge, publish. These need the answer to where the post will be published.

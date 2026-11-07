# Assessment: "The Five Phases of AI Adoption in a Project" — round 3

Reviewed: `blog-post.md` (the source) and the generated `blog-post.html` with the concept-2 illustrations, 2026-11-07, at commit 489b766.
Length: about 1,630 words of body text (7 min read), five illustrations, one table, nine links in the body.
Mechanical checks: `make check` passes (every image and local link resolves; the agent-docs checker reports 0 errors and 0 warnings).

## Verdict

Still ready to publish, and the model is stronger. Tests in phase 3, quality measurement in phase 4 and a validated setup before phase 5 turn the phases into a ladder: each one builds the safety the next one needs. The orchestration paragraph gives phase 3 a forward-looking reason to exist beyond "shorter prompts".

The cost is that phase 3 has grown to about 435 words, more than phases 4 and 5 (about 300 each). Its paragraphs are also in a slightly odd order. Fixing that order is the main edit left.

## Round 2: status

| # | Issue | Status |
|---|---|---|
| 1 | Phase 5 hedged twice | Fixed. A new two-colon sentence came in with the "validated" wording, though (see issue 3). |
| 2 | Setup checker introduced twice | Fixed. The callout stays, and "Getting started" no longer mentions the checker. |
| 3 | Intro list missed phase 4 | Fixed ("how the code is shaped"). |
| 4 | Phase 3 list intro did two jobs | Fixed. |
| 5 | Closing more certain than phases 4–5 | Fixed. |
| 6 | Images, date, drawn titles, heading font | Still open. See issue 6. |
| — | Line edits | All applied. |

## What works now

- **The phases form a ladder.** Each phase now gives the next one a precondition: tests (3) → quality measured (4) → a setup you've seen hold (5). Phase 5's "every change passes the tests and quality checks from the earlier phases" ties the three together explicitly.
- **"Context tells the agent what to do; tests tell it whether it did."** This is the best line in the post. It's short and quotable, and it explains why tests belong in phase 3.
- **Orchestration is a real argument for phase 3.** "None of them can borrow the context from your head" is concrete. The note about merging is precise: decisions reach the other agents when the branch is merged, not instantly.
- **The table now has distinct signals for 3 and 4** ("runs the tests itself", "code quality is measured"). Readers can place themselves more easily.
- **The images match the text again.** The phase 3 image has a "✓ unit + function tests" chip and a "runs tests" arrow. The phase 4 whiteboard ends in "code quality measured". Phase 5's gate ("tests, hooks, review") and its foundation ("tests & checks") already fit.

## Remaining issues, most important first

### 1. Phase 3's paragraphs are out of order

The current order is:
1. the context list
2. the naming note
3. **tests**
4. "The application code itself hasn't changed yet. What changed is that the agent now starts every session already knowing the project."
5. orchestration
6. the callout

Paragraph 4 sums up the *context* change. Because the tests paragraph sits in front of it, "what changed" seems to refer to the tests. "The application code itself hasn't changed" also reads oddly right after a paragraph about adding test code.

*Suggestion:* list → naming note → "The application code hasn't changed yet…" → tests → orchestration → callout. The section then goes: context → its payoff → tests → scaling to many agents → try it.

### 2. Tests aren't new in phase 3; the agent running them is

Many phase 1 and phase 2 projects already have unit tests. "Tests belong in this phase too" can read as if phase 3 is where tests first appear, which experienced readers will push back on. The table already gets the nuance right ("the agent … runs the tests itself").

*Suggestion:* "Tests belong in this phase too, whether they're new or already there. Once the commands to run them are in the context docs, the agent checks that its change works before you look at it. Context tells the agent what to do; tests tell it whether it did."

### 3. Phase 5's opening sentence has two colons and runs to 60 words

"…this is my guess at what it takes: it only works once the project is **fully set up and safe**, and you've seen that setup hold: the context is complete, …"

*Suggestion:* split it. "It's the furthest out, so this is my guess at what it takes. It only works once the project is **fully set up and safe**, and you've seen that setup hold: the context is complete, the rules are enforced…"

### 4. Phase 3 is now the longest section

At about 435 words, phase 3 is close to half as long again as phases 4 or 5, and the callout adds to it. Once the order is fixed (issue 1), the length is defensible, because phase 3 is where most readers can act today. If you want to trim, the orchestration paragraph's last sentence ("In phase 2, every extra agent means another long prompt; in phase 3, it's a short one.") repeats the earlier "Prompts get shorter" and could go.

### 5. Quality measurement sits under "Architecture chosen for AI"

Measuring complexity and coverage isn't strictly an architecture decision. The bullet still fits, because the thresholds become checks that keep the architecture intact, and the whiteboard presents it as one of the decisions. A reader might still trip on the heading.

*Suggestion (optional):* widen the phase 4 intro by a few words: "…**the developer to start choosing the architecture for it**, and measuring whether it holds."

### 6. Still open from round 2 (not editorial)

- **Images are about 7.6 MB in total.** M8 (WebP) waits on where the post will be published.
- **The frontmatter date** is still 2026-10-30. Set it when you publish (M10).
- **The titles drawn inside the images** state things plainly while the text hedges. This still seems fine to me.
- **The Bangers heading font** is still an open question in the plan.

## Smaller line edits

- **Phase 4 alt text:** "…and, instead of “no quality measurement”, “code quality measured”" reads awkwardly. Try "…“explicit contract per feature” and “code quality measured” (replacing “no quality measurement”)".
- **Phase 3 image:** the "runs tests" label sits closer to the purple code arrow than to its own green arrow. The colour carries it. Not worth credits unless you're regenerating anyway.
- **Intro (optional):** "Each one changes what the AI knows, how the code is shaped, who drives the changes…" could add "how changes get checked", now that checks run through phases 3–5. It might also make the sentence too long; your call.
- **"Getting started"** lists what the setup page covers. It correctly doesn't claim to cover quality measurement, which the setup page doesn't have. Leave it as it is.

## Suggested next steps

1. Apply issues 1–3 and the alt-text fix. These are text-only edits, about five minutes.
2. Decide on issues 4 and 5, both optional.
3. Then the plan's M8–M10: WebP, final proofread and merge, publish.

# Assessment: "The Five Phases of AI Adoption in a Project"

Reviewed: `blog-post.md` and `blog-post.html` with the concept-2 illustrations, 2026-10-31.
Length: about 1,200 words of body text (5 min read), five illustrations, one table.

## Verdict

The post is ready to publish after a short editing pass. The model is simple and memorable, the framing is honest, and it ends in something readers can do today. The main weaknesses are in phase 4, whose text and image make two different lists, and in phase 5, which leaves open who reviews stakeholder changes. Both are fixable in a few sentences.

## What works

- **One clear idea per phase.** Each phase changes one thing: who writes the code, then where the knowledge lives, then how the code is shaped, then who drives features. The illustrations reinforce this. The same repository box appears in every one, so the reader sees it change.
- **Honest framing.** Saying that most teams are in phase 2, and that phases 4 and 5 are where you think this is heading rather than something you've seen, makes the post credible. It also keeps it from reading like a sales pitch.
- **Concrete artifacts.** Phases 3 and 4 name real files and patterns (`CLAUDE.md`, cards, `project-plan.md`, hooks, skills), so readers know what "doing phase 3" actually means.
- **The self-placement table** is the most shareable part of the post. Each signal is a single checkable sentence.
- **The call to action is actionable and low-risk.** "Tell your agent: `Follow https://ai.memention.net/setup`" is a one-liner, and the post says the setup asks before applying anything.
- **The facts check out.** Every claim about the setup page matches its source (`../ai-setup/site/setup`): lazy-loaded cards, the plan file every agent reads and updates, the Python venv default, splitting into `CLAUDE_full.md` when a file gets too long, hooks over prose, project-scoped skills, the read-only checker, and re-running to refresh. Every card link points to a file that exists.

## Issues, most important first

### 1. Phase 4: the text and the image list different things

The image's decision board lists four trades: small features with hooks, rules enforced by hooks, an explicit contract per feature, and fast tests. The text lists five bullets, and two of them aren't architecture decisions:
- **Project-scoped skills** are tooling.
- **Per-feature `CLAUDE.md`** is documentation, and really a continuation of phase 3.

*Suggestion:* make the bullets mirror the board. That means feature-first with hooks, hooks over prose, a contract per feature (which is where per-feature `CLAUDE.md` belongs), and fast tests. Move skills to phase 3 or to a closing "tooling" note.

### 2. Phase 4 contradicts itself slightly

It says the AI-friendly option wins "even if it's not the one you'd have picked for a human-only team". Two paragraphs later it says these choices "help human developers too". Readers will notice.

*Suggestion:* make the tension the point. For example: "Most of these choices are good for humans too. What changes is that AI becomes the tie-breaker."

### 3. Phase 5: who reviews?

The checks gate includes "review", and the text says every change passes "tests and review". If the developer reviews every stakeholder change, the developer is still the feature bottleneck, which undercuts the phase's main claim.

*Suggestion:* add one sentence saying what review means at this stage. For example: automated checks plus a lightweight human sign-off, or stakeholders owning acceptance while developers audit samples and the guardrails themselves.

### 4. "Yet" repeated three times

- The intro says "few dare to go there yet".
- Phase 4 says "I haven't seen a team fully here yet".
- Phase 5 says "Few projects have earned that level of trust yet".

The intro already sets the expectation. Cut one of the later two; I'd keep the phase 5 line because it's about trust, which is new information.

### 5. The section headings don't match the images

The text headings and the titles drawn in the images say different things:

| Phase | Text heading | Image title |
|---|---|---|
| 3 | "AI context engineering is scaffolded into the project" | "AI context in the project" |
| 4 | "The project is architected for agentic tools" | "Architecture chosen for AI" |
| 5 | "The developer stops adding features" | "Safe enough for stakeholders to drive" |

The image titles are shorter and closer to what each phase means. Adopting them, or a blend, would make the post easier to skim. For phase 5 you could keep both ideas: "Safe enough that the developer stops adding features".

### 6. Intro overclaims slightly

"Each one changes who touches the code, what touches it, and what the developer spends their day on." Phase 3 doesn't change who or what touches the code; it changes what the AI knows.

*Suggestion:* "Each one changes what the AI knows, who drives the changes, and what the developer spends their day on."

### 7. Claude-specific terms in a tool-neutral post

The post says "AI" and "agent" throughout, but its examples are Claude Code paths (`CLAUDE.md`, `.claude/settings.json`, `.claude/skills/`). That's fine, but say so once, for example: "Examples use Claude Code; `AGENTS.md` plays the same role for other agents."

### 8. Nothing on cost or risk

Phases 4 and 5 are presented as pure upside. Two or three sentences on the trade-offs would add credibility:
- the time spent on setup and keeping the context up to date
- token cost
- the security side of letting non-developers trigger changes

### 9. The markdown and HTML versions have drifted

- The phase 3 heading differs: the HTML says "AI context is scaffolded", the markdown says "AI context engineering is scaffolded".
- The HTML has a "Try it on your repo" callout in phase 3 that the markdown lacks.
- The markdown has a line, "Here they are, with an illustration for each.", that the HTML lacks.

Pick one version as the source of truth, ideally the markdown, and regenerate the other from it.

### 10. Illustrations

- **Phase 4:** the AI is drawn twice, as a robot head on the "+ new" block and as a purple "AI" drop below it. Most readers won't notice, but a regeneration or a small edit would clean it up.
- **Phase 5:** the stakeholder wears glasses here but not in other versions. This only matters if you reuse the characters elsewhere.
- **Duplicated titles:** each image carries its own title and subtitle, which repeat the section heading. That works for sharing a single image on social media. In the post it's a little redundant but acceptable.
- **Weight:** the five images are about 1.5 MB each, around 7.5 MB in total. Converting them to WebP (about 200 KB each) would make the page load much faster.

## Smaller line edits

- **Line 13:** "Here they are, with an illustration for each." adds nothing; cut it.
- **Line 31:** "between the developer's hands and the code" is nice, but "hands" now clashes slightly with phase 1's "types every line". Consider "between the developer and the code".
- **Line 41:** "The obvious fix" → "The natural fix". It's only obvious in hindsight, and most teams haven't done it.
- **Line 58:** "From here on, we're looking ahead." This is good signposting. Keep it, and remove the "yet" sentence that follows it (see issue 4).
- **Line 78:** "They move to the other lane." This only makes sense with the image. Add "(the lower one in the picture)", or rephrase as "They move from building features to tending the system that builds them."
- **Line 86:** "steward of the system that produces them" is a strong closing line for the section; keep it.
- **Line 102:** the paragraph repeats "phase" six times. Tighten it.
- **Line 106:** "If you want to move a project from phase 2 to phase 3 or 4" is accurate. Consider also saying it helps teams already in phase 3, because its refresh mode updates an existing setup.

## Suggested next steps

1. Make phase 4's bullets match the board in the image (issues 1 and 2).
2. Add one sentence on who reviews in phase 5 (issue 3).
3. Cut the repeated "yet" sentence and align the headings with the image titles (issues 4 and 5).
4. Treat the markdown as the source, regenerate the HTML from it, and convert the images to WebP (issues 9 and 10).

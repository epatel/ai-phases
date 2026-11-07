# setup-site-links

Facts about ai.memention.net, which the post links to as its call to action. Present it humbly: the author's own setup, one example or starting point to adapt, not the way to do it.

- `https://ai.memention.net/setup` is a page written for a coding agent, not for people: the reader tells their agent `Follow https://ai.memention.net/setup` and the agent assesses the repo, recommends patterns, and asks before applying anything. Re-running it refreshes an existing setup.
- Pattern cards live at `https://ai.memention.net/cards/<file>`: `cards-instructions.md` (context cards), `project-plan.md`, `standing-defaults.md`, `feature-first-structured.md`, `two-tier-claude-md.md`, `hooks-over-prose.md`, `known-stack.md`, `feature-first-advanced.md`, `check-agent-docs.py`, `setup-changelog.md`.
- There is **no** page at `https://ai.memention.net/` or `https://ai.memention.net/cards/` — never link those.
- Skills referenced by the site: `https://github.com/epatel/agent-skills/` and `https://github.com/anthropics/skills`.

## When the site is unreachable

The site has had routing problems. The source is checked out locally at `../ai-setup/site/` (`setup` and `cards/`). Verify claims and link targets there: a card URL is valid if `../ai-setup/site/cards/<file>` exists.

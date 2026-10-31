---
title: "The Five Phases of AI Adoption in a Project"
date: 2026-10-30
author: Edward Patel
---

# The Five Phases of AI Adoption in a Project

Most teams don't decide to "adopt AI" in one go. It happens gradually, and the project itself changes along the way. I think of it as five phases. Each one changes who touches the code, what touches it, and what the developer spends their day on.

From what I see, most teams are in phase 2 today. Some have reached phase 3. Phases 4 and 5 I have yet to see in practice; few dare to go there yet. So read the first three as a map of where teams are now, and the last two as where I think this is heading.

Here they are, with an illustration for each.

---

## Phase 1: Nothing added

![The developer types every line at a keyboard; an arrow labelled “types code” leads into a repository that holds only code files.](images/concept-2/phase-1.png)

This is where every project starts. The developer types every line of code themselves. Maybe there's autocomplete in the editor, but nothing in the project knows or cares that AI exists. The repository holds source code and nothing else.

There's nothing wrong with this phase. It's just the baseline.

---

## Phase 2: The developer writes prompts that edit the project

![A thought cloud “in the developer's head” holds React, tests in /spec and don't touch /legacy. The developer sends “prompt + all of that, again every session” to an AI that starts empty each session.](images/concept-2/phase-2.png)

Now an AI sits between the developer's hands and the code. The developer describes a change, the agent makes it, and the developer reviews the result.

The catch is that **all the context lives in the developer's head** and has to be typed again in every prompt. Each session starts from zero: "We use this framework, tests are run like this, don't touch that folder…" It works, but it doesn't scale, and the quality of the output depends on how well the developer remembers to explain things that day.

---

## Phase 3: AI context engineering is scaffolded into the project

![The developer gives a short prompt, “Add a login page.” The AI reads the AI context stored inside the repository (CLAUDE.md, cards/, project-plan.md and the project facts) and then edits the code.](images/concept-2/phase-3.png)

The obvious fix for phase 2 is to write the context down *in the project*. The repository now holds a small set of documents written for the agent, not for humans: what the project is, how to build and test it, conventions, and the things that are easy to get wrong.

In practice this means files like:

- **`CLAUDE.md` / `AGENTS.md`**: the project overview, the commands, and an index of where to find more.
- **Context cards** (`cards/`): small, lazy-loaded notes the agent reads only when the situation calls for them, so the main file stays short.
- **`project-plan.md`**: one shared file with the goal, non-goals, milestones, decisions and current state, which every agent session reads and updates.
- **Standing defaults**: decisions made once (e.g. "always use a Python venv") so they aren't debated again in every session.

The code hasn't changed yet. What changed is that the agent now starts every session already knowing the project. Prompts get shorter, and the results get more consistent.

---

## Phase 4: The project is architected for agentic tools

![The developer works through a board of architecture decisions, crossing out options like “one big shared module” in favour of “small features with clear hooks”, “rules enforced by hooks”, “explicit contract per feature” and “fast tests the AI can run”. The resulting repository has features with open hook slots, sits inside enforced rules, and the AI plugs a new step into one slot.](images/concept-2/phase-4.png)

From here on, we're looking ahead. I haven't seen a team fully here yet, but the pieces exist today. In phase 3 the documentation adapted to the agent. In phase 4 **the developer starts choosing the architecture for it**. Whenever there's a design decision to make, the option that suits how an AI works wins, even if it's not the one you'd have picked for a human-only team.

Each of these is a deliberate trade, made because it lets an agent read and change the code safely:

- **Feature-first architecture**: features are documented as pipelines of named steps with clear hook points, so an agent can add behaviour without having to understand the whole system.
- **Per-feature `CLAUDE.md` files**, split into a short overview and a full contract (`CLAUDE_full.md`) once they grow too long.
- **Hooks over prose**: mechanical "always/never" rules move out of the documentation and into `.claude/settings.json` permissions and hooks. The harness enforces them, so the agent doesn't have to remember them.
- **Project-scoped skills** in `.claude/skills/`: repeatable workflows (refactoring, reviews, releases) checked into the repo, so every collaborator and worktree gets them.
- **Fast tests the AI can run**: a quick, reliable test suite is how an agent checks its own work before you ever look at it.

The guiding idea is that a well-structured project gives an agent less room to make mistakes. Clear boundaries, enforced rules and documented extension points help human developers too.

---

## Phase 5: The developer stops adding features

![The repository is fenced in on every side. The stakeholder asks “Dark mode, please.” and their AI's change must pass a checks gate (tests, hooks, review) before it reaches the features layer. The developer's AI does upkeep on the foundation of context, guardrails, tests and skills that keeps it safe.](images/concept-2/phase-5.png)

This is the phase that changes the role, and the one that takes the most nerve. It only works once the project is **fully set up and safe**: the context is complete, the rules are enforced by hooks and permissions, and every change passes tests and review on its way in. When a project is guarded that well, **the people who want features can drive them directly**. A stakeholder works with their own AI session against the same project, inside the same guardrails, and features come out the other end. Few projects have earned that level of trust yet.

The developer doesn't disappear. They move to the other lane. Their AI now points at the **AI layer and the project's health**:

- keeping the context documents and cards accurate as the code changes,
- tightening hooks and permissions when an agent does something it shouldn't,
- refactoring where the structure has started to drift,
- improving the tests and checks that let stakeholder-driven changes land safely,
- reviewing and auditing the agentic setup itself.

In short, the developer stops being the bottleneck for features and becomes the steward of the system that produces them.

---

## Where is your project?

A quick way to place a project:

| Phase | Signal |
|---|---|
| 1 | No AI tooling touches the repo |
| 2 | You use an agent, but you explain the project again in every prompt |
| 3 | There's a `CLAUDE.md`/`AGENTS.md` and the agent "knows" the project |
| 4 | Architecture decisions are made with the agent in mind |
| 5 | The project is safe enough that non-developers ship features; developers mostly work on its health |

You don't have to rush through them, and different parts of a codebase can be in different phases. If you're in phase 2, you're in good company: that's where most teams are. Phase 3 is the step almost any team can take today, and each step makes the next one possible. Phase 5 doesn't work without the context of phase 3 and the guardrails of phase 4.

## Getting started

If you want to move a project from phase 2 to phase 3 or 4, I've collected the patterns, files and skills I use at **[ai.memention.net/setup](https://ai.memention.net/setup)**. It covers context cards, the shared project plan, standing defaults, feature-first documentation, hooks over prose, project-scoped skills, and a read-only checker you can run against your repo to see where it stands.

The page is written for your agent, not for you. Open your coding agent in the project and tell it: `Follow https://ai.memention.net/setup`. It assesses the repo, recommends which patterns fit, and asks before applying anything. Run it again later to pick up what's new.

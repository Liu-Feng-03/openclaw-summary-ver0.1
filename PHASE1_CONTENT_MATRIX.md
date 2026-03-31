# PHASE1_CONTENT_MATRIX.md — openclaw-summary

Last updated: 2026-03-31
Status: Phase 1 design deliverable

---

## 1. Purpose

This file defines the **Phase 1 content architecture** for `openclaw-summary`.

Its job is to convert the roadmap into a page-by-page content plan that a new implementation process can use directly.

Phase 1 focuses on:
- what pages exist
- what each page must teach
- who each page is for
- how deep each page should go
- which pages should be built first

This is still a **product/content planning artifact**, not implementation work.

---

## 2. Content Depth Levels

To avoid content becoming either too shallow or too overwhelming, use these depth labels:

### L1 — Orientation
Very short, confidence-building, used for first contact.

### L2 — Practical Understanding
Enough to help a user make progress or understand usage.

### L3 — System Understanding
Explains relationships, architecture, tradeoffs, and mental models.

### L4 — Advanced Practice
For experienced users who want best practices, edge cases, and deeper operating knowledge.

---

## 3. Priority Levels

### P0 — Must exist first
These pages define the product skeleton and first usable experience.

### P1 — Should follow immediately
These pages make the site genuinely useful.

### P2 — Important expansion
These pages deepen completeness and sharing value.

### P3 — Polishing / later expansion
These pages are useful, but not blockers for the first meaningful version.

---

## 4. Module Overview

| Module | Goal | Primary audience |
|---|---|---|
| Home | Explain the product and route users | All users |
| Getting Started | Help absolute beginners enter smoothly | New users |
| Core Concepts | Build a correct mental model | New + intermediate users |
| Setup | Help users get OpenClaw running | New + practical users |
| Use Cases | Show why OpenClaw matters in practice | Curious + practical users |
| Advanced | Explain deeper mechanisms and best practices | Intermediate + advanced users |
| FAQ | Reduce frustration and unblock adoption | All users |

---

## 5. Page-by-Page Content Matrix

---

## 5.1 Home

### `/`
- Priority: P0
- Depth: L1 → L2
- Audience: all users
- Goal:
  - explain what the site is
  - explain why it exists
  - route users into beginner path / concept path / setup path / scenario path
- Must teach:
  - this is a Chinese interactive learning site for OpenClaw
  - OpenClaw has a learning path from basics to advanced
  - users can enter by sequence or by topic
- Must include:
  - hero section
  - learning path section
  - module entry cards
  - scenario entry cards
  - concept map preview
  - advanced topics preview
  - FAQ entry
- Exit paths:
  - getting started
  - concepts
  - setup
  - use cases

---

## 5.2 Getting Started

### `/getting-started`
- Priority: P0
- Depth: L1 → L2
- Audience: beginners
- Goal:
  - provide the recommended beginner route
- Must teach:
  - what order a newcomer should follow
  - what they need to know first vs later
- Must include:
  - beginner roadmap
  - estimated learning path
  - links to first 3–5 key pages

### `/getting-started/what-is-openclaw`
- Priority: P0
- Depth: L1 → L2
- Audience: absolute beginners
- Goal:
  - answer “what is OpenClaw?” clearly
- Must teach:
  - one-sentence definition
  - what problem it solves
  - what makes it different from a plain chat UI
- Must avoid:
  - too much architecture too early

### `/getting-started/how-to-learn`
- Priority: P1
- Depth: L1 → L2
- Audience: beginners
- Goal:
  - help users choose a learning route
- Must teach:
  - different reading strategies
  - if you only want setup, go here
  - if you want architecture, go here
  - if you want use cases, go here

### `/getting-started/first-roadmap`
- Priority: P1
- Depth: L2
- Audience: beginners
- Goal:
  - give a realistic “from zero to first success” journey
- Must teach:
  - what minimum success looks like
  - what knowledge is optional at first
  - what commonly confuses new users

---

## 5.3 Core Concepts

### `/concepts`
- Priority: P0
- Depth: L1 → L3
- Audience: beginner + intermediate
- Goal:
  - act as the gateway to the concept system
- Must teach:
  - OpenClaw is a system of related parts
  - understanding component relationships is important
- Must include:
  - concept map entry
  - concept cards
  - recommended reading order

### `/concepts/architecture`
- Priority: P0
- Depth: L2 → L3
- Audience: all serious learners
- Goal:
  - explain the overall architecture before isolated concepts
- Must teach:
  - the main building blocks
  - how requests/messages/actions move through the system
  - where gateway, session, skills, tools, memory, nodes fit

### `/concepts/agent`
- Priority: P1
- Depth: L2 → L3
- Audience: beginner + intermediate
- Goal:
  - explain what an agent is in OpenClaw context
- Must teach:
  - role, behavior, scope
  - relation to instructions, tools, skills, memory

### `/concepts/session`
- Priority: P0
- Depth: L2 → L3
- Audience: beginner + intermediate
- Goal:
  - explain session as a core operating concept
- Must teach:
  - what a session is
  - how context accumulates
  - why session boundaries matter
  - difference from simply “a chat window”

### `/concepts/gateway`
- Priority: P0
- Depth: L2 → L3
- Audience: beginner + intermediate
- Goal:
  - explain gateway as the main service layer users interact with operationally
- Must teach:
  - why gateway matters
  - what it handles
  - relation to dashboard/control UI and remote connectivity

### `/concepts/node`
- Priority: P1
- Depth: L2 → L3
- Audience: practical + intermediate users
- Goal:
  - explain node/device connectivity model
- Must teach:
  - where node fits
  - local vs remote usage intuition
  - common connection misunderstandings

### `/concepts/skills`
- Priority: P0
- Depth: L2 → L3
- Audience: beginners moving deeper
- Goal:
  - explain how skills guide behavior and tool use
- Must teach:
  - what skills are
  - when they are loaded
  - why they matter
  - how they differ from tools and model capabilities

### `/concepts/tools`
- Priority: P0
- Depth: L2 → L3
- Audience: beginners moving deeper
- Goal:
  - explain tools as executable actions/capabilities
- Must teach:
  - what tools do
  - how tools differ from skills
  - why some actions require tools

### `/concepts/memory`
- Priority: P0
- Depth: L2 → L3
- Audience: all users
- Goal:
  - explain short-term vs file-backed continuity
- Must teach:
  - what memory means in OpenClaw context
  - daily memory vs long-term memory intuition
  - security/privacy boundaries

### `/concepts/dashboard`
- Priority: P2
- Depth: L2
- Audience: practical users
- Goal:
  - explain dashboard / control UI role

### `/concepts/heartbeat-cron`
- Priority: P2
- Depth: L2 → L3
- Audience: users exploring automation
- Goal:
  - explain periodic checking vs scheduled tasks

### `/concepts/subagents`
- Priority: P2
- Depth: L3
- Audience: intermediate + advanced
- Goal:
  - explain when and why to use sub-agents

### `/concepts/acp`
- Priority: P2
- Depth: L3
- Audience: advanced / developer-oriented users
- Goal:
  - explain ACP harness role in coding/tooling workflows

---

## 5.4 Setup & Deployment

### `/setup`
- Priority: P0
- Depth: L1 → L2
- Audience: practical beginners
- Goal:
  - provide the setup journey overview
- Must teach:
  - setup has an order
  - users should verify success step by step

### `/setup/requirements`
- Priority: P0
- Depth: L2
- Audience: practical beginners
- Goal:
  - explain environment prerequisites

### `/setup/install`
- Priority: P0
- Depth: L2
- Audience: practical beginners
- Goal:
  - explain installation path clearly

### `/setup/configuration`
- Priority: P0
- Depth: L2 → L3
- Audience: practical beginners
- Goal:
  - explain the configuration layer without overwhelming the user
- Must teach:
  - what needs configuring first
  - what can wait
  - how config affects behavior

### `/setup/start-gateway`
- Priority: P0
- Depth: L2
- Audience: practical beginners
- Goal:
  - explain how to start and verify the gateway
- Must teach:
  - what “healthy startup” looks like
  - how to check status

### `/setup/first-message`
- Priority: P0
- Depth: L2
- Audience: practical beginners
- Goal:
  - walk user to first successful interaction

### `/setup/troubleshooting`
- Priority: P1
- Depth: L2 → L3
- Audience: practical beginners
- Goal:
  - catch the most common problems immediately after setup

---

## 5.5 Use Cases

### `/use-cases`
- Priority: P1
- Depth: L1 → L2
- Audience: all users
- Goal:
  - show the scenario landscape
  - route users by goal

### `/use-cases/personal-assistant`
- Priority: P1
- Depth: L2
- Audience: general users
- Goal:
  - explain OpenClaw as a personal assistant system

### `/use-cases/messaging-platforms`
- Priority: P1
- Depth: L2 → L3
- Audience: practical users
- Goal:
  - explain Telegram / Discord / Signal style integration idea

### `/use-cases/github-workflow`
- Priority: P2
- Depth: L2 → L3
- Audience: technical users
- Goal:
  - explain GitHub and development collaboration workflows

### `/use-cases/notes-reminders`
- Priority: P2
- Depth: L2
- Audience: productivity-focused users
- Goal:
  - show note/reminder workflows and their value

### `/use-cases/google-workspace`
- Priority: P2
- Depth: L2
- Audience: productivity-focused users
- Goal:
  - show Gmail/Calendar/Docs style integration value

### `/use-cases/heartbeat-automation`
- Priority: P2
- Depth: L2 → L3
- Audience: users exploring routine automation
- Goal:
  - explain periodic assistance workflows

### `/use-cases/remote-access`
- Priority: P2
- Depth: L2 → L3
- Audience: practical + advanced users
- Goal:
  - explain remote/device-connected usage patterns

---

## 5.6 Advanced Topics

### `/advanced`
- Priority: P1
- Depth: L2 → L4
- Audience: intermediate + advanced users
- Goal:
  - provide an overview of deeper topics

### `/advanced/session-model`
- Priority: P1
- Depth: L3
- Audience: intermediate users
- Goal:
  - explain why session design matters operationally

### `/advanced/memory-design`
- Priority: P1
- Depth: L3 → L4
- Audience: intermediate users
- Goal:
  - explain practical memory strategy and boundaries

### `/advanced/skill-design`
- Priority: P2
- Depth: L3 → L4
- Audience: advanced users
- Goal:
  - explain when and how skill design matters

### `/advanced/subagent-workflows`
- Priority: P2
- Depth: L3 → L4
- Audience: advanced / builder users
- Goal:
  - explain decomposition and separate-process workflows

### `/advanced/safety-boundaries`
- Priority: P1
- Depth: L3
- Audience: all serious users
- Goal:
  - explain why some actions require confirmation and why boundaries matter

### `/advanced/debugging-logs`
- Priority: P2
- Depth: L3 → L4
- Audience: technical users
- Goal:
  - explain how to read logs and not overreact to benign issues

### `/advanced/best-practices`
- Priority: P1
- Depth: L3
- Audience: intermediate + advanced users
- Goal:
  - summarize operational wisdom and anti-patterns

---

## 5.7 FAQ

### `/faq`
- Priority: P1
- Depth: L1 → L2
- Audience: all users
- Goal:
  - provide categorized problem entry points

### `/faq/setup`
- Priority: P1
- Depth: L2
- Audience: practical beginners
- Goal:
  - answer the most common setup failures

### `/faq/connectivity`
- Priority: P1
- Depth: L2 → L3
- Audience: practical users
- Goal:
  - explain connection, token, and access issues

### `/faq/ws-http-fallback`
- Priority: P2
- Depth: L2 → L3
- Audience: practical + technical users
- Goal:
  - explain ws-stream fallback without causing unnecessary panic

### `/faq/files-and-memory`
- Priority: P2
- Depth: L2
- Audience: all users
- Goal:
  - explain file expectations, missing files, and benign ENOENT cases

### `/faq/skills-and-tools`
- Priority: P2
- Depth: L2 → L3
- Audience: learners moving deeper
- Goal:
  - explain why tools/skills sometimes appear confusing or do not behave as expected

### `/faq/security-and-behavior`
- Priority: P2
- Depth: L2 → L3
- Audience: all users
- Goal:
  - explain safety/approval behavior and group chat boundaries

---

## 6. Recommended Build Order

This is the suggested order for the next process to execute.

### Wave 1 — Product skeleton (must build first)
1. `/`
2. `/getting-started`
3. `/getting-started/what-is-openclaw`
4. `/concepts`
5. `/concepts/architecture`
6. `/concepts/session`
7. `/concepts/gateway`
8. `/concepts/skills`
9. `/concepts/tools`
10. `/concepts/memory`
11. `/setup`
12. `/setup/requirements`
13. `/setup/install`
14. `/setup/configuration`
15. `/setup/start-gateway`
16. `/setup/first-message`

Why first:
- these pages create the minimum learning loop:
  understand → orient → set up → succeed once

### Wave 2 — Make it truly useful
17. `/setup/troubleshooting`
18. `/use-cases`
19. `/use-cases/personal-assistant`
20. `/use-cases/messaging-platforms`
21. `/advanced`
22. `/advanced/session-model`
23. `/advanced/memory-design`
24. `/advanced/safety-boundaries`
25. `/advanced/best-practices`
26. `/faq`
27. `/faq/setup`
28. `/faq/connectivity`

Why next:
- this wave turns the site from “intro” into a practical, recommendable learning product

### Wave 3 — Advanced completeness and expansion
29. `/getting-started/how-to-learn`
30. `/getting-started/first-roadmap`
31. `/concepts/agent`
32. `/concepts/node`
33. `/concepts/dashboard`
34. `/concepts/heartbeat-cron`
35. `/concepts/subagents`
36. `/concepts/acp`
37. `/use-cases/github-workflow`
38. `/use-cases/notes-reminders`
39. `/use-cases/google-workspace`
40. `/use-cases/heartbeat-automation`
41. `/use-cases/remote-access`
42. `/advanced/skill-design`
43. `/advanced/subagent-workflows`
44. `/advanced/debugging-logs`
45. `/faq/ws-http-fallback`
46. `/faq/files-and-memory`
47. `/faq/skills-and-tools`
48. `/faq/security-and-behavior`

Why later:
- these pages deepen the site and improve completeness, but are not blockers for the first meaningful public version

---

## 7. Homepage Content Priority

The homepage should be designed around five user intents:

1. I am completely new — what is this?
2. I want a learning route
3. I want to set it up
4. I want to know what it can do
5. I already know some things — take me to advanced topics

Therefore homepage section priority should be:

### P0 homepage sections
- hero
- what this site helps with
- learning path
- top-level module cards
- setup entry
- concepts entry

### P1 homepage sections
- use case cards
- concept map preview
- advanced topics preview
- FAQ entry

### P2 homepage sections
- visual storytelling enhancements
- social/share-focused module blocks
- update history or version notes

---

## 8. Content Writing Rules for Next Process

When the next process starts writing actual page content, it should follow these rules:

### Rule 1
Always start with a short answer before expanding.

### Rule 2
Teach “what it is” + “why it matters” + “what to read next”.

### Rule 3
Avoid dropping raw jargon without relationship context.

### Rule 4
Prefer layered reading:
- quick summary
- practical explanation
- deeper system explanation
- advanced notes

### Rule 5
For setup/troubleshooting pages, define expected success signals clearly.

### Rule 6
For advanced pages, avoid becoming abstract for its own sake; tie concepts back to real user decisions.

---

## 9. Suggested Deliverables for the Next Process

The next process should pick up from here and produce:

1. final confirmed sitemap
2. low-fidelity page outlines for Wave 1 pages
3. homepage wireframe/content outline
4. concept page layout pattern
5. setup page layout pattern
6. FAQ page layout pattern
7. initial implementation plan aligned with Wave 1

---

## 10. Short Handoff

If another process starts from this file, the immediate focus should be:

> Build the first meaningful public version by completing **Wave 1** first, then **Wave 2**, then expand to **Wave 3**.

This preserves clarity, token efficiency, and product coherence.

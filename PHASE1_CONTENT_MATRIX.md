# PHASE1_CONTENT_MATRIX.md — openclaw-summary

Last updated: 2026-03-31
Status: upgraded for v0.2 redesign planning

---

## 1. Purpose

This file defines the **content and interaction architecture** for `openclaw-summary` after v0.1 feedback.

Its job is no longer only to say:
- what pages exist
- what each page must teach

It must also define:
- how users should enter the content
- how module pages should preview content before navigation
- what metadata each page/card should expose
- how detail pages should orient the user

This is still a **product/content planning artifact**, not implementation work.

---

## 2. Core v0.2 planning shift

v0.1 proved that the topic model is valid.

v0.2 must solve a different problem:

> The product needs to feel guided, expandable, and confidence-building instead of page-jumpy and directory-like.

Therefore this matrix now covers both:
- content architecture
- experience architecture

---

## 3. Content Depth Levels

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

## 4. Priority Levels

### P0 — Must exist first
These pages/patterns define the product skeleton and first usable experience.

### P1 — Should follow immediately
These pages/patterns make the site genuinely useful.

### P2 — Important expansion
These pages/patterns deepen completeness and sharing value.

### P3 — Polishing / later expansion
These pages are useful, but not blockers for the next meaningful public version.

---

## 5. New Interaction Layers

All major content in v0.2 should ideally support 3 layers:

### Layer A — Preview
A card, expandable item, or route block that helps the user decide whether to enter.

### Layer B — Page Summary
The top of an independent page should quickly explain what the page is about and why it matters.

### Layer C — Full Reading
The deeper explanation, examples, misunderstandings, related pages, and next steps.

This means not every click must immediately trigger a hard context switch.

---

## 6. Shared Metadata Model

The following metadata fields should be treated as first-class content fields where useful:

- audience
- difficulty
- estimated reading time
- prerequisites
- tags
- recommended sequence step
- related pages
- recommended next step
- module
- role in learning path

This metadata should be displayable both on cards and on detail pages.

---

## 7. Module Overview

| Module | Goal | Primary audience | v0.2 experience role |
|---|---|---|---|
| Home | Explain the product and route users | All users | Routing + confidence building |
| Getting Started | Help absolute beginners enter smoothly | New users | Guided onboarding hub |
| Core Concepts | Build a correct mental model | New + intermediate users | Expandable concept hub |
| Setup | Help users get OpenClaw running | New + practical users | Stepwise progress hub |
| Use Cases | Show why OpenClaw matters in practice | Curious + practical users | Goal-based scenario hub |
| Advanced | Explain deeper mechanisms and best practices | Intermediate + advanced users | Depth map |
| FAQ | Reduce frustration and unblock adoption | All users | Fast unblock hub |

---

## 8. Page-by-Page Content Matrix

---

## 8.1 Home

### `/`
- Priority: P0
- Depth: L1 → L2
- Audience: all users
- Goal:
  - explain what the site is
  - explain how to use it
  - route users into the right path quickly
- Must teach:
  - this is a Chinese interactive learning site for OpenClaw
  - OpenClaw has a learning path from basics to advanced
  - users can enter by stage, goal, or module
- Must include:
  - hero section
  - one primary CTA
  - one secondary CTA
  - three entry modes
  - stronger learning path section
  - module exploration section
  - shareable deep-link recommendations
- Must avoid:
  - exposing too many equal-weight options too early
  - feeling like a flat directory
- v0.2 interaction requirements:
  - route blocks or cards should reveal enough context before navigation
  - learning path steps should be expandable or strongly previewed
- Exit paths:
  - getting started
  - concepts
  - setup
  - use cases
  - faq

---

## 8.2 Getting Started

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
  - “if you only have 10 minutes” shortcut
- v0.2 interaction requirements:
  - expandable beginner steps
  - each step shows expected outcome, estimated time, and next move

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
- Must include page-level orientation:
  - breadcrumb
  - beginner-friendly badge
  - what to read next

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
- v0.2 interaction opportunity:
  - compare learning paths as route cards

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

## 8.3 Core Concepts

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
- v0.2 interaction requirements:
  - cards should be expandable before navigation
  - expanded state should show why the concept matters, relationships, difficulty, related pages, and next step

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
- Must include:
  - relation map or relation summary
  - what to read next by concept branch

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

## 8.4 Setup & Deployment

### `/setup`
- Priority: P0
- Depth: L1 → L2
- Audience: practical beginners
- Goal:
  - provide the setup journey overview
- Must teach:
  - setup has an order
  - users should verify success step by step
- Must include:
  - stepwise setup overview
  - expected success checkpoints
  - “I only want the shortest route” shortcut
- v0.2 interaction requirements:
  - setup steps should be expandable
  - each step should show purpose, actions, success signal, and common pitfall

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

## 8.5 Use Cases

### `/use-cases`
- Priority: P1
- Depth: L1 → L2
- Audience: all users
- Goal:
  - show the scenario landscape
  - route users by goal
- v0.2 interaction requirements:
  - scenario cards should reveal who the scenario is for and what capabilities it uses before navigation

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

## 8.6 Advanced Topics

### `/advanced`
- Priority: P1
- Depth: L2 → L4
- Audience: intermediate + advanced users
- Goal:
  - provide an overview of deeper topics
- v0.2 interaction requirements:
  - advanced topics should be grouped by theme and difficulty rather than presented as a flat list

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

## 8.7 FAQ

### `/faq`
- Priority: P1
- Depth: L1 → L2
- Audience: all users
- Goal:
  - provide categorized problem entry points
- v0.2 interaction requirements:
  - FAQ categories and questions should be collapsible
  - users should be able to preview likely cause and confidence level before entering full pages

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

## 9. Shared Page Pattern Requirements

### 9.1 Top-level module pages
Every top-level module page should include:
- module intro
- recommended reading order
- expandable cards/items
- quick-start or “only read this first” shortcut
- next-step guidance

### 9.2 Detail pages
Every detail page should include:
- breadcrumb
- current module indicator
- page purpose statement
- recommended next page
- related pages
- previous / next navigation

### 9.3 Preferred detail page structure
1. short answer
2. why it matters
3. deeper explanation
4. common misunderstandings
5. related concepts/pages
6. what to read next

---

## 10. Updated Homepage Content Priority

The homepage should be designed around three entry modes rather than many equal-weight jumps.

### P0 homepage sections
- hero
- one main CTA
- three entry modes (stage / goal / module)
- guided learning path

### P1 homepage sections
- module exploration area
- shareable deep-link recommendations
- concept relationship preview
- FAQ / troubleshooting fast entry

### P2 homepage sections
- visual storytelling enhancements
- update history or version notes
- stronger social/share blocks

---

## 11. Updated Build / Rebuild Order

This is the suggested order for the next implementation process.

### Wave 1 — Experience skeleton + core user journey
1. Astro project scaffold
2. global layout system
3. metadata model
4. top navigation + breadcrumb + previous/next components
5. reusable expandable card / accordion component
6. homepage rebuild
7. `/getting-started`
8. `/concepts`
9. `/setup`
10. `/faq`

Why first:
- these deliver the biggest UX improvement
- these solve orientation and jump-friction first
- these build the reusable component system for the whole site

### Wave 2 — Representative deep pages + scenario layer
11. `/getting-started/what-is-openclaw`
12. `/getting-started/how-to-learn`
13. `/concepts/architecture`
14. `/concepts/session`
15. `/concepts/gateway`
16. `/concepts/skills`
17. `/concepts/tools`
18. `/concepts/memory`
19. `/setup/requirements`
20. `/setup/install`
21. `/setup/configuration`
22. `/setup/start-gateway`
23. `/setup/first-message`
24. `/setup/troubleshooting`
25. `/use-cases`
26. `/advanced`

Why next:
- this establishes the most meaningful learning loop and representative patterns

### Wave 3 — Full migration and expansion
27. remaining detail pages across concepts / use-cases / advanced / faq
28. concept relationship interaction upgrade
29. shareability and browsing polish
30. optional search/filter/progress enhancements

Why later:
- these deepen the experience after the core interaction model is stable

---

## 12. Content Writing Rules for Next Process

When the next process starts writing or rewriting actual page content, it should follow these rules:

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

### Rule 7
Write preview-friendly summaries suitable for expandable cards.

### Rule 8
Treat metadata as part of content design, not as optional decoration.

---

## 13. Suggested Deliverables for the Next Process

The next process should pick up from here and produce:

1. Astro-based scaffold
2. confirmed metadata schema
3. homepage wireframe/content outline
4. module page pattern
5. detail page pattern
6. navigation component spec
7. card/accordion component spec
8. first rebuilt core pages aligned with Wave 1

---

## 14. Short Handoff

If another process starts from this file, the immediate focus should be:

> Rebuild the site around guidance, previews, and orientation first.

Do not treat the next phase as a plain content expansion pass.

Treat it as:

> a shift from a static directory-like learning site to a guided interactive learning product.

# ROADMAP.md — openclaw-summary

Last updated: 2026-03-31
Status: Product design phase

---

## 1. Project Positioning

**openclaw-summary** is a Chinese interactive learning website for newcomers to OpenClaw.

Its job is not to mirror the official docs, but to make OpenClaw easier to understand, easier to learn, and easier to share.

Core value:

- explain OpenClaw from basics to advanced topics
- provide a clear learning path instead of scattered documentation
- present knowledge as an interactive web experience
- make every major topic shareable via URL

In one sentence:

> A shareable, interactive Chinese learning site that helps users systematically understand OpenClaw from introduction to setup, usage, advanced mechanisms, and troubleshooting.

---

## 2. Confirmed Product Decisions

### Language
- Chinese only

### Product form
- Multi-page site + homepage overview

### Visual style
- Card-based learning product style
- With a light technology feel
- Prioritize clarity, structure, and readability over flashy effects

### Depth of v1
- Cover both beginner and advanced knowledge from the start
- But still organize content in layered form so beginners are not overwhelmed

### Content source strategy
- Combination of official OpenClaw documentation and real-world practical experience

### Collaboration mode for this repo
- **Current process only handles product design and roadmap writing**
- **Actual development should happen in a separate new process/session**
- This follows the previously agreed token-saving / low-context workflow

---

## 3. Product Goals

The site should help a user:

1. understand what OpenClaw is
2. understand the core concepts and architecture
3. complete basic setup and first use
4. see practical real-world use cases
5. understand advanced mechanisms and best practices
6. solve common problems quickly
7. share specific pages with others via URL

Success means:

- a newcomer can build a usable mental model quickly
- users know what to read first, next, and later
- the site is easier to learn from than reading raw docs alone
- individual pages are worth sharing directly

---

## 4. Product Principles

### P1. Beginner-first, but not dumbed down
Explain clearly without assuming too much background, while staying professional.

### P2. Teach relationships, not just definitions
The hard part of OpenClaw is how components fit together.

### P3. Learning path matters more than information volume
The site should always answer: where am I, what is this, what should I read next?

### P4. Interaction must help understanding
Interactive maps, cards, path navigation, and step guides should reduce cognitive load.

### P5. Every important page should be independently shareable
Pages should still make sense when opened directly from a shared URL.

---

## 5. Primary Users

### A. New Chinese-speaking OpenClaw users
Need a structured path from zero to usable.

### B. Existing users who want to recommend OpenClaw to others
Need a page they can share with friends, coworkers, or communities.

### C. Users with fragmented knowledge
Need a system-level explanation, advanced understanding, and troubleshooting support.

---

## 6. Information Architecture

The product will be organized into 7 top-level modules.

### 1) Home
Purpose:
- explain what this site is
- provide major entry points
- show the learning path

### 2) Getting Started
Purpose:
- help absolute beginners understand OpenClaw at a high level
- provide a recommended first reading path

### 3) Core Concepts
Purpose:
- explain architecture and key concepts
- show relationships between components

### 4) Setup & Deployment
Purpose:
- guide users from environment prep to first successful interaction

### 5) Use Cases
Purpose:
- show practical applications and common scenarios

### 6) Advanced Topics
Purpose:
- explain deeper mechanisms, workflows, best practices, and architectural thinking

### 7) FAQ / Troubleshooting
Purpose:
- reduce friction by addressing common setup, connectivity, behavior, and logging problems

---

## 7. Planned Sitemap (v0.1)

### Top-level pages
- `/` Home
- `/getting-started`
- `/concepts`
- `/setup`
- `/use-cases`
- `/advanced`
- `/faq`

### Getting Started
- `/getting-started/what-is-openclaw`
- `/getting-started/how-to-learn`
- `/getting-started/first-roadmap`

### Core Concepts
- `/concepts/architecture`
- `/concepts/agent`
- `/concepts/session`
- `/concepts/gateway`
- `/concepts/node`
- `/concepts/skills`
- `/concepts/tools`
- `/concepts/memory`
- `/concepts/dashboard`
- `/concepts/heartbeat-cron`
- `/concepts/subagents`
- `/concepts/acp`

### Setup & Deployment
- `/setup/requirements`
- `/setup/install`
- `/setup/configuration`
- `/setup/start-gateway`
- `/setup/first-message`
- `/setup/troubleshooting`

### Use Cases
- `/use-cases/personal-assistant`
- `/use-cases/messaging-platforms`
- `/use-cases/github-workflow`
- `/use-cases/notes-reminders`
- `/use-cases/google-workspace`
- `/use-cases/heartbeat-automation`
- `/use-cases/remote-access`

### Advanced Topics
- `/advanced/session-model`
- `/advanced/memory-design`
- `/advanced/skill-design`
- `/advanced/subagent-workflows`
- `/advanced/safety-boundaries`
- `/advanced/debugging-logs`
- `/advanced/best-practices`

### FAQ
- `/faq/setup`
- `/faq/connectivity`
- `/faq/ws-http-fallback`
- `/faq/files-and-memory`
- `/faq/skills-and-tools`
- `/faq/security-and-behavior`

---

## 8. Content Model

To keep the site maintainable, each content type should follow a fixed structure.

### Concept page template
- one-sentence definition
- detailed explanation
- relationship to other concepts
- common use cases
- common misunderstandings
- related pages
- recommended next step

### Setup page template
- goal of this step
- prerequisites
- actions to take
- why this matters
- expected result
- common errors
- next step

### Use case page template
- who this is for
- what problem it solves
- involved OpenClaw capabilities
- typical workflow
- caveats
- further reading

### FAQ page template
- question
- symptoms
- likely cause
- solution
- prevention
- related concept/setup pages

---

## 9. Key Interactive Experiences

These are the main interaction ideas that distinguish the project from a plain docs site.

### A. Learning Path Navigation
Users can learn by:
- recommended sequence
- topic browsing
- goal-based exploration

### B. Card-Based Knowledge Browsing
Use cards for:
- concepts
- scenarios
- setup steps
- advanced topics
- FAQs

### C. Interactive Concept Map
A clickable visual relationship map for:
- OpenClaw core
- gateway
- agent
- session
- node
- skills
- tools
- memory
- dashboard/control UI
- heartbeat/cron
- subagents / ACP

### D. Guided Setup Flow
A step-by-step setup experience with:
- current step
- purpose
- actions
- expected result
- troubleshooting hints

### E. Use-Case Explorer
Entry by user goal, such as:
- I want to understand OpenClaw
- I want to set it up
- I want to connect Telegram/Discord
- I want calendar/notes/reminders workflows
- I want GitHub/dev workflows
- I want remote access / multi-device usage

---

## 10. Visual Direction

Keywords:
- structured
- clean
- readable
- slightly futuristic
- modular
- shareable

Design guidance:
- card-heavy layout
- strong hierarchy
- subtle gradients and grid/connection motifs
- avoid over-designed cyberpunk aesthetics
- content comprehension first

---

## 11. Scope Strategy

Although v1 covers beginner through advanced topics, the implementation should still be layered.

### Include in v1
- full top-level information architecture
- homepage overview
- beginner onboarding content
- concept pages
- setup path
- use-case section
- advanced section
- FAQ section
- shareable page URLs

### Avoid in this phase
- account system
- comment/community features
- online execution sandbox
- complex CMS/backend editing system
- AI chatbot layer on top of content

---

## 12. Product Risks

### Risk 1: Scope explosion
“Beginner to advanced” can easily become “rewrite the whole universe.”

Mitigation:
- keep a strong top-level structure
- write layered content instead of dumping everything flat

### Risk 2: Becoming just another docs mirror
Mitigation:
- prioritize pathing, relationships, visual navigation, and interaction

### Risk 3: Too hard for beginners, too shallow for experienced users
Mitigation:
- each page must support progressive depth

### Risk 4: Pages are not independently useful when shared
Mitigation:
- every page needs self-contained context and next-step guidance

---

## 13. Delivery Strategy

This roadmap intentionally stops at **product design and planning**.

### What this current process is responsible for
- define product positioning
- define information architecture
- define scope and principles
- write roadmap into the repo

### What the next separate development process should handle
- technical stack decision
- project scaffolding
- page implementation
- component system
- content authoring workflow
- deployment and share URL setup

This separation is intentional to reduce context bloat and token usage.

---

## 14. Phases

### Phase 0 — Product Definition ✅
Status: done in current process

Includes:
- product positioning
- target users
- product principles
- information architecture
- sitemap draft
- interaction direction
- scope boundaries

### Phase 1 — Content Architecture
Goal:
- turn sitemap into a page-by-page content matrix
- define what each page must teach
- define reading order and cross-links

Suggested outputs:
- content matrix
- page inventory
- module-level briefs
- homepage content outline

### Phase 2 — Experience & UI Blueprint
Goal:
- turn content architecture into UX structure

Suggested outputs:
- low-fidelity wireframes
- navigation model
- card system
- concept-map interaction design
- responsive layout rules

### Phase 3 — Technical Planning
Goal:
- choose frontend architecture and deployment route

Suggested outputs:
- stack decision
- folder structure
- routing strategy
- content source format
- deployment plan

### Phase 4 — Implementation (separate process)
Goal:
- build the first working version of the site

Suggested outputs:
- scaffolded frontend project
- homepage
- top-level sections
- initial concept pages
- initial setup pages
- initial FAQ pages

### Phase 5 — Content Expansion & Refinement
Goal:
- fill out beginner + advanced coverage
- improve writing, visuals, and internal linking

---

## 15. Immediate Next Step

The next session/process should begin from:

> Build **Phase 1: Content Architecture** for openclaw-summary.

That means producing:
- detailed sitemap confirmation
- content matrix for each page
- module descriptions
- priority order for writing/implementation

---

## 16. Current Project Status Snapshot

Current state:
- repo initialized
- product direction confirmed
- roadmap written
- implementation not started yet

Current rule:
- do not start coding in this process
- continue in a separate fresh process/session for implementation planning or development

---

## 17. Short Handoff Summary

If another process picks this up, the handoff is:

- project: `openclaw-summary`
- repo: `Liu-Feng-03/openclaw-summary-ver0.1`
- current stage: product design completed, roadmap written
- next stage: content architecture, then UX blueprint, then technical planning, then implementation
- working style: keep context lean; use separate sessions/processes for development work

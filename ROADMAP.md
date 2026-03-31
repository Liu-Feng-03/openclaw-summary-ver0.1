# ROADMAP.md — openclaw-summary

Last updated: 2026-03-31
Status: v0.1 completed; v0.2 redesign direction confirmed

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
- Each important topic should still have an independent URL
- The browsing experience should no longer rely on hard page jumps alone

### Visual style
- Card-based learning product style
- With a light technology feel
- Prioritize clarity, structure, and readability over flashy effects

### Depth of v1 / v2 continuity
- Cover both beginner and advanced knowledge from the start
- Organize content in layered form so beginners are not overwhelmed
- Add stronger progressive disclosure in v0.2

### Content source strategy
- Combination of official OpenClaw documentation and real-world practical experience

### Confirmed redesign decision
- Keep the 7-module knowledge model
- Keep public shareable URLs
- Migrate implementation from pure static hand-authored multi-page HTML to a **lightweight frontend framework**
- Prefer a route that still supports **static deployment** and easy public access

### Recommended framework direction
Preferred order:
1. Astro
2. Next.js with static export
3. Vite + React

Current recommendation:
- **Astro**

### Collaboration mode for this repo
- Product design was completed first in a lightweight planning process
- v0.1 implementation was completed in a separate low-context development process
- v0.2 redesign / IA / UX revision should continue in focused planning updates
- v0.2 implementation should be handled in a new lean development process after design docs are aligned

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
8. know where they are, what a page is for, and what to read next

Success means:

- a newcomer can build a usable mental model quickly
- users know what to read first, next, and later
- the site is easier to learn from than reading raw docs alone
- individual pages are worth sharing directly
- users can browse with confidence instead of feeling lost after each click

---

## 4. Product Principles

### P1. Beginner-first, but not dumbed down
Explain clearly without assuming too much background, while staying professional.

### P2. Teach relationships, not just definitions
The hard part of OpenClaw is how components fit together.

### P3. Learning path matters more than information volume
The site should always answer: where am I, what is this, what should I read next?

### P4. Interaction must help understanding
Interactive maps, cards, path navigation, previews, and step guides should reduce cognitive load.

### P5. Every important page should be independently shareable
Pages should still make sense when opened directly from a shared URL.

### P6. Guide before exposing too many choices
Users should not have to solve navigation ambiguity before learning begins.

### P7. Use progressive disclosure to reduce jump friction
Users should be able to preview and expand before committing to a page transition.

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

The product remains organized into 7 top-level modules.

### 1) Home
Purpose:
- explain what this site is
- explain how to use the site
- provide major entry points
- show the learning path
- route users by stage, goal, or module

### 2) Getting Started
Purpose:
- help absolute beginners understand OpenClaw at a high level
- provide a recommended first reading path
- reduce fear of “not knowing where to begin”

### 3) Core Concepts
Purpose:
- explain architecture and key concepts
- show relationships between components
- help users build a correct mental model before going deeper

### 4) Setup & Deployment
Purpose:
- guide users from environment prep to first successful interaction
- make the setup journey feel stepwise and verifiable

### 5) Use Cases
Purpose:
- show practical applications and common scenarios
- let users enter by real goals, not only abstract concepts

### 6) Advanced Topics
Purpose:
- explain deeper mechanisms, workflows, best practices, and architectural thinking

### 7) FAQ / Troubleshooting
Purpose:
- reduce friction by addressing common setup, connectivity, behavior, and logging problems
- provide quick confidence-building answers when users feel blocked

---

## 7. Planned Sitemap

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

Note:
- The sitemap stays broadly stable in v0.2
- The main redesign is in interaction, navigation, and presentation logic rather than a full sitemap reset

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

### New metadata layer for v0.2
Each page or preview card should support, when useful:
- audience
- difficulty
- estimated reading time
- prerequisites
- tags
- related pages
- recommended next step
- place in learning path

---

## 9. Key Interactive Experiences

These are the main interaction ideas that distinguish the project from a plain docs site.

### A. Guided Entry System
Users can enter by:
- stage
- goal
- module

The homepage should not expose all paths with equal weight at once.

### B. Learning Path Navigation
Users can learn by:
- recommended sequence
- topic browsing
- goal-based exploration

The learning path should become a clearer UI object, not just text blocks.

### C. Card-Based Knowledge Browsing
Use cards for:
- concepts
- scenarios
- setup steps
- advanced topics
- FAQs

In v0.2, cards should support preview / expansion before full navigation.

### D. Expandable Module Hubs
Top-level module pages should become expandable knowledge hubs rather than simple jump lists.

### E. Interactive Concept Relationship View
A clickable visual or semi-visual relationship layer for:
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

### F. Guided Setup Flow
A step-by-step setup experience with:
- current step
- purpose
- actions
- expected result
- troubleshooting hints
- next step guidance

### G. Strong Wayfinding
Detail pages should clearly show:
- breadcrumb
- current module
- recommended next page
- related pages
- previous / next navigation

---

## 10. Visual Direction

Keywords:
- structured
- clean
- readable
- slightly futuristic
- modular
- shareable
- confidence-building
- guided

Design guidance:
- card-heavy layout
- strong hierarchy
- subtle gradients and grid/connection motifs
- avoid over-designed cyberpunk aesthetics
- content comprehension first
- use expansion and visual grouping to reduce jump anxiety

---

## 11. Scope Strategy

Although v1 covers beginner through advanced topics, the implementation should still be layered.

### Include in v0.2
- framework migration to lightweight component architecture
- preserve all important independent page URLs
- homepage redesign around routing and confidence-building
- module pages redesigned as expandable hubs
- improved detail-page wayfinding
- stronger card system with metadata
- clearer learning path UI
- improved concept relationship interaction

### Avoid in this phase
- account system
- comment/community features
- online execution sandbox
- complex CMS/backend editing system
- AI chatbot layer on top of content
- unnecessary server-side complexity

---

## 12. Product Risks

### Risk 1: Scope explosion
“Beginner to advanced” can easily become “rewrite the whole universe.”

Mitigation:
- keep a strong top-level structure
- write layered content instead of dumping everything flat
- prioritize experience architecture before content expansion

### Risk 2: Becoming just another docs mirror
Mitigation:
- prioritize pathing, relationships, previews, visual navigation, and interaction

### Risk 3: Too hard for beginners, too shallow for experienced users
Mitigation:
- each page must support progressive depth
- cards and previews must help users pick the right depth level

### Risk 4: Pages are not independently useful when shared
Mitigation:
- every page needs self-contained context and next-step guidance

### Risk 5: Framework migration adds complexity without improving UX
Mitigation:
- migrate only to a lightweight framework
- preserve static deployment
- focus the migration on reusable navigation, card, and expansion patterns

---

## 13. Delivery Strategy

### Planning process already completed for v0.1
- product positioning
- information architecture
- scope and principles
- roadmap writing
- content matrix definition

### Development process already completed for v0.1
- technical route chosen as static multi-page site
- project scaffold created
- all planned v0.1 pages generated as independent URLs
- shared visual system / navigation / layout implemented
- GitHub Pages deployment configured and working

### Confirmed v0.2 planning direction
- redesign the experience architecture based on real usage feedback
- update roadmap and content matrix
- define homepage/module/detail/navigation patterns before the new implementation pass

### Recommended future workflow
- product redesign, IA changes, and copy strategy updates should happen in separate focused sessions
- implementation updates should continue in lean development sessions
- keep roadmap and implementation state synchronized after each milestone

---

## 14. Phases

### Phase 0 — Product Definition ✅
Status: done

Includes:
- product positioning
- target users
- product principles
- information architecture
- sitemap draft
- interaction direction
- scope boundaries

### Phase 1 — Content Architecture ✅
Status: completed

Goal:
- turn sitemap into a page-by-page content matrix
- define what each page must teach
- define reading order and cross-links

### Phase 2 — Experience & UI Blueprint ✅
Status: completed in lightweight implementation form for v0.1

Goal:
- turn content architecture into UX structure

### Phase 3 — Technical Planning ✅
Status: completed for v0.1

Goal:
- choose frontend architecture and deployment route

### Phase 4 — Implementation (v0.1) ✅
Status: completed

Goal:
- build the first working version of the site

### Phase 5 — Content Expansion & Refinement ✅
Status: first pass completed

Goal:
- fill out beginner + advanced coverage
- improve writing, visuals, and internal linking

Current result:
- all planned sitemap pages for v0.1 have been created
- homepage + 7 top-level modules are online
- first-pass Chinese content has been written across beginner, concept, setup, use-case, advanced, and FAQ sections
- internal linking, sitemap, robots.txt, 404, and GitHub Pages deployment are in place

### Phase 6 — Experience Architecture Redesign 🔄
Status: confirmed next phase

Goal:
- redesign the product from a static docs-like site into a guided interactive learning product

Includes:
- homepage routing redesign
- module-page expandable hub pattern
- detail-page wayfinding pattern
- improved card system and metadata
- concept relationship interaction upgrade
- framework migration decision and implementation planning

### Phase 7 — Framework Migration & v0.2 Rebuild
Status: next implementation phase

Goal:
- rebuild the core experience using a lightweight frontend framework while preserving public accessibility and static deployment

Includes:
- Astro scaffold
- shared layout/components
- data-driven page metadata
- accordion/expandable interaction
- rebuilt homepage and key modules

---

## 15. Immediate Next Step

The next session/process should begin from:

> Rebuild the product design and experience architecture for v0.2, then start framework-based implementation in a separate lean process.

Recommended priorities:
- finalize homepage redesign and user-routing logic
- define module-page expandable card pattern
- define detail-page navigation / orientation system
- define metadata model for cards and pages
- migrate from pure static pages to Astro while preserving static deployment
- rebuild the core modules first: home, getting-started, concepts, setup, faq

---

## 16. Current Project Status Snapshot

Current state:
- repo initialized and pushed to GitHub
- product direction confirmed
- roadmap written and updated
- Phase 1 content matrix completed and updated
- v0.1 first implementation completed
- GitHub Pages deployment completed
- live site available at: `https://liu-feng-03.github.io/openclaw-summary-ver0.1/`

Current rule:
- future product redesign happens in focused planning sessions
- future implementation updates continue in separate low-context development sessions

Implementation snapshot:
- total coverage includes homepage plus all planned v0.1 sitemap pages
- current implementation is a static multi-page site with shared assets and generated page files
- latest completed development milestone includes build, commit, push, and successful GitHub Pages deployment

---

## 17. Short Handoff Summary

If another process picks this up, the handoff is:

- project: `openclaw-summary`
- repo: `Liu-Feng-03/openclaw-summary-ver0.1`
- current stage: v0.1 completed, v0.2 redesign direction confirmed
- live site: `https://liu-feng-03.github.io/openclaw-summary-ver0.1/`
- current implementation form: static multi-page Chinese learning site
- next implementation form: lightweight framework-based site with static deployment (recommended: Astro)
- next stage: experience architecture redesign and framework migration planning, then v0.2 rebuild
- working style: keep context lean; separate product-design revisions from implementation sessions

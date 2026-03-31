# openclaw-summary v0.2 implementation plan

## Goal for this rebuild pass
先建立 Astro 版的产品系统骨架，而不是继续给 v0.1 静态页打补丁。

## Implemented in this run
1. Astro static scaffold
2. Shared data model for modules + topics
3. Shared layout shell and responsive global styles
4. Top nav + breadcrumb + metadata row
5. Expandable topic card / accordion pattern
6. Next-step / related / prev-next systems
7. Homepage rebuilt as routing page
8. Module page rebuilt as expandable knowledge hub
9. Detail page rebuilt as self-orienting reading page
10. Core priority modules wired first:
   - getting-started
   - concepts
   - setup
   - faq
11. Representative detail pages wired first:
   - getting-started/what-is-openclaw
   - getting-started/how-to-learn
   - concepts/architecture
   - concepts/session
   - concepts/gateway
   - setup/install
   - setup/configuration
   - setup/start-gateway
   - setup/first-message
   - faq/setup
   - faq/connectivity

## Next recommended build wave
1. Add more concept detail pages: skills / tools / memory / node
2. Add setup requirements + troubleshooting detail pages
3. Upgrade FAQ hub into grouped symptom accordion with category sections
4. Add module-specific visual accents and stronger iconography
5. Fill use-cases and advanced with grouped representative cards
6. Add concept relationship mini-panel with actual linked relation notes
7. Migrate remaining sitemap pages into the shared schema
8. Build and verify GitHub Pages deployment output

## Notes
- Current build intentionally prioritizes architecture and page-type separation.
- Content depth is still representative, not fully migrated from v0.1.
- The old static HTML remains in the repo for reference, but the new source of truth for v0.2 implementation is now under `src/`.

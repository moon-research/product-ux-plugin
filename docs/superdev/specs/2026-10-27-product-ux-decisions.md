# Product UX plugin — decision log

Authority: current HUMAN instructions govern. This log records confirmed choices and clearly labels proposals. Append decisions as they are resolved.

## D1 — Standalone product repository and local home

**When:** 2026-10-27T08:25:16+00:00 · **Phase:** brainstorm · **Status:** locked
**Decided by:** HUMAN, selecting `https://github.com/moon-research/product-ux-plugin` and requiring the standalone plugin inside `~/Projects`.

- **Trigger:** where the extracted product UX workflow should live and be published independently.
- **Options weighed:** keep it inside Product Graph (shares its lifecycle and internal dependencies); extract to its own product repository (independent installation/releases, requires explicit integration boundaries).
- **Decided:** use `moon-research/product-ux-plugin`, checked out at `/Users/tadas/Projects/product-ux-plugin`. The existing `setup-ux.sh` remains preserved.
- **Rests on:** explicit HUMAN repository/location selection; clone and clean-baseline evidence in the census.
- **Affects:** repository ownership, packaging, documentation and future releases.
- **Revisit-when:** the HUMAN changes the product's repository or distribution home.

## D2 — Workflow stages requested

**When:** 2026-10-27T08:25:16+00:00 · **Phase:** brainstorm · **Status:** locked for requirements; packaging and implementation remain proposed
**Decided by:** HUMAN, requesting the existing site work, a Product Graph landing-page capability, regular requirements brainstorming, a separate UX brainstorm with component-by-component refinement, artifact review and later Cloudflare production release.

- **Trigger:** a single site-building guide does not cover the requested requirements-to-UX-to-release journey.
- **Options weighed:** retain one site/publishing skill; provide a coordinated workflow with distinct requirements, UX and delivery stages.
- **Decided:** preserve those stages as the requested product behavior. The user has not yet selected skill boundaries, the artifact destination, or the exact breadth of landing-page implementation in this scope.
- **Rests on:** current HUMAN message; CRAFT/PUBLISHING evidence in the census.
- **Affects:** proposed skill boundaries and Product Graph/design/publishing integration points.
- **Revisit-when:** scope is refined during this brainstorm.

## Pending agenda — proposed, awaiting discussion

1. Standalone boundary: which reusable behavior ships with the plugin, and which integrations stay optional?
2. Review progression: what moves from requirements to visual UX, component acceptance and an assembled page?
3. Publishing boundary: where review artifacts are shown, and how reviewed source becomes an authorized Cloudflare release?

The agenda may be amended by the HUMAN. No plugin implementation or external publication has occurred.

## D3 — Superdesign is the design-review destination

**When:** 2026-10-27T08:26:47+00:00 · **Phase:** brainstorm · **Status:** locked
**Decided by:** HUMAN, explicitly selecting “Superdesign for design review.”

- **Trigger:** “publishing into superdev” could name either a design canvas or a development/reporting workflow.
- **Options weighed:** Superdesign canvas review; Superdev artifact/report publishing; support both destinations.
- **Decided:** use Superdesign for visual design review. Cloudflare remains the later working-site/production publishing stage. Canvas approval must be linked to the implementation reviewed for release; a canvas draft alone is not a production deployment.
- **Rests on:** HUMAN's answer to the clarification question in this session.
- **Affects:** UX brainstorming, review artifacts, design-to-code correspondence and site-release handoff.
- **Revisit-when:** the HUMAN requests another review destination.

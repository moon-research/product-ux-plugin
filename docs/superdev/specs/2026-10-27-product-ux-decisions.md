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

## Initial agenda — historical; superseded by D3–D4

1. Standalone boundary: which reusable behavior ships with the plugin, and which integrations stay optional?
2. Review progression: what moves from requirements to visual UX, component acceptance and an assembled page?
3. Publishing boundary: where review artifacts are shown, and how reviewed source becomes an authorized Cloudflare release?

At this initial checkpoint the agenda awaited discussion and no implementation had occurred. D3–D4 subsequently settled the destination and approved implementation; the plan and verification report record completion.

## D3 — Superdesign is the design-review destination

**When:** 2026-10-27T08:26:47+00:00 · **Phase:** brainstorm · **Status:** locked
**Decided by:** HUMAN, explicitly selecting “Superdesign for design review.”

- **Trigger:** “publishing into superdev” could name either a design canvas or a development/reporting workflow.
- **Options weighed:** Superdesign canvas review; Superdev artifact/report publishing; support both destinations.
- **Decided:** use Superdesign for visual design review. Cloudflare remains the later working-site/production publishing stage. Canvas approval must be linked to the implementation reviewed for release; a canvas draft alone is not a production deployment.
- **Rests on:** HUMAN's answer to the clarification question in this session.
- **Affects:** UX brainstorming, review artifacts, design-to-code correspondence and site-release handoff.
- **Revisit-when:** the HUMAN requests another review destination.

## D4 — Approved implementation and dual-host support

**When:** 2026-10-27T10:04:32+00:00 · **Phase:** build · **Status:** locked
**Decided by:** HUMAN: “ok work on it, make sure it could be used by Claude and Codex as plugin, use that repo.”

- **Trigger:** proposed scope and five skill boundaries required an implementation decision.
- **Options weighed:** leave the proposal for discussion; implement the shared workflow as a separately installable plugin.
- **Decided:** implement the proposal in this repository for Claude Code and Codex. Use one shared skills tree, a portable root manifest and thin host manifests/catalogs. Preserve setup-ux.sh.
- **Rests on:** explicit HUMAN instruction and D1–D3.
- **Affects:** all five skills, packaging, installation tests and release documentation.
- **Revisit-when:** either host's actual discovery requires a different compatibility wrapper.

## D5 — Landing-page capability and bounded integration work

**When:** 2026-10-27T10:04:32+00:00 · **Phase:** build · **Status:** provisional (author assumption, stated to HUMAN)
**Decided by:** author, continuing the approved scope with the reusable-capability interpretation.

- **Trigger:** no product-specific brief was supplied for an actual new landing page.
- **Options weighed:** invent and publish a Product Graph page; provide the reusable research-to-landing-page capability and examples.
- **Decided:** implement the reusable capability. Provider integrations are documented and tested for package behavior; creating paid design drafts, provisioning accounts and deploying live sites are outside this plugin test.
- **Rests on:** approved standalone product request, available site workflow and missing page brief.
- **Affects:** Product Graph reference, examples and verification limits.
- **Revisit-when:** HUMAN requests an actual page with its product brief.

## D6 — Native host verification and packaging boundary

**When:** 2026-10-27T10:19:18+00:00 · **Phase:** build · **Status:** locked (implementation detail)
**Decided by:** author from actual host checks and independent review.

- **Trigger:** a Codex session with `--ignore-user-config` did not expose the plugin even when catalog discovery worked; package review found nested local artifacts could ship.
- **Options weighed:** treat file-reading as proof of native loading and ignore nested artifacts; exercise an actual installed plugin in a normal native session and make package containment explicit.
- **Decided:** use real native install/discovery/session receipts, clean only the new Product UX test installation afterward, and retain existing user setup. Reject env/Git/cache/provider-local artifacts under skills; package only the explicit distribution boundary. Use namespaced Codex invocation shown by native skills/list.
- **Rests on:** actual Claude Skill invocation, Codex installed native skills/list and session output; independently reproduced archive leak and red/green boundary test.
- **Affects:** README commands, skill UI prompts, validator/archive utility, package tests and verification evidence.
- **Revisit-when:** host formats or discovery behavior changes, or a valid runtime asset requires extending the explicit distribution boundary.

## D7 — Add orchestration and improvement using Claude rooms

**When:** 2026-10-27T14:55:14+00:00 · **Phase:** build · **Status:** locked
**Decided by:** HUMAN, requesting orchestrator and self-improvement skills and then “skip codex-worker, just claude.”

- **Trigger:** the five-phase workflow lacked full enterable room coordination and a source-level improvement/release loop.
- **Options weighed:** couple the plugin to Superdev/private worker tooling; bundle the relevant skills and native Claude room mechanics.
- **Decided:** add `orchestrator` and `self-improvement`, use Claude Code background rooms from either leader host, and version the additive release as 0.2.0. Read Superdev as prior art; do not modify its source or require it at runtime.
- **Rests on:** explicit current HUMAN instructions and native CLI capability inspection.
- **Affects:** new skills/references, router/contribution guidance, manifests, changelog and verification.
- **Revisit-when:** the HUMAN requests another room runtime or measured native mechanics change.

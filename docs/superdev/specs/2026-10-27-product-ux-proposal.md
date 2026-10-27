# Product UX plugin — proposed v1

Status: approved for implementation by the HUMAN on 2026-10-27 (D4); five skill boundaries implemented. See [decision log](2026-10-27-product-ux-decisions.md) and [source census](2026-10-27-product-ux-census.md).

## Purpose

A standalone installable plugin in `moon-research/product-ux-plugin`, locally `~/Projects/product-ux-plugin`, that carries a business or product brief through requirements, visual UX decisions, component-by-component refinement, implementation and Cloudflare publication. It must work on a project with no Product Graph room graph or Superdev installation.

## Proposed skills

| Skill | Responsibility | Useful result |
|---|---|---|
| `product-ux` | Route the current request to its relevant phase; resume existing decisions and accepted work. | Clear current phase and next useful action. |
| `requirements-brainstorming` | Bundle an adapted version of our regular brainstorming approach: goals, audience, journeys, scope, constraints, decisions and acceptance. Scale detail to the work. | A usable requirements brief and decisions for UX work. |
| `ux-brainstorming` | Use Superdesign for actual visual alternatives, page composition, interaction states and responsive behavior; refine selected sections/components individually when detail is needed. | Reviewed design references and accepted component/page decisions. |
| `building-sites` | Translate accepted design into maintainable page/layout/component code; assemble accepted components and validate the working page. | Reviewable implementation with contribution breadcrumbs. |
| `publishing-sites` | Prepare a Cloudflare review deployment and, once authorized, promote the reviewed source to production with checks and recovery evidence. | Working review/live URLs, release receipt and rollback target. |

The skill names and split were approved through D4. The requirements and UX skills are independently invokable; they do not force a full journey on a small change.

## Flow and review boundaries

`existing research or business brief -> requirements -> Superdesign UX review -> accepted components -> assembled implementation -> Cloudflare review URL -> authorized production release`

A requirement change can return to requirements; a visual adjustment can remain in UX/component review. A later section does not require rewriting already accepted sections. Record Superdesign project/draft/element references with the source component and a short design note. This correspondence is maintained through skills and visual review, not deterministic canvas-to-code synchronization.

Superdesign review establishes a design decision. Browser review establishes what the implemented site does. Production approval covers the actual release scope; retain the existing distinction without repeated requests for already granted authority.

## Product Graph integration

Provide an optional landing-page input guide: audience/problem, research evidence, positioning, chosen angles, offer and intended action. Consume existing Product Graph outputs where supplied, retain provenance for factual claims and distinguish illustrative cases from observed results. Missing inputs are surfaced in requirements work rather than replaced with fabricated performance claims.

This proposal treats the request as a reusable capability to build Product Graph-driven landing pages. An actual new product's landing-page content, name and domain would require that product's brief. The plugin repository itself holds the reusable workflow; generated customer/product sites have their own project homes.

## Existing work carried forward

Extract the reusable AppFX/site playbook and publishing guide: incremental visual review; maintainable templates; Markdown blog authoring; typed source and operational scripts; content-driven metadata, robots, sitemap, RSS and LLM-readable exports; Google Analytics via the existing Firebase CLI pattern when requested; consent/privacy alignment; isolated build/test output; preview/production configuration; source/artifact receipts; actual host checks and rollback.

Keep these as focused references or proven implementation patterns, loaded as needed. Preserve the accepted project stack during contributions and choose a fitting stack for new sites; an Astro/static-site reference can be the worked example without making every product adopt it. Do not copy AppFX branding, account IDs, tokens or private room dependencies into reusable defaults. Policy pages describe the actual project practices rather than promising automatic legal compliance.

Every generated/maintained project gets clear contributor instructions and a path to report a reusable lesson back to this plugin. Product-specific decisions remain local. The existing `setup-ux.sh` is preserved; it is not executed or rewritten by this extraction.

## Independence and packaging

Bundle the requirements workflow and references it needs, retaining appropriate attribution for reused Superdev material. Product Graph is an optional input integration. Superdesign is the requested visual-review integration and needs its own available tools/authentication; the plugin should explain missing access rather than silently install software or claim a design was published. Cloudflare publishing likewise uses explicit project/account configuration and existing authorized tooling.

Keep skill bodies portable across Claude Code and Codex, with thin runtime/package discovery where needed. Start with the repository's plugin manifest, the five proposed skill folders and only the references needed by those skills. Avoid adding an application backend, orchestration framework, deterministic design registry or broad automation platform as part of extraction.

## Agreed scope boundaries

1. **Standalone boundary:** confirm the bundled workflow with optional Product Graph inputs and explicit Superdesign/Cloudflare integrations.
2. **Review progression:** confirm requirements, separate visual UX work and optional component-by-component refinement before assembly.
3. **Publishing boundary:** Superdesign for design review is confirmed; Cloudflare review and production remain separate site releases with recorded authority.

Implementation is recorded in the plan and verification report. This scope does not authorize provider account/domain changes, a customer-site release or submission to a public host directory.

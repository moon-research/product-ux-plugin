---
name: building-sites
description: "Use when implementing an accepted website or landing-page design, assembling reviewed components, maintaining site templates or adding content such as Markdown blog articles."
---

# Building sites

Implement the accepted experience in maintainable source, preserving the reviewed visual decisions and the project's existing conventions.

Read the brief/design notes, contributor instructions, source and relevant build commands. Locate the actual template/component boundary before editing. An existing accepted design is the visual contract; a request for one section or article does not expand into a whole-page redesign or framework migration.

For a new project, choose the smallest stack that meets the brief. Static HTML/CSS suits fixed pages; Astro is a useful reference for templates and Markdown publishing. Use [the static-site/content guide](references/static-sites.md) when repeated content is needed. Authentication, forms and backends follow an actual brief, not an assumed platform roadmap.

Build in useful review increments. Keep reusable layout, navigation, metadata and named page sections separate from page-specific content. Assemble accepted components, then inspect their transitions and responsive behavior. Consult [the project contract](../product-ux/references/project-contract.md) for contribution breadcrumbs and design/source correspondence.

Validate the changed surface: appropriate type/build checks; rendered content, links and metadata; desktop/mobile and keyboard behavior for affected UI. Use published-content-derived assertions instead of hard-coded article counts. Put test fixtures, output and writable caches in disposable workspaces; tests must not mutate author content or replace a review build.

For authorized visit measurement, read [Analytics through Firebase](references/analytics.md). Keep actual practices, consent controls, privacy text and CSP aligned; provider settings and incoming events need their own evidence.

Example: a third article should enter the shared published collection, cards, sitemap, feed and Markdown export without changing the landing composition or editing a fixed “two articles” checker.

Leave a concrete source/build/review handoff with checks and unresolved limitations. Route publication through `publishing-sites`; building local output does not establish that an uploaded site is working.

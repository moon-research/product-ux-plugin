# Static sites, templates and content

Preserve an existing stack unless a migration is requested. For a new site, choose the stack from its needs; a build step does not require browser JavaScript. Astro is the reference for repeated static layouts and Markdown blogs, not a required dependency of Product UX.

## Useful source boundaries

```text
src/components/       shared controls and named landing sections
src/layouts/          document shell, navigation and metadata
src/content/          validated article source, outside public assets
src/pages/            routes and discovery endpoints
public/               public assets and platform headers/redirects
scripts/              small authoring, artifact and deployment commands
```

Follow equivalent existing conventions rather than moving files to match this example. Keep design correspondence in project notes: the Superdesign draft/element, the actual component path and its acceptance. Design iteration should normally replace that component's implementation, not a copied whole-page export.

## Markdown publishing

Use one validated content model with a single explicit published filter across article routes, index/cards, related items, RSS, sitemap, LLM-readable index and Markdown exports. Require an explicit publish state; unfinished drafts stay absent from all public bytes. Validate unique slugs, meaningful descriptions, dates and asset/alt-text relationships. Use author/topic constraints only when the project's editorial model needs them.

An article author should have an obvious non-overwriting command or documented example, a complete frontmatter example, a local preview command and the checks to run. New articles should not require changing route lists, fixed page counts or test expectations. Keep authoring helpers typed when part of the Node toolchain.

Emit canonical/social URLs from explicit environment configuration. Production and review origins differ, and a review build should not accidentally index. `robots.txt` must allow a crawler to observe `noindex`; robots blocking is not a substitute for it. A sitemap lists published canonical URLs. Generate RSS only when there is feed content. `llms.txt` and article Markdown are useful machine-readable outputs, not a guarantee of model discovery or use.

Preserve existing clean paths and redirects. A policy URL used by an app store is an external contract; keep that route and relevant links working through migrations. Describe the actual product and operator practices in its policies; do not reuse another product's policy blindly.

## Checks that grow with the site

- Type-check templates, content entries, helpers and operational scripts. Build checks should actually fail on invalid types or metadata.
- Validate local links/anchors, canonical/robots/social metadata, structured data, public asset references and cross-output content agreement.
- Exercise table/figure overflow with keyboard and mobile access; no page-wide horizontal scrolling.
- Isolate content fixtures, build output and writable framework/dependency caches. Sharing installed packages does not make the entire `node_modules` tree read-only. Do not install dependencies concurrently with a build using them.
- Keep historical migration/parity checks separate from ongoing content checks. Approved future changes should not have to match the old site forever.

Official reference: [Astro documentation](https://docs.astro.build). Inspect the installed framework version and its docs before choosing version-specific APIs or configuration.

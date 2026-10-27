# Contribution and continuity contract

Keep project-specific instructions in the project, reusable workflow in this plugin. Use the existing documentation home; when starting from scratch, `docs/product-ux/` is a useful place for the brief, decisions, design notes and release notes. These are small working records, not a required document count.

## Breadcrumbs for the next contributor

The site's README owns setup/build/check commands, source/content/component locations, preview/production hosts, contribution steps, provider configuration and current publishing/rollback evidence. An `AGENTS.md` entry point routes agents to that README and relevant current notes. For Claude Code compatibility a thin `CLAUDE.md` can import the same source with `@AGENTS.md`; verify actual loading in the host rather than assuming a running session reloaded a new file. Follow equivalent established runtime conventions.

The brief records audience, intended action, scope and acceptance. The decision record explains choices and changes. Design notes connect real Superdesign project/draft/element references with actual source component paths and accepted states. Release notes connect reviewed source, uploaded artifact, deployment ID/hosts and recovery target. Keep one owner for each piece of guidance rather than copying commands across several documents.

If this plugin is installed, name its relevant skills in the README. A portable link to [the Product UX repository](https://github.com/moon-research/product-ux-plugin) is more durable than a relative path to an author's private checkout. Record the plugin version used when behavior depends on it. Installing the plugin does not automatically rewrite every project's instructions.

## After each contribution

Record what changed, why, validation, source/deployment state and remaining uncertainty in the existing local log or handoff. A sentence can be enough. Preserve the distinction between an observed result, owner confirmation and an unverified assumption.

When a lesson is reusable, propose the smallest correction in the Product UX repository with the local evidence and affected skill/reference. When it is adopted, link the shared change back to that evidence and the local note to the shared change; apply relevant guidance to the current project. Leave customer secrets and private details out of public examples. Do not edit installed plugin caches as the source of truth.

Local branding, account IDs, copy and domain facts remain local. No new lesson is a valid outcome; do not invent process rules for each routine contribution. Updating a shared guide is not permission to change or redeploy unrelated sites.

Example: a site's build silently inlined a consent script blocked by CSP. The local record names the observed failure, the correction and browser check; a reusable note belongs in the Analytics/build reference. A particular measurement ID does not.

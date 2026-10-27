---
name: publishing-sites
description: "Use when deploying a working site to a Cloudflare Pages review address, promoting an approved site release to production, verifying published links or preparing a rollback."
---

# Publishing sites

Publish the reviewed implementation with a traceable artifact and check the actual result. Superdesign is the design-review destination; Cloudflare Pages serves the working website.

Read the site README, current request and recorded release authority. Establish the exact Cloudflare account/project, production branch, attached hosts and current successful deployment. Follow [the release runbook](references/cloudflare-pages.md). Reuse existing projects and credentials; publishing site files normally needs no DNS change.

Prepare everything that can be reviewed before asking for missing release authority. Use a fresh isolated build of the reviewed source, correct review/production configuration, meaningful artifact checks and an explicit recovery target. Source/config/lockfile and emitted-byte hashes connect the review to the upload; arbitrary existing `dist` is insufficient.

Publish only to the authorized target. Review permission does not authorize replacing a live site, attaching domains or changing mail. A mockup approval settles design, not an unspecified whole-site cutover. Once the user has authorized the concrete release, complete it without asking for duplicate approval.

Record the actual deployment ID/URL/status, then verify HTTPS, important links, policy/legacy routes, redirects, unknown-route 404, canonical/indexing settings, security headers and affected assets on every attached host. Keep browser interaction and Analytics/provider evidence distinct from HTTP checks.

Retain the prior successful production deployment for rollback. On an unclear upload outcome, inspect deployment history before retrying. Update contribution instructions, release evidence and the next contributor's handoff, including honest commit/push state and any verification limits.

Example: publishing to a project's production branch can update both attached `www` and `info` hosts. Establish that whole-artifact scope before upload, then check both hosts; do not repoint DNS to repair a bad release artifact.

The runbook also covers Search Console/sitemap follow-up. Public noindex previews are not private hosting, and sitemap submission does not prove indexing.

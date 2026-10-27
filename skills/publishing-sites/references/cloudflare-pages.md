# Cloudflare Pages release runbook

Use the site's own README for real project/account/branch/origin values and executable commands. This plugin supplies the workflow; it never ships a customer's credentials or a universal production target. Inspect the installed Wrangler's help for current syntax.

## 1. Establish the release and recovery point

Read the current request, site brief/design acceptance, source state and previous release notes. Identify the reviewed implementation and the requested scope: component preview, site preview or production replacement. Review approval does not identify an unspecified production project. Do not reopen settled authority; ask only for missing decisions that materially change the upload.

Inspect existing projects, current successful production deployment, production branch and domain attachments through the dashboard, API or CLI. Typical read-only CLI operations are:

```sh
wrangler --version
wrangler pages project list
wrangler pages deployment list --project-name '<project>'
```

Record the current successful deployment as this release's rollback target. Confirm which hosts share the artifact and what rollback would remove. Capture relevant HTTP/DNS state when cutover or protected mail/verification records are in scope. A DNS comparison is not an email-delivery test.

Keep tokens in existing credential tooling or per-command environment, outside source and output logs. Do not switch unrelated accounts, reconfigure Workspace or change nameservers merely to deploy files to an existing Pages project.

## 2. Build and review the right source

Use the site's guarded preview command if present. Prefer a separate review project without production custom domains when that is the agreed setup. A branch preview on an existing project is another valid arrangement when explicitly understood. Record the actual review deployment and a receipt for source/config/lockfile and artifact hashes. A dry run is not a published review URL.

For production, snapshot the reviewed source and compare its hashes/revision to the review receipt. Explain and review material differences instead of asserting equivalence. Build with the production origin and mode; preview bytes may contain noindex and preview canonical URLs and are not blindly promoted.

Type/build and artifact checks run against the snapshot. Include important policy URLs, local links, metadata, content/discovery agreement and expected scripts/assets. Isolate source/output and writable caches; do not overwrite working review output. Keep dependency installation stable while building. Copy only public build inputs; room notes, credentials and previous output are not inputs.

Keep review noindex/canonical rules separate from production. On production, normal public pages should carry intended indexing settings, while a custom 404 can remain noindex. Preserve legacy app/store policy addresses and compatibility redirects.

## 3. Upload the prepared public output

Before upload, retain a uniquely named source/output receipt and, where useful, the exact public artifact archive. Recheck prepared hashes. Upload the same verified bytes without rebuilding between final check and upload:

```sh
wrangler pages deploy '<prepared-output-directory>' --project-name '<project>' --branch '<branch>'
```

The project's production branch is a live mutation. Use only the named authorized target; a convenient alias is not sufficient evidence of scope. `--commit-dirty=true`, if needed for intentionally uncommitted source, acknowledges Git state and does not commit it.

Record the actual deployment ID, deployment URL and successful status. If a timeout leaves the outcome unclear, inspect history and hashes before retrying; avoid duplicate releases or accidental project creation. Keep the prepared output until the outcome is known.

## 4. Verify outside the build workspace

On every intended custom host, check:

- HTTPS with certificate validation and expected HTTP status.
- Public files matching prepared bytes, including affected images/styles/scripts.
- Homepage/navigation, published articles, company policies and product-specific legacy links.
- Redirect status/location, clean canonical paths and an unknown route returning an actual custom 404.
- Intended indexing/canonicals, CSP/security headers and robots/sitemap/feed/LLM exports when present.
- Relevant desktop/mobile/keyboard interactions and tracking consent/provider receipt, with separate evidence.
- Expected domain attachments and unchanged protected DNS records.

A successful upload does not prove custom-host behavior. Record unavailable checks honestly. Owner confirmation is useful evidence when attributed, not an automated browser trace.

## 5. Recover and hand off

For an authorized release recovery, use the recorded prior successful production deployment in the same Pages project's Deployments view and its rollback action. Check live hosts again. Rollback restores the whole previous artifact; describe lost new routes/features. It normally needs no DNS change. Keep the recovery deployment/artifact available.

The release note includes scope/authority, source revision or hashes, build mode/origin, artifact receipt, account/project/branch, deployment ID, exact live/review URLs, checks/results, evidence limits, recovery target and outstanding work. Keep source, lockfile and contributor instructions versioned so another checkout can reproduce the work. Uploaded bytes alone do not solve an uncommitted-source gap.

After retaining evidence, remove only this release's recorded temporary workspace. Do not delete historical baselines or unrelated branches/output as cleanup.

## Search Console follow-up

Record the site's property and whether ownership verification was checked independently or reported by the owner. Fetch the production sitemap over HTTPS. If account work is authorized and the sitemap has not already been submitted, submit its URL in the property's Sitemaps report; otherwise leave the exact URL for the owner.

Registration, submission, successful Google fetch and indexing are separate statuses. Keep the same generated sitemap as articles are added; successful existing submission normally does not require repetitive manual submission. Do not submit the noindex preview as production. Search Console is separate from Analytics and app/Branding approval.

References: [Pages Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/), [Wrangler Pages commands](https://developers.cloudflare.com/workers/wrangler/commands/pages/), [Pages rollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/), [Search Console Sitemaps report](https://support.google.com/webmasters/answer/7451001?hl=en).

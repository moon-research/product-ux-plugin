# Verification — Product UX 0.1.0

## Baseline before authoring

On 2026-10-27 an independent fresh-context agent responded to the five prompts in `tests/scenarios.json` without reading this plugin. Its responses correctly preserved accepted design, identified missing buyer/action decisions, distinguished mockup and release approval, rejected stale build promotion and recognized content-test isolation. No unsafe behavior was observed; we do not claim a fabricated behavioral failure.

The baseline confirms the model already knows many general practices. The product adds a discoverable, portable package and concrete shared handoffs/references rather than an expanding prohibition list. Before implementation the repository had no plugin manifest or skills, so neither host could discover the requested workflow. Package/utility tests below are the deterministic red/green checks for that missing capability.

The baseline's five next actions were: prepare an evidence-led page brief; prepare scoped alternatives while Superdesign is unavailable; identify release target/scope and prepare a fresh build; add an article and repair relevant test isolation; shortlist offers before writing landing copy.

## Package and utility checks

- Before implementation, `python3 -m unittest discover -s tests -v` failed because `scripts/validate.py` did not exist; the package surface was absent.
- The initial utility implementation passed 11 tests. Independent review then reproduced a real gap: local `.env`, `.DS_Store` and `__pycache__` files nested under a skill were included in a ZIP.
- A new nested-artifact test failed all five subcases before correction. Validation now rejects these local artifacts and packaging leaves no output on failure. Independent review re-ran its original reproducer and confirmed the correction.
- Final fast lane: `python3 -m unittest discover -s tests -v` — 12 tests, all pass. These are utility tests with disposable fixtures, not provider execution evidence.
- `python3 scripts/validate.py` — five shared skills; matching manifests/catalogs; all runtime references remain inside the distribution. A scan of runtime skills/README found no private checkout path, AppFX account/measurement ID or room-publishing command.
- `claude plugin validate .` and `claude plugin validate .claude-plugin/plugin.json` — pass with advisory warnings. The root CLAUDE.md warning is expected: it serves contributors, while runtime context is in skills. A listing icon is absent; public directory submission is outside this release.
- The official skill-creator quick validator requires PyYAML, absent in system Python. No dependency was installed just for that check. Native host parsing and the bundled stdlib validator were used; do not report the unavailable validator as run.

## Behavioral probes

An independent agent exercised requirements, another exercised UX, and another exercised building/publishing from the shipped skills and relevant references. No probe read the author's plan as runtime context.

| Surface | Observed result |
|---|---|
| Requirements / Product Graph inputs | Asked for existing research, proposed a buyer/offer shortlist and wrote a provisional UX handoff without inventing a selected offer. No private repo or Superdev requirement. |
| Selected-section UX | Preserved accepted graph scope, proposed component alternatives, reported unavailable Superdesign access and created a useful provisional handoff with no invented draft URL. |
| Third article | Used the existing content model, dynamic published-entry checks and isolated fixtures/caches while preserving landing-page design. |
| Production preparation | Identified missing target/whole-site authority and fresh reviewed-source needs; did not upload stale dist or treat a mockup as implementation approval. |
| Router | Both native hosts selected requirements before UX for an unselected buyer/offer. |

The early delivery probe noted the shared project-contract reference while it was still being authored. That file now exists and complete package validation confirms the reference resolves. Probes exercised reasoning/handoffs, not live customer-site behavior.

## Claude Code — actual native path

Tested installed version: **2.1.311**.

1. Loaded the checkout through `claude --plugin-dir <checkout>` in a separate empty consuming project with only Read/Skill tools and no provider MCP servers. Its actual tool trace invoked `Skill` with `product-ux:product-ux`, then read the bundled requirements skill and Product Graph input reference. It selected an evidence-backed buyer/offer decision before design.
2. Tested the documented marketplace/install path using a disposable `CLAUDE_CONFIG_DIR`, preserving the normal Claude configuration:

   ```text
   claude plugin marketplace add <checkout>
   ✔ Successfully added marketplace: moon-research-product-ux
   claude plugin install product-ux@moon-research-product-ux
   ✔ Successfully installed plugin: product-ux@moon-research-product-ux
   claude plugin details product-ux
   Skills (5) building-sites, product-ux, publishing-sites, requirements-brainstorming, ux-brainstorming
   Agents (0), Hooks (0), MCP servers (0), LSP servers (0)
   ```

All three commands exited 0. The plugin's estimated token figures are host estimates, not an acceptance/performance claim.

## Codex — actual native path

Tested installed version: **0.164.0**.

A command-scoped marketplace override avoided registering a permanent marketplace:

```text
-c 'marketplaces.moon-research-product-ux={source_type="local",source="<checkout>"}'
```

- Native `plugin list --marketplace moon-research-product-ux --available --json` identified Product UX 0.1.0, local source, AVAILABLE installation and ON_USE authentication policy.
- Native `plugin add product-ux@moon-research-product-ux --json` installed the real package into the host cache. A new Product UX plugin entry was temporarily created; other plugin configuration was left intact.
- Native app-server `skills/list` returned all five namespaced skills enabled, each with pluginId `product-ux@moon-research-product-ux`, UI metadata and its actual cache path. No skill parsing errors were reported.
- A fresh normal `codex exec --ephemeral --sandbox read-only` session first listed the five available namespaced skills, then read the router, requirements skill and bundled Product Graph reference from its installed cache. It selected the correct requirements step without searching the filesystem or reading author planning files.
- An earlier exec probe using `--ignore-user-config` did **not** expose skills; filesystem reads in that probe were not counted as native-load success. The successful proof uses actual installation and a normal configured native session.
- After verification, `codex plugin remove product-ux@moon-research-product-ux --json` removed only this newly created test installation/cache/config entry. Native listing then showed it available but not installed/enabled. The source remains installable; it is not represented as currently installed in the user's regular session.

Observed invocation names:

```text
product-ux:product-ux
product-ux:requirements-brainstorming
product-ux:ux-brainstorming
product-ux:building-sites
product-ux:publishing-sites
```

## Real package operator path

The independent executor/evaluator transcript is in `docs/superdev/checkrides/2026-10-27-product-ux-package.md`. It uses this real repository and its actual ZIP, not a synthetic plugin fixture.

The inspected archive has **26 files**, **52,932 uncompressed bytes**, and SHA-256:

```text
bcafe4ff71821e1e2026fac198a2bd11888ad39fb610b51dbb7facbb46d722b6
```

The existing-output retry exited 1 with a file-exists diagnostic and preserved the exact checksum. The real ZIP unpacked outside the checkout and validated successfully through the public path argument. The independent evaluator returned **PASS**, with no blocking findings; all ten step receipts are recorded in the ledger. One low-priority usability observation is owned here: the diagnostic identifies the existing path but could explicitly suggest choosing a new `--output` filename. README already gives that recovery direction; no deletion is suggested.

## Scope and evidence limits

Superdesign authentication/generation and Cloudflare account/deployment operations were intentionally not executed for this skills-only release. Those workflows require each consuming project's requested work, accounts and authorization. No customer site, DNS, email, Analytics property, live blog or Product Graph marketing page was changed. Provider CLI commands remain subject to their current help/documentation.

Native CLI install/discovery and an actual router task were exercised in both hosts. Other desktop UI versions and approval/listing by public plugin directories were not tested or claimed. The bundled package has no MCP server, runtime hooks, automatic installs or persistent background service.

Source, tests, install/contribution instructions, attribution and evidence are versioned with this repository; release archive generation is explicit and excludes development/planning material. `setup-ux.sh` remains unchanged from the initial repository commit and was never executed.

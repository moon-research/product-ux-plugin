# Product UX

A standalone plugin for Claude Code and Codex: clarify product requirements, review UX in Superdesign, refine web and Android components, build maintainable sites and publish through Cloudflare Pages.

One shared `skills/` tree supplies both hosts. Product Graph can supply research and positioning, but neither Product Graph nor Superdev is required. Superdesign and Cloudflare remain separately authenticated services. Installing this skills-only plugin creates no provider accounts, tracking or live website changes.

## Install in Claude Code

From a terminal with Claude Code installed:

```sh
claude plugin marketplace add moon-research/product-ux-plugin
claude plugin install product-ux@moon-research-product-ux
claude plugin details product-ux
```

Start a new session in the project you want to work on. Invoke `/product-ux:product-ux`, or a specific skill such as `/product-ux:ux-brainstorming`.

For local development, load the checkout directly without registering a marketplace:

```sh
claude --plugin-dir /absolute/path/to/product-ux-plugin
```

## Install in Codex

With a Codex CLI that supports `codex plugin`:

```sh
codex plugin marketplace add moon-research/product-ux-plugin
codex plugin add product-ux@moon-research-product-ux
codex plugin list --marketplace moon-research-product-ux --json
```

For a local checkout, replace the first command's repository selector with its absolute path. Start a new session in the consuming project and invoke `$product-ux:product-ux` or a specific skill such as `$product-ux:ux-brainstorming`. If several plugins supply the same name, select the Product UX entry from the skill picker.

Codex desktop surfaces that expose local marketplaces can use the included `.agents/plugins/marketplace.json`. Open the plugin directory, select the **Moon Research Product UX** source and install Product UX; refresh/restart if newly added files are not discovered. Exact installation surfaces vary by client version; inspect `codex plugin --help` and the current host documentation. CLI/package discovery checks do not prove every desktop build has the same UI.

The package supplies a portable root manifest and Claude/Codex compatibility manifests. Both catalogs point to the same package root; no duplicated skill content or provider MCP configuration is generated.

## The workflow

| Skill | Use it for |
|---|---|
| [product-ux](skills/product-ux/SKILL.md) | Route or resume a task at the right phase. |
| [requirements-brainstorming](skills/requirements-brainstorming/SKILL.md) | Audience, problem, offer, scope, journeys and acceptance. |
| [ux-brainstorming](skills/ux-brainstorming/SKILL.md) | Superdesign visual alternatives and component-level refinement. |
| [android-design](skills/android-design/SKILL.md) | Adaptive Android UI, emulator/capture workflow and evidence-based designer handoffs. |
| [building-sites](skills/building-sites/SKILL.md) | Accepted designs, templates, landing pages and Markdown blogs. |
| [publishing-sites](skills/publishing-sites/SKILL.md) | Cloudflare review deployments, authorized production releases and rollback. |
| [orchestrator](skills/orchestrator/SKILL.md) | Coordinate persistent, enterable Claude rooms and their dependencies. |
| [self-improvement](skills/self-improvement/SKILL.md) | Diagnose workflow failures, fix the source and verify versioned updates. |

For coordinated work, use `orchestrator` to charter requirements, UX and build/review rooms with isolated write ownership and concrete handoffs. Rooms use the installed Claude Code CLI, including when the leader is Codex. There is no separate worker broker or service. See [room mechanics](skills/orchestrator/references/claude-rooms.md) for launch, messaging, attach and same-session recovery. Single tasks can still use a skill directly.

Typical progression: brief/research → requirements → Superdesign review → accepted components → assembled implementation → Cloudflare preview → production. Enter where useful; a small correction does not restart the entire workflow.

Example requests:

- “Use the Product Graph research packet to compare the viable offers and prepare a landing-page brief.”
- “The graph is accepted. Show alternatives for the funnel section in Superdesign, one component at a time.”
- “Assemble the approved sections and add a Markdown use-case blog using our existing style.”
- “Review the Android timer in compact and tablet split windows; prepare the lab request for large text, RTL and keyboard captures.”
- “Prepare a Cloudflare preview, then publish the reviewed release after its production scope is authorized.”

## Integrations and boundaries

[Product Graph input](skills/requirements-brainstorming/references/product-graph-input.md) translates evidence, angles, business cases, suppliers and logistics into public positioning. The plugin builds from supplied research or an ordinary brief; it contains no private research dataset or preselected customer offer.

[Superdesign](skills/ux-brainstorming/references/superdesign.md) is the design-review destination. Use its available official tooling and actual returned draft links. Missing access is reported; the plugin can prepare context but does not fabricate an uploaded design. Design references are linked to source components through notes and visual review.

[Android design](skills/android-design/SKILL.md) preserves the consuming app's actual toolkit and review destination. Invoke `/product-ux:android-design` in Claude or `$product-ux:android-design` in Codex. It covers current app-window dimensions, logical density, font scaling, insets/keyboard, RTL, real screenshots and build provenance. An installed Android SDK/adb, suitable AVD or device and the app's build prerequisites are needed for execution; the skill installs none of them. If a project assigns captures to a lab, the designer sends a request instead of taking over its devices. Otherwise the authorized operator can follow the inspected CLI/SDK launch and capture recipes. App implementation and Play release remain under the app's own instructions.

[Site/content guidance](skills/building-sites/references/static-sites.md) covers typed templates, Markdown authoring, shared published-content outputs, robots/sitemap/RSS/LLM exports and isolated checks. It preserves an existing stack and offers Astro as a reference when appropriate. It is guidance, not an embedded Astro application or a framework installer.

[Analytics](skills/building-sites/references/analytics.md) reuses the Firebase CLI and Google tag pattern when measurement is requested. Each site supplies its own account/project/measurement configuration and actual consent/privacy practices. No Firebase Hosting, SDK or Analytics service is installed by this plugin.

[Cloudflare publishing](skills/publishing-sites/references/cloudflare-pages.md) uses existing authorized account/project configuration, fresh reviewed-source artifacts, actual host checks and a concrete rollback point. A preview does not authorize production or DNS/email changes. Once a release is authorized, the workflow completes it without repeated approval requests.

Authentication, form handling, databases and a specific product's new landing-page content need their own brief. This package delivers the reusable capability; it does not publish a Product Graph marketing site by installation.

## How to contribute

Clone this repository and read `AGENTS.md`. Claude Code's `CLAUDE.md` imports the same instructions. Edit shared skills and their focused references; keep runtime manifests thin and consistent. The project contract describes [contributor breadcrumbs and the learning loop](skills/product-ux/references/project-contract.md).

From a **repository checkout** with Python 3.9+:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
claude plugin validate .
```

The validator checks this package's supported scalar frontmatter, matching metadata, contained references and archive inputs; it is not a general Agent Plugins/YAML schema validator. Host-native validation/discovery complements it. Utility tests run in disposable directories. Behavioral scenarios are in `tests/scenarios.json`; execute changed workflows in a fresh context and record outcomes/limits in `docs/verification.md` and the version-specific verification note.

For a release, update the version in all three manifests, run the checks and native discovery tests, then create a new archive without overwriting existing output:

```sh
python3 scripts/package.py --output /tmp/product-ux-0.3.0.zip
```

The ZIP contains only manifests/catalogs, shared skills, this README, LICENSE and NOTICE. Repository setup, tests, planning records, environment files and Git data are excluded; local environment/Git/cache artifacts nested inside `skills/` cause validation to fail. Development utilities are used from a checkout, not from that runtime ZIP. The existing `setup-ux.sh` is an optional machine-bootstrap script, preserved separately; never run it as a plugin install or validation step.

Commit/push reviewed source to the repository. Catalog installs follow their configured Git ref; update the installed plugin through the host's update/refresh mechanism and start a new session. A GitHub release/archive is separate from acceptance into a public host directory; do not describe a repository push as directory approval.

Keep site-specific evidence local. Use [self-improvement](skills/self-improvement/SKILL.md) for a reusable correction: diagnose the actual input/return boundary, make the smallest authorized source fix, update the version and release notes, verify the affected scenario and confirm the installed snapshot/reload state. Link the adopted plugin change back to the originating project. Do not edit installed cache copies as the maintained source.

## Sources

Requirements exploration, orchestration and self-improvement adapt the Superdev/Superpowers approach; retained attribution is in NOTICE. Site delivery generalizes the AppFX collaboration and Product Graph site playbook.

The Android workflow generalizes verified practices from Pomodrone's designer/lab and gallery tooling. Device-lab ownership and project-specific values stay in the consuming app. Coordination refinements also draw on room-graph-orchestration; see NOTICE. The scans and verification limits are recorded in `docs/verification-0.3.0.md` in the repository checkout (development notes are not in the runtime ZIP).

Host references: [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins), [Claude plugin manifests](https://code.claude.com/docs/en/plugins-reference), [Claude marketplaces](https://code.claude.com/docs/en/plugin-marketplaces). See the integration references for provider documentation and current-command checks.

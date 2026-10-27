# Standalone Product UX implementation plan

**Goal:** Deliver the approved requirements → UX → implementation → publishing workflow as one independently installable Claude Code and Codex plugin.

**Architecture:** One shared `skills/` tree. Root Agent Plugins metadata plus thin Claude/Codex compatibility manifests and native marketplace catalogs. Focused references carry optional Product Graph, Superdesign, Astro/blog, Analytics and Cloudflare details. No server, hooks or application runtime is required.

**Execution:** inline for the cohesive skills/documentation package; independent agents exercise baseline scenarios and review the completed package. User approved work in this repository on 2026-10-27. Work on `feat/standalone-product-ux` in the newly cloned checkout; no extra worktree is needed for this isolated repository task.

**Mode:** autonomous within the approved plugin scope. No new live website, domain changes, provider account provisioning or public plugin-directory submission.

**Context pack:** [proposal](../specs/2026-10-27-product-ux-proposal.md), [decisions](../specs/2026-10-27-product-ux-decisions.md), [census](../specs/2026-10-27-product-ux-census.md). The proposal is the approved design anchor with the decisions below. No application-domain or API migration; domain/pipeline/CLI companion documents are not required for the instruction package. Command behavior of package utilities is specified in their tests and README.

## Constraints and verification

- Preserve `setup-ux.sh`; never run it as part of install or testing.
- Runtime skills work without private repositories, room infrastructure or Superdev. Superdesign and Cloudflare are separately authenticated integrations used only for their requested stage.
- Keep portable skills in one place. Thin host metadata must agree on identity/version. Preserve upstream MIT attribution for adapted brainstorming guidance.
- Use standard-library Python for package validation/archive generation. No installed runtime dependencies or secrets.
- Fast lane: `python3 -m unittest discover -s tests -v` and `python3 scripts/validate.py`.
- Packaging lane: create an archive in a disposable directory and inspect/extract its exact contents; reject existing output and symlinks.
- Host lane: Claude manifest validation and skill discovery; Codex marketplace discovery/install using command-scoped marketplace configuration; when native installation requires a cache/config entry, remove only the newly created Product UX entry after the test, preserving other plugins.
- Behavioral lane: fresh-context tasks without and with the skills, covering all five entry points. Save findings and honest limits; never perform a real site deployment for a plugin test.
- Engineering patterns: stdlib Python for small utilities, focused functions and explicit failures; no project canon declared. Apply process-discipline guidance used by the development session, without making it a runtime dependency of this plugin.

## Tasks

- [x] **1. Freeze acceptance and record baseline.** Record user approval, Superdesign decision and the reusable-landing-page interpretation. Save five realistic scenario prompts before authoring skills and inspect no-skill responses. Acceptance: the package covers each proposed skill, resumes small tasks without replaying the entire workflow, and identifies missing provider access honestly.
- [x] **2. Package shared skills.** Add portable/Claude/Codex manifests and catalogs; write each skill with only its necessary linked references and verify it before moving to the next. Include examples of Product Graph input, requirements/UX handoff and per-project learning. Acceptance: all links resolve after copying the package outside this repo; no private paths/account IDs or undeclared mandatory companion skills.
- [x] **3. Make the product installable and maintainable.** Document actual Claude/Codex commands, local development, provider prerequisites, invocation examples, contribution and releasing. Add contributor entry points and upstream notice. Write utility tests first, then the package validator and explicit allowlist archive generator. Acceptance: incomplete or unsafe packages fail with actionable diagnostics; archives contain only the distributable runtime and install documentation.
- [x] **4. Exercise and deliver.** Run real host discovery/installation in disposable settings, behavioral probes, archive validation and independent review. Fix confirmed issues. Commit and push the feature branch to the supplied repository and open a reviewable PR if available. Acceptance: provide exact Git state, validation receipts, remaining integration limits and install links. Never claim a public directory listing or live site release.

## Acceptance receipts

Record executed commands/results in `docs/verification.md`; mark each task only after its checks pass. Keep behavioral prompts under `tests/scenarios.json`; model responses belong in the verification report or a temporary review workspace, not a new operational framework.

## Package operator verification plan

Use the real repository and generated release artifact, with the scenario in `../scenarios/2026-10-27-product-ux-package.md`. The executor proposes one command at a time; an independent evaluator rules before execution and judges the actual result. Cover command discovery/validation, archive creation, repeated-output refusal and unpacked-package validation. Record the command, output, exit status and judgment in the checkride ledger. No synthetic plugin fixture is used for this final operator path.

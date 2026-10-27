# Verification — Product UX 0.3.0

Recorded 2026-10-27. Scope: portable Android designer guidance, small orchestration/evidence contract refinements and a separate Pomodrone contributor quickstart. No app source change, app release, customer-site deployment, Play/account write or new orchestration service.

## Sources and behavioral evidence

The [scan record](superdev/scans/2026-10-27-orchestration-android.md) records the prior art and known/carried/received gaps. Baseline fresh-context agents already respected Views, lab ownership, stale APK limits and independent work. Specific omissions were current-app-window measurement, immutable capture paths and an explicit response when accepted evidence is later contradicted. No fabricated broad baseline failure is claimed.

A fresh application agent read the new Android skill and all three references, then applied both the lab-owned Pomodrone scenario and a standalone authorized operator scenario. It produced a concrete capture request, distinguished target dp from observed window bounds, required actual build provenance and separated Android CLI flags from SDK backend flags. It preserved lab ownership and chapter cadence. Its remaining suggestions led to explicit port-race/launch-failure protection and a raw window-receipt route with unmeasured values marked UNDECIDED.

An independent reviewer inspected both repository diffs and replayed the invalidated-handoff case. It held affected R4 work, required leader/decision-owner resolution and an exact-input consumer receipt, continued the article independently and preserved superseded evidence without reusing it. Its only initial blocker was the then-unwritten verification report; this file closes that documentation gap. Follow-up review of the runtime refinements found no new blocker and confirmed the app guide is discoverable without changing local design policy.

`tests/scenarios.json` now has eleven replayable cases, including Android design, standalone operation and invalidated handoffs. These are human/agent prompts and checks, not an automated model grader. The fresh probes were planning/application checks; they did not verify Pomodrone's current layout.

## Native host discovery

Claude Code **2.1.311**: a disposable `CLAUDE_CONFIG_DIR` was used to add this checkout as a local marketplace, install Product UX and inspect native details. It reported **0.3.0** and eight skills:

```text
android-design, building-sites, orchestrator, product-ux,
publishing-sites, requirements-brainstorming, self-improvement,
ux-brainstorming
```

No agents, hooks, MCP servers or LSP servers were bundled. This test did not change the normal Claude profile.

Codex CLI **0.164.0**: confirmed no pre-existing Product UX installation, used a scoped local marketplace configuration, installed **0.3.0**, then queried native app-server `skills/list`. All eight `product-ux:` skills were enabled, including `product-ux:android-design`. Removed only this test install/cache afterward. Other plugins were preserved. No Codex room runtime was introduced.

These checks establish native discovery, not public directory approval or every desktop version's UI. The 0.2.0 room handshake/attach/same-session resume exercise remains historical evidence in [its report](verification-0.2.0.md); those native mechanics were not changed or repeated here.

## Actual emulator and screenshot transport

Installed tools observed: Android CLI **1.0.16261425**, SDK emulator **37.1.11.0**, adb **1.0.41** / platform-tools **37.0.1-15733141**. Inspected current start/run/capture help, AVD inventory and port availability. No SDK images or tool updates were installed.

Existing devices were inventoried without changing them. When the bounded exercise began, only the owner's API37 instance remained. Launched an unused `phone35` AVD as one owned **windowed, read-only, no-snapshot** SDK instance on the project's lab port, with a bounded boot check. It reported boot completion. Selected only the owned serial, opened the Android launcher and captured:

- Raw `adb … exec-out screencap -p` PNG: **1080 × 2400**, API35, logical density420, font setting1.0. Opened the actual image and inspected it; it showed the Android launcher.
- `android screen capture --device=… --output=…`: exit0 and a second **1080 × 2400** PNG.

Original adb PNG SHA-256: `693028ff5dc9051a3ea8c0a16fa3b4835ef6f47e364e4debaa27eb67ff0cb82e`.

Raw images and local receipt are retained under ignored `dist/verification-0.3.0/`; they are not packaged. This is **launch/capture transport evidence only**, not Pomodrone UI acceptance, current-source build proof, accessibility coverage or a measured adaptive matrix. No APK was installed and no app build was performed. Existing app output was historical; it was not relabeled as current.

Stopped the owned emulator through its exact serial and confirmed it exited; final device inventory retained the owner's original instance. No global kill/reset, other-device settings, user accounts or persistent AVD state were changed. Backend help's printed port range lagged the project's existing lab recipe; the bounded actual launch established the selected port worked with this installed backend, not a universal range claim.

## Package and local documentation checks

- `python3 scripts/validate.py`: eight skills, matching manifests/catalogs and contained references.
- `python3 -m unittest discover -s tests -v`: all **12** utility/package tests passed.
- `claude plugin validate .`: passed with existing advisory warnings for contributor-only root CLAUDE.md and missing public-listing icon.
- `git diff --check`: passed in both the plugin checkout and isolated app documentation worktree.
- App guide links resolve to tracked local sources; `tools/gallery/m2_gallery.py --help` confirms `--states`, `--driver-root`, `--configs`, `--font` and `--reviewed`. Help invocation performed no build or device action.
- The archive contains **39 files**, **98,866 uncompressed bytes**. Every member matched runtime source bytes. Extraction to a fresh directory passed validation. An initial validation invocation used an unsupported `--root` option; reran successfully with the documented positional path. This was a command-invocation correction, not a hidden package failure.

Archive: ignored `dist/product-ux-0.3.0-final.zip`.

SHA-256: `36fec4c33b1cf529ce14af38ebb16bfc075bc96ccd985052998dd58507ce1903`.

Pomodrone's guide and designer-skill breadcrumb live on `docs/product-ux-designer-guide` in an isolated documentation worktree. They do not alter its app, design system, roadmap, protocol or master branch. Delivery links and source commits are recorded in the task's final handoff. Catalog installations from main will gain this release only after the plugin PR is merged and the host refreshes; no normal user plugin snapshot was upgraded by these tests.

## Git delivery boundary learned during this task

The app guide is committed locally as `809c93df` on `docs/product-ux-designer-guide`. The app's actual GitHub master is over 2,000 commits behind its working checkout. A first SSH attempt failed; an HTTPS attempt using existing GitHub authentication timed out locally but its transport briefly completed the new branch. No PR was created. After checking the actual remote base and detecting the unrelated outgoing history, removed only the newly created branch after verifying its SHA matched this task's local commit. A subsequent API check returned404 for that ref; remote master remained unchanged. The local guide/worktree is preserved for review. No app origin/settings/credentials were changed.

The missed check was the actual remote base **before** pushing. The shared contribution contract now requires the full outgoing commit/file range, not just the last commit's diff; shipping links that boundary. A fresh-context regression applied it to the same 2,000-commit scenario and refused the push, preserving the local guide or preparing against an authorized published base instead. This is observed failure plus a planning regression, not proof of a new automated Git guard. The final archive above includes this focused correction; the earlier reviewed ZIP is retained as an intermediate artifact.

The standalone plugin continues through its existing PR #2; this app delivery exception does not authorize uploading unrelated app history. Normal catalog/installed state remains pending merge and refresh.

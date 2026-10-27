# Verification — Product UX 0.2.0

Recorded 2026-10-27T15:08:16+00:00. Scope: add `orchestrator` and `self-improvement` to the standalone plugin. The HUMAN explicitly chose Claude rooms and excluded codex-worker. No Codex room/worker or alternative room daemon was launched.

## Source and behavioral review

Read Superdev's orchestrator, room mechanics/contract/durable-state guidance and self-improvement/flow-mapping guidance as prior art. Adapted the necessary mechanics into this package, retaining MIT attribution; no Superdev source or installed snapshot was modified.

A baseline agent considered both new scenarios before seeing the new skills. It already knew useful generic coordination and focused-fix practices; no fabricated unsafe baseline failure is claimed. The package adds discoverable instructions, concrete native room mechanics and a maintained handoff/update contract.

An independent agent then applied the new runtime skills and references to the requirements → selected offer → UX → build dependency case and the omitted-component-path failure. It preserved prior authority, held dependent rooms until their inputs existed and diagnosed the actual emitted/consumed contract rather than blindly adding a field already present. It confirmed no private Product Graph/Superdev runtime dependency. A final re-read of the corrected native mechanics, metadata and the seven replayable scenarios found no remaining source/documentation blockers.

## Actual Claude room exercise

Installed native CLI: Claude Code **2.1.311**. The bounded test used a read-only Claude session in an isolated Git worktree, with no file writes, shell tools, design generation or site deployment requested. Its actual data was the current plugin/runtime and a unique conversation marker; this is native transport/recovery evidence, not proof of a business workflow or provider-side design integration.

Session name: `ux-orchestration-smoke-1793113125`.
Original session UUID: `e08a9b74-1747-46d1-b9d8-f9475bd69aaf`.

1. Created a test worktree from the pushed source revision, with a uniquely owned branch.
2. Initial native background launch refused the new untrusted workspace before creating a room. Used the normal interactive trust flow after reviewing this self-created worktree, without global bypass settings. The guide now documents this preflight.
3. Launched using native `claude --bg --plugin-dir <source>`, a unique name, per-session `crossSessionInbound: accept`, and only Read tools under dontAsk. Actual launch returned:

   ```text
   backgrounded · e08a9b74 · ux-orchestration-smoke-1793113125
   claude attach e08a9b74
   ```

   `claude agents --json` identified the same UUID as a background session in the assigned worktree. The observed assistant output was `ROOM_READY CEDAR-742`.
4. Sent a single message to that exact room through a restricted native Claude `SendMessage` relay, using argument-vector invocation and no extra provider tools. Message ID: `4c13f643-ee68-4914-9632-dd3825a06101`. The relay first reported queued/sent only; that was not treated as an acknowledgment. The actual receiver transcript subsequently contained:

   ```text
   RECEIVED_SEQUOIA CEDAR-742
   ```

   The marker was not supplied again by the handshake, so this also demonstrated continuing conversation context. Native status returned idle/done.
5. Stopped the original session. A first resume attempt repeated launch options and created copy `4e797058-483f-4b79-9f54-71c59a704243`. The UUID assertion failed and prevented a false same-room success claim. The CLI explicitly explained that repeating flags started a copy.
6. Stopped that owned test copy. Corrected the guide at the native-mechanics boundary, then ran:

   ```text
   claude --bg --resume e08a9b74-1747-46d1-b9d8-f9475bd69aaf <continuation>
   backgrounded · e08a9b74 · ux-orchestration-smoke-1793113125
   note: woke session e08a9b74 with its saved options ...
   ```

   Native inventory confirmed the exact original UUID. The assistant replied `RESUMED_JUNIPER CEDAR-742` without receiving the original marker again.
7. Ran `claude attach e08a9b74` in an actual terminal. The room UI opened with its name and retained response. Detached the test client and stopped only the owned room.
8. Removed the two exclusively test-created background sessions after preserving these receipts; both native remove commands returned success. The clean, unchanged test worktree/branch and scratch files are removed during delivery cleanup.

The lesson is concrete: in this CLI version, same-room resume uses saved options. Repeating plugin/settings/name launch flags creates a fork even when the original is stopped. The corrected runtime guide and orchestration scenario encode that behavior. A different returned UUID must remain a failed recovery, not a silent replacement.

## Native plugin discovery

Claude: native marketplace add/install in a disposable configuration, then `claude plugin details product-ux`, reported **Product UX 0.2.0**, the updated description and seven shared skills:

```text
building-sites, orchestrator, product-ux, publishing-sites,
requirements-brainstorming, self-improvement, ux-brainstorming
Agents (0), Hooks (0), MCP servers (0), LSP servers (0)
```

Codex CLI **0.164.0**: native Product UX 0.2.0 installation and `skills/list` exposed the same seven namespaced skills enabled, including `product-ux:orchestrator` and `product-ux:self-improvement`. This was a plugin-inventory check only. Codex did not execute any room task. The newly created test installation/cache/config entry was removed afterward, leaving other plugins intact.

The initial 0.1.0 native router tasks remain historical evidence in `docs/verification.md`; their counts/hash are not presented as the new release's receipt. Desktop directory approval and every desktop version are not tested or claimed.

## Package checks

- `python3 scripts/validate.py`: seven shared skills, matching manifests/catalogs, contained references.
- `python3 -m unittest discover -s tests -v`: all 12 package/utility tests passed.
- `claude plugin validate .`: passed, with the existing advisory warnings for contributor-only root CLAUDE.md and missing public-listing icon.
- `tests/scenarios.json` now has seven realistic cases, adding orchestration and self-improvement. These are replayable prompts/checks, not a claim that an automated model-grading harness exists.
- The reviewed ZIP has 34 files and 74,940 uncompressed bytes. Every file was compared to the current runtime source, then extracted outside the checkout and validated successfully.

Archive: `dist/product-ux-0.2.0-reviewed.zip` (ignored generated output).
SHA-256:

```text
cbc373f28259c758d9736d58446c6b2e9719456e81f288fdee22d6be4228b21e
```

An earlier unshipped 0.2.0 development ZIP was superseded and removed; the separate original 0.1.0 archive remains unchanged. No overwrite guard was disabled.

## Delivery boundaries

The initial 0.1.0 PR #1 was already merged at `a026866`. This additive change is delivered from that merged baseline on `feat/claude-room-orchestration` in a follow-up PR. Default-ref installs receive 0.2.0 when that follow-up is merged. The source guides distinguish existing edit authorization, repository review, installed snapshot refresh and running-session reload.

No live customer site, DNS/email, Google account/property, Superdesign draft or Cloudflare deployment was changed. No plugin cache was edited as the maintained source, and no polling service or scheduler was installed. Raw test scratch was retained until the source receipts and reviewed archive were preserved, then removed.

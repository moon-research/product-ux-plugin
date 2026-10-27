# Product UX orchestration and self-improvement plan

User scope: add standalone orchestrator and self-improvement skills, adapting Superdev; explicitly use Claude rooms and skip codex-worker. The plugin remains usable by Claude and Codex leaders.

- [x] Add orchestrator skill: room graph and charters, isolated workspaces, Claude native spawn/attach/status/messages, read-only handshake, recovery, release boundaries and closing. Bundle mechanics and a concise room contract; no private room infrastructure, Codex worker or background polling daemon.
- [x] Add self-improvement skill: evidence, live information-flow map, smallest fix in source, existing authorization, focused regression, version/catalog update, actual install/reload verification and bidirectional learning. Include a small feedback/diagnosis reference.
- [x] Extend router, project contract, README, attribution and three manifests to 0.2.0; record changes in CHANGELOG. Preserve 0.1.0 historical verification.
- [x] Exercise actual Claude spawn → message → stop/resume on a bounded read-only room in an isolated worktree, and realistic self-improvement probes. Run package/host checks, create a separate 0.2.0 archive and deliver a follow-up PR from the merged 0.1.0 baseline. Never modify Superdev or other live rooms, account settings, domains or sites.

Acceptance: seven skills are discoverable in both hosts; a leader can launch and contact an enterable Claude room using bundled instructions; session IDs/transport states are observed, not invented; a resumed room preserves context; self-improvement changes the source and versioned package without requiring Superdev or editing an installed cache. Static tests are not presented as proof of room delivery.

Source evidence read on 2026-10-27T14:55:14+00:00: /Users/tadas/Projects/superdev/skills/orchestrator/{SKILL.md,room-mechanics.md,room-brief-template.md,durable-state.md} and skills/self-improvement/{SKILL.md,flow-mapping-guide.md}. Superdev's private corpus/registry conventions are not copied as runtime dependencies. Actual installed Claude CLI help establishes --bg, --resume, --plugin-dir, agents --json, attach, logs and stop.

Delivery adjustment: PR #1 was discovered already merged at its 0.1.0 head. The 0.2.0 commit is carried on a new branch from origin/main; historical PR #1 metadata is restored to its actual merged scope.

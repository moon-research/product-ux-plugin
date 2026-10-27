---
name: orchestrator
description: "Use when coordinating product UX work across persistent Claude rooms that the user can enter and resume, with dependencies, separate write ownership and shared delivery checkpoints."
---

# Product UX orchestrator

Coordinate full, enterable Claude sessions. Temporary subagents can help inside a room, but they are not rooms. Either Claude or Codex can lead; the room runtime is Claude Code's native background sessions.

1. Read the current brief, decisions, accepted designs, source/release state and existing room records. Explain the proposed room graph in business terms. Start only rooms the current task authorizes; do not rebuild an existing room graph merely because a session changed.
2. Give each room an outcome, inputs, dependencies, workspace/write ownership, relevant bundled skills, acceptance and reporting contract. Use [the room contract](references/room-contract.md). Requirements must settle the offer before dependent UX work; accepted UX must be available before its implementation. Independent inventory/research can proceed in parallel.
3. Follow [Claude room mechanics](references/claude-rooms.md) to launch a uniquely named session from its isolated workspace. Record the actual session ID and attach command. Send a harmless handshake and confirm a reply before relying on cross-room delivery. A queued message is not receipt of the work.
4. Maintain a small durable room table and cursor: current phase, dependency state, actual session/worktree, reviewed outputs, last evidence, blocker, next action and release authority. Resume from files plus native status after compaction or machine sleep. Give decisions and source paths to the next room explicitly; the leader's memory is not shared context.
5. Review reports against the actual artifacts and checks. Keep human decisions at meaningful boundaries: offer/positioning, visual selection, wider scope and production release. Continue authorized independent work while a dependent decision is pending. Do not silently convert a provisional direction into accepted public copy.
6. Close with integrated review, working links, checks, recovery, owned remaining work and contributor handoff. Route publication through `publishing-sites`. Retire only owned sessions/workspaces after preserving their useful output; do not delete unmerged work or another room's state.

Use one project integration branch for collaborative code when appropriate. Each room commits its own source and reports the commit; the charter names who integrates it and which checks must pass. Never imply a room's uncommitted files exist in another worktree.

Capture recurring handoff/process failures with evidence for `self-improvement`. The orchestrator can improve the next room's brief within scope; changing the reusable plugin follows that separate skill.

For a single section, article or small correction, run the relevant skill directly. Orchestration is an optional coordination layer, not a prerequisite for ordinary site work.

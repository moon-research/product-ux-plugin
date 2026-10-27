# Android design toolkit and orchestration scan

Approved scope: audit Superdev and related orchestration; add a reusable Android design skill grounded in the Pomodoro project and a small app-local designer quickstart. Claude-only rooms remain the runtime choice. This is not an app redesign or release.

- [x] Read-only scan: Superdev, room-graph-orchestration, Product Graph native room contracts; Pomodrone production/design/lab/Android CLI references.
- [x] Add `android-design` with focused adaptive-layout, emulator/device, raw screenshot/evidence and designer-handoff references. Reuse existing tools instead of a new automation framework. Support Views/Compose/Flutter according to the actual consuming target, not a forced migration.
- [x] Apply small orchestration fixes for invalidated inputs, consumer grounding receipts, peer disagreements and superseded evidence. Keep existing launch/recovery mechanics.
- [x] Add app-local commands and source pointers in an isolated Pomodrone documentation worktree, respecting the current designer/lab split and avoiding app code or design decisions.
- [x] Bump Product UX to 0.3.0, update routing, discovery, release/contribution guidance and replayable scenarios. Verify native package discovery, external extraction and bounded emulator screenshot instructions; preserve existing devices and use an explicitly owned test slot only.
- [x] Independent review and separate app documentation branch. App guide is committed locally as `809c93df`; its temporary remote branch was removed after discovering unrelated unpublished history (D10). Product UX commit/push and PR #2 update are the final delivery steps.

Grounded 2026-10-27T16:30:33+00:00. App source is `/Users/tadas/Projects/pomodrone/Pomodrone` (Views). `/Users/tadas/Projects/pomodoro/focus-ecosystem` is competitor research, not app source. Android CLI, SDK emulator and adb are installed; two emulators were already active and are not owned by this task. Existing app debug APK is historical, not evidence of the current source revision.

Useful sources: Pomodrone CLAUDE.md; .claude/skills/android-designer/SKILL.md; .claude/skills/android-cli; .claude/skills/android-e2e-tester/references/{large-screens,locale-layout-check,device-catalogue}.md; tools/gallery/{README.md,CAPTURE-DETERMINISM.md}; docs/design/PROTOCOL.md. Scan detail and actual checks will be recorded in version-specific verification.

# Orchestration and Android design scan

The user authorized scanning Superdev/other orchestration and the Pomodoro project, adding a portable Android design skill and leaving app-local designer instructions. This is a toolkit change, not an app redesign, app release or new room service. Rooms remain Claude-only; either host can lead.

## Sources inspected

- Superdev: orchestrator, room brief/communication/protocol, dependency and failure/return guidance; skill authoring and self-improvement. Existing Product UX launch, handshake, durable state and same-session recovery already cover the necessary native mechanics.
- room-graph-orchestration: failure modes, protocol and graph edge/authority guidance. Product Graph's orchestration/room contracts were comparison inputs; neither room graph becomes a runtime dependency.
- Pomodrone production checkout: `CLAUDE.md`, `.claude/skills/android-designer/SKILL.md`, Android CLI and e2e tester references, `docs/design/PROTOCOL.md`, orchestration conventions, `tools/gallery/README.md`, capture determinism, E2E environment, manifest and build configuration.
- Official Android documentation and the actually installed Android CLI/SDK/adb help. Provider links and the date checked live in the portable references.

The app is native Views. The similarly named Pomodoro folder contains competitor research; the gallery and POC are evidence/tooling, not a Flutter production app. Existing build output was historical and was not assigned today's source identity.

## Adopted changes and why

| Boundary | Existing behavior / evidence | Smallest adopted change |
|---|---|---|
| Accepted input becomes stale | Leader reviews READY output, but later contradiction was not explicit. Baseline replay identified this gap. | Name invalidated revision, affected consumers, decision owner, replacement and resume check; preserve independent work. |
| Producer → consumer | Exact paths were already required; leader inspection alone did not prove consumer grounding. | Consumer names revisions/files/states actually inspected and missing mappings. |
| Peer → leader | Direct technical exchanges are useful, but a peer cannot accept a new direction for another role. | Initiator returns conclusion/changes to leader; unresolved authority conflicts hold affected work. |
| Capture → conclusion | Baseline agent respected lab ownership/stale APKs, but used display receipts without an explicit app-window measurement and overwritable example paths. | Current-window/logical-density review, build lineage, fresh raw files, visual inspection and explicit evidence limits. |
| Shared skill → app | Pomodrone already has mature lab/gallery ownership and chapter publication. | Portable skill plus a narrow local quickstart; reuse gallery rather than duplicate tooling or change designer policy. |

No invented unsafe baseline is claimed. The baseline Android plan already preserved Views, lab operation and chapter review, rejected old-APK current-UI proof and used logical density. The orchestration baseline also reasoned sensibly about stale evidence; the package lacked an explicit maintained response contract. These are targeted retrieval/output-shape improvements, not evidence that agents always fail without the plugin.

## Local versus portable

The portable skill contains conditional lab/direct-operation routes, current-window review, inspected command recipes, provenance and handoff rules. It contains no Pomodrone application IDs, private driver roots, preset sizes, font ceiling, release targets or room-port defaults.

Pomodrone's separate documentation branch contains its actual variant, launcher, gallery flags, protocol links and ownership. The current protocol's publish-once-per-chapter ruling remains authoritative over older brief cadence. Designer-owned topics, roadmap, design system and app source were not edited.

No Superdev, orchestration or Product Graph source/cache was changed. Retained attribution is in NOTICE. Product UX source changes do not automatically refresh any installed plugin snapshot or another project's instructions. Version-specific verification records the tested host/tool behavior and limits.

## Delivery correction

The app-local guide exposed one additional real gap: a docs-only last commit did not mean a docs-only push, because local master contained a long unpublished history. The temporary remote branch was removed after SHA ownership verification; the guide stays committed locally. Product UX's contribution contract now requires an actual remote base and full outgoing range before Git delivery, with a scenario proving the intended refusal/preservation behavior. Details and verification limits are in the 0.3.0 report.

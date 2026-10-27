---
name: android-design
description: "Use when designing or reviewing an Android app screen, adaptive phone/tablet/foldable layouts, font scaling, insets or RTL, or when a designer needs emulator launch and real-device screenshot evidence."
---

# Android design

Ground visual decisions in the app's actual UI and current window. Read the project's designer, developer and device-lab instructions first. Preserve its toolkit: Views, Compose or Flutter as found; this skill does not authorize a migration or app release.

1. Establish the selected screen/component, accepted surroundings, unresolved decision and relevant states. Inspect source, design tokens and current design artifacts. Use [UX brainstorming](../ux-brainstorming/SKILL.md) for visual alternatives, with the project's existing review destination. Work one component at a time when requested; retain approved sources and renders beside the decision.
2. Build a small [adaptive review matrix](references/adaptive-layouts.md) from current **app-window** bounds, logical density, font scale, orientation, locale and system UI. A device label or `wm size` alone does not establish usable window size. Separate window variation from API variation.
3. Follow [the emulator workflow](references/emulator-workflow.md). If a lab owns devices, send a capture request with exact build, states and matrix; the designer does not take over its emulators. Otherwise use an explicitly owned slot, inspect installed command help and select a serial for every device command. Reuse existing gallery/capture tools.
4. Review [raw captures and evidence](references/screenshots-and-handoff.md), including keyboard, bars, large text and RTL where relevant. Distinguish observed pixels, source findings and design judgments. A historical APK, mockup or synthetic state is not proof of the current app's behavior. Numeric checks supplement image inspection.
5. Record the chosen design, exact source/design revision, tested configurations, defects, untested states and implementation owner in [the handoff](../ux-brainstorming/references/design-handoff.md). The consumer acknowledges what it inspected. Contradicted evidence invalidates affected dependent work until its owner resolves it; independent work can continue.

Keep package/activity IDs, device leases, project-specific font limits and capture paths in the consuming project. Restore settings you changed and stop only an emulator you started. Publication follows the project's existing acceptance rules.

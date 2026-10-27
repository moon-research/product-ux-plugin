# Review the current app window

Inspect the existing toolkit, layout resources/components, minimum/target API, manifest resize/orientation behavior and design system. Views resource qualifiers and WindowManager guidance differ from Compose APIs; Flutter has its own logical layout coordinates. Keep the current implementation unless a migration has its own brief.

## A small, purposeful matrix

Start with the selected surface and the configurations likely to change its layout. Record actual window width **and height**, API, logical density, font scale, locale/layout direction, orientation, navigation mode and relevant system UI. Include a constrained window as well as a roomy one. A tablet in split screen can have a compact window; rotating or resizing can change class without changing devices.

Android's width classes are compact below 600dp, medium 600–839dp, expanded 840–1199dp, large 1200–1599dp and extra-large from 1600dp. Treat these as planning vocabulary, not an instruction to redesign at every boundary. Check just below/above a breakpoint actually used by the app. Short height, near-square, split/freeform and fold posture can matter more than a device's marketing category. Hold API constant while exploring window layouts, then vary API for platform behavior.

| Dimension | Useful checks |
|---|---|
| Space | Small supported width/height, ordinary phone, larger window, rotation, live resize/split/fold when supported. |
| Text | Default and large system text, long translations, actual RTL language, bold text if relevant. |
| System UI | Gesture/three-button navigation, status/cutout/navigation insets, keyboard and modal states. |
| Interaction | Idle/running/paused or equivalent product states, focus, errors, empty/loading where applicable. |

Choose relevant cells; don't claim a full cross-product from two screenshots. Mark missing cells **PENDING** with an owner or reason.

## Measurement traps

- Android dp derives from **logical** density: `dp = px × 160 / densityDpi`. Physical screen PPI is not the layout density. Record both base and override values from `wm density` when present.
- `wm size` describes a display, not necessarily the current app window or content area. Inspect the foreground window/activity's bounds and visible insets, using existing probes, WindowMetrics or the project's layout tooling. Keep global screenshot coordinates distinct from app-local coordinates in split/freeform windows.
- Text uses platform sp conversion and may scale nonlinearly on newer Android. Read the actual setting and any app restriction; do not multiply every text size by a constant or export one app's font cap as universal advice. Test large text rather than imposing a cap to make captures pass.
- Measure the relevant View/component bounds. A circular control's diameter is not automatically `min(displayWidth, displayHeight)`. Verify clipping, surrounding labels, touch bounds and reachable controls.
- Use the currently visible system-bar/IME/cutout insets for that state. Aggregated all-rotation inset provider sizes can overstate available occlusion. Verify target/API-dependent edge-to-edge and large-screen orientation behavior against current docs and the actual manifest/window.

## Look at the experience

Inspect text clipping/wrapping, reading order, hierarchy, contrast, touch targets (normally at least 48dp), keyboard/focus access, accessible labels, motion and transitions. Confirm controls remain reachable with the keyboard open. RTL requires an actual RTL locale and real translated strings; forced direction alone cannot validate typography. A screenshot cannot establish screen-reader order, touch behavior or transition continuity: exercise those separately or mark them untested.

For a defect, retain the raw image and report configuration, reproduction, expected/observed result, relevant bounds and proposed design change. Do not hide the defect by cropping or retouching it. Before/after comparison should vary the intended change while keeping renderer, device configuration and app state stable.

Official references, checked 2026-10-27: [Views responsive/adaptive design](https://developer.android.com/develop/ui/views/layout/responsive-adaptive-design-with-views), [window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes), [Views insets](https://developer.android.com/develop/ui/views/layout/insets), [large-screen compatibility behavior](https://developer.android.com/guide/practices/device-compatibility-mode). Check current guidance when target/API behavior changes.

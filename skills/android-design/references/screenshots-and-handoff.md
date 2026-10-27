# Raw screenshots and a useful handoff

Prefer the existing project capture/gallery pipeline: it may already validate installed APKs, state transitions, frame stability and original evidence. Don't replace it with a generic script just because adb can take a PNG.

## Capture the selected serial

Use a fresh run directory; never overwrite an accepted capture. After assigning an owned `device_serial`, this POSIX-shell example saves raw binary stdout with clobber protection:

```sh
capture_dir=$(mktemp -d "${TMPDIR:-/tmp}/android-design.XXXXXX")
adb -s "$device_serial" shell getprop ro.build.version.sdk > "$capture_dir/api.txt"
adb -s "$device_serial" shell wm size > "$capture_dir/display-size.txt"
adb -s "$device_serial" shell wm density > "$capture_dir/density.txt"
adb -s "$device_serial" shell settings get system font_scale > "$capture_dir/font-scale.txt"
(set -C; adb -s "$device_serial" exec-out screencap -p > "$capture_dir/screen.png")
```

Run one step at a time and check exit status. A failed capture can leave a partial file: retain the failure reason and retry under a new filename. Confirm PNG decoding and dimensions, then **open the image**. Binary output must not pass through a PTY or text decoder. Android CLI 1.0.16261425 also supports `android screen capture --device=<serial> --output=<new-path>`; inspect current help. Its annotated output is useful for locators, but preserve an unannotated original as evidence.

These display/settings receipts alone do not measure the current window. Add foreground activity/window bounds, visible system/IME insets, rotation, locale and state from the project's probes. A useful raw starting point is `adb -s "$device_serial" shell dumpsys window windows > "$capture_dir/windows.txt"`; identify the actual foreground window and visible state rather than assuming one field is stable across APIs. Name the probe/fields used and distinguish whole-window bounds, app-content bounds and IME occlusion. If you cannot establish them, mark window measurements UNDECIDED. Layout hierarchy can explain element bounds/text but cannot substitute for pixels and may omit custom-drawn content. Keep potentially sensitive dumps local; don't commit user data or device identifiers to public examples.

## Receipt beside the image

```text
Kind: CAPTURED / DRAWN / PREDICTED
Question: what this state/configuration establishes
Source: commit + dirty-state/snapshot; build command/variant; APK SHA-256
Execution: capture time; local device alias; API; renderer/tool versions
Configuration: display px; logical density; app-window bounds/dp; visible insets;
               font setting; locale/RTL; rotation/posture; navigation mode
State: exact setup/actions/data; foreground screen; dev preset if used
Files: original PNG, state/window receipts and optional hierarchy/probes
Review: observed result; design judgment; reviewer; defects and evidence limits
Coverage: untested states PENDING; unmeasured claims UNDECIDED; owner/next action
```

Commit public-safe aliases/configurations rather than physical identifiers; keep serial routing in local execution notes when needed. Never write today's commit into a receipt for an APK built earlier without verifying provenance and installed artifact. If it can't be established, label it unknown/historical.

## Review and compare

Look at clipping, overlaps, bars, keyboard, controls, text, alignment and the selected design question. Keep original PNGs immutable. Presentation frames, callouts and resized contact sheets are derivatives; preserve the raw source and don't crop or retouch defects away. Compare the same configuration, renderer, state and repeatable data. Mask only a measured nondeterministic region, retain the unmasked originals and inspect the diff visually. A whole-screen tolerance or mask is not evidence of layout parity.

Report observed behavior, source inspection and judgment separately. Two reviewers reading the same screenshot provide review consistency, not independent device corroboration. A synthetic layout preset is evidence of that renderer/state only. Pixel checks cannot prove accessibility, animation continuity or business logic; exercise those or state the limit.

## Close the loop

Return the exact accepted design revision, source/component correspondence, reviewed configurations, defects, missing states and next owner through [the design handoff](../../ux-brainstorming/references/design-handoff.md). The receiving builder/lab acknowledges the revisions/files/states it actually inspected before proceeding.

If a capture/build/input is contradicted, identify the dependent design/code affected, mark that evidence **superseded — do not reuse**, and hold those consumers until the named owner supplies a valid revision and a resume condition. Independent work continues. Preserve rejected evidence for diagnosis without leaving it among accepted examples. Publish at the project's existing acceptance cadence; a capture pass does not authorize app-store, artifact or production release.

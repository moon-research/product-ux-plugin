# Emulator and device workflow

## Preflight and ownership

Read the project's device-lab/lease instructions. List current devices with `adb devices -l` and identify their owners before acting. An idle-looking emulator is not free. Do not install, resize, rotate, capture personal content, reset or stop another room's device. If the designer requests captures from a lab, use the request template below; commands in this guide are for the authorized operator.

Locate installed tools without changing them: `command -v android`, `command -v adb`, `adb version`, existing `ANDROID_HOME`/`ANDROID_SDK_ROOT`, project `local.properties` or Android Studio's SDK setting. Keep local SDK paths out of the shared skill. Check the selected emulator's host architecture and installed system image. Don't install/update tools or download images merely to validate a skill.

Inspect installed help before copying a command. The Android CLI and SDK emulator are distinct interfaces; flags are not interchangeable. With Android CLI 1.0.16261425, these were observed:

```sh
android emulator start --help
android screen capture --help
android run --help
```

That CLI's start interface is `android emulator start [--cold] <device>`; it does not document SDK `--port` or `--read-only` flags. Use it when the project's ownership/isolation requirements permit its actual behavior. Do not invent `--name` or build-variant flags.

## Start an owned emulator

Reuse the project's lab launcher when present. For explicit isolation with an installed SDK backend, inspect its `-help` and `-list-avds`. Choose an unused AVD and a free **even** port plus its following adb port, within the backend's supported range and the project's resource/lease rules. An AVD's existence is not permission to use it. If the required slot is occupied, leave the request pending; don't bypass a gallery's refusal.

Example SDK invocation after assigning `sdk_emulator`, `avd_name` and `emulator_port` from the local configuration:

```sh
"$sdk_emulator" -avd "$avd_name" -port "$emulator_port" -read-only -no-snapshot
```

Run it in an owned terminal/process; keep the window visible when the project requires it. Read-only mode avoids saving guest disk changes but does not establish ownership or replace shared-resource coordination. Record the process and returned serial. Port checks are not reservations: if launch fails or collides, stop there rather than falling through to a pre-existing serial. Confirm the live process/AVD and serial belong to this launch before mutation. Check that exact serial with `adb -s "$device_serial" shell getprop sys.boot_completed` until it reports `1`, using a bounded retry/time budget. Stop and inspect failures instead of an unbounded wait. Never use `killall`, global `adb kill-server`, or wipe an existing AVD to fix a failed launch.

## Build, install and enter the real screen

Inspect build variants and toolchain requirements in the project. Use its existing build command, a development package and an APK whose provenance is known. Record source commit, dirty-state/patch or source snapshot, variant, build command/time and APK SHA-256; `git rev-parse HEAD` alone does not describe a dirty build. An old APK is historical evidence even if its filename matches today's variant.

Read the merged manifest/APK for the application ID and exported launcher component. A development application ID suffix does not necessarily change the activity class's package. Prefer the existing navigation harness for non-exported screens. Installation/update can change app data; use an owned test device/account and avoid a production package.

After defining actual `apk_path`, `app_id`, fully qualified `launch_activity` and `device_serial`:

```sh
adb -s "$device_serial" install -r "$apk_path"
adb -s "$device_serial" shell am start -n "$app_id/$launch_activity"
```

If using the inspected Android CLI instead, its observed equivalent is `android run --apks=<apk-path> --activity=<activity> --device=<serial>`; confirm the installed help and required activity format. Do not substitute either example for an established project launcher that manages navigation/state correctly. Clearing data, force-stopping or clearing tasks can invalidate continuity tests; do it only when the agreed scenario calls for it.

Observe → act → observe on that same serial. Establish the screen/state through the actual app or a documented dev-only preset. A synthetic renderer can prove layout pixels, not timer, billing or notification behavior. Follow [capture and handoff](screenshots-and-handoff.md).

## Capture request when a lab owns execution

```text
Decision/surface: selected screen and question this capture should answer
Source: commit + dirty/source snapshot, variant, APK path/hash or build owner
Design input: accepted revision and source/component paths
Matrix: app-window sizes, API, logical density, font, locale, bars/IME/posture
States: navigation/reproduction, exact data and expected visible state
Return: unaltered PNGs + configuration/state receipts, failure/missing-state reasons
Limits: layout vs engine evidence, private data to exclude, requested review date
Owner: lab slot/executor; designer reviews; implementation owner for defects
```

Use the project's existing queue/report-file route; do not introduce a parallel lease service. Preserve current settings before mutation. Restore only settings you changed, clear owned dev presets and stop only the instance you started, using the exact serial/owned process. Keep raw evidence and failed-run reasons for the next reviewer.

Official command references: [emulator command line](https://developer.android.com/studio/run/emulator-commandline), [adb](https://developer.android.com/tools/adb). These were checked 2026-10-27; local backend help and project ownership rules still govern execution.

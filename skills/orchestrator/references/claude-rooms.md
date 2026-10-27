# Native Claude rooms, from either leader host

Requires an installed, authenticated Claude Code CLI supporting `--bg`, `--resume`, `agents --json`, `attach`, `logs` and `stop`. Check current `claude --help` before adapting commands. This plugin ships no separate worker broker, service or credential store.

## Prepare and launch

Inspect existing sessions with `claude agents --json`. Match an exact name/ID; ambiguity or unknown status is not permission to launch a duplicate. Prepare the room brief and workspace first. For concurrent code writers, create a Git worktree from the intended integration revision and record its ownership. Keep worktrees outside deployable output.

A newly created workspace may not yet be trusted by Claude Code. Background launch then refuses before creating a room. Review the workspace and use the normal interactive `claude` trust flow for that exact folder before retrying; obtain the user's decision when the trust choice is theirs. Do not edit global trust settings or treat this refusal as a missing session to duplicate. The launch and permission policies are separate from workspace trust.

Launch from that room's worktree. A shell-readable example is:

```sh
claude --bg --plugin-dir '<installed-plugin-root>' --settings '{"crossSessionInbound":"accept"}' -n '<unique-room-name>' '<complete-room-brief>'
```

For file-based briefs or text supplied by the user, pass an argument vector rather than interpolating the text into shell code:

```python
from pathlib import Path
import subprocess

subprocess.run([
    "claude", "--bg", "--plugin-dir", str(plugin_root),
    "--settings", '{"crossSessionInbound":"accept"}',
    "-n", room_name, Path(brief_path).read_text(),
], cwd=room_worktree, check=True)
```

Here `plugin_root`, `room_name`, `brief_path` and `room_worktree` are the values the leader inspected and recorded. A source checkout or the actual installed plugin root works; do not assume the user's personal filesystem layout. Loading this plugin does not require Superdev.

The inbound setting applies only to the launched session and permits messages into that room. Do not rewrite global Claude settings. For a room where the user must control incoming messages, use `hold` and record the resulting delivery boundary.

Use the host's existing permission policy by default. A background room may need the user to attach for approvals. A read-only reviewer should receive read-only tool access. Use broader permissions only when the task actually grants them; do not silently add bypass-permission flags to make a room run unattended.

Record the ID actually returned by launch and confirm it with `claude agents --json`. Give the user `claude attach <id>` so they can enter the same session. The room's useful context lives in its conversation plus versioned project notes.

## Talk to a room

In a Claude leader use the native `SendMessage` tool addressed to the exact registered session name. In a Codex leader without that tool, use a narrowly scoped Claude relay through the same installed CLI. For example, invoke `claude -p` with `--tools SendMessage --allowedTools SendMessage --no-session-persistence`, passing a prompt to send the named message once and report the tool result. Pass the prompt as a subprocess argument, not interpolated shell code. This is a short transport call, not a replacement room.

Inspect the target's status before sending new work. Do not launch a second conversation when the existing room is busy. Use short pointers to the actual brief/design/source files and the concrete next action. Send only to chartered recipients within the authorized project; the skill does not authorize unrelated email or external messages.

Have a new room acknowledge a harmless uniquely identified message, then inspect `claude logs <id>` for its receipt/reply. A relay reporting success/queued establishes only the send state; an explicit reply establishes receipt. Completed work requires the actual returned artifact or commit and its verification.

If native messaging is unavailable, use a report file and make the missing wake-up route explicit. Do not claim a file write automatically woke another session or silently build a polling service. The user can attach to the room while transport is restored.

## Inspect, recover and resume

`claude agents --json` shows current session status; `claude logs <id>` shows recent terminal output. Long-running work may be waiting for permission or a decision. Inspect before retrying, stopping or relaunching. Repeated acknowledgments are not progress.

To stop an owned room while preserving its conversation, use `claude stop <id>`. To continue later, use `claude attach <id>`, or the background continuation:

```sh
claude --bg --resume '<full-session-id>' '<continuation>'
```

Check that the original session is stopped before background resume. Reuse its saved options: in Claude Code 2.1.311, repeating `--plugin-dir`, `--settings`, `-n` or other launch options creates a copy even after the original is stopped. Do not repeat them for same-room recovery. A different returned ID is a fork, not successful recovery; record and inspect the discrepancy rather than producing another duplicate. Changing saved launch options is a separate, intentional operation.

After sleep or a crash, inspect existing status/logs, source commits and room notes, then resume the same conversation. Do not assume a silent room is dead. Keep service restarts and unrelated sessions outside a room's recovery scope.

## Close

Preserve committed output, design links, validation, outstanding decisions and useful retrospectives. Verify that any owned worktree has been integrated or explicitly handed off before retiring it. Stop only the exact session the leader owns. Removing a session/worktree is separate from stopping it; deletion requires the applicable cleanup authority and must never erase unmerged work.

This workflow runs during active turns. The plugin installs no scheduler and guarantees no between-turn wake-ups beyond the native transport that was actually established.

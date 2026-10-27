# A room's contract and the leader's durable state

Write a short brief for the specific room, not a universal procedure pasted into every role. Use existing project documentation; a useful default home is `docs/product-ux/rooms/<room>/`.

Include:

- Identity: unique session name, role, orchestrator contact and whether the user is expected to enter for a decision.
- Outcome: the user-visible result and its scope/exclusions.
- Read first: the relevant brief/decisions and exact input artifacts/revisions, their acceptance owner/status and relevant states. Quote only the decisions needed to avoid ambiguity; link the rest.
- Design context: actual Superdesign project/draft/selected element, accepted surroundings and source correspondence when relevant.
- Workspace: absolute worktree path, branch, allowed edits and integration/review responsibility. Read-only research can use a separate folder; concurrent code writers need separate worktrees.
- Outputs: actual design/source/report locations, acceptance and the check evidence needed by the next room.
- Dependencies and authority: what is already decided, which input must arrive before implementation, what can proceed now, who resolves conflicting inputs and who may authorize release.
- Reporting/transport: exact leader address, or a report-file route when cross-session transport has not been established.

Useful reporting events are START (inputs read/first action), REVIEW (artifact and decision needed), BLOCKED (specific missing input), READY (source/commit, checks and limitations), and CLOSE (handoff plus learning). Adapt this small vocabulary to the project; a status ACK is not a completed result.

For design/lab work, return evidence lineage: exact design revision, source/build identity (including dirty-source snapshot when applicable), state/configuration and capture/check paths. Separate device observations, source findings and design judgments; name untested states. Multiple reviews of the same screenshot do not create independent device evidence. Use [Android capture guidance](../../android-design/references/screenshots-and-handoff.md) for native UI work.

## Example: funnel UX room

```text
Role: funnel UX under the named Product UX leader
Home: assigned isolated worktree; only the funnel component and its design notes
Input: accepted buyer/offer brief, existing Superdesign draft and source section
Preserve: the accepted graph and strategy sections
Work: compare funnel representations in Superdesign, then refine the selected component
Decision: user chooses the visual direction before its implementation
Return: actual review URL, selected element, accepted states, exact component path,
        what changed, what remains provisional and the implementation checks
Authority: no whole-page rewrite, provider account changes or production publication
```

## Leader state

Maintain one room table and a short cursor in the project's existing notes. Record name/ID, role/runtime, workspace/branch, dependencies, status, artifact/commit, last observed result and next action. The leader owns this shared view; rooms return their own artifacts rather than racing to edit one shared ledger.

After a room reports READY, inspect its output and commit before unblocking consumers. Pass a self-contained handoff with the input location and acceptance, not merely “design is done.” The consumer returns a grounding receipt naming the actual revisions/files/states inspected and missing mappings before implementation. Source changes need integration into the consumer's branch; read-only cross-worktree inspection is not source integration.

When new evidence contradicts an accepted input, record: invalidated revision/evidence, affected consumers, current work to hold, decision/correction owner, replacement input and the check/acceptance needed to resume. Mark superseded material **do not reuse** while preserving it for recovery. Continue unrelated work; a stale input does not invalidate the whole project automatically.

Rooms may resolve technical details directly within their authority. The initiator returns the conclusion, changed input and affected consumers to the leader. A peer cannot widen another room's scope or approve a user preference. Escalate unresolved feasibility/design conflicts to the named decision owner and hold affected work until resolved. A local implementation correction can stay within accepted intent; changed direction needs the appropriate acceptance.

Each remaining item has an owner and disposition: resolve in current scope, explicitly defer with a reason, or ask for a missing decision. Close with the accepted replacement revision and the disposition of rejected/superseded evidence so later rooms do not reuse it. Record process learning with the actual exchange for the [improvement workflow](../../self-improvement/SKILL.md). Keep customer details in the project rather than a public plugin example.

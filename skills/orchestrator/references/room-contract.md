# A room's contract and the leader's durable state

Write a short brief for the specific room, not a universal procedure pasted into every role. Use existing project documentation; a useful default home is `docs/product-ux/rooms/<room>/`.

Include:

- Identity: unique session name, role, orchestrator contact and whether the user is expected to enter for a decision.
- Outcome: the user-visible result and its scope/exclusions.
- Read first: the relevant brief/decisions and exact input artifacts. Quote only the decisions needed to avoid ambiguity; link the rest.
- Design context: actual Superdesign project/draft/selected element, accepted surroundings and source correspondence when relevant.
- Workspace: absolute worktree path, branch, allowed edits and integration/review responsibility. Read-only research can use a separate folder; concurrent code writers need separate worktrees.
- Outputs: actual design/source/report locations, acceptance and the check evidence needed by the next room.
- Dependencies and authority: what is already decided, which input must arrive before implementation, what can proceed now and who may authorize release.
- Reporting/transport: exact leader address, or a report-file route when cross-session transport has not been established.

Useful reporting events are START (inputs read/first action), REVIEW (artifact and decision needed), BLOCKED (specific missing input), READY (source/commit, checks and limitations), and CLOSE (handoff plus learning). Adapt this small vocabulary to the project; a status ACK is not a completed result.

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

After a room reports READY, inspect its output and commit before unblocking consumers. Pass a self-contained handoff with the input location and acceptance, not merely “design is done.” Source changes need integration into the consumer's branch; read-only cross-worktree inspection is not source integration.

Each remaining item has an owner and disposition: resolve in current scope, explicitly defer with a reason, or ask for a missing decision. Record process learning with the actual exchange for the [improvement workflow](../../self-improvement/SKILL.md). Keep customer details in the project rather than a public plugin example.

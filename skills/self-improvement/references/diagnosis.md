# Evidence, information flow and the smallest fix

Keep the evidence in the existing project log/retro or a focused plugin issue/change record. A useful feedback entry has date, originating project/room, observed request/return, affected skill/reference, consequence, source artifact and verification limits. Redact customer/private material before sharing it publicly.

For one failure, write a small map from actual current files:

```text
Caller/request -> skill -> referenced context/room brief
              -> room/agent input -> returned handoff -> downstream consumer
```

At every boundary ask: what was known, what was carried, what was received, what was needed? Include both the input and return contracts. A message saying “done” does not carry the component path known only inside the room.

| Finding | Likely correction |
|---|---|
| The handoff format never requests a needed field | Add the field to that contract and show how the consumer uses it. |
| The leader had context but omitted it from dispatch | Fix the leader's handoff/brief guidance. |
| The receiver read a stale or thin reference | Fix the actual source reference. |
| The workflow has no owner for a necessary check | Add a bounded responsibility/stage before inventing a new role. |
| A provider command contract changed | Verify the installed/official interface and fix the provider-specific reference. |
| One project's private configuration is missing | Correct that project; do not turn its account/path into plugin defaults. |

Compare a few concrete correction options and explain why the selected layer is enough. Avoid shotgun changes to caller, skill, references and every downstream stage at once. A single severe failure can justify a fix; repeated small friction makes a stronger case for a reusable rule.

The correction record should connect evidence → diagnosis → changed source → regression/result → release/install state. If no useful general change follows, record the local finding and end there. Self-improvement is not an instruction to accumulate universal rules or edit unrelated plugins.

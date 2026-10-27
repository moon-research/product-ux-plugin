# Requirements-to-UX handoff

Use the project's existing brief and decision record. When none exists, `docs/product-ux/brief.md` and `docs/product-ux/decisions.md` are useful defaults. Keep the artifact proportional; do not create empty documents for every possible topic.

The brief should answer:

| Question | Useful content |
|---|---|
| Who and why? | Primary audience, their situation/problem and the value proposition. |
| What action? | The main action the page/product should help them take, with a concrete journey. |
| What evidence? | Research links, truthful claims, counter-cases and uncertainty. |
| What is being designed? | Page/feature/component boundaries, existing accepted design and relevant routes. |
| What must work? | User-visible acceptance examples, important states and accessibility/responsive needs. |
| What constrains it? | Brand/content assets, existing stack, budget/time and provider access when material. |
| What is excluded? | Unrequested forms, authentication, backends, redesigns or production changes. |
| What is open? | The decisions that block the next affected step and who can answer. |

For a landing page, add a provisional message hierarchy: promise → evidence → how it works → practical use cases → next action. Use the hierarchy that fits the actual audience rather than forcing those sections into every page.

A decision entry records the date, question, alternatives, selected choice, person deciding, reasoning and affected surface. Mark an agent assumption as an assumption. If a decision changes, add the superseding choice and update the brief; keep the reason discoverable.

For complex behavior, add states, relationships and failure/recovery paths where they affect the experience. A user-visible acceptance example such as “a reader can compare two cases and return without losing their selection” is more useful at this phase than an invented test command.

Before UX work, reconcile the brief with the actual decisions. A single local approval is enough for a small change; do not repeatedly reopen a settled audience, offer or accepted section.

# Design-to-build handoff

Keep one short design note beside the project brief, or extend an existing design document. Useful default: `docs/product-ux/design.md`.

| Field | What to record |
|---|---|
| Intent | Audience/action and the requirement this surface serves. |
| Surface | Route, section/component, and what the current edit includes. |
| Review artifact | Actual Superdesign project/draft URL and selected element if applicable. |
| Accepted direction | Composition, message hierarchy, typography, color, spacing, illustration/asset choice and interaction intent. |
| Source correspondence | Actual component/layout/style paths after inspecting the implementation. |
| States | Relevant default, focus, hover, active, loading, empty, error and mobile behavior; mark unused states as inapplicable. |
| Review status | What was accepted, by whom, what is still provisional and what changed in this iteration. |
| Browser checks | What the implemented page must demonstrate; separate these from canvas acceptance. |

For component-by-component work, maintain a simple section list with accepted/current/pending status and links. Do not add a registry/database or generated ID mapping merely to maintain this list.

Example record:

```text
Surface: opportunity funnel section
Design: actual provider-returned draft link + selected element
Source: src/components/home/OpportunityFunnel.astro
Accepted: evidence narrows into three viable opportunities; people stay visible in the loop
Check: keyboard can select an opportunity; labels remain readable on narrow screens
Surroundings: accepted graph and strategy sections remain intact
```

When assembling, inspect section transitions, navigation, shared typography, repeated assets and responsive flow. An accepted component can still need a local integration correction; explain it and update the affected note without reopening the entire page.

Canvas and source will evolve separately. Skill-guided review keeps them aligned; neither a saved draft ID nor a code export proves implementation parity.

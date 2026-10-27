# Superdesign review integration

Superdesign is a separately authenticated design service. The Product UX plugin bundles the review workflow; it does not bundle credentials, paid generation credits or an MCP server. Use the official Superdesign skill/tooling when available. Otherwise use its CLI through the shell and inspect current command help rather than assuming old flags still work.

## Connect and resume

1. Check shell/tool availability. The official on-demand CLI preflight is `npx --yes @superdesign/cli@latest`; it reports authentication and recent projects. This uses the network and can download the CLI. Follow project restrictions on command execution/downloads. Do not install global packages as an implicit plugin-install step.
2. If authentication is missing, use the official login flow with the user's participation. Read the result; a previous session's authentication is not proof of current access. If connection is unavailable, prepare local context and report the blocker; no canvas artifact exists yet.
3. Reuse a supplied project/draft and selected element before creating anything. For an existing frontend, follow the provider's current initialization/resume guidance; inspect only relevant components, routes and design tokens. A new visual concept with no codebase needs a brief rather than a fabricated repository analysis.
4. Retrieve the full selected design context. For the CLI's current `get-design` command, inspect `npx --yes @superdesign/cli@latest get-design --help`, then use the supplied draft ID. Preserve the original request's selected element/context.

## Show, iterate and hand off

Use the official create/iterate operations and current help. State the target surface, accepted surroundings, business message, visual purpose and relevant states in the design request. Avoid uploading unrelated private research or the entire repository as context.

Small corrections refine the existing direction. Comparison requests create named alternatives. Keep a component's source boundary and full-page integration in view. Upload reusable brand assets through supported asset operations so a real logo is used consistently; do not replace an available brand mark with an invented icon.

Return the actual `canvas` and/or `preview` URL from the provider response. Treat an operation still generating as in progress. Never construct an apparently valid preview from guessed IDs, relabel raw HTML as a published draft, or claim a local mockup was uploaded.

For a failed create/iterate with unclear outcome, inspect project state before retrying to avoid duplicate paid drafts. Bound retries to one after correcting the cause. If generation remains unavailable, report what happened and obtain a decision before switching the user's requested review destination.

Save the project/draft/element reference and the corresponding source component in the project's design notes. A new session resumes from those notes and current provider state; it does not recreate the accepted page by default.

Provider reference: [Superdesign](https://superdesign.dev). Check its installed skill and CLI help for current command contracts; this document intentionally does not duplicate the complete provider manual.

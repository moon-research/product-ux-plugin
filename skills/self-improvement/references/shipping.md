# Ship and verify an improvement

Find the actual Product UX source repository from its manifest/marketplace metadata. Work in that source, never in a versioned installed cache. If only an installed package is available, obtain the maintained source before editing. This plugin does not require the author's local directory layout.

1. Make the authorized focused correction and update the affected examples/contributor instructions.
2. Bump the same version in `plugin.json`, `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Use a patch for a focused correction and a minor version for an additive skill or flow. Update the source repository's release notes/changelog with the evidence and changed boundary. Do not modify the originating project's release/deployment targets as a side effect.
3. Run the source checkout's documented validation/tests and the affected realistic scenario. Generate a new non-overwriting package if releasing an archive. Preserve the original observation and observed correction; a new instruction alone does not prove behavior improved.
4. Commit and deliver through the repository's review/release process. Follow the [Git delivery boundary](../../product-ux/references/project-contract.md#after-each-contribution): record actual remote base and full outgoing range before pushing. Record source revision and review state. A pushed branch does not automatically update default-ref marketplace installs.
5. Refresh the intended host's installation only within the granted install/update scope. Do not update every unrelated marketplace or interrupt active rooms merely to load new instructions.

For Claude Code, the current scoped update form is:

```sh
claude plugin update product-ux@moon-research-product-ux
claude plugin details product-ux
```

For Codex, inspect the installed CLI's current `plugin` help. Where it provides marketplace upgrade and plugin add, refresh only `moon-research-product-ux`, then install/refresh Product UX and inspect `plugin list` for the actual version. Do not label a successful marketplace refresh as proof the installed package changed. A local source may not need a Git marketplace upgrade at all.

Start a fresh session or use the host's supported reload operation. Confirm the new version and changed skill/reference in the actual installed package and its available skill inventory, then exercise the previously failing scenario. A running room can still hold old instructions; record the loaded version and arrange a safe reload/resume rather than assuming hot reload.

When an update cannot be performed because the change is still under review, access is unavailable or a session is active, distinguish the verified source/package from the pending installed state. Leave exact next steps instead of claiming “shipped” for all layers.

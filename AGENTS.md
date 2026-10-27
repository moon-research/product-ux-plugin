# Contributing to Product UX

Read `README.md` for the product boundary, native Claude/Codex installation commands and checks. The plugin's shared runtime source is `skills/`; root and host manifests package those same files. Keep identity/version and marketplace entries consistent.

Work from the current user request and the relevant design/decision notes under `docs/`. Preserve `setup-ux.sh`; it is an optional existing machine bootstrap, not plugin installation or a test fixture. Never run it to validate this plugin.

Keep skill instructions portable and focused. Put provider-specific detail in linked references. Product Graph and Superdev checkouts/room tooling are not runtime dependencies. Credentials, customer identifiers and live targets belong in each site's configuration, not plugin defaults.

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v` after package changes. Check affected workflows with realistic fresh-context tasks; record what was actually exercised and its limits. Use temporary projects/settings for integration tests and never deploy a live customer site as a package test.

When changing behavior or adding a skill, update its discovery description, references, examples and contribution/release documentation as needed. Record reusable lessons with their evidence; changes to this repository do not implicitly update installed caches or unrelated projects. Finish with honest commit/push, installation and verification state.

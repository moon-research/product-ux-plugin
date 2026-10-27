# Product UX package — operator scenario

The operator has cloned the actual product-ux-plugin repository and wants to validate it, create a distributable archive, and share that archive with someone who uses Claude or Codex. They start from the README, not the utility internals.

Actual data: this repository's real manifests, skill tree and release documents. Provider accounts and live site data are not needed for package creation. The actual host-discovery path is recorded separately in docs/verification.md.

Good looks like understandable checks, a self-contained archive of the real plugin, a refusal rather than replacement of an existing release archive, and validation after unpacking elsewhere. Repository machine setup, Git/environment files and planning/test data stay outside the distributed package.

Journey: inspect the documented commands; validate the checked-out plugin; create the release ZIP at an explicit new path; observe safe handling of the same path on a retry; unpack it outside the checkout and validate its portability.

The package test does not create a design draft, provision services, submit to a host directory or publish a customer site.

## 2026-10-27 — criteria refined from the actual operator path

A refusal must preserve the artifact checksum, not merely print an error. The operator can discover the validator's external-root argument through public `--help`, then validate the actual unpacked runtime independently of the checkout's source files.

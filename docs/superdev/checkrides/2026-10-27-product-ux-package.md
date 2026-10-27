# Product UX package operator checkride — 2026-10-27

Actual substrate: `/Users/tadas/Projects/product-ux-plugin`, its real manifests, shared skills and release documents; no fixtures. Scenario: `docs/superdev/scenarios/2026-10-27-product-ux-package.md`. Read README before proposing commands. No provider, user configuration or site changes.

Source branch: `feat/standalone-product-ux`. HEAD: `30bcd1c7ce210a383b77feebfe0c5094618cbd21`. Merge base with `origin/main`: `418b5daea6c4bf218b18437e1d3951c5d413159c`. Actual package files are uncommitted checkout content; HEAD alone does not identify their contents.

All operator commands below use explicit workdir `/Users/tadas/Projects/product-ux-plugin` and shell `/bin/zsh`. Executor proposed each operation and waited for root to relay evaluator GO. Root authorized this evidence ledger separately; implementation is not edited by executor.

## Step 1 — validate checkout

Proposal: `python3 scripts/validate.py`. Intent: documented actual package validation. Expected writes: none. Expected success: valid manifests/catalogs, shared skills and references. Evaluator GO relayed by root before execution. Evaluator subsequently judged OK.

Exit: 0. Full output:

```text
Valid package: 5 shared skills, matching manifests/catalogs, contained references
```

## Step 2 — allocate external release location

Proposal: `mktemp -d /tmp/product-ux-package-checkride.XXXXXX`. Intent: retain release and unpacked artifacts outside checkout. Expected writes: one new empty directory. Evaluator GO relayed by root before execution. Evaluator subsequently judged OK.

Exit: 0. Full output:

```text
/tmp/product-ux-package-checkride.GbjFsu
```

## Step 3 — create actual release ZIP

Proposal: `python3 scripts/package.py --output /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip`. Intent: execute README release command against actual plugin. Expected writes: one new ZIP. Evaluator GO relayed by root before execution. Evaluator subsequently judged OK.

Exit: 0. Full output:

```text
Created /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip: 26 files
```

## Step 4 — inspect release inventory

Proposal: `unzip -l /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip`. Intent: inspect archive before sharing/extraction. Expected writes: none. Expected inventory: manifests/catalogs, shared skills, README/LICENSE/NOTICE, excluding checkout-only material. Evaluator GO relayed by root before execution. Judgment pending.

Exit: 0. Full output:

```text
Archive:  /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
      376  01-01-2026 00:00   .agents/plugins/marketplace.json
      378  01-01-2026 00:00   .claude-plugin/marketplace.json
      371  01-01-2026 00:00   .claude-plugin/plugin.json
      742  01-01-2026 00:00   .codex-plugin/plugin.json
     1070  01-01-2026 00:00   LICENSE
     1877  01-01-2026 00:00   NOTICE
     8401  01-01-2026 00:00   README.md
      446  01-01-2026 00:00   plugin.json
     2418  01-01-2026 00:00   skills/building-sites/SKILL.md
      221  01-01-2026 00:00   skills/building-sites/agents/openai.yaml
     3622  01-01-2026 00:00   skills/building-sites/references/analytics.md
     3561  01-01-2026 00:00   skills/building-sites/references/static-sites.md
     2037  01-01-2026 00:00   skills/product-ux/SKILL.md
      204  01-01-2026 00:00   skills/product-ux/agents/openai.yaml
     2933  01-01-2026 00:00   skills/product-ux/references/project-contract.md
     2421  01-01-2026 00:00   skills/publishing-sites/SKILL.md
      217  01-01-2026 00:00   skills/publishing-sites/agents/openai.yaml
     6767  01-01-2026 00:00   skills/publishing-sites/references/cloudflare-pages.md
     2404  01-01-2026 00:00   skills/requirements-brainstorming/SKILL.md
      226  01-01-2026 00:00   skills/requirements-brainstorming/agents/openai.yaml
     2298  01-01-2026 00:00   skills/requirements-brainstorming/references/product-graph-input.md
     2123  01-01-2026 00:00   skills/requirements-brainstorming/references/requirements-handoff.md
     2303  01-01-2026 00:00   skills/ux-brainstorming/SKILL.md
      213  01-01-2026 00:00   skills/ux-brainstorming/agents/openai.yaml
     2060  01-01-2026 00:00   skills/ux-brainstorming/references/design-handoff.md
     3243  01-01-2026 00:00   skills/ux-brainstorming/references/superdesign.md
---------                     -------
    52932                     26 files
```

## Step 5 — baseline archive checksum

Evaluator amended the next step to `shasum -a 256 /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip` and root relayed GO. Intent: establish unchanged-output evidence before refusal test. Expected writes: none.

Exit: 0. Full output:

```text
bcafe4ff71821e1e2026fac198a2bd11888ad39fb610b51dbb7facbb46d722b6  /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip
```

Steps 4 and 5 subsequently judged OK by evaluator, relayed through root.

## Step 6 — existing output refusal

Proposal: `python3 scripts/package.py --output /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip`. Intent: observe documented refusal for existing release path. Expected writes: none. Expected result: nonzero exit and clear refusal. Evaluator GO relayed by root before execution.

Exit: 1. Full combined stdout/stderr from execution tool:

```text
ERROR: [Errno 17] File exists: '/tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip'
```

Step 6 judged OK by evaluator. Low advisory: file-exists diagnostic could suggest choosing a new `--output` path; no blocker.

## Step 7 — compare checksum

Proposal: `shasum -a 256 /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip`. Intent: establish existing archive remains unchanged after refusal. Expected writes: none. Expected: same SHA-256 as step 5. Evaluator GO relayed by root before execution.

Exit: 0. Full output:

```text
bcafe4ff71821e1e2026fac198a2bd11888ad39fb610b51dbb7facbb46d722b6  /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip
```

Step 7 judged OK by evaluator: identical hash.

## Step 8 — unpack external copy

Proposal: `unzip /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip -d /tmp/product-ux-package-checkride.GbjFsu/unpacked`. Intent: unpack actual release elsewhere for portability validation. Expected writes: new unpacked directory and archive files under the external temporary directory. Expected: clean extraction with exit 0. Evaluator GO relayed by root before execution.

Exit: 0. Full output:

```text
Archive:  /tmp/product-ux-package-checkride.GbjFsu/product-ux-0.1.0.zip
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/.agents/plugins/marketplace.json  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/.claude-plugin/marketplace.json  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/.claude-plugin/plugin.json  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/.codex-plugin/plugin.json  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/LICENSE  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/NOTICE  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/README.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/plugin.json  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/building-sites/SKILL.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/building-sites/agents/openai.yaml  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/building-sites/references/analytics.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/building-sites/references/static-sites.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/product-ux/SKILL.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/product-ux/agents/openai.yaml  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/product-ux/references/project-contract.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/publishing-sites/SKILL.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/publishing-sites/agents/openai.yaml  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/publishing-sites/references/cloudflare-pages.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/requirements-brainstorming/SKILL.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/requirements-brainstorming/agents/openai.yaml  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/requirements-brainstorming/references/product-graph-input.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/requirements-brainstorming/references/requirements-handoff.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/ux-brainstorming/SKILL.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/ux-brainstorming/agents/openai.yaml  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/ux-brainstorming/references/design-handoff.md  
  inflating: /tmp/product-ux-package-checkride.GbjFsu/unpacked/skills/ux-brainstorming/references/superdesign.md
```

Step 8 judged OK by evaluator.

## Step 9 — discover validator root argument

Original proposal to validate unpacked package was amended by evaluator to discover CLI syntax first. Proposal: `python3 scripts/validate.py --help`. Intent: discover accepted root argument before invoking undocumented positional-root syntax. Expected writes: none. Expected: usage/help with accepted root argument. Evaluator GO relayed by root before execution.

Exit: 0. Full output:

```text
usage: validate.py [-h] [path]

Validate this skills-only distribution without installing dependencies.

positional arguments:
  path

optional arguments:
  -h, --help  show this help message and exit
```

Step 9 judged OK by evaluator.

## Step 10 — validate unpacked package

Proposal: `python3 scripts/validate.py /tmp/product-ux-package-checkride.GbjFsu/unpacked`. Intent: validate actual unpacked runtime package using checkout development utility (helpers are excluded from runtime archive). Expected writes: none. Expected: same package validation success as checkout. Evaluator GO relayed by root before execution.

Exit: 0. Full output:

```text
Valid package: 5 shared skills, matching manifests/catalogs, contained references
```

Step 10 judgment: PASS.

Final evaluator verdict relayed by root, verbatim:

> Evaluator final PASS: step10 passed; no blockingfindings. Runtimeinventorymatches docs; retry exit1/checksum unchanged proves preservation. One lowresidual messagecouldsuggest new --output (ownedverificationdoc).

Release archive and unpacked package retained under `/tmp/product-ux-package-checkride.GbjFsu`. No runtime changes made. No more operator steps proposed.

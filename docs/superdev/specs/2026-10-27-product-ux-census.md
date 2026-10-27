CENSUS — evidence record; rules nothing

# Product UX plugin — extraction census

Recorded: 2026-10-27T08:25:16+00:00

- **MEASURED:** `gh repo view moon-research/product-ux-plugin --json nameWithOwner,isPrivate,defaultBranchRef` returned the public repository `moon-research/product-ux-plugin`, branch `main`. `git clone git@github-clawsmith:moon-research/product-ux-plugin.git /Users/tadas/Projects/product-ux-plugin` succeeded.
- **MEASURED:** `git ls-files` returned only `setup-ux.sh`; `git log -1 --format='%h %s'` returned `418b5da Add Mac setup script for UX designer`. Initial working tree was clean. The setup script was inspected, not executed.
- **READ:** `/Users/tadas/Projects/supplements/product-graph/graph/briefs/site/CRAFT.md:9–19` provides business-brief discovery, stack selection, incremental section review and skill-guided Superdesign correspondence. Lines 25–42 provide contributor breadcrumbs, content/discovery outputs and isolated checks. Its later sections cover Firebase-linked Analytics and bidirectional learning.
- **READ:** `/Users/tadas/Projects/supplements/product-graph/graph/briefs/site/PUBLISHING.md:5–45` distinguishes review and production authority, exact reviewed-source promotion, prepared artifacts, deployment receipts and actual host checks; subsequent sections describe recovery and Search Console follow-up. These reusable rules must be extracted without depending on private room paths or copying AppFX account IDs.
- **READ:** `/Users/tadas/.codex/plugins/cache/superdev-dev/superdev/8.6.7/skills/brainstorming/SKILL.md:1–25` defines collaborative requirements/design exploration before implementation. Its remaining workflow includes decision capture, written specifications and review. `/Users/tadas/Projects/superdev/LICENSE:1–21` is MIT; preserve attribution for substantial reused material. The final extent of reuse is undecided.
- **READ:** `/Users/tadas/Projects/supplements/product-graph-plugin/.claude-plugin/plugin.json:1–5` and adjacent `marketplace.json` demonstrate existing product plugin packaging. Product Graph's init/improve skills are graph-specific, not a standalone UX workflow.
- **FLAGGED:** The HUMAN said “artifact publishing … into the superdev.” It is unclear whether this means Superdesign canvas review, Superdev's artifact workflow, or both. A clarification is pending; no publishing backend is selected from this phrase.
- **FLAGGED:** “For the product graph, the landing page that is needed” is provisionally understood as consuming Product Graph research/positioning to build a product landing page. Whether an actual new page is requested in this extraction scope remains to be settled.

The old site-appfx worktree directory no longer exists. Extraction reads the current Product Graph main checkout; historical chat paths are evidence pointers, not operational dependencies.

Resolution update: the HUMAN selected Superdesign review (D3), then approved implementation for both hosts (D4). The reusable-capability interpretation of landing-page work is explicit in D5. Earlier FLAGGED rows record the uncertainty at the time of discovery.

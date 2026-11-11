# Sales project: shared Resolvable brand skill

This repository holds the reusable Resolvable brand skill and supplied logo assets so cloud chats checking out the Sales repository can load the same guidance.

## Start a task

Use a cloud environment configured to check out **JMResolvable/salesboard**, then ask the chat to read `AGENTS.md` and use the **resolvable-brand** skill. The standard skill location is [`.agents/skills/resolvable-brand/SKILL.md`](.agents/skills/resolvable-brand/SKILL.md).

The cloud environment's checkout location may vary. Find the repository root and resolve all paths from there. Sharing a repository provides persistent files; it does not make independent chats share a live filesystem. Existing chats need to fetch the latest repository version before the files appear.

## Included

- Full skill with eleven topic references: visual identity, logos, typography, iconography, voice/content, products, pricing/claims and production checks.
- All 58 supplied logo files, with SHA-256 integrity manifest.
- Twelve clearly labelled proposed companion icons.
- Exact SVG colours in JSON/CSS.
- Exhibition-artwork overview and logo contact sheet.
- Visual reference board in HTML and PDF.

Read the [source register](.agents/skills/resolvable-brand/references/sources-and-maintenance.md) for provenance and known gaps. The exact font family has not been established; any fallback and proposed icon/layout defaults are labelled. Original large PDF/ZIP uploads remain in the creation chat; extracted logos and artwork preview are included here.

## Verify

```sh
python .agents/skills/resolvable-brand/scripts/validate.py
```

No extra Python packages are required for validation. Web research and image generation are platform capabilities that each chat must have independently.

## Publication

The user explicitly authorised publishing this brand kit in the public `JMResolvable/salesboard` repository on 11 November 2026. Original assets remain owned by their respective rights holders; no general third-party reuse licence is granted by this repository.

# Resolvable brand skill

Reusable brand guidance based on Resolvable's public website and the user's supplied artwork/logo archive. Read **SKILL.md** first.

Includes visual identity, exact SVG colours, supplied logos, typography guidance, iconography, tone/content patterns, current products, pricing/claims checks and production recipes. Official/source-backed facts are distinguished from proposed implementation defaults. Exact typography remains unverified because the supplied PDF and logos use outlines and website styles were inaccessible.

## Use

Ask your agent to use the **resolvable-brand** skill for Resolvable work. Keep this whole directory together so asset/reference links work. The repository root `AGENTS.md` points relevant work here; the skill also lives in the standard `.agents/skills/` directory. This is a repository skill, not an account-wide installation in the cloud Skills catalogue.

To install in another tool, copy the folder into that tool's supported skill directory. For Codex, a typical user skill location is `$CODEX_HOME/skills/resolvable-brand` (usually `~/.codex/skills/resolvable-brand`). Use your environment's documented writable location; this package does not write outside the workspace.

## Review

- `evidence/artwork-overview.png`: stand preview.
- `evidence/logo-contact-sheet.png`: all 14 supplied logo variants.
- `brand-board.html`: portable visual reference; uses actual supplied SVGs.
- `brand-board.pdf`: four-page visual reference export.
- `assets/manifest.json`: supplied asset hashes.
- `assets/icons/README.md`: proposed companion icon status.
- `references/sources-and-maintenance.md`: evidence and remaining gaps.

Run `python scripts/validate.py` from this directory. Sources and assets remain owned by their respective rights holders. Use them for authorised Resolvable work; no third-party font is bundled.

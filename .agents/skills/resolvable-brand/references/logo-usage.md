# Logo selection and handling

The user supplied 14 logo variants in four formats plus two favicon SVGs: 58 files. The archive's original names, including spaces, are preserved under `assets/logos/Resolvable Logos/`. See `assets/manifest.json` for hashes, dimensions and fills, and `evidence/logo-contact-sheet.png` for a visual inventory.

## Selection table

All names below are in `assets/logos/Resolvable Logos/SVG/`.

| Context | Exact file |
|---|---|
| Parent brand, light background | Resolvable logo Full colour black.svg |
| Parent brand, dark background | Resolvable logo Colour white.svg |
| Parent brand, single dark ink | Resolvable logo Full black.svg |
| Parent brand, reversed single ink | Resolvable logo Full white .svg |
| AI, light background | Resolvable logo Full-colour black_AI.svg |
| AI, dark background | Resolvable logo Full colour white_AI.svg |
| AI, reversed single ink | Resolvable logo Full white_AI.svg |
| Outsourcing, light background | Resolvable logo Full colour black_outsourcing.svg |
| Outsourcing, dark background | Resolvable logo Full-colour white outsourcing.svg |
| Outsourcing, single dark ink | Resolvable logo Full_black_outsourcing.svg |
| Outsourcing, reversed single ink | Resolvable logo Full white_outsourcing.svg |
| Standalone coloured symbol | Resolvable logo Icon colour.svg |
| Standalone black symbol | Resolvable logo Icon black.svg |
| Standalone white symbol | Resolvable logo Icon white .svg |

Some filenames say black but the full-colour lettering is #231F20. Treat the actual file as authoritative. A supplied monochrome-black AI lockup is absent; do not manufacture one by silently editing the coloured lockup. Use the parent monochrome mark with a separate textual product label if necessary.

## Practical handling

- Prefer SVG for web and diagrams; supplied PDF for print; PNG where vector is unsupported. JPG has no transparency: inspect its background before use.
- Keep the original aspect ratio. Parent colour SVG: 3648:512; AI: 4482:512; coloured Outsourcing: 5861:512. Other variants vary slightly: read their viewBox rather than forcing a common ratio.
- The symbol contains seven directional segments arranged in an open circular form. Preserve all seven, their relative positions and colour sequence.
- Product lockups include the brand, divider and descriptor. Use them as a unit; do not recreate a divider or retype the descriptor.
- Preserve the registration mark already present in the master. Do not add one to plain text mentions or fabricate a trademark status.
- Never stretch, crop, apply outlines, shadows, gradients or transparency to the mark. Do not place it on a visually busy image.

## Working clear space and minimum sizes — proposed

No formal measurements were supplied. For new work, reserve at least half the symbol height around the complete lockup. Start with a 24 px symbol, a 160 px parent lockup, a 200 px AI lockup or a 280 px Outsourcing lockup in digital layouts; inspect actual legibility and increase as necessary. These are starting recommendations, not official minimum sizes. For print, approve a proof at final output size.

## Favicons

The supplied `Favicon_Light.svg` and `Favicon_Dark.svg` have 1024-square viewBoxes. Verify what each renders before mapping it to light/dark browser themes; filenames alone do not establish whether “Light” describes the icon or the background. Use the icon-only asset for compact avatars, never squeeze a wordmark into a square.

Accessible naming: `Resolvable`, `Resolvable AI` or `Resolvable Outsourcing` as appropriate. A repeated decorative logo should have empty alt text; a logo link needs an accessible destination name.

# Visual identity and colour

## Evidence levels

**Exact:** fills read from supplied SVG logos. **Observed:** appearance or PDF vector values from the supplied stand. **Recommended:** production defaults proposed in this package. No live website stylesheet or computed font/colour audit was possible; do not call these website design tokens.

## Exact logo colours

| Token | Hex | Evidence / use |
|---|---|---|
| wordmark-ink | #231F20 | Parent wordmark in full-colour dark-lettering SVG |
| ai-teal | #61B9BA | AI label and divider in supplied AI lockups |
| outsourcing-pink | #D77FB5 | Outsourcing label and divider in supplied lockups |
| symbol-lime | #B5D48B | Multicolour symbol |
| symbol-gold | #E5C46B | Multicolour symbol |
| symbol-rose | #E1779E | Multicolour symbol |
| symbol-orchid | #BF8BBE | Multicolour symbol |
| symbol-lavender | #AAA3D0 | Multicolour symbol |
| symbol-sky | #97C9E5 | Multicolour symbol |
| symbol-mint | #92D1B7 | Multicolour symbol |
| white / mono black | #FFFFFF / #000000 | Supplied monochrome assets |

Keep the symbol's colour order and geometry intact. The pink symbol segment and the Outsourcing label use different colours; do not merge them into one token. AI teal is also distinct from symbol mint.

## Stand appearance

The artwork uses a near-black field, white wordmarks and headlines, white rounded content cards, teal AI details, pink Outsourcing details, lavender trust marks, thin borders and soft coloured light behind the hero. Its workflow diagram uses pale blue-to-neutral capsules and fine connecting arrows.

PDF vector extraction includes #171623 (dark ink), #A1A1D0 (lavender), #605E93 (muted purple), #9CB6DF (blue), #60B9BB (teal) and #D77FB4 (pink). These are PDF-reported RGB values, potentially affected by source colour space and conversion. Use SVG colours for digital product identity. The rendered background varies around #151417; **#151417 is a recommended digital approximation**, not an official flat source swatch.

## Recommended application system

Use near-black for high-impact hero sections, white for reading-heavy content, and a restrained accent tied to the product. Parent-brand work may use both product colours with equal weight. Keep multicolour detail concentrated in the actual symbol and limited supporting accents.

- Light canvas: #FFFFFF; text #231F20.
- Dark canvas: #151417; text #FFFFFF.
- Cards: white on a dark canvas, or #F5F5F7 on white (proposed neutral).
- Borders: #DAD9DE on light; rgba(255,255,255,.16) on dark (proposed).
- Accent labels: AI teal / Outsourcing pink; pair with dark text when used as filled pills.
- Diagram nodes: pale blue or neutral fill, dark line icon, clear label and directional connector.

Do not assume pastel accents are accessible as small text on white. Use dark text, a stronger accessible variant identified as an implementation colour, or a dark background. Check actual combinations, focus states and disabled states.

## Layout, imagery and motion — recommendations derived from the stand

Use generous space, strong aligned grids, rounded rectangles and readable hierarchy. Suggested spacing scale: 4, 8, 12, 16, 24, 32, 48, 64, 96 px. Cards: 20–32 px radius; pills: fully rounded. These are proposed values, not measurements of the website.

Use restrained blurred glows behind major compositions. Keep body text and logos over calm opaque areas. Use authentic team/customer imagery when available and permissioned. Illustrate product value with a short operational scenario, not decorative science-fiction imagery. Avoid cartoon robots as the default AI identity.

Motion should explain sequence or state change. Honour reduced motion, avoid constant spinning symbols and do not make an animated scene the only way to understand a claim.

For print, use supplied vector PDF/SVG and a printer-agreed colour profile. No Pantone reference or official CMYK conversion is established. Do not infer a bleed, physical stand size or output scale from the supplied filename.

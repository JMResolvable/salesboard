# Typography

## What is established

The stand uses a clean sans serif, large bold headlines, regular body copy, compact bullet lists and pill-shaped calls to action. The supplied logos are outlined vector shapes. The stand PDF has no embedded or named fonts (`pdffonts` returns no font rows), and text extraction is empty. No font files are present in the logo archive. Live website CSS/computed styles were not available.

**The actual brand font family and licensed weights are unverified.** Do not identify it by eye as Inter, Helvetica, Arial, or another font. The wordmark is an asset, not permission to use a similar font in place of it.

## Temporary implementation choice

Until a font source is verified, use `Arial, "Helvetica Neue", Helvetica, sans-serif` as a labelled substitute for editable layouts. This is a practical recommendation, not a discovered brand stack. In an existing project, preserve the established font configuration until evidence justifies a change. Do not download or redistribute a commercial font without a valid licence.

## Suggested hierarchy, not measured brand specifications

| Role | Digital starting point | Weight / leading |
|---|---|---|
| Hero | clamp(40px, 5.5vw, 80px) | 700 / 1.04 |
| Section heading | clamp(30px, 3.5vw, 48px) | 700 / 1.12 |
| Card heading | 24–28px | 700 / 1.2 |
| Intro | 20–22px | 400 / 1.45 |
| Body | 16–18px | 400 / 1.5 |
| UI label / caption | 14px minimum where practical | 400–700 / 1.4 |

Use sentence case. Keep body measures around 45–75 characters. Allow natural wrapping rather than forcing the exhibition headline into all formats. Small legal conditions need enough contrast and space; do not imitate the stand's tiny footnotes on a phone screen.

Headlines may use short, rhythmic clauses. Use punctuation for clarity; do not split every sentence into fragments. Avoid excessive tracking, condensed display faces or novelty type that changes the calm, practical character.

## How to close the gap

Obtain the brand's actual font files or an accessible live site, inspect computed `font-family` and loaded font faces, then record family, weight, style, licensing/source and usage roles with date. Replace the fallback token and update this reference. Outlined artwork alone cannot establish the exact font.

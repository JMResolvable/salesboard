#!/usr/bin/env python3
"""Validate local skill structure, relative references and supplied asset integrity."""
from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
errors=[]
text=(root/'SKILL.md').read_text()
if not text.startswith('---\nname: resolvable-brand\ndescription: '):errors.append('Missing skill frontmatter')
manifest=json.loads((root/'assets/manifest.json').read_text())
if len(manifest)!=58:errors.append(f'Expected 58 supplied assets, got {len(manifest)}')
for row in manifest:
 p=root/row['path']
 if not p.is_file():errors.append(f'Missing asset {p}')
 elif hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:errors.append(f'Changed source asset {p}')
for p in root.rglob('*.svg'):
 try: ET.fromstring(p.read_text())
 except Exception as e:errors.append(f'Invalid SVG {p}: {e}')
for p in root.rglob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if link.startswith(('https:','http:','#')):continue
  target=link.split('#')[0]
  if target and not (p.parent/target).exists():errors.append(f'Broken reference in {p.name}: {target}')
tokens=json.loads((root/'assets/tokens.json').read_text())
if tokens['verified_logo_colours']['ai-teal']!='#61B9BA':errors.append('AI master colour changed')
if tokens['verified_logo_colours']['outsourcing-pink']!='#D77FB5':errors.append('Outsourcing master colour changed')
icons=list((root/'assets/icons').glob('*.svg'))
if len(icons)!=12:errors.append('Expected 12 proposed companion icons')
for p in icons:
 el=ET.fromstring(p.read_text())
 if el.get('viewBox')!='0 0 24 24' or el.get('stroke-width')!='1.75':errors.append(f'Icon style mismatch: {p}')
if errors:
 print('FAILED\n'+'\n'.join(errors));raise SystemExit(1)
print(f'PASS: skill frontmatter; {len(manifest)} unchanged supplied assets; SVG syntax; relative Markdown links; 12 companion icons; master colour tokens.')

"""Build Markdown notes and the static GitHub Pages site into docs/."""
from pathlib import Path
import html
import json
import re
import shutil
import subprocess
import markdown
from urllib.parse import urlparse, parse_qs

root=Path(__file__).resolve().parent
dist=root/'docs'
if dist.exists():shutil.rmtree(dist)
shutil.copytree(root/'src',dist)
# Self-host the math stylesheet and fonts; no runtime CDN is needed.
katex=root/'node_modules/katex/dist'
if not katex.exists():raise SystemExit('Run npm ci before building.')
math_assets=dist/'assets/katex'
math_assets.mkdir(parents=True,exist_ok=True)
css=(katex/'katex.min.css').read_text()
css=re.sub(r',url\([^)]*\.(?:woff|ttf)\)format\([^)]*\)', '',css)
(math_assets/'katex.min.css').write_text(css)
(math_assets/'fonts').mkdir()
for font in (katex/'fonts').glob('*.woff2'):shutil.copy(font,math_assets/'fonts'/font.name)
shutil.copy(root/'node_modules/katex/LICENSE',math_assets/'LICENSE')
notes=json.loads((root/'content/notes/index.json').read_text())
asset_map=json.loads((root/'content/notion-assets.json').read_text())
asset_names={local:parse_qs(urlparse(original).query).get('name',[Path(local).name])[0] for original,local in asset_map.items()}
(dist/'notes').mkdir(exist_ok=True)
valid={'Paper Reviews','Mathematics','Computer Science','Coding','Miscellaneous'}
seen=set();equations=[];prepared=[]
for note in notes:
 assert note['slug'] not in seen,'Duplicate slug'
 seen.add(note['slug']);assert note['category'] in valid
 path=(root/'content/notes'/note['file']).resolve()
 assert path.is_relative_to(root/'content/notes')
 source=path.read_text()
 # Convert only export/display syntax. Source Markdown remains byte-for-byte intact.
 for original,local in asset_map.items():source=source.replace(original,local)
 source=re.sub(r'<table_of_contents[^>]*\s*/>', '\n\n[TOC]\n\n', source)
 source=re.sub(r'<empty-block[^>]*\s*/>', '\n\n', source)
 source=re.sub(r'^\s*</?(?:columns|column)\b[^>]*>\s*$', '', source, flags=re.M)
 source=re.sub(r'^\s*(!\[.*)',r'\1',source,flags=re.M)
 def attachment(m):
  local=m.group(1)
  return '\n\n['+asset_names.get(local,Path(local).name)+']('+local+')\n\n'
 source=re.sub(r'<(?:file|pdf) src="([^"]+)"[^>]*>.*?</(?:file|pdf)>',attachment,source,flags=re.S)
 source=re.sub(r'<span underline="true">(.*?)</span>',r'<u>\1</u>',source,flags=re.S)
 source=re.sub(r'\s*\{(?:color|toggle)="[^"\n]*"(?:\s+[^}\n]*)?\}', '',source)
 # Bold with trailing whitespace is valid in Notion; normalize its delimiter placement for HTML.
 source=re.sub(r'\*\*([^*\n]+?)\s+\*\*',lambda m:'**'+m.group(1).rstrip()+'**',source)

 def stash(m):
  display=m.group(1) is not None
  tex=(m.group(1) if display else m.group(2)).strip()
  index=len(equations);equations.append({'tex':tex,'display':display,'note':note['slug']})
  placeholder=f'NOTIONMATHPLACEHOLDER{index:06d}END'
  return ('\n\n'+placeholder+'\n\n') if display else placeholder
 # Protect math before Markdown can interpret underscores, escapes, and angle brackets.
 source=re.sub(r'\$\$\s*\n?(.*?)\n?\$\$|\$`(.*?)`\$',stash,source,flags=re.S)
 rendered=markdown.markdown(source,extensions=['fenced_code','tables','toc','md_in_html','sane_lists','nl2br'])
 prepared.append(rendered)
result=subprocess.run(['node',str(root/'scripts/render_math.cjs')],input=json.dumps(equations),text=True,capture_output=True,check=True)
math_results=json.loads(result.stdout)
errors=[{'note':e['note'],'tex':e['tex'],'error':r['error']} for e,r in zip(equations,math_results) if 'error' in r]
if errors:
 print(json.dumps(errors,ensure_ascii=False,indent=2))
 raise SystemExit(f'{len(errors)} math expressions could not be rendered.')
for note,rendered in zip(notes,prepared):
 def replace(m):
  index=int(m.group(1));return math_results[index]['html']
 rendered=re.sub(r'NOTIONMATHPLACEHOLDER(\d+)END',replace,rendered)
 rendered=rendered.replace('href="/p/', 'href="https://app.notion.com/p/')
 # Image requests go to durable local assets and wait until needed.
 rendered=re.sub(r'<img (?![^>]*loading=)', '<img loading="lazy" decoding="async" ',rendered)
 if 'notion-file-block://' in rendered:raise SystemExit(f'Unresolved image or attachment in {note["slug"]}')
 (dist/'notes'/f'{note["slug"]}.html').write_text(rendered)
 note['contentUrl']=f'notes/{note["slug"]}.html'
notes.sort(key=lambda n:(n['date'],n.get('topic',''),n['slug']),reverse=True)
(dist/'notes.json').write_text(json.dumps(notes,ensure_ascii=False))
(dist/'.nojekyll').touch()
print(f'Built {len(notes)} notes with {len(equations)} rendered equations.')

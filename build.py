"""Build Markdown notes and the static GitHub Pages site into docs/."""
from pathlib import Path
import html
import hashlib
import json
import re
import shutil
import subprocess
import markdown
from markdown.extensions.toc import slugify
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
css=re.sub(r',url\([^)]*\.(?:woff|ttf)\)\s*format\([^)]*\)', '',css)
(math_assets/'katex.min.css').write_text(css)
(math_assets/'fonts').mkdir()
for font in (katex/'fonts').glob('*.woff2'):shutil.copy(font,math_assets/'fonts'/font.name)
shutil.copy(root/'node_modules/katex/LICENSE',math_assets/'LICENSE')
notes=json.loads((root/'content/notes/index.json').read_text())
asset_map=json.loads((root/'content/notion-assets.json').read_text())
image_dimensions=json.loads((root/'content/image-dimensions.json').read_text())
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
 source=re.sub(r'<table_of_contents[^>]*\s*/>', '', source)
 source=re.sub(r'<callout[^>]*>', '\n\n<div class="note-callout" markdown="1">\n\n',source)
 source=source.replace('</callout>', '\n\n</div>\n\n')
 source=source.replace('<details>', '<details markdown="1">')
 source=re.sub(r'<empty-block[^>]*\s*/>', '\n\n', source)
 source=re.sub(r'^\s*</?(?:columns|column)\b[^>]*>\s*$', '', source, flags=re.M)
 source=re.sub(r'^\s*(!\[.*)',r'\1',source,flags=re.M)
 def attachment(m):
  local=m.group(1)
  return '\n\n['+asset_names.get(local,Path(local).name)+']('+local+')\n\n'
 source=re.sub(r'<(?:file|pdf) src="([^"]+)"[^>]*>.*?</(?:file|pdf)>',attachment,source,flags=re.S)
 source=re.sub(r'<span underline="true">(.*?)</span>',r'<u>\1</u>',source,flags=re.S)
 source=re.sub(r'\s*\{(?:color|toggle)="[^"\n]*"(?:\s+[^}\n]*)?\}', '',source)
 source=re.sub(r'\*\*[ \t]+\*\*', '',source)
 # Bold with trailing whitespace is valid in Notion; normalize its delimiter placement for HTML.
 source=re.sub(r'\*\*([^*\n]+)\*\*',lambda m:m.group(1)[:len(m.group(1))-len(m.group(1).lstrip())]+'**'+m.group(1).strip()+'**'+m.group(1)[len(m.group(1).rstrip()):],source)

 def stash(m):
  display=m.group(1) is not None
  tex=(m.group(1) if display else m.group(2)).strip()
  index=len(equations);equations.append({'tex':tex,'display':display,'note':note['slug']})
  placeholder=f'NOTIONMATHPLACEHOLDER{index:06d}END'
  return ('\n\n'+placeholder+'\n\n') if display else placeholder
 # Protect math before Markdown can interpret underscores, escapes, and angle brackets.
 source=re.sub(r'\$\$\s*\n?(.*?)\n?\$\$|\$`(.*?)`\$',stash,source,flags=re.S)
 source=source.replace(r'\<','&lt;').replace(r'\>','&gt;')
 # Notion indents ordinary prose and callouts with tabs. They are not code blocks.
 source=re.sub(r'^>\s*\n[\t ]+([^\n]+)', r'\n> \1\n\n',source,flags=re.M)
 source=re.sub(r'^(?:\t| {4})+([^\n]+)', r'\n\1\n',source,flags=re.M)
 # One page title, then a consistent section hierarchy for all imported reviews.
 source=re.sub(r'^(#{1,5})(?= )',r'#\1',source,flags=re.M)
 md=markdown.Markdown(extensions=['fenced_code','tables','toc','md_in_html','sane_lists'],extension_configs={'toc':{'slugify':lambda value,separator:slugify(re.sub(r'NOTIONMATHPLACEHOLDER\d+END','formula',value),separator)}})
 rendered=md.convert(source)
 prepared.append((rendered,md.toc))
result=subprocess.run(['node',str(root/'scripts/render_math.cjs')],input=json.dumps(equations),text=True,capture_output=True,check=True)
math_results=json.loads(result.stdout)
errors=[{'note':e['note'],'tex':e['tex'],'error':r['error']} for e,r in zip(equations,math_results) if 'error' in r]
if errors:
 print(json.dumps(errors,ensure_ascii=False,indent=2))
 raise SystemExit(f'{len(errors)} math expressions could not be rendered.')
for note,(rendered,toc) in zip(notes,prepared):
 def replace(m):
  index=int(m.group(1));return math_results[index]['html']
 rendered=re.sub(r'NOTIONMATHPLACEHOLDER(\d+)END',replace,rendered)
 toc=re.sub(r'NOTIONMATHPLACEHOLDER(\d+)END',replace,toc)
 rendered=rendered.replace('href="/p/', 'href="https://app.notion.com/p/')
 # Image requests go to durable local assets and wait until needed.
 rendered=re.sub(r'<img (?![^>]*loading=)', '<img loading="lazy" decoding="async" ',rendered)
 if 'notion-file-block://' in rendered:raise SystemExit(f'Unresolved image or attachment in {note["slug"]}')
 def pack_image(m):
  pack,key=m.group(1).split('#',1)
  width,height=image_dimensions[key]
  placeholder=f'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 {width} {height}%22%3E%3C/svg%3E'
  return f'src="{placeholder}" width="{width}" height="{height}" data-image-pack="../{pack}" data-image-key="{key}"'
 rendered=re.sub(r'src="(assets/notes/pack-[^"#]+\.json#[^"]+)"',pack_image,rendered)
 # Paths are relative to the standalone review page, including PDF downloads.
 rendered=rendered.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')
 esc=lambda value:html.escape(str(value),quote=True)
 meta=' · '.join(esc(note.get(k,'')) for k in ('category','topic','paperYear') if note.get(k))
 paper=(f'<a href="{esc(note["paperUrl"])}" target="_blank" rel="noopener noreferrer">Original paper ↗</a>' if note.get('paperUrl') else '')
 authors=f'<p class="review-authors">{esc(note["authors"])}</p>' if note.get('authors') else ''
 version=hashlib.sha256((dist/'style.css').read_bytes()).hexdigest()[:12]
 loader_version=hashlib.sha256((dist/'note-assets.js').read_bytes()).hexdigest()[:12]
 image_loader=f'<script src="../note-assets.js?v={loader_version}" defer></script>' if 'data-image-pack=' in rendered else ''
 outline=f'<aside class="review-outline" aria-label="Table of contents"><details open><summary>On this page</summary>{toc}</details></aside>' if '<li>' in toc else ''
 page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(note['title'])} — Kim Su Hwan</title>
<meta name="description" content="{esc(note.get('summary') or note['title'])}">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css?v={version}"><link rel="stylesheet" href="../assets/katex/katex.min.css">
{image_loader}</head><body class="review-page"><a class="skip" href="#review-body">Skip to review</a>
<header class="review-topbar"><a href="../index.html">Kim Su Hwan</a><a href="../index.html#notes">← All notes</a></header>
<main class="review-shell"><article class="review-article"><header class="review-header"><p class="note-meta">{meta}</p><h1>{esc(note['title'])}</h1>{authors}<div class="review-links">{paper}</div></header>
<div class="review-body" id="review-body">{rendered}</div>
<footer class="review-footer"><a href="../index.html#notes">← Back to all notes</a><a href="#">Back to top ↑</a></footer></article>{outline}</main>
</body></html>'''
 page='\n'.join(line.rstrip() for line in page.splitlines())+'\n'
 (dist/'notes'/f'{note["slug"]}.html').write_text(page)
 note['contentUrl']=f'notes/{note["slug"]}.html'
notes.sort(key=lambda n:n['title'].casefold())
(dist/'notes.json').write_text(json.dumps(notes,ensure_ascii=False))
# Version asset URLs so readers always receive the matching script and stylesheet.
index=(dist/'index.html').read_text()
for filename,attribute in [('script.js','src'),('style.css','href')]:
 version=hashlib.sha256((dist/filename).read_bytes()).hexdigest()[:12]
 index=index.replace(f'{attribute}="{filename}"',f'{attribute}="{filename}?v={version}"')
(dist/'index.html').write_text(index)
(dist/'.nojekyll').touch()
print(f'Built {len(notes)} notes with {len(equations)} rendered equations.')

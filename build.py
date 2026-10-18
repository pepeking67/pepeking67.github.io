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
experience_index=root/'content/experiences/index.json'
experiences=json.loads(experience_index.read_text()) if experience_index.exists() else []
entries=notes+experiences
asset_map=json.loads((root/'content/notion-assets.json').read_text())
image_dimensions=json.loads((root/'content/image-dimensions.json').read_text())
asset_names={local:parse_qs(urlparse(original).query).get('name',[Path(local).name])[0] for original,local in asset_map.items()}
(dist/'notes').mkdir(exist_ok=True)
(dist/'experiences').mkdir(exist_ok=True)
valid={'Paper Reviews','Mathematics','Computer Science','Coding','Miscellaneous','Experiences'}
seen=set();equations=[];prepared=[]
for note in entries:
 assert note['slug'] not in seen,'Duplicate slug'
 seen.add(note['slug']);assert note['category'] in valid
 source_directory=root/('content/experiences' if note['category']=='Experiences' else 'content/notes')
 path=(source_directory/note['file']).resolve()
 assert path.is_relative_to(source_directory)
 source=path.read_text()
 # Convert only export/display syntax. Source Markdown remains byte-for-byte intact.
 for original,local in asset_map.items():source=source.replace(original,local)
 source=re.sub(r'<unknown url="([^"]+)"[^>]*/>',lambda m:'\n\n[View embedded link on Notion ↗]('+m.group(1)+')\n\n',source)
 source=re.sub(r'<video src="([^"]+)"[^>]*>\s*</video>',lambda m:'\n\n<div class="note-video" style="margin:24px 0"><button type="button" data-load-video style="padding:10px 16px;border:1px solid #ddd;border-radius:5px;background:#fff;cursor:pointer">Load demo video</button><video hidden controls preload="none" playsinline style="width:100%;max-height:720px" data-video-manifest="'+html.escape(m.group(1),quote=True)+'"></video><p role="status" hidden></p></div>\n\n',source)
 if note['category']=='Experiences':source=re.sub(r'^(Tab\s*\d+\s*:[^\n]+)$',r'## \1',source,flags=re.M)
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
 source=re.sub(r'\*\*[ \t]+\*\*(?=\s|$)', '',source)
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
 if note['category']=='Experiences':
  # Keep project directory trees and code indentation intact.
  lines=source.splitlines(keepends=True);in_code=False;unindented=[]
  for line in lines:
   if line.lstrip().startswith(('```','~~~')):in_code=not in_code
   unindented.append(line if in_code else re.sub(r'^(?:\t| {4})+([^\n]+)',r'\n\1\n',line))
  source=''.join(unindented)
 else:source=re.sub(r'^(?:\t| {4})+([^\n]+)', r'\n\1\n',source,flags=re.M)
 # Notion exports adjacent paragraph/list blocks without Markdown's blank lines.
 # Add display-only boundaries so bullets do not become inline paragraph text.
 if note.get('sourceFormat')=='notion':
  lines=source.splitlines();normalized=[];in_code=False
  is_list=lambda line:bool(re.match(r'^\s*(?:[-+*]|\d+[.)])\s+',line))
  for i,line in enumerate(lines):
   if line.lstrip().startswith(('```','~~~')):in_code=not in_code
   if not in_code and i and line.strip() and lines[i-1].strip():
    previous=lines[i-1]
    starts_list=is_list(line) and not is_list(previous)
    ends_list=is_list(previous) and not is_list(line) and not line.startswith(('  ','\t'))
    if starts_list or ends_list:normalized.append('')
   normalized.append(line)
  source='\n'.join(normalized)
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
for note,(rendered,toc) in zip(entries,prepared):
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
 rendered=rendered.replace('data-video-manifest="assets/', 'data-video-manifest="../assets/').replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')
 esc=lambda value:html.escape(str(value),quote=True)
 meta=' · '.join(esc(note.get(k,'')) for k in ('category','topic','paperYear','period') if note.get(k))
 is_experience=note['category']=='Experiences'
 folder='experiences' if is_experience else 'notes'
 home_anchor='experiences' if is_experience else 'notes'
 back_label='All experiences' if is_experience else 'All notes'
 footer_label='Back to experiences' if is_experience else 'Back to all notes'
 skip_label='Skip to content' if is_experience else 'Skip to review'
 paper=(f'<a href="{esc(note["paperUrl"])}" target="_blank" rel="noopener noreferrer">Original paper ↗</a>' if note.get('paperUrl') else '')
 authors=f'<p class="review-authors">{esc(note["authors"])}</p>' if note.get('authors') else ''
 version=hashlib.sha256((dist/'style.css').read_bytes()).hexdigest()[:12]
 loader_version=hashlib.sha256((dist/'note-assets.js').read_bytes()).hexdigest()[:12]
 media_loader=f'<script src="../madcamp-media.js?v={hashlib.sha256((root / "src" / "madcamp-media.js").read_bytes()).hexdigest()[:12]}" defer></script>' if 'data-video-manifest=' in rendered else ''
 image_loader=f'<script src="../note-assets.js?v={loader_version}" defer></script>' if 'data-image-pack=' in rendered else ''
 outline=f'<aside class="review-outline" aria-label="Table of contents"><details open><summary>On this page</summary>{toc}</details></aside>' if '<li>' in toc else ''
 page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(note['title'])} — Kim Su Hwan</title>
<meta name="description" content="{esc(note.get('summary') or note['title'])}">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css?v={version}"><link rel="stylesheet" href="../assets/katex/katex.min.css">
{image_loader}{media_loader}</head><body class="review-page"><a class="skip" href="#review-body">{skip_label}</a>
<header class="review-topbar"><a href="../index.html">Kim Su Hwan</a><a href="../index.html#{home_anchor}">← {back_label}</a></header>
<main class="review-shell"><article class="review-article"><header class="review-header"><p class="note-meta">{meta}</p><h1>{esc(note['title'])}</h1>{authors}<div class="review-links">{paper}</div></header>
<div class="review-body" id="review-body">{rendered}</div>
<footer class="review-footer"><a href="../index.html#{home_anchor}">← {footer_label}</a><a href="#">Back to top ↑</a></footer></article>{outline}</main>
</body></html>'''
 page='\n'.join(line.rstrip() for line in page.splitlines())+'\n'
 (dist/folder/f'{note["slug"]}.html').write_text(page)
 note['contentUrl']=f'{folder}/{note["slug"]}.html'
notes.sort(key=lambda n:n['title'].casefold())
(dist/'notes.json').write_text(json.dumps(notes,ensure_ascii=False))
# Version asset URLs so readers always receive the matching script and stylesheet.
index=(dist/'index.html').read_text()
for filename,attribute in [('script.js','src'),('style.css','href')]:
 version=hashlib.sha256((dist/filename).read_bytes()).hexdigest()[:12]
 index=index.replace(f'{attribute}="{filename}"',f'{attribute}="{filename}?v={version}"')
(dist/'index.html').write_text(index)
(dist/'.nojekyll').touch()
print(f'Built {len(notes)} notes and {len(experiences)} experience pages with {len(equations)} rendered equations.')

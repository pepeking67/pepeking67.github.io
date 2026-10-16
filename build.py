"""Build the static site. Notes metadata lives in content/notes/index.json."""
from pathlib import Path
import json
import shutil
root = Path(__file__).resolve().parent
dist = root / 'docs'
if dist.exists():
    shutil.rmtree(dist)
shutil.copytree(root / 'src', dist)
notes = json.loads((root / 'content/notes/index.json').read_text())
valid_categories = {'Paper Reviews', 'Mathematics', 'Computer Science', 'Coding', 'Miscellaneous'}
seen = set()
for note in notes:
    assert note['slug'] not in seen, 'Duplicate note slug'
    seen.add(note['slug'])
    assert note['category'] in valid_categories, 'Unknown category'
    path = (root / 'content/notes' / note['file']).resolve()
    assert path.is_relative_to(root / 'content/notes'), 'Invalid note path'
    import markdown
    note['html'] = markdown.markdown(path.read_text(), extensions=['fenced_code', 'tables', 'toc'])
notes.sort(key=lambda n: n['date'], reverse=True)
(dist / 'notes.json').write_text(json.dumps(notes, ensure_ascii=False))
(dist / '.nojekyll').touch()
print(f'Built site with {len(notes)} notes.')

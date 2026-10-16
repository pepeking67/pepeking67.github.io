# Kim Su Hwan — Personal Website

Live website: https://pepeking67.github.io

## Structure
- `src/`: homepage HTML, CSS, JavaScript, and assets.
- `content/notes/`: Markdown notes and their metadata index.
- `docs/`: generated site published by GitHub Pages from `main`.

## Update the website
1. Edit source files or add Markdown notes.
2. Run `python -m pip install -r requirements.txt`.
3. Run `python build.py` to regenerate `docs/`.
4. Commit both source and generated files. GitHub Pages updates automatically after changes reach `main`.

## Add a note
Add a Markdown file under `content/notes/` and an entry to `content/notes/index.json`:
```json
[{"slug":"my-note","title":"My Note","date":"2026-10-17","category":"Mathematics","summary":"A short description.","file":"my-note.md"}]
```
Supported categories: Paper Reviews, Mathematics, Computer Science, Coding, Miscellaneous. Notes are read inside the website. Mathematical typesetting is not configured yet.

## Local preview
Run `python -m http.server 8000 --directory docs` after building.

## Hosting
GitHub Pages: Deploy from a branch → `main` → `/docs`. No backend, credentials, or paid hosting is needed.

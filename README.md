# Kim Su Hwan — Personal Website

Live website: https://pepeking67.github.io

## Structure
- `src/`: homepage HTML, CSS, JavaScript, and assets.
- `content/notes/`: Markdown notes and their metadata index.
- `docs/`: generated site published by GitHub Pages from `main`.

## Update the website
1. Edit source files or add Markdown notes.
2. Run `python -m pip install -r requirements.txt` and `npm ci`.
3. Run `python build.py` to regenerate `docs/`.
4. Commit both source and generated files. GitHub Pages updates automatically after changes reach `main`.

## Add a note
Add a Markdown file under `content/notes/` and an entry to `content/notes/index.json`:
```json
[{"slug":"my-note","title":"My Note","date":"2026-10-17","category":"Mathematics","summary":"A short description.","file":"my-note.md"}]
```
Supported categories: Paper Reviews, Mathematics, Computer Science, Coding, Miscellaneous. Notes are read inside the website. Equations are rendered at build time with self-hosted KaTeX. Imported Notion Markdown is kept verbatim in `content/notes/`; the builder converts only presentation syntax and uses `content/notion-assets.json` to resolve original image and attachment references. The import date is not a paper reading date.

## Local preview
Run `python -m http.server 8000 --directory docs` after building.

## Hosting
GitHub Pages: Deploy from a branch → `main` → `/docs`. No backend, credentials, or paid hosting is needed.

## Adding study notes

All categories share the standalone reading page with the table of contents on the right (above the article on smaller screens). Keep the imported Markdown body unchanged in `content/notes/`, and add its title, category, topic, slug, file, and sourceId to `content/notes/index.json`. Course notes use the course name followed by `(1)`, `(2)`, etc.; the summary identifies the source section. Counts, title sorting, and 15-entry pagination update from this index.

Notion callouts and proofs are converted only for presentation. Course images retain their original bytes in local image packs under `src/assets/notes/`; `content/notion-assets.json` and `content/image-dimensions.json` connect stable references to those images. The reader loads image packs as they approach the viewport. Never commit temporary signed Notion URLs or modify the Notion source while importing.

For newly imported Notion pages, set `sourceFormat` to `notion` in the metadata. The builder adds Markdown list boundaries for display without changing the stored source body.

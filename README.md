# Mutasim Billah — Portfolio

A responsive static portfolio for Mutasim Billah, featuring robotics projects, achievements, selected photography, public repositories, and contact links.

## What is included

- Facebook-style cover and profile introduction
- Project galleries for DurontoJatra, Pagla Ghora LFR, personal builds, and QuadBits
- Achievement cards and photography stories
- Full-image viewer: photos keep their original proportions on the page and open larger when selected
- Links to GitHub, Facebook, Instagram, and WhatsApp
- A GitHub Pages workflow that publishes the contents of `dist/`

## Project structure

```text
dist/                         Published website files
  assets/images/              Optimized WebP images used by the site
  index.html                  Page content and photo captions
  styles.css                  Design and responsive layout
  app.js                      Mobile menu and full-image viewer
tools/serve.mjs               Local static preview server
tools/import-images.mjs       Local image conversion helper
.github/workflows/pages.yml   GitHub Pages deployment workflow
```

## Preview the site locally

No package installation is needed to preview the current website. From the project folder, run:

```powershell
node tools/serve.mjs
```

Then open `http://127.0.0.1:4318` in your browser. Stop the preview with `Ctrl + C` in the terminal.

## Update content

- Edit `dist/index.html` for text, project cards, links, and photo stories.
- Edit `dist/styles.css` for layout, colours, and responsive behaviour.
- Put replacement website images in `dist/assets/images/` and update the matching path in `dist/index.html`.

The `tools/import-images.mjs` helper converts the original image folders into WebP files. It is intended for this local workspace; the published site only needs the ready-to-use files already inside `dist/`.


# Maintaining the portfolio

Notes for updating and publishing the site. For what the portfolio is about, see the [README](../README.md).

## Project structure

```text
dist/                            Published website files
  index.html                     Page content and photo captions
  styles.css                     Design and responsive layout
  app.js                         Mobile menu and full-image viewer
  assets/images/                 Optimized WebP images used by the site
  assets/manrope-variable.woff2  Self-hosted Manrope font (all weights, SIL OFL, see assets/OFL.txt)
  assets/og-image.jpg            1200x630 preview image for social link shares
  assets/Mutasim-Billah-CV.pdf   Downloadable CV (generated, see below)
tools/serve.mjs                  Local static preview server
tools/import-images.mjs          Local image conversion helper
tools/build-cv.py                Generates the CV PDF from tools/cv-profile.json
tools/cv-profile.json            CV content
.github/workflows/pages.yml      GitHub Pages deployment workflow
```

## Preview locally

No package installation is needed. From the project folder, run:

```powershell
node tools/serve.mjs
```

Then open `http://127.0.0.1:4318`. Stop the preview with `Ctrl + C`.

## Update content

- Edit `dist/index.html` for text, project cards, links, and photo stories.
- Edit `dist/styles.css` for layout, colours, and responsive behaviour.
- Put replacement images in `dist/assets/images/` and update the matching path in `dist/index.html`.

`tools/import-images.mjs` converts the original image folders into WebP files. It is intended for the local workspace; the published site only needs the files already inside `dist/`.

## Rebuild the CV

The CV is generated from `tools/cv-profile.json`. After changing the facts there, install ReportLab once with `python -m pip install reportlab`, then run:

```powershell
python tools/build-cv.py
```

The script writes a review copy in `output/pdf/` and updates `dist/assets/Mutasim-Billah-CV.pdf`. Check that it still fits on one page.

`.gitattributes` marks PDFs, images, and fonts as binary so Git never rewrites their line endings. Without it, Windows line-ending conversion can corrupt the CV PDF.

## Publish

Every push to `main` runs **Deploy Portfolio to GitHub Pages**, which publishes `dist/` to https://1467mutasim-ctrl.github.io/MTB-Portfolio/. GitHub Pages must stay set to **Settings → Pages → Source: GitHub Actions**.

```powershell
git add .
git commit -m "Update portfolio"
git push
```

The canonical URL and `og:image` in `dist/index.html`, and the `portfolio` link in `tools/cv-profile.json`, point to `https://mutasim-billah-portfolio.ekincihalime54.chatgpt.site/`. If GitHub Pages or a custom domain becomes the main address, update all three.

## Notes

- Keep `dist/` in the repository. It is the website that GitHub Pages publishes.
- Keep `reference/` private. It is ignored by Git and is not needed for the live site.
- Don't put private API keys, passwords, or personal documents in the repository.

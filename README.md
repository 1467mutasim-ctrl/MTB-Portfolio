# Mutasim Billah — Portfolio

A responsive static portfolio for Mutasim Billah, featuring robotics projects, achievements, selected photography, public repositories, and contact links.

## What is included

- Cover photo and profile introduction with CV, LinkedIn, and GitHub links
- Project case studies: CPU Scheduler Visualizer (featured), Robo Soccer, Pagla Ghora LFR, ESP32 builds, DurontoJatra, and QuadBits AgroBot
- Competition results and leadership roles, with photos that open in the full-image viewer
- Photography stories with short captions and expandable backstories
- Links to email, LinkedIn, GitHub, Facebook, Instagram, and WhatsApp
- A social preview image (`assets/og-image.jpg`) for link shares
- A one-page downloadable CV generated from `tools/cv-profile.json`
- A GitHub Pages workflow that publishes the contents of `dist/`

## Project structure

```text
dist/                         Published website files
  assets/images/              Optimized WebP images used by the site
  assets/manrope-variable.woff2  Self-hosted Manrope font (all weights, SIL OFL, see assets/OFL.txt)
  assets/og-image.jpg         1200x630 preview image for social link shares
  index.html                  Page content and photo captions
  styles.css                  Design and responsive layout
  app.js                      Mobile menu and full-image viewer
tools/serve.mjs               Local static preview server
tools/import-images.mjs       Local image conversion helper
tools/build-cv.py             Generates the CV PDF from tools/cv-profile.json
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

The downloadable CV is generated from `tools/cv-profile.json`. After changing the facts there, install ReportLab once with `python -m pip install reportlab`, then run `python tools/build-cv.py`. The script writes a review copy in `output/pdf/` and updates the website copy at `dist/assets/Mutasim-Billah-CV.pdf`. Check that it still fits on one page.

`.gitattributes` marks PDFs, images, and fonts as binary so Git never rewrites their line endings. Without it, Windows line-ending conversion can corrupt the CV PDF.

The canonical URL and `og:image` in `dist/index.html` point to the live site at `https://mutasim-billah-portfolio.ekincihalime54.chatgpt.site/`. If you move the site to GitHub Pages or a custom domain, update those tags and the `portfolio` link in `tools/cv-profile.json`.

## Push updates to GitHub

This folder is already connected to `https://github.com/1467mutasim-ctrl/MTB-Portfolio`. To publish changes:

```powershell
git add .
git commit -m "Update portfolio"
git push
```

## Publish with GitHub Pages

After the first push:

1. Open the repository on GitHub.
2. Go to **Settings** → **Pages**.
3. Under **Build and deployment**, choose **GitHub Actions** as the source.
4. Open the **Actions** tab and wait for **Deploy Portfolio to GitHub Pages** to finish.

Your site will be available at:

```text
https://1467mutasim-ctrl.github.io/MTB-Portfolio/
```

Every push to `main` will publish the latest contents of `dist/` automatically. This workflow follows GitHub’s recommended Pages deployment pattern using a deployment artifact and the official Pages actions. [GitHub’s Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## Notes

- Keep `dist/` in the repository. It is the website that GitHub Pages publishes.
- Keep `reference/` private. It is ignored by Git and is not needed for the live site.
- Avoid putting private API keys, passwords, or personal documents in the repository.

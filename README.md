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

## Upload to GitHub

The cleanest approach is to create an empty GitHub repository, then push this project with Git. Do **not** add a README, `.gitignore`, or license while creating the GitHub repository because this project already has them.

Open PowerShell in this folder and run the following commands. Replace `YOUR-REPOSITORY` with the repository name you chose.

```powershell
cd D:\Claude\mutasim-portfolio
git add .
git commit -m "Publish portfolio website"
git branch -M main
git remote add origin https://github.com/1467mutasim-ctrl/MTB-Portfolio.git
git push -u origin main
```

If GitHub asks you to sign in, complete the browser sign-in prompt, then run the last command again.

For later updates, only these three commands are needed:

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
https://1467mutasim-ctrl.github.io/YOUR-REPOSITORY/
```

Every push to `main` will publish the latest contents of `dist/` automatically. This workflow follows GitHub’s recommended Pages deployment pattern using a deployment artifact and the official Pages actions. [GitHub’s Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## Notes

- Keep `dist/` in the repository. It is the website that GitHub Pages publishes.
- Keep `reference/` private. It is ignored by Git and is not needed for the live site.
- Avoid putting private API keys, passwords, or personal documents in the repository.

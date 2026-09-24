# Nick Visuthikosol, portfolio

Plain HTML/CSS/JS. No build step. Live at https://visuthikosol.github.io

## Structure
- `index.html`: landing page (products, then design projects)
- `projects.html`: all projects grid
- `work/*.html`: one page per project (Read more / Learn more)
- `about.html`, `contact.html`
- `css/style.css`, `js/main.js`: shared styles, mobile menu, reveals, image lightbox
- `assets/img/*.webp`: cover images

## Editing a project
Open `work/<project>.html` and edit the text directly. To add gallery images,
copy a `<figure>` line inside a `.pgrid` div and change the `src`.

## Publish
```
git add -A
git commit -m "describe your change"
git push
```
GitHub Pages redeploys in a minute or two.

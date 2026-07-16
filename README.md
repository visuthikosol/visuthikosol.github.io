# Nick Visuthikosol — Portfolio Site

Plain HTML/CSS/JS. No build step, no framework, no npm install needed —
just files you can open directly or push straight to GitHub.

## 1. Add your photos

The site is already wired up to look for images at these exact paths.
Drop your photos in with these exact filenames and they'll appear
automatically — no code editing needed. If a file is missing, that spot
shows a clean placeholder instead of a broken image icon, so the site
never looks broken while you're filling things in.

Put files in `assets/img/`:

| Filename                     | Used for                          |
|-------------------------------|------------------------------------|
| `liminal-umbrella.png`        | ✅ already added                   |
| `whifflewash.jpg`              | WhiffleWash                        |
| `oscar.jpg`                    | OSCAR 3D Model Validation Tool     |
| `ps4-controller.jpg`           | One-Handed PS4 Controller          |
| `arm-rehab.jpg`                 | Arm Rehabilitation Machine        |
| `surf-chair.jpg`                | Surf Chair                        |
| `architectural-design.jpg`      | Architectural Design tile          |
| `industrial-design.jpg`         | Industrial Design tile             |
| `cad-modeling.jpg`              | 3D Modeling (CAD) tile             |
| `rendering-animation.jpg`       | Rendering and Animation tile       |
| `profile-photo.jpg`             | About page portrait                |

Any image format works (jpg/png/webp) as long as the filename matches —
just keep the extension consistent with what's in the HTML, or tell me
the real filenames and I'll update the code to match.

## 2. Preview locally (optional)

You don't need this to push to GitHub, but if you want to look at it
first: open `index.html` directly in your browser (double-click it), or
for the most accurate preview run a tiny local server from this folder:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000` in your browser.

## 3. Push to GitHub

If you don't have a repo yet:

1. Go to github.com → **New repository**. Name it whatever you want —
   for a personal site, naming it `yourusername.github.io` gets you the
   cleanest URL (see step 5).
2. On your computer, open a terminal in this folder and run:

```bash
git init
git add .
git commit -m "Initial portfolio site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

(Replace the URL with the one GitHub shows you after creating the repo.)

## 4. Turn on GitHub Pages

1. In your repo on GitHub, go to **Settings → Pages**.
2. Under "Build and deployment," set **Source** to `Deploy from a branch`.
3. Set **Branch** to `main` and folder to `/ (root)`. Save.
4. Wait ~1 minute, then refresh — GitHub will show you the live URL at
   the top of that page.

## 5. Your URL

- If your repo is named `yourusername.github.io` → your site is live at
  `https://yourusername.github.io`
- Any other repo name → it's live at
  `https://yourusername.github.io/repo-name`

## Making future edits

Every page is a plain `.html` file you can open and edit directly —
`index.html` (Home), `about.html`, `projects.html`, `contact.html`.
Shared styling lives in `css/style.css`. After editing, just:

```bash
git add .
git commit -m "describe your change"
git push
```

GitHub Pages redeploys automatically within a minute or two.

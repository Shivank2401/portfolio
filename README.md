# Shivank Rajput – Portfolio

A Framer-style portfolio site (inspired by [DevSync](https://devsync.framer.website/)), built with static HTML/CSS/JS and ready for **GitHub Pages**.

Content is sourced from the project’s DOCX and PPT files (resume/CV and presentation).

---

## Run locally

Open the site from the `docs` folder:

- **Option A:** Open `docs/index.html` in your browser.
- **Option B:** From project root, run a simple server, e.g.:
  - `python -m http.server 8000` then visit `http://localhost:8000/docs/`
  - or use the “Live Server” extension in VS Code and open `docs/index.html`.

---

## Deploy on GitHub Pages

1. **Create a GitHub repo** (e.g. `portfolio` or `username.github.io`).

2. **Push this project** to the repo (include the `docs` folder and `docs/index.html`).

3. **Enable GitHub Pages:**
   - Repo → **Settings** → **Pages**
   - Under **Build and deployment**:
     - **Source:** Deploy from a branch
     - **Branch:** `main` (or your default branch)
     - **Folder:** `/docs`
   - Click **Save**.

4. **View the site:**  
   `https://<username>.github.io/<repo-name>/`  
   If the repo is named `username.github.io`, the URL is `https://username.github.io/`.

---

## Project structure

- `docs/index.html` – Single-page portfolio (HTML, CSS, JS).
- `docs/.nojekyll` – Tells GitHub Pages not to use Jekyll (optional, for consistency).
- `word.py` – Generates DOCX resume/CV.
- `ppt.py` – Generates PPTX presentation.
- `brain/` – Project notes and knowledge base (do not delete).

To update the website content, edit `docs/index.html` and push to the same branch; GitHub Pages will update after a short delay.


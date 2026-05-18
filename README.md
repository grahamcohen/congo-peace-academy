# Congo Peace Academy — Website

A new website for [Congo Peace Academy](https://www.congopeaceacademy.org/) — a Goma-based organization transforming communities in Eastern DRC through education, peacebuilding, entrepreneurship, and conservation agriculture.

The visual direction is inspired by [Bridge2Rwanda](https://www.bridge2rwanda.org/) — clean editorial typography, generous whitespace, alternating image/text rows — adapted to CPA's brand colors (deep forest green and warm amber) and using CPA's own content verbatim.

## What's in here

```
cpa-site/
├── index.html                        Homepage
├── about/
│   ├── index.html                    About landing
│   ├── our-history.html              Brief history + impacts + partners
│   ├── our-team.html                 Team profiles + values
│   └── blog.html                     "Peace Today" blog post
├── agri-peace.html                   Foundation for Farming program
├── path-to-the-future.html           College Prep 2025
├── health-for-peace.html             Health program
├── our-events/
│   ├── index.html                    Humanitarian crisis / IDP camp coverage
│   ├── peace-today.html              Long-form field reports
│   └── become-volunteers.html        Fellows / volunteer application
├── assets/
│   ├── css/style.css                 Design system + all components
│   ├── js/main.js                    Mobile nav, scroll reveal, sticky header
│   └── images/favicon.svg            CPA monogram
├── build_pages.py                    Generator for the inner pages (not required at runtime)
├── download_images.sh                One-shot script to self-host the images
└── README.md
```

Plain static HTML/CSS/JS. No framework, no build step, no dependencies.

## Preview locally

Open `index.html` in a browser, or run a tiny local server (recommended so paths behave like production):

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Deploy

Any static host works. A few zero-config options:

- **GitHub Pages** — push to GitHub, then in repo Settings → Pages, select branch `main` and folder `/ (root)`. Done.
- **Netlify** — drag the `cpa-site` folder onto [app.netlify.com/drop](https://app.netlify.com/drop). Or connect the GitHub repo and accept defaults (no build command, publish directory `/`).
- **Vercel** — `vercel` from inside this directory; accept defaults.
- **Cloudflare Pages** — connect the repo, leave build settings empty, set output directory to `/`.

## Important note on images

Images currently load from `lh3.googleusercontent.com` — the same URLs the existing Google-Sites version of CPA uses. They work today but **Google can rotate or expire those URLs at any time**. Before the site goes live for real, run:

```bash
./download_images.sh
```

This pulls every Google-hosted image into `assets/images/downloaded/` and rewrites the HTML to use local copies. After running it once, commit the new images and you're permanently free from Google's image hosting.

Requires `bash`, `curl`, and `python3`.

## Customizing

### Colors

All brand colors are CSS variables at the top of `assets/css/style.css`:

```css
--green-deep: #0F3B26;   /* primary brand */
--green:      #1B5E3A;
--green-mid:  #2A7A4F;
--green-bright:#3FA06A;
--amber:      #D69A30;   /* accent */
--amber-deep: #A87324;
--cream:      #FAF6EE;   /* background */
--ink:        #0E1614;   /* body text */
```

Change them in one place and the whole site follows.

### Typography

- Display: **Fraunces** (variable serif — used for headings, with italic for accents)
- Body: **DM Sans**

Loaded via Google Fonts. Already preconnected for performance.

### Content

Each page is a single HTML file you can edit directly. The page generator (`build_pages.py`) created the inner pages from a shared template — useful for sweeping changes (footer text, nav links) — but you can also just edit the HTML by hand. Don't worry about regenerating unless you want to.

### Adding a new page

1. Copy any existing inner page (e.g. `about/blog.html`) as a starting point.
2. Update the page hero, breadcrumbs, and content.
3. Add it to the nav in **every** HTML file (no JS includes, so nav is duplicated per page — search and replace is your friend).
4. Add it to the footer's link lists.

## Browser support

Modern evergreen browsers (Chrome, Edge, Firefox, Safari — last two versions). Uses CSS Grid, custom properties, `aspect-ratio`, `:focus-visible`. Works on IE11? No, and nobody asked.

## Accessibility

- Skip-to-main link
- Visible focus states (`:focus-visible`)
- Semantic landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`)
- Mobile nav opens with `Esc` to close
- Reduced-motion media query disables scroll reveals
- Color contrast meets WCAG AA throughout

## Credits

Built for Bienfait Mugenza and the Congo Peace Academy team. All copy and content is © Congo Peace Academy.

## Contact

congopeaceacademy@gmail.com · Goma, DRC · +243 992 767 008

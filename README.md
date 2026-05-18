# Congo Peace Academy

Website for [Congo Peace Academy](https://www.congopeaceacademy.org/) — a Goma-based organization transforming communities in Eastern DRC through education, peacebuilding, entrepreneurship, and conservation agriculture.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Structure

```
index.html
about/                   About, History, Team, Blog
agri-peace.html          Foundation for Farming program
path-to-the-future.html  College Prep 2025
health-for-peace.html
our-events/              Humanitarian coverage, Peace Today, Volunteers
assets/css/style.css     Design system
assets/js/main.js        Mobile nav + scroll reveal
```

Plain static HTML/CSS/JS. No framework, no build step.

## Deploy

Any static host. Configured for GitHub Pages — push to `main` and enable Pages in repo settings.

## Customizing

Brand colors live as CSS variables at the top of `assets/css/style.css`. Change them in one place and the whole site follows.

Fonts: **Fraunces** (display) and **DM Sans** (body), loaded from Google Fonts.

## Contact

congopeaceacademy@gmail.com · Goma, DRC · +243 992 767 008

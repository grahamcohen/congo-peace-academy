#!/usr/bin/env python3
"""Generate the remaining CPA site pages from a shared template."""
import os, html
from pathlib import Path

ROOT = Path(__file__).parent

# ---------------------------------------------------------------------------
# Template parts
# ---------------------------------------------------------------------------

def head(title, desc, prefix):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)} — Congo Peace Academy</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="theme-color" content="#0F3B26" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..900,30..100;1,9..144,300..900,30..100&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="{prefix}assets/css/style.css" />
  <link rel="icon" type="image/svg+xml" href="{prefix}assets/images/favicon.svg" />
</head>
<body>

<a href="#main" class="skip-link">Skip to main content</a>

<div class="banner">
  <div class="container banner-content">
    <span>Path to the Future 2025 — College Prep applications open</span>
    <a href="{prefix}path-to-the-future.html">Apply now →</a>
  </div>
</div>
"""

def header(prefix, current_section=None):
    """current_section: 'about' | 'agri' | 'path' | 'health' | 'events' | None"""
    aria_about = ' aria-current="page"' if current_section == 'about' else ''
    aria_agri  = ' aria-current="page"' if current_section == 'agri'  else ''
    aria_path  = ' aria-current="page"' if current_section == 'path'  else ''
    aria_health= ' aria-current="page"' if current_section == 'health'else ''
    aria_events= ' aria-current="page"' if current_section == 'events'else ''
    return f"""
<header class="site-header">
  <div class="container">
    <nav class="nav" aria-label="Primary">
      <a href="{prefix}index.html" class="brand" aria-label="Congo Peace Academy home">
        <span class="brand-mark" aria-hidden="true">CPA</span>
        <span class="brand-text">Congo Peace Academy<span class="brand-text-sub">Goma · DRC</span></span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="nav-list">
        <span class="nav-toggle-bar" aria-hidden="true"></span>
      </button>
      <ul class="nav-list" id="nav-list">
        <li class="nav-item has-sub">
          <a class="nav-link" href="{prefix}about/index.html"{aria_about}>About</a>
          <ul class="subnav">
            <li><a class="subnav-link" href="{prefix}about/index.html">About Us</a></li>
            <li><a class="subnav-link" href="{prefix}about/our-history.html">Our History</a></li>
            <li><a class="subnav-link" href="{prefix}about/our-team.html">Our Team</a></li>
            <li><a class="subnav-link" href="{prefix}about/blog.html">Blog</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="{prefix}agri-peace.html"{aria_agri}>Agri Peace</a></li>
        <li class="nav-item"><a class="nav-link" href="{prefix}path-to-the-future.html"{aria_path}>Path to the Future</a></li>
        <li class="nav-item"><a class="nav-link" href="{prefix}health-for-peace.html"{aria_health}>Health for Peace</a></li>
        <li class="nav-item has-sub">
          <a class="nav-link" href="{prefix}our-events/index.html"{aria_events}>Our Events</a>
          <ul class="subnav">
            <li><a class="subnav-link" href="{prefix}our-events/index.html">All Events</a></li>
            <li><a class="subnav-link" href="{prefix}our-events/peace-today.html">Peace Today</a></li>
            <li><a class="subnav-link" href="{prefix}our-events/become-volunteers.html">Become Volunteers</a></li>
          </ul>
        </li>
      </ul>
      <div class="nav-actions">
        <a class="btn btn-primary" href="https://donorbox.org/congo-peace-academy-1-3?default_interval=o" target="_blank" rel="noopener">Donate</a>
      </div>
    </nav>
  </div>
</header>

<main id="main">
"""

def footer(prefix):
    return f"""
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="brand" style="color:var(--paper)">
          <span class="brand-mark" aria-hidden="true">CPA</span>
          <span class="brand-text">Congo Peace Academy<span class="brand-text-sub" style="color:rgba(250,246,238,0.6)">Goma · DRC</span></span>
        </div>
        <p>A movement of hope working hand in hand with communities to build peace, dignity, and lasting opportunity across Eastern DRC.</p>
      </div>
      <div>
        <h4>Programs</h4>
        <ul class="footer-list">
          <li><a href="{prefix}agri-peace.html">Agri Peace</a></li>
          <li><a href="{prefix}path-to-the-future.html">Path to the Future</a></li>
          <li><a href="{prefix}health-for-peace.html">Health for Peace</a></li>
          <li><a href="{prefix}our-events/peace-today.html">Peace Today</a></li>
        </ul>
      </div>
      <div>
        <h4>About</h4>
        <ul class="footer-list">
          <li><a href="{prefix}about/index.html">About Us</a></li>
          <li><a href="{prefix}about/our-history.html">Our History</a></li>
          <li><a href="{prefix}about/our-team.html">Our Team</a></li>
          <li><a href="{prefix}about/blog.html">Blog</a></li>
          <li><a href="{prefix}our-events/become-volunteers.html">Become a Volunteer</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <div class="footer-contact">
          <p style="color:rgba(250,246,238,0.8);max-width:none;margin-bottom:1rem">
            <a href="mailto:congopeaceacademy@gmail.com">congopeaceacademy@gmail.com</a><br />
            +243 992 767 008<br />
            Goma, DRC
          </p>
        </div>
        <div class="socials">
          <a href="https://web.facebook.com/congopeaceacademy" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.51 1.49-3.89 3.78-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.77l-.44 2.89h-2.33v6.99A10 10 0 0 0 22 12z"/></svg></a>
          <a href="https://www.instagram.com/congopeaceacademy/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
          <a href="https://youtu.be/6_g-ZvBbn6o" target="_blank" rel="noopener" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.58 7.19a2.5 2.5 0 0 0-1.76-1.77C18.25 5 12 5 12 5s-6.25 0-7.82.42A2.5 2.5 0 0 0 2.42 7.2 26.06 26.06 0 0 0 2 12a26.06 26.06 0 0 0 .42 4.81 2.5 2.5 0 0 0 1.76 1.77C5.75 19 12 19 12 19s6.25 0 7.82-.42a2.5 2.5 0 0 0 1.76-1.77A26.06 26.06 0 0 0 22 12a26.06 26.06 0 0 0-.42-4.81zM10 15.02V8.98L15.2 12 10 15.02z"/></svg></a>
          <a href="https://chat.whatsapp.com/JzBHcnJe77zBzk28pUauEM" target="_blank" rel="noopener" aria-label="WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4l-2-1c-.3-.1-.5-.1-.7.1l-.9 1.1c-.2.2-.4.3-.7.1a8 8 0 0 1-3.9-3.9c-.2-.3-.1-.5.1-.7l1.1-.9c.2-.2.2-.4.1-.7l-1-2c-.1-.3-.5-.5-.8-.4l-1.8.6c-.3.1-.5.4-.5.7.1 3 1.5 5.8 3.7 8 2.2 2.2 5 3.6 8 3.7.3 0 .6-.2.7-.5l.6-1.8c.1-.3-.1-.7-.4-.8z"/><path d="M12 2A10 10 0 0 0 3.5 17.3L2 22l4.8-1.5A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-3.1 1 1-3-.2-.3A8 8 0 1 1 12 20z"/></svg></a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2025 Congo Peace Academy. All rights reserved.</span>
      <span>Built with care for the people of Eastern DRC.</span>
    </div>
  </div>
</footer>

<script src="{prefix}assets/js/main.js"></script>
</body>
</html>
"""

def page_hero(crumbs, h1, lede):
    """crumbs is a list of (label, href) tuples; final one has href=None."""
    parts = []
    for i, (label, href) in enumerate(crumbs):
        if i > 0:
            parts.append('<span class="breadcrumb-sep">/</span>')
        if href:
            parts.append(f'<a href="{href}">{html.escape(label)}</a>')
        else:
            parts.append(f'<span>{html.escape(label)}</span>')
    crumbs_html = "".join(parts)
    return f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb reveal">
        {crumbs_html}
      </div>
      <h1 class="reveal">{h1}</h1>
      <p class="reveal">{lede}</p>
    </div>
  </section>
"""

def cta_donate(headline, body):
    return f"""
  <section class="bg-cream">
    <div class="container container-narrow">
      <div class="cta-band reveal">
        <h2>{headline}</h2>
        <p>{body}</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-primary btn-lg" href="https://donorbox.org/congo-peace-academy-1-3?default_interval=o" target="_blank" rel="noopener">Donate now</a>
        </div>
      </div>
    </div>
  </section>
"""

def write(path, content):
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")

# ---------------------------------------------------------------------------
# Image URLs (Google Sites — see download_images.sh for self-hosting)
# ---------------------------------------------------------------------------
IMG = {
    # team
    "bienfait":   "https://lh3.googleusercontent.com/sitesv/AA5AbUAGL9pmvcZolvJUCN26tXJVN7ZGuiEmzduQb-1z5hdlyc4wk72BYSmMmKd1K7nfHunSWjW5tK1tx4DxOdHe0AxsAdgyONHHneoJgbZ4l_d1CwCPAI2xQWnM33PEqSJDbEDfb67jjZBPD1UDkv0_kFrj3WW_X5oj97nFeSRzaH3lURgSTLHWt-AOT_AsdeQbifGhSmIaRrriTB4rImS7c6EQConL0JfeeJceZmM=w1280",
    # agri
    "agri_hero":  "https://lh3.googleusercontent.com/sitesv/AA5AbUA3Bu-52NDuLH-MS0BPEmJLCJS4JSmpPj_nxFazdeXBjHdRxK7RixkP3PKU0Q-q3zyclwoZM74Lw9yPAg4PGobgF7arhAdk6MPBW7-_uPxe250Q93JA0q-CGtgRLbUbJ9rZZ2rCab3EkyfNQG8OIbpEZnYIN7nxams9Bm1FxkeCe-ng2AzED1-EZDWMy3DBlnyxA2TjaM3gxleWv-SAgNBt_Di1L_EAd1ag=w1280",
    "agri_2":     "https://lh3.googleusercontent.com/sitesv/AA5AbUARpm9WXNfiNJyhLaShTG8jlocPtqxjTL8FuUisvbZQgr6yqOz-LKuiYZzJX14vDPzLYUCu4z8SH0Y3Ki4gYQEmylWMOYz6X4iqgDWlNgZis2Q8KrbhQx0PeLkwR7YCRd6IWjOIfLh9ptSYWqa8PaTqWbDgZ4Rx7zWouwSss7R-IiC_OEIDrYFhn3jZWwV_OqefiEEPYWavQZP230j4L7jPrxcghOL4QTqYFig=w1280",
    "agri_3":     "https://lh3.googleusercontent.com/sitesv/AA5AbUBeXTGTJkqY1fZbisyOnfwxgWYfWF79nBAgGv6Izelsx1TKDLYJZEAVfXLwCKBuCz2hgFYT90kllx6guLEM7zck0xM3FXeWAVzaa8blEYcnGOs1FRN5pTuMmwlSMElmhtDE_50QjCOQyMlaDK1rspLlijPR_giwso4L5bQqltO6OxlurS7yDIrr05bdjqlXLl4sctFWWtsL30raqfv8QER8YVpnl6FE9oPEcaw=w1280",
    "agri_4":     "https://lh3.googleusercontent.com/sitesv/AA5AbUD7L-i0qOw1QjjNqmg8kcUqqGkGG0A-EFTTlIj1JCXLgS2JuaFyFtVSlVqzhy5Mh68g4cEzGIWRkyw5FAogeGd5POcTGZqFg9ObWdFJSptrU9T9ib8fMH-AJdWhaGsjVFl_pFHEidzXqEmBzoaQX91mSbJ_EPk8Kb6Q5IlVyw7iYfJIKFs1_6B3-Dk9EnIet3Cc5J3nj2MmqidDZ8QSk3znGkMb3Xelc4r44qg=w1280",
    "agri_5":     "https://lh3.googleusercontent.com/sitesv/AA5AbUAqO6PtYbMwUQnOAXZGuxhsp8U5fa3yjjB9dEi7E9C-RWNl83cYowe16FTqIljmzcQZF6vvmcTsMU7MmUtesDxzNHXY8izx07gsqsPrOF6ISCGK1uZRdWKqtBGYjbiRYmz2d8HtoVJdnX31cePrvqHjhptjvf9Mh9Ri12okJhff41zLu8KY4ydT6YeYYlwjoPoNb9X0FAdQQIw6_0p3C_JMOLyMccq7-mCz=w1280",
    "agri_cf":    "https://lh3.googleusercontent.com/sitesv/AA5AbUBhp9O_fqNyZEYQOOaXV9awdS9lZ11ttbYgbXE7ty8lrEXmlw_oFvo9uNjdZRr6yKN0WJ8XGxB_gxrWGNf3UCAdYvEo4KCV0D1m8OCYBfg2XYtXy87WOLhR3HDbtTPIdRcieNKlRS1e5EQXpgXyPOoAodNGfdys0F1dbT59BESiTzdjALAW-dKM9MexKO-u0qUCukNIMGuOLRfO9v8GS8SGwdSBidRk8rmM744=w1280",
    "agri_tot":   "https://lh3.googleusercontent.com/sitesv/AA5AbUBZ7ki8fKoG4LRp1CLRhLNJrNSN7RuEOfJIk57qXRXjxKuvSXtWc0GONqTf21B7WFRJyTZLk0lBb1Xhin-TcK8XMCj0V9nmoGzU9Zi4I3Wro9kRHHDVxduavMMR4BNgQwUvucABdzl_oGBvCFxlIhmI9lzZb1TeQOC99gmPAmg3OMtz8XpbAcnG-HTpq1ppBNogF-xPLKoJpGn5Y9bAGBqJnXNIeKzAf01nW2M=w1280",
    # path to the future
    "path_what":  "https://lh3.googleusercontent.com/sitesv/AA5AbUB8hFyNkacretvz202BzT32QbhvpLi3TNjaP_H68U8juqLfOh5FlXgV92TACmoZTRLBQeqvLP50sjSzx_Wb7Rq3XiQouHmaeIt7BGDj9EMs1_z00Hiao-ULImnKWDJCwhbDOOCWo6QPOlC8Tq3svKiz5RkqMFHANHlFLCG4b-Y_6sS7raO5YJOKYZH5yvdOdUovX9jcoheXHPwVZjpdwSrKrMldwFaroY6eslQ=w1280",
    # health
    "health_hero":"https://lh3.googleusercontent.com/sitesv/AA5AbUB9AhXyslLE7W_OJasERjyd_QPMM9Y26xpo7PYXIB33q3MEwFpymkk65IYz51BSXAane5j0oLznGBiglq-cfT_Me-QbQLEtN82rf0d50qIHvNyacoe4cSI0hBZLzPMb7mxpq5T40nxBT9enTgIOMdZd6JppEGeo5BGN06uZ3SlhfwmhOrPBO6iagxdJfVuzFsGIJmccZw2mIrBVNQsWLlEsHeOcXFd96jkRxbs=w1280",
    # events
    "ev_hero":    "https://lh3.googleusercontent.com/sitesv/AA5AbUD3uJqTGG8Runk6YIAAKvLRdR1-yM3iBXBKnG3KbjNZMm8eIuwc8Iy5xsHaB0XXc8Svx17WSpqKcoqTGgFIg851b89QxoYgeIimvY7GojiMVLoYhu3bQMXzJkINADWgo9iVuChLjnZjwegOWXz9mQ_qJ-MNgww_n2-iTeiFdmrgPH5tklHWhWs_kmM0EJtpveCFMuwfPG0CnXuVpK5qV3QP7krqYz5C9zTBTEc=w1280",
    "ev_camp":    "https://lh3.googleusercontent.com/sitesv/AA5AbUDbyJAJEv67EBQ6k4-EpNCELsPGEwwAsDpIbERc0yS4j_nI21WUtu-_rWC9iAl3Gum_jhU95hEcvDNRCIQANR3dynRFdo1B77U59rdaHLIxadsU8jtuTS3VFiYdEGAca7Log34Kh2HKuWDpsWTUOiKbdKTLM1PgndlbEvq0EIOz17JEfgtVLkSVk6fQlvvG6EcfSmqI6PW4H5QfpxxzXBabbEXhJcmhjK4c=w1280",
    "ev_g1":      "https://lh3.googleusercontent.com/sitesv/AA5AbUDWZQq548d-BA27bapvnDQOHhI4e5WDxdIZa44ujUYogHRgEZQUgT63QpwByvJ5SMteg8GrqyO1JupBQGklwuejtJQerQ-W4804v8gZD8LHzrUamLiPWE3rO657nptpNDmyvwBFgBB7FYk5uy2lrat13_wEVZHuNzC9Y8KAe_bTEcKjbYtrqZwpg2yjvByP3sNN6i3jUmcnSZEmTaw2v3OUaIoxorUvRgRM8D8=w1280",
    "ev_g2":      "https://lh3.googleusercontent.com/sitesv/AA5AbUC9PWg1cewN8UBdqS9AY2mAqwZhR8fOqMz4YvXMTXkCuIAwXOjHdb0XhPoiCc508Gysth9gEhKCtS3kaySJ8BsillpKmIEho6CuPlyUcntDBkCkIb2xeJ53y0IUFk1S1pOmO8KmN8UkbVUTTF_HiJbaWAI3oQQnBUbK1ip7JhQ51W6JhAEBrIKWnY-9XnWg_B7U04CSFIf1WUPVLobqvbJBwdkCFzdShsP_Fns=w1280",
    "ev_g3":      "https://lh3.googleusercontent.com/sitesv/AA5AbUDDxWo07mnDJkhACM26sUehUfY4Df7zIbCMVjq51Sm7GEnQHnF_S6DyfBg5BpiIufTlLSeW5mpCTQHu6QVzGp_sixysg51nLyVhgVEKOYKisA6K5veCmdpTwP5Ty_u9wgVv4dq6Nbw3B2j0vNKd0MXBDlhvd-Sad5WzTmWHGT7_jgcYB_u8S6TKpf5UYFLUAt9Bc4nvbsKxFjTWqEUZ9Scvpey-FjVX7H0z=w1280",
    "ev_g4":      "https://lh3.googleusercontent.com/sitesv/AA5AbUA8semFQ0zKScjWacYul_FvUWfokG24TF2602TKZuo53Et-wybVvvT4Ei815FO6QQipgnV_i2zOpFuUYkZN-0MnFjsa_WtjT_eGGqWCqWMb6nLaoLPAUFFe5FkK4WY7novPXBxKsSah_HN4FhYL_QoppYy6mTU0bYsdQW3rG5f77HmGsG3XNdJnM1wiOUa80L-jWgZq7OJ24KBfGvbCQNLbIoDuFn4K55k6xn8=w1280",
    "ev_g5":      "https://lh3.googleusercontent.com/sitesv/AA5AbUAZT56VHWq_8-DcPg9ZMl5VZ47jIDaaV2-3VjTrDdZKgkCpq8HB3wO5b4rcgSO0M8O2oN8t0GEl-xTfrCCJrWto76sYchh_Ee6uy54F59uyZOfmdkNYkFyES2mYUQ--Yl159PsoXx0YaM6f5GUUiiV7FACNtd9IfJ45Q4aMBy3Vka-mkAB-eZZgobZMmKvKg6BsfNYS2wu-9DIR1TphErdT3cl3hbpT3VXjB9E=w1280",
    "pt_body_bag":"https://lh3.googleusercontent.com/sitesv/AA5AbUBcSx50C6migEIywihlgYr9-vzLeouAOVSV6cWkpgLP0--AlkA0F3aku8egkHfkH7hlhixlLsytWa9ilOqEQwunsTgu-zUoT1tJyiFglq37CepPfAIU2VMkZcw-0Gv4eUy2pWbrjtckZHgbyWo57qw2uOG3TzcV0hhxjv2ninZpRkWaDC46p3pDLP4LBhAc7xXjvxdH9xrbzFBmDHM0fFous-LzHARk6D_8fpo=w1280",
    "fellows":    "https://lh3.googleusercontent.com/sitesv/AA5AbUCxN0e1KhCwNS7udsm8f_fHDFk2A-GrV4Iqnmc2WbUKn5Tc0i1VSqunNIziB--070h55jRIV5v4JYXAWjZ_qrlUYU4h7N15Do76bYkX9r6xS5VytGx31sIUvHKL2KVxCyMxJDwadBBk-oCKDGnoFwQk5nC_cqrtR-lDXGZ8Ktf4EaNHfbfYGL4XMD4UOECqR_HG2hlrl7CasVHq-vZf8zJeN5e5gRLDbaZvH48=w1280",
}

# ===========================================================================
# 1) health-for-peace.html
# ===========================================================================
def build_health():
    p = ""  # root
    body = f"""
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb reveal">
        <a href="index.html">Home</a><span class="breadcrumb-sep">/</span><span>Health for Peace</span>
      </div>
      <h1 class="reveal">Health for Peace.</h1>
      <p class="reveal">Empowering communities through healthcare — because access to care is a cornerstone of peace and stability.</p>
    </div>
  </section>

  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['health_hero']}" alt="Health for Peace program — community healthcare in Eastern DRC" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">A program of Congo Peace Academy</span>
          <h2 class="reveal">Empowering Communities Through Health</h2>
          <p class="reveal">At Congo Peace Academy, we believe that access to healthcare is a cornerstone of peace and stability. Under the visionary leadership of Prince, the Health for Peace Program has been at the forefront of delivering life-saving health interventions to some of the most vulnerable communities in the Democratic Republic of Congo.</p>
          <p class="reveal">From leading COVID-19 awareness and prevention campaigns on Idjwi Island to providing free medication and healthcare guidance in internally displaced persons (IDP) camps around Goma, the program has reached thousands of individuals with vital support. Today, as the world grapples with the alarming spread of MPox, Prince and his team are spearheading education and prevention initiatives to protect these at-risk populations, particularly young women and children who often bear the brunt of health crises.</p>
          <p class="reveal">What makes this program truly unique is its community-centered approach and focus on sustainable impact. By combining on-the-ground efforts with a vision for integrating modern technology and artificial intelligence into healthcare, the Health for Peace Program is setting new standards for delivering care in resource-limited settings.</p>
          <p class="reveal">This is more than a healthcare initiative — it's a movement to build healthier, stronger, and more resilient communities, one campaign at a time.</p>
          <p class="reveal">Together, we can make a difference. Support our mission to bring hope and healing to the most vulnerable. Follow our journey, share our story, and join us in creating a future where healthcare is a right, not a privilege.</p>
        </div>
      </div>
    </div>
  </section>

{cta_donate("Support healthier, more resilient communities.", "Your gift helps deliver vital medical supplies, prevention campaigns, and on-the-ground care to the families who need it most.")}
"""
    write("health-for-peace.html",
          head("Health for Peace", "Empowering communities through healthcare in Eastern DRC — COVID-19 prevention, free medication in IDP camps, and MPox awareness.", p) +
          header(p, "health") + body + footer(p))

# ===========================================================================
# 2) about/blog.html
# ===========================================================================
def build_blog():
    p = "../"
    body = page_hero(
        [("Home", "../index.html"), ("About", "index.html"), ("Blog", None)],
        "Peace Today.",
        "Stories from the field — how Congo Peace Academy is cultivating peace, leadership, and unity in Eastern Congo."
    ) + f"""
  <section class="bg-paper">
    <div class="container container-narrow">
      <article class="prose">
        <p class="eyebrow reveal">From the field</p>
        <h2 class="reveal">Congo Peace Academy: Cultivating Peace, Leadership, and Unity in Eastern Congo</h2>
        <p class="reveal">On the tranquil shores of Idjwi Island and amidst the challenges of Goma, the Congo Peace Academy (CPA) has been steadfast in its mission to transform lives through peacebuilding and leadership education. Since our inception in 2018, with support from the Davis Projects for Peace through the University of Rochester, CPA has dedicated itself to empowering youth, fostering social cohesion, and championing gender equality.</p>
        <p class="reveal">What makes CPA extraordinary is its commitment to a deeply inclusive, community-based approach to peacebuilding. By rooting our programs in the historical and cultural context of Congolese society, we tackle the root causes of ethnic and familial violence. From schools to communities, we focus on preventing conflicts and nurturing an environment where peace can thrive.</p>

        <div class="video-frame reveal">
          <iframe src="https://www.youtube.com/embed/6_g-ZvBbn6o" title="Congo Peace Academy — Peace Today" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        </div>

        <p class="reveal">Our initiatives are more than just programs; they are lifelines for hope and resilience. CPA's work is a testament to the power of collaboration, inclusivity, and local engagement in addressing some of the most pressing challenges in eastern Congo.</p>
        <p class="reveal">Through tailored workshops, dialogue forums, and skill-building opportunities, we empower young leaders to become agents of positive change. These individuals are not only reducing tensions but also fostering a generation committed to justice, equality, and unity.</p>
        <blockquote class="reveal">As we look to the future, CPA continues to be a symbol of what is possible when communities come together with a shared vision for peace. Join us on this transformative journey and become part of the movement to create a peaceful and prosperous DR Congo.</blockquote>
      </article>
    </div>
  </section>

{cta_donate("Be part of the movement.", "Your support helps us continue cultivating peace, leadership, and unity in Eastern Congo — one community at a time.")}
"""
    write("about/blog.html",
          head("Blog — Peace Today", "Stories from the field: how Congo Peace Academy is cultivating peace, leadership and unity in Eastern Congo.", p) +
          header(p, "about") + body + footer(p))

# ===========================================================================
# 3) about/our-team.html
# ===========================================================================
def build_team():
    p = "../"
    body = page_hero(
        [("Home", "../index.html"), ("About", "index.html"), ("Our Team", None)],
        "Peacemakers.",
        "Meet the people building Congo Peace Academy — a team of leaders, educators, pastors, lawyers, and organizers united by a vision of peace through education, entrepreneurship, and conservation agriculture."
    ) + f"""
  <!-- Founder feature -->
  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['bienfait']}" alt="Bienfait Mugenza, Founder and Director of Congo Peace Academy" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">Founder &amp; Director</span>
          <h2 class="reveal">Bienfait MUGENZA</h2>
          <p class="reveal">Bienfait Mugenza is a visionary leader, social entrepreneur, and peacebuilder dedicated to fostering peace, social justice, and sustainable development in the Democratic Republic of Congo (DRC). As the Founder and Director of Congo Peace Academy, he has been empowering young people and conflict-affected communities with skills in conflict resolution, leadership, and entrepreneurship.</p>
          <p class="reveal">Having grown up during the Second Congo War, Bienfait witnessed firsthand the devastating impact of violence and displacement. Determined to create sustainable solutions, he pursued a degree in Political Science at the University of Rochester as a MasterCard Foundation Scholar before returning to the DRC to expand his peacebuilding initiatives. In 2018, he launched "Peace through Entrepreneurship," a project that has enabled young people in Goma to create businesses, reducing economic vulnerability and preventing recruitment by armed groups.</p>
          <p class="reveal">One of his most impactful initiatives is Agri Peace, which integrates conservation agriculture with peacebuilding, helping internally displaced people (IDPs) and their host communities rebuild their livelihoods. His leadership has earned him international recognition, including the $50,000 2024 Projects for Peace Alumni Award and the $10,000 Davis Peace Award. Today, Bienfait continues to leverage agriculture, entrepreneurship, and education as powerful tools for peacebuilding and a more just, stable, and self-sufficient future for the people of eastern DRC.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Team grid -->
  <section class="bg-cream">
    <div class="container">
      <div class="section-header center">
        <span class="eyebrow reveal">Meet the team</span>
        <h2 class="reveal">The people behind Congo Peace Academy.</h2>
      </div>
      <div class="team-grid">

        <article class="team-card reveal">
          <h3>Prof. Jean Claude Mubalama Zibona</h3>
          <p class="role">Legal Adviser &amp; Board Member</p>
          <p>Professor Jean Claude MUBALAMA Zibona is a distinguished Congolese lawyer practicing at the Bar of Bukavu, advisor to the International Criminal Court, and member of the Bar Committee of this Court from 2012 to 2016. He is a professor at the Catholic University of Bukavu and the University of Cinquantenaire in Lwiro. He is currently the Director of the Cabinet of the Governor of South Kivu, in Bukavu. He is passionate about peace, justice, and human rights, which he has defended throughout his career.</p>
        </article>

        <article class="team-card reveal">
          <h3>Pastor Isaac Mukoka Muena Kavula</h3>
          <p class="role">Head of Leadership and Discipleship</p>
          <p>Pastor Isaac is a multilingual educator and an ordained pastor. He comes to Congo Peace Academy with a leadership degree from Light of the Nation, International Bible College in Polokwane, South Africa, and a Bachelor of Arts degree in Social Sciences from Université Libre de Kigali (ULK), Rwanda. With more than five years of experience in organizational management and impact evaluation of humanitarian relief projects, Pastor Isaac is a recognized trainer for the national financial education program. He is fluent in French, English, Swahili, Tshiluba, Lingala, Kinyarwanda and Kirundi.</p>
        </article>

        <article class="team-card reveal">
          <h3>Shagali Mugenza</h3>
          <p class="role">Outreach Specialist and IT Manager</p>
          <p>Shagali joined the Congo Peace Academy in 2021. He is a motivated and talented outreach manager who leads our communications and IT department. He is responsible for producing excellent informative content that engages our audience and builds brand recognition. He creates press releases, reports, and media materials for the Congo Peace Academy and Congo Dynamic Initiatives. He is an excellent communicator with brilliant presentation and organizational skills.</p>
        </article>

        <article class="team-card reveal">
          <h3>John Kwizera</h3>
          <p class="role">Associate IT</p>
          <p>John works with the outreach manager in the communications and IT department. He is responsible for producing excellent graphic content that engages our audience and builds brand recognition. Together with his department manager, they create press releases, reports, and media materials for the Congo Peace Academy and Congo Dynamic Initiatives. He is an excellent communicator with sharp presentation and organizational skills.</p>
        </article>

        <article class="team-card reveal">
          <h3>Anita Nelly</h3>
          <p class="role">Accountant</p>
          <p>Under the direct supervision of the finance manager, Nelly is responsible for the short, medium, and long-term financial efficiency of all activities of Congo Peace Academy, including accounting, budgetary control, treasury, fundraising, banking, risk management, and auditing.</p>
        </article>

        <article class="team-card reveal">
          <h3>Ntabankabo Aime Bahozi</h3>
          <p class="role">Program Coordinator</p>
          <p>As Associate Director of Curriculum and Learning Design, Ntabankabo Aime shapes curriculum strategy and oversees the development and delivery of learning experiences for the Congo Peace Academy. Aime has worked as a trainer for EDC in the IDIJ project financed by USAID. He is a dedicated educator who has promoted innovation, development, and management of education programs in numerous schools in Goma for over five years.</p>
        </article>

        <article class="team-card reveal">
          <h3>Eric Okolisa Lokamba</h3>
          <p class="role">Administration and Finance Manager</p>
          <p>Eric holds a degree in project management from the Institut Supérieur de Développement Rural in Goma. He has over three years of experience in administration and finance. His role within the Congo Peace Academy is to establish reliable and accurate accounting and financial procedures to enable effective planning and use of resources for adequate implementation of activities.</p>
        </article>

        <article class="team-card reveal">
          <h3>Patric Kacheranga</h3>
          <p class="role">Head of Education</p>
          <p>Under the supervision of the Director, Patrick coordinates and oversees the peace education activities at the center. He also teaches English.</p>
        </article>

      </div>
    </div>
  </section>

  <!-- Become Peacemakers / Values -->
  <section class="bg-paper">
    <div class="container">
      <div class="section-header center">
        <span class="eyebrow reveal">Become peacemakers</span>
        <h2 class="reveal">The values that guide us.</h2>
        <p class="lede reveal">Four commitments shape how we work — with each other, with partners, and with the communities we serve.</p>
      </div>
      <div class="values">
        <article class="value-card reveal">
          <div class="value-num">01</div>
          <h3 class="value-title">Accountability</h3>
          <p>Congo Peace Academy prioritizes accountability as a core value, ensuring that all members of the organization are responsible and transparent in their actions and decisions. This helps to build trust and credibility with stakeholders and promote a culture of integrity.</p>
        </article>
        <article class="value-card reveal">
          <div class="value-num">02</div>
          <h3 class="value-title">Collaboration</h3>
          <p>Another core value for Congo Peace Academy is collaboration, emphasizing the importance of working together effectively to achieve common goals. This involves fostering partnerships with other organizations, encouraging teamwork among staff members, and promoting open communication and cooperation.</p>
        </article>
        <article class="value-card reveal">
          <div class="value-num">03</div>
          <h3 class="value-title">Empowerment</h3>
          <p>Congo Peace Academy also prioritizes empowerment as a core value, seeking to empower individuals and communities to take charge of their own development and peace-building efforts. This involves providing training, resources, and support to help people build their skills and capacities, as well as promoting participatory decision-making processes.</p>
        </article>
        <article class="value-card reveal">
          <div class="value-num">04</div>
          <h3 class="value-title">Respect</h3>
          <p>Finally, Congo Peace Academy adopts respect as a core value, emphasizing the importance of treating all individuals with dignity and compassion. This involves promoting diversity and inclusion within the organization, as well as fostering a culture of mutual respect and understanding.</p>
        </article>
      </div>
    </div>
  </section>

{cta_donate("Join the movement.", "Stand alongside our team and the communities we serve. Your support helps train the next generation of peacemakers, farmers, and entrepreneurs across Eastern DRC.")}
"""
    write("about/our-team.html",
          head("Our Team — Peacemakers", "Meet the team of Congo Peace Academy — leaders, educators, lawyers, and organizers building peace across Eastern DRC.", p) +
          header(p, "about") + body + footer(p))

# ===========================================================================
# 4) agri-peace.html
# ===========================================================================
def build_agri():
    p = ""
    body = page_hero(
        [("Home", "index.html"), ("Agri Peace", None)],
        "Agri Peace.",
        "An integrated, community-led model that combines practical conservation agriculture with intentional peacebuilding and economic design."
    ) + f"""
  <!-- Why it matters -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Why our model matters</span>
        <h2 class="reveal">A whole new way of working — not a small tweak.</h2>
        <p class="reveal">Across eastern DRC, many responses to food insecurity and livelihoods are well-intentioned but fragmented: short emergency distributions that ease hunger for a season, single-sector projects that ignore social tensions, and farming practices that rely on repeated tilling, monoculture, or costly external inputs. Those approaches can provide temporary relief but rarely restore the land, change behaviours, or repair the social bonds that make communities resilient. In places where resources are scarce, this cycle of dependency and competition often feeds the very conflicts projects aim to reduce.</p>
        <h2 class="reveal">Our approach — what we do differently</h2>
        <p class="reveal">Agri Peace is an integrated, community-led model that combines practical conservation agriculture (Foundation for Farming, FFF) with intentional peacebuilding and economic design. The difference is not one small tweak — it is a whole way of working:</p>
      </article>
    </div>
  </section>

  <!-- Five differentiators as alternating splits -->
  <section class="bg-cream">
    <div class="container">
      <div class="split reveal">
        <div class="split-media"><img src="{IMG['agri_hero']}" alt="Farmers training in Foundation for Farming techniques" loading="lazy" /></div>
        <div class="split-content">
          <span class="eyebrow">01</span>
          <h2>Mindset + Method, not just inputs.</h2>
          <p>Instead of delivering seeds or fertiliser alone, we teach FFF practices (minimum tillage, mulching, correct seed spacing, crop diversity, and high management standards) while also working with farmers' values and motivations — restoring stewardship of the land and confidence in their skills.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-paper">
    <div class="container">
      <div class="split reverse reveal">
        <div class="split-media"><img src="{IMG['agri_2']}" alt="Cohort-based farmer training, learning together" loading="lazy" /></div>
        <div class="split-content">
          <span class="eyebrow">02</span>
          <h2>Learning together → becoming families.</h2>
          <p>Trainings are cohort-based and paired with dialogue exercises, cooperative tasks, and shared responsibilities. Participants who start as individuals learn together, solve problems together, and form teams that act like extended families — sharing labour, protecting each other's plots, and resolving disputes internally.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-cream">
    <div class="container">
      <div class="split reveal">
        <div class="split-media"><img src="{IMG['agri_3']}" alt="Programs co-designed with local chiefs and women's groups" loading="lazy" /></div>
        <div class="split-content">
          <span class="eyebrow">03</span>
          <h2>Locally owned and culturally grounded.</h2>
          <p>Programs are co-designed with chiefs, women's groups, youth networks and partner NGOs (e.g., FfFI, local chefferies). This ensures relevance, local legitimacy, and sustainable hand-over.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-paper">
    <div class="container">
      <div class="split reverse reveal">
        <div class="split-media"><img src="{IMG['agri_4']}" alt="Farmer entrepreneurs accessing markets and savings groups" loading="lazy" /></div>
        <div class="split-content">
          <span class="eyebrow">04</span>
          <h2>Economic pathways, not dependency.</h2>
          <p>We connect higher yields to market access, savings groups, small grants/seed capital and value-addition (processing, collective marketing) so families convert production into income and dignified enterprise — alternatives to risky coping strategies or recruitment into armed groups.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-cream">
    <div class="container">
      <div class="split reveal">
        <div class="split-media"><img src="{IMG['agri_5']}" alt="Joint demonstration plots and mixed-team peacebuilding" loading="lazy" /></div>
        <div class="split-content">
          <span class="eyebrow">05</span>
          <h2>Integrated peacebuilding, not an add-on.</h2>
          <p>Every agricultural intervention is intentionally linked to reconciliation: community dialogues, joint demonstration plots with mixed-ethnic teams, and local mediator training mean that improved livelihoods and restored relationships advance side by side.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Conservation farming -->
  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['agri_cf']}" alt="Conservation farming — restoring degraded land" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">In practice</span>
          <h2 class="reveal">Conservation Farming for Peace and Resilience.</h2>
          <p class="reveal">Our conservation farming approach empowers local farmers to restore degraded land, increase yields, and break cycles of poverty and dependence. By combining simple, climate-smart practices like mulching, minimal tillage, composting, and agroforestry, we heal the soil, conserve water, and steward creation. More than growing food, we're cultivating dignity, self-reliance, and peace — one farm at a time.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Training of trainers -->
  <section class="bg-cream">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['agri_tot']}" alt="Training of trainers on Idjwi Island" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">Training of trainers</span>
          <h2 class="reveal">A new generation of "Farmers of Peace" rises.</h2>
          <p class="reveal">Congo Peace Academy's Agri Peace program continues to offer transformative Foundation for Farming (FFF) Training of Trainers to hundreds of farmers on the beautiful island of Idjwi. This is no ordinary training — it's a powerful convergence of hope, healing, and hands-on agricultural education.</p>
          <p class="reveal">For communities long marked by violence, displacement, and division, this training is a radical act of restoration. It reaffirms our belief that regenerative farming can regenerate communities, not only economically, but spiritually and socially. These trainees are now champions of change, ready to pass on their knowledge and cultivate peace where it's most needed. We are incredibly proud of these brave individuals — especially the young women — who are stepping up to lead in spaces where peace is fragile but deeply needed.</p>
          <p class="reveal">Your support can help us scale this model. As we prepare to expand Agri Peace to more regions affected by displacement and conflict, we invite you to partner with us in training the next cohort of Farmers of Peace — those who will nourish both the soil and society.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Reports -->
  <section class="bg-paper">
    <div class="container">
      <div class="section-header center">
        <span class="eyebrow reveal">From the field</span>
        <h2 class="reveal">Our recent reports.</h2>
        <p class="lede reveal">Documentation of our Agri Peace work on Idjwi and across Eastern DRC.</p>
      </div>
      <div class="reports-list">
        <div class="report-item reveal">
          <span class="report-icon" aria-hidden="true">PDF</span>
          <div>
            <p class="report-title">Agri Peace Idjwi Expansion Report — April 2025</p>
            <p class="report-meta">Field report on program expansion</p>
          </div>
        </div>
        <div class="report-item reveal">
          <span class="report-icon" aria-hidden="true">PDF</span>
          <div>
            <p class="report-title">CPA · FFF Expansion Report — Idjwi, June 2025</p>
            <p class="report-meta">Foundation for Farming expansion update</p>
          </div>
        </div>
        <div class="report-item reveal">
          <span class="report-icon" aria-hidden="true">PDF</span>
          <div>
            <p class="report-title">Congo Peace Academy — Work Overview</p>
            <p class="report-meta">Programmatic summary</p>
          </div>
        </div>
        <div class="report-item reveal">
          <span class="report-icon" aria-hidden="true">PDF</span>
          <div>
            <p class="report-title">Congo Peace Academy — Annual Report 2024–2025</p>
            <p class="report-meta">Full-year results and stories</p>
          </div>
        </div>
      </div>
    </div>
  </section>

{cta_donate("Cultivate peace through agriculture.", "Join us in our mission to cultivate peace through agriculture. Your support trains the next cohort of Farmers of Peace — those who will nourish both the soil and society.")}
"""
    write("agri-peace.html",
          head("Agri Peace", "Congo Peace Academy's flagship model — conservation agriculture (Foundation for Farming) combined with peacebuilding and economic design.", p) +
          header(p, "agri") + body + footer(p))

# ===========================================================================
# 5) path-to-the-future.html
# ===========================================================================
def build_path():
    p = ""
    body = page_hero(
        [("Home", "index.html"), ("Path to the Future", None)],
        "Path to the Future — College Prep 2025.",
        "A cross-border college preparation program for exceptionally gifted students from Eastern DRC and Western Rwanda, in partnership with Acting Globally."
    ) + f"""
  <!-- Program overview -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Program overview</span>
        <h2 class="reveal">More ambitious and inclusive than ever.</h2>
        <p class="reveal">Path to the Future 2025 is Congo Peace Academy's flagship college preparation program — now more ambitious and inclusive than ever. In partnership with Acting Globally, a U.S.-based nonprofit, this cross-border initiative brings together exceptionally gifted students from Eastern DRC and Western Rwanda, particularly those living in fragile, conflict-affected border communities, to learn and grow together.</p>
        <p class="reveal">We believe education can do more than prepare students for university — it can ignite social change, foster peace, and transform entire communities.</p>
        <p class="reveal">Our program is designed to address the systemic barriers that limit access to global opportunities — from language gaps to lack of information, mentorship, and financial support — and provide students with the tools to compete for and secure fully funded international university scholarships.</p>
      </article>
    </div>
  </section>

  <!-- What we offer -->
  <section class="bg-cream">
    <div class="container">
      <div class="section-header center">
        <span class="eyebrow reveal">What we offer</span>
        <h2 class="reveal">A holistic, intensive program that goes far beyond academics.</h2>
      </div>
      <div class="values">
        <div class="value-card reveal">
          <div class="value-num">01</div>
          <h3 class="value-title">English Language Immersion</h3>
          <p>Intensive training to break down the biggest barrier to global higher education access.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-num">02</div>
          <h3 class="value-title">Leadership &amp; Peacebuilding</h3>
          <p>Students learn nonviolent communication, dialogue facilitation, and community leadership.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-num">03</div>
          <h3 class="value-title">Entrepreneurship &amp; Innovation</h3>
          <p>Cultivating problem-solvers who will launch ventures or lead change in their home regions.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-num">04</div>
          <h3 class="value-title">University &amp; Scholarship Prep</h3>
          <p>Tailored guidance on SAT, TOEFL, essay writing, and application processes.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-num">05</div>
          <h3 class="value-title">Cross-Border Cultural Exchange</h3>
          <p>Rwandan and Congolese students learn and live together, fostering mutual understanding, healing, and peacebuilding.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Partnership -->
  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['path_what']}" alt="Path to the Future — students in cross-border program" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">Partnership</span>
          <h2 class="reveal">Congo Peace Academy + Acting Globally.</h2>
          <p class="reveal">This initiative is made possible through our strategic partnership with Acting Globally, a U.S.-based organization committed to empowering grassroots peacebuilders and educational leaders. Together, we bring global resources, mentorship, and opportunity to youth who have been systematically left out of the global conversation.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Who can apply -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Who can apply</span>
        <h2 class="reveal">We're looking for:</h2>
        <ul class="reveal">
          <li>Exceptionally motivated high school graduates or final-year students (ages 17–21)</li>
          <li>From Eastern DRC or Western Rwanda, especially border communities (e.g. Goma, Idjwi, Minova, Sake, Gisenyi, Rubavu)</li>
          <li>Demonstrated leadership potential and a commitment to community impact</li>
          <li>Interest in applying for international university scholarships (U.S., Canada, Europe, etc.)</li>
          <li>Willingness to engage in cross-cultural learning and peacebuilding</li>
        </ul>
      </article>
    </div>
  </section>

  <!-- Apply -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <div class="cta-band reveal">
        <span class="eyebrow">Join the 2025 cohort</span>
        <h2>Applications open June 2025.</h2>
        <div class="info-grid">
          <div><strong>Location</strong><br />Gisenyi &amp; Goma</div>
          <div><strong>Deadline</strong><br />June 30, 2025</div>
          <div><strong>Ages</strong><br />17–21</div>
        </div>
        <p>Whether you're a student with a dream, a parent, or a teacher wanting to refer someone — this is your moment to act.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-primary btn-lg" href="https://forms.gle/m59n7CviaZchGbhZ8" target="_blank" rel="noopener">Apply today</a>
        </div>
      </div>
    </div>
  </section>

{cta_donate("Help us expand Path to the Future.", "Every scholarship won, every life transformed, and every cross-border friendship forged begins with your support. We're currently seeking partners, mentors, and donors to help us expand Path to the Future in 2025 and beyond.")}
"""
    write("path-to-the-future.html",
          head("Path to the Future — College Prep 2025", "A cross-border college prep program for gifted students from Eastern DRC and Western Rwanda — English immersion, leadership, entrepreneurship, scholarship prep.", p) +
          header(p, "path") + body + footer(p))

# ===========================================================================
# 6) our-events/index.html
# ===========================================================================
def build_events_index():
    p = "../"
    body = page_hero(
        [("Home", "../index.html"), ("Our Events", None)],
        "Humanitarian Crisis in Goma, DRC.",
        "The humanitarian crisis caused by the ongoing war in Eastern DRC has spiraled out of control. Hundreds of thousands of people have been displaced and need emergency support."
    ) + f"""
  <!-- Crisis hero -->
  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['ev_hero']}" alt="Humanitarian crisis in Goma, DRC" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">The crisis</span>
          <h2 class="reveal">Escalating war worsens crisis.</h2>
          <p class="reveal">The humanitarian crisis caused by the ongoing war between the Congolese armed forces and the M23 rebel group in the DRC has spiraled out of control. At least 400,000 people are currently in a horrible situation as displaced in the Kanyaruchinya camp near Goma, while several thousand more from Bunagana and Rutshuru have fled to Uganda.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- What displaced people need -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">What's needed</span>
        <h2 class="reveal">What do displaced people need after leaving everything behind, fleeing violence and war?</h2>
        <p class="reveal">Imagine running away from home with little more than the clothes on your back and the few things you can carry. You are running for your life — forced to exit the comfort of your home, you leave your job, your school, your car, your possessions, and your memories — behind. This situation typifies the reality for thousands of internally displaced eastern Congolese who have fled even to neighboring countries to protect themselves from the war and violence ravaging their country for decades. In the moments immediately following the decision to leave and run empty-handed into the unknown, how do they do it?</p>
        <p class="reveal">Below, discover some of the essential items that Congo Peace Academy will provide to displaced Congolese living in the camps around Goma. The goal is to focus on supplies that help the most vulnerable refugee families survive and cope after enormous losses.</p>
      </article>
    </div>
  </section>

  <!-- Needs grid -->
  <section class="bg-paper">
    <div class="container">
      <div class="needs-grid">
        <article class="need-card reveal">
          <h3>Tents</h3>
          <p>When families desperately flee ruthless fighting, they leave everything behind and need immediate help to find a place to live that protects them from the elements, rain, cold and hot sun. We need to provide emergency shelter for displaced people by setting up tents while at the same time looking for durable solutions that provide security and hope for the future. Living in a camp is not a sustainable or long-term solution, and this is something that residents of the Kanyaruchinya camp near Goma know from painful experiences. In this rainy season, refugees need shelter to protect them from malaria, cold, and death.</p>
        </article>
        <article class="need-card reveal">
          <h3>Food</h3>
          <p>We need to help displaced people meet their emergency food needs. Many are fleeing with little or no possessions and money. Without assistance, refugees struggle to access necessities, including nutritious food, to keep their families healthy and alive. Without food, the ability of displaced people to become productive and begin to rebuild their lives diminishes. We are organizing a campaign to distribute food items such as pasta, cooking oil, and milk powder to help them feed their families and focus on the future as they go through this challenging time.</p>
        </article>
        <article class="need-card reveal">
          <h3>Cooking utensils and dishes</h3>
          <p>After fleeing their homes and leaving everything behind, even the most basic household tasks can seem impossible. Refugees and internally displaced people must wash, dress, house, and feed their families with the only supplies they managed to carry. This living condition is an incredible burden at a time when fear and uncertainty are already overwhelming. The cooking utensils and dishes help refugees rebuild their homes in the most basic ways and allow them to prepare safe and nutritious meals for their children. These tools also enable Congolese families to keep an essential part of their culture alive — cooking and gathering around food.</p>
        </article>
        <article class="need-card reveal">
          <h3>Hygiene items</h3>
          <p>Hygiene items are essential to the health and survival of families, as the facilities where they seek refuge are often rudimentary at best. Refugees often live in unsanitary overcrowded makeshift shelters without adequate water or sanitation facilities: tent camps, chicken coops, abandoned schools, buildings — anywhere they can find relative safety. These dire conditions have disastrous consequences for their health and morale. Without essential hygiene items to help them stay clean, displaced people are at greater risk of disease, malnutrition, and loss of confidence to face an uncertain future. Hygiene items such as soap, toothpaste, and razors can help refugees stay healthy and maintain their dignity.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- See what we see -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <div class="section-header center">
        <span class="eyebrow reveal">From the camps</span>
        <h2 class="reveal">See what we see.</h2>
      </div>
      <div class="video-frame reveal">
        <iframe src="https://www.youtube.com/embed/6_g-ZvBbn6o" title="Inside an IDP camp near Goma" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </div>
  </section>

  <!-- Photo grid -->
  <section class="bg-paper">
    <div class="container">
      <div class="section-header center">
        <span class="eyebrow reveal">A look at life in the IDP camp — Goma</span>
        <h2 class="reveal">Photos from the field.</h2>
      </div>
      <div class="photo-grid">
        <img class="reveal" src="{IMG['ev_camp']}" alt="Displaced families at the Kanyaruchinya camp" loading="lazy" />
        <img class="reveal" src="{IMG['ev_g1']}" alt="Life in the camp" loading="lazy" />
        <img class="reveal" src="{IMG['ev_g2']}" alt="Distribution of supplies" loading="lazy" />
        <img class="reveal" src="{IMG['ev_g3']}" alt="Children at the camp" loading="lazy" />
        <img class="reveal" src="{IMG['ev_g4']}" alt="Shelter conditions" loading="lazy" />
        <img class="reveal" src="{IMG['ev_g5']}" alt="Daily life in displacement" loading="lazy" />
      </div>
    </div>
  </section>

{cta_donate("Our work is made possible through the support of generous donors like you.", "Please donate today. Every contribution helps us deliver tents, food, cooking utensils, and hygiene supplies to families who have lost everything.")}
"""
    write("our-events/index.html",
          head("Our Events — Humanitarian Crisis in Goma", "Coverage of the humanitarian crisis in Eastern DRC — what displaced people need, photos from the IDP camps, and how to help.", p) +
          header(p, "events") + body + footer(p))

# ===========================================================================
# 7) our-events/peace-today.html
# ===========================================================================
def build_peace_today():
    p = "../"
    body = page_hero(
        [("Home", "../index.html"), ("Our Events", "index.html"), ("Peace Today", None)],
        "Peace Today.",
        "Through the Peace Today platform, we inform our audience about security and peace in the DRC. We examine issues related to the police, defense, justice, respect for human rights, and national cohesion to forecast peace and stability."
    ) + f"""
  <!-- Body bag story -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Field report</span>
        <h2 class="reveal">A body bag instead of a pillow.</h2>
      </article>
      <div class="prose-image reveal">
        <img src="{IMG['pt_body_bag']}" alt="Inside the Kanyaruchinya IDP camp" loading="lazy" />
      </div>
      <article class="prose">
        <p class="reveal">On Sunday, November 27, 2022, the Congolese Peace Academy leadership team visited the Kanyaruchinya IDP camp, where 3,999 families from Tongo, Rugari, Rutshuru, Tchegera, Nyiragongo, and some from Masisi have come to seek refuge as the war intensifies. The camp president noted that it is currently very difficult to know exactly how many people have arrived by the end of the weekend because there are many sudden arrivals in the camp.</p>
        <p class="reveal">Unfortunately, the IDPs' hopes for peace and security in Kanyaruchinya are facing enormous difficulties, including the lack of adequate shelter, food, water, toilets, and medicine. Thus, people who flee the comfort of their homes to seek safety around the city of Goma face extreme desolation, as "living in this fragile, unhealthy and overcrowded camp is nothing short of hell," they say.</p>
        <p class="reveal">The highlight of the visit was the story of Sekajumba Kajibwami. Mr. Kajibwami is a seventy-year-old man from Rugari, extremely ill, afflicted by disease and hunger, who is currently in the camp without family or support. On Sunday afternoon, Mr. Kajibwami was expelled from a nearby hospital/clinic on a stretcher with a body bag instead of a pillow, suggesting that they were disposing of the human body of a sick and starving man who is not yet dead.</p>
        <p class="reveal">Everyone who witnessed this event was shocked. Looking into the man's eyes, everyone could tell that Mr. Kajibwami was sick, tired, and hungry but not yet dead. He could still talk and eat, or at least barely. He was offered a doughnut, and he ate and swallowed. Kajibwami's story is an illustration of the current conditions in the Kanyaruchinya "concentration camp".</p>
        <p class="reveal">We believe that Mr. Kajibwami's life could still be saved if people of goodwill acted immediately to help him gain access not only to urgent health care but also to food.</p>
        <blockquote class="reveal">Human life is sacred and should be treated as such.</blockquote>
      </article>
    </div>
  </section>

  <!-- Humanitarian crisis -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Background</span>
        <h2 class="reveal">Humanitarian crisis in Eastern Congo.</h2>
        <p class="reveal">Since the 1990s, the Democratic Republic of Congo (DRC) has been facing intractable conflicts and recurrent wars. Even with elected governments starting in 2006 following the implementation of multiple peace agreements, the country still faces considerable challenges in consolidating peace throughout its territory. The eastern regions of the DRC have historically experienced high levels of insecurity and repeated incidences of war and violence, often due to interference from neighboring countries.</p>
        <p class="reveal">Recurrent episodes of violence, both in the east and in other parts of the DRC, indicate that structural problems deeply rooted in society hamper the process of conflict transformation and peace. Therefore, to achieve sustainable peace in the DRC and the Great Lakes region, we must address the problems.</p>
      </article>
    </div>
  </section>

{cta_donate("Stand with the families of Eastern DRC.", "Your support helps Congo Peace Academy deliver urgent relief and build the foundations for lasting peace across the region.")}
"""
    write("our-events/peace-today.html",
          head("Peace Today", "Stories and analysis from the Peace Today platform — security, justice, and human rights in the DRC.", p) +
          header(p, "events") + body + footer(p))

# ===========================================================================
# 8) our-events/become-volunteers.html
# ===========================================================================
def build_volunteers():
    p = "../"
    body = page_hero(
        [("Home", "../index.html"), ("Our Events", "index.html"), ("Become Volunteers", None)],
        "Congo Peace Academy Fellows.",
        "Educate and mentor top high school students in the Democratic Republic of Congo — and help cultivate the next generation of Congolese leaders."
    ) + f"""
  <!-- Hero photo -->
  <section class="bg-paper">
    <div class="container">
      <div class="profile-feature">
        <div class="profile-feature-media reveal">
          <img src="{IMG['fellows']}" alt="Congo Peace Academy Fellows mentoring students" loading="lazy" />
        </div>
        <div class="profile-feature-body">
          <span class="eyebrow reveal">College Prep Program</span>
          <h2 class="reveal">Congo Peace Academy's College Prep.</h2>
          <p class="reveal">Congo Peace Academy's College Prep Program offers intensive English language training and a university preparation program designed to equip top Congolese high school students with the skills they need to compete for and win university scholarships within and outside the continent.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- What is a Fellow -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">The role</span>
        <h2 class="reveal">Congo Peace Academy Fellows.</h2>
        <p class="reveal">A Congo Peace Academy fellow is an individual who has been selected by Congo Peace Academy to educate and mentor top high school students in the Democratic Republic of Congo (DRC). This individual is responsible for providing guidance and support to these students, helping them to develop their academic skills, leadership abilities, and personal qualities to realize their incredible potential.</p>
        <p class="reveal">The fellow must be knowledgeable about the academic curriculum and possess strong teaching skills, as well as have experience working with young people in a mentoring or coaching capacity. Additionally, the fellow should be committed to promoting peace and social justice in the DRC, and be able to serve as a positive role model for their students.</p>
        <p class="reveal">In summary, an ideal Congo Peace Academy fellow should possess a strong academic background, excellent communication skills in French and English, a passion for empowering young people, strong leadership skills, a commitment to promoting peace and reconciliation through education, and a commitment to lifelong learning.</p>
      </article>
    </div>
  </section>

  <!-- What role -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Impact</span>
        <h2 class="reveal">What role does a fellow play?</h2>
        <p class="reveal">The role of a Congo Peace Academy fellow is crucial in helping to build a brighter future for the DRC by empowering its youth. By providing high-quality education and mentorship to top high school students, fellows can help to cultivate a new generation of leaders who are equipped with the skills and knowledge needed to make positive changes in their communities and transform our world.</p>
      </article>
    </div>
  </section>

  <!-- How to become -->
  <section class="bg-cream">
    <div class="container container-narrow">
      <article class="prose">
        <span class="eyebrow reveal">Apply</span>
        <h2 class="reveal">How to become a Congo Peace Academy Fellow.</h2>
        <p class="reveal">To be selected, the Fellow must demonstrate exceptional qualities and values. He/she must be familiar with the curriculum and possess strong pedagogical skills, as well as experience working with young people in a mentoring or coaching capacity.</p>
        <p class="reveal">In addition, the Fellow must be committed to promoting peace and social justice in the DRC, and be able to serve as a positive role model for his or her students. His / her role is crucial in helping Congo Peace Academy build a better future for the DRC by empowering its young people and helping to cultivate a new generation of leaders who are equipped with the skills and knowledge to bring about positive change in their communities.</p>
        <p class="reveal">If you can recognize yourself in this profile, don't hesitate to fill in the following application form and we'll get back to you within 48 hours.</p>
      </article>
    </div>
  </section>

  <!-- Apply CTA -->
  <section class="bg-paper">
    <div class="container container-narrow">
      <div class="cta-band reveal">
        <h2>Ready to mentor the next generation?</h2>
        <p>Apply to join the Congo Peace Academy Fellows program. We'll review your application and get back to you within 48 hours.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-primary btn-lg" href="https://forms.gle/gU7G5wXaPiLu75m76" target="_blank" rel="noopener">Apply now</a>
        </div>
      </div>
    </div>
  </section>
"""
    write("our-events/become-volunteers.html",
          head("Become a Volunteer — Congo Peace Academy Fellows", "Join the Congo Peace Academy Fellows program — mentor top Congolese students through our College Prep program.", p) +
          header(p, "events") + body + footer(p))

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Building pages…")
    build_health()
    build_blog()
    build_team()
    build_agri()
    build_path()
    build_events_index()
    build_peace_today()
    build_volunteers()
    print("Done.")

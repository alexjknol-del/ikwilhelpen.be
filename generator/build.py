#!/usr/bin/env python3
"""
Bouwscript voor ikwilhelpen.be
Genereert de volledige statische site in ../site op basis van de content
hieronder. Uitbreiden met een nieuw artikel? Voeg een item toe aan ARTICLES
in content.py en run: python3 pages.py
"""
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
SITE_URL = "https://ikwilhelpen.be"
SITE_NAME = "ikwilhelpen.be"

NAV_ITEMS = [
    ("Home", "/"),
    ("Over", "/over/"),
    ("Nieuws", "/nieuws/"),
    ("Partners", "/partners/"),
    ("Contact", "/contact/"),
]

FOOTER_COLS = {
    "Platform": [
        ("Over ikwilhelpen.be", "/over/"),
        ("De schrijfster", "/schrijfster/"),
        ("Veelgestelde vragen", "/faq/"),
        ("Partners", "/partners/"),
    ],
    "Informatie": [
        ("Disclaimer", "/disclaimer/"),
        ("Privacybeleid", "/privacybeleid/"),
        ("Cookiebeleid", "/cookiebeleid/"),
        ("Contact", "/contact/"),
    ],
}


def base_html(title, description, canonical_path, content, active=None, og_image="/images/favicon.svg"):
    nav_html = ""
    for label, href in NAV_ITEMS:
        is_active = " actief" if active == href else ""
        nav_html += f'<li><a href="{href}" class="{is_active.strip()}">{label}</a></li>\n'

    footer_cols_html = ""
    for heading, links in FOOTER_COLS.items():
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links)
        footer_cols_html += f"<div><h4>{heading}</h4><ul>{items}</ul></div>\n"

    canonical = f"{SITE_URL}{canonical_path}"
    year = "2026"

    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:image" content="{SITE_URL}{og_image}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a href="/" class="logo">ikwilhelpen<span>.be</span></a>
    <button class="menu-toggle" id="menuToggle" aria-label="Menu openen" aria-expanded="false">
      <span></span>
    </button>
    <nav class="main-nav" id="mainNav">
      <ul>
        {nav_html}
      </ul>
    </nav>
  </div>
</header>

<main>
{content}
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>ikwilhelpen.be</h4>
        <p>Praktische hulp en heldere uitleg voor grote en kleine vragen uit het dagelijkse leven. Onafhankelijk, getest en zonder overbodige poespas.</p>
      </div>
      {footer_cols_html}
    </div>
    <div class="footer-onder">
      <span>&copy; {year} ikwilhelpen.be</span>
      <span>Contact: <a href="mailto:info@ikwilhelpen.be">info@ikwilhelpen.be</a></span>
    </div>
  </div>
</footer>

<script>
  var toggle = document.getElementById('menuToggle');
  var nav = document.getElementById('mainNav');
  if (toggle && nav) {{
    toggle.addEventListener('click', function () {{
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }});
  }}
</script>
</body>
</html>
"""


def write_page(path, html):
    full_dir = os.path.join(OUT, path.strip("/")) if path != "/" else OUT
    os.makedirs(full_dir, exist_ok=True)
    with open(os.path.join(full_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

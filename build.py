# -*- coding: utf-8 -*-
"""
build.py — Static site generator for Al Jawareh Auto Spare Parts.

Reads content from data.py and writes a complete static website into dist/.
Pure HTML + modern CSS + vanilla JS. No frameworks, no runtime dependencies.

Usage:
    python3 build.py
Then commit the whole repo (including dist/) and let cPanel deploy dist/ to
public_html via .cpanel.yml.  See README.md.
"""

import os
import re
import json
import shutil
import html as _html
from datetime import date
from urllib.parse import quote

from data import SITE, BRANDS, CATEGORIES, LOCATIONS, FAQS, POSTS
import theme
import hashlib


def _asset_version():
    h = hashlib.sha1()
    for part in (theme.STYLE_CSS, theme.MAIN_JS, theme.FAVICON_SVG):
        h.update(part.encode("utf-8"))
    for d in (getattr(theme, "SITE_IMAGES_B64", {}), getattr(theme, "BRAND_LOGOS_B64", {})):
        for k in sorted(d):
            h.update(k.encode("utf-8"))
            h.update(d[k].encode("utf-8"))
    return h.hexdigest()[:10]


ASSET_VER = _asset_version()

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
ASSETS_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
TODAY = date.today().isoformat()

# Collected for sitemap.xml as we write pages.
PAGES = []

# Every image that actually exists in the build (filled by copy_assets). Pages only
# reference files in here, so the site never requests a missing image.
AVAILABLE_IMAGES = set()

# Quick lookups
BRAND_BY_SLUG = {b["slug"]: b for b in BRANDS}
CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}
POST_BY_SLUG = {p["slug"]: p for p in POSTS}


# ---------------------------------------------------------------------------
# SVG ICONS (inline, currentColor, no manufacturer trademarks)
# ---------------------------------------------------------------------------
ICONS = {
    'engine': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13H3v-3h2V8h3l2-2h4v2h3l2 2v3h2v3h-2v2l-2 2h-4l-2-2H8l-2 2H5z"/><path d="M8 10v4"/><path d="M14 6v3"/></svg>',
    'suspension': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3h4"/><path d="M12 3v3"/><path d="M8 6h8l-1.5 3H9.5z"/><path d="M12 9c-2 1.4-2 2.6 0 4s2 2.6 0 4"/><path d="M8 21h8l-1.5-3H9.5z"/><path d="M12 18v3"/></svg>',
    'brakes': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="12" r="7.5"/><circle cx="11" cy="12" r="3"/><path d="M18 8.5a4 4 0 0 1 3 3.5v2a1.5 1.5 0 0 1-1.5 1.5H18"/></svg>',
    'filter': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16"/><path d="M7 5v3.5a2 2 0 0 0 .6 1.4L12 14v6"/><path d="M17 5v3.5a2 2 0 0 1-.6 1.4L12 14"/></svg>',
    'electrical': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 5 13h5l-1 9 8-11h-5z"/></svg>',
    'body': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13l1.6-4.2A3 3 0 0 1 7.4 7h9.2a3 3 0 0 1 2.8 1.8L21 13"/><path d="M2.5 13h19v3.5a1 1 0 0 1-1 1H19a2 2 0 0 1-4 0H9a2 2 0 0 1-4 0H3.5a1 1 0 0 1-1-1z"/><path d="M6.5 15.5h.01M17.5 15.5h.01"/></svg>',
    'transmission': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="7" r="2.4"/><circle cx="7" cy="17" r="2.4"/><path d="M7 9.4v5.2"/><path d="M7 7h5a2 2 0 0 1 2 2v0"/><circle cx="16.5" cy="9" r="2.4"/><path d="M16.5 11.4V15a2 2 0 0 1-2 2h-3"/></svg>',
    'cooling': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M4.5 6.5 12 11l7.5-4.5"/><path d="M4.5 17.5 12 13l7.5 4.5"/><path d="M12 2 9.5 4M12 2l2.5 2M12 22l-2.5-2M12 22l2.5-2M3 12l2.2-1.3M3 12l2.2 1.3M21 12l-2.2-1.3M21 12l-2.2 1.3"/></svg>',
    'steering': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.4"/><path d="M12 14.4V21M9.9 11 3.7 8.4M14.1 11l6.2-2.6"/></svg>',
    'whatsapp': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.49s1.07 2.89 1.22 3.09c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.29.17-1.42-.07-.13-.27-.2-.57-.35zM12.05 21.7h-.01a9.6 9.6 0 0 1-4.9-1.34l-.35-.21-3.64.95.97-3.55-.23-.36a9.56 9.56 0 0 1-1.47-5.1c0-5.29 4.31-9.6 9.61-9.6 2.57 0 4.98 1 6.79 2.82a9.54 9.54 0 0 1 2.81 6.79c0 5.29-4.31 9.6-9.6 9.6zm8.17-17.77A11.5 11.5 0 0 0 12.05.55C5.7.55.55 5.7.55 12.04c0 2.02.53 4 1.54 5.74L.5 23.5l5.86-1.54a11.47 11.47 0 0 0 5.69 1.45h.01c6.35 0 11.5-5.16 11.5-11.5a11.44 11.44 0 0 0-3.34-8.08z"/></svg>',
    'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3h-2A1.5 1.5 0 0 0 3 4.6C3 13 11 21 19.4 21A1.5 1.5 0 0 0 21 19.5v-2a1 1 0 0 0-.8-1l-3-.6a1 1 0 0 0-1 .4l-.9 1.2a13 13 0 0 1-5.8-5.8l1.2-.9a1 1 0 0 0 .4-1l-.6-3a1 1 0 0 0-1-.8z"/></svg>',
    'location': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 5.5-8 12-8 12s-8-6.5-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 1.8"/></svg>',
    'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.2"/><path d="m4 7 8 5.5L20 7"/></svg>',
    'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13M13 6l6 6-6 6"/></svg>',
    'chevron': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    'close': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    'search': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5 4.5 5.2v6.1c0 4.6 3.2 7.8 7.5 9.7 4.3-1.9 7.5-5.1 7.5-9.7V5.2z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/></svg>',
    'truck': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6.5A1.5 1.5 0 0 1 4.5 5H13a1 1 0 0 1 1 1v9H3z"/><path d="M14 9h3.5a2 2 0 0 1 1.6.8L21 12.5V15h-7z"/><circle cx="7" cy="18" r="1.9"/><circle cx="17.5" cy="18" r="1.9"/></svg>',
    'vin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="19" height="12" rx="1.5"/><path d="M6 9v6M9 9l1.5 6L12 9l1.5 6L15 9M18 9v6"/></svg>',
    'quote': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 11h9"/><path d="m14 13 2.5 2.5L22 10"/><path d="M4 16h6"/></svg>',
    'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 20.5 12z"/><path d="M8.5 11h.01M12 11h.01M15.5 11h.01"/></svg>',
    'tag': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20.6 13.4 12 22l-9-9V4.5A1.5 1.5 0 0 1 4.5 3H13z"/><circle cx="7.5" cy="7.5" r="1.3"/></svg>',
    'star': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.5 2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 18.9 6.1 21l1.1-6.5L2.5 9.9l6.5-.9z"/></svg>',
    'money': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/></svg>',
    'wrench': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M15.2 6.3a4 4 0 0 0-5.3 5L3.5 17.7l2.8 2.8 6.4-6.4a4 4 0 0 0 5-5.3l-2.6 2.6-2.2-2.2z"/></svg>',
    'box': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8.2 12 3 3 8.2m18 0L12 13.4 3 8.2m18 0V16L12 21m0-7.6V21M3 8.2V16l9 5"/></svg>',
    'headset': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 13a8 8 0 0 1 16 0"/><rect x="2.5" y="13" width="4" height="6" rx="1.6"/><rect x="17.5" y="13" width="4" height="6" rx="1.6"/><path d="M20 19a4 4 0 0 1-4 3h-2.5"/></svg>',
    'external': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M18 13v5a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h5"/></svg>',
    'dot': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="12" r="6"/></svg>',
    'sparkles': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.6 4.4L18 9l-4.4 1.6L12 15l-1.6-4.4L6 9l4.4-1.6z"/><path d="M18 14l.8 2.2L21 17l-2.2.8L18 20l-.8-2.2L15 17l2.2-.8z"/></svg>',
    'award': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="5.5"/><path d="M9 13.5 7.5 21l4.5-2.5L16.5 21 15 13.5"/></svg>',
    'gauge': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15a8 8 0 1 1 16 0"/><path d="M12 15l4-4"/><circle cx="12" cy="15" r="1"/></svg>',
    'layers': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg>',
    'plus': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>',
    'car': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12l1.7-4.5A3 3 0 0 1 7.5 6h9a3 3 0 0 1 2.8 1.5L21 12"/><path d="M2.5 12h19v4.5a1 1 0 0 1-1 1H19a2 2 0 0 1-4 0H9a2 2 0 0 1-4 0H3.5a1 1 0 0 1-1-1z"/><path d="M6.5 15h.01M17.5 15h.01"/></svg>',
    'spark': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/></svg>',
    'refresh': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-2.6-6.3"/><path d="M21 4v5h-5"/></svg>',
}


def icon(name, cls="ic"):
    svg = ICONS.get(name, "")
    return f'<span class="{cls}" aria-hidden="true">{svg}</span>'


# ---------------------------------------------------------------------------
# SMALL HELPERS
# ---------------------------------------------------------------------------
def esc(s):
    return _html.escape(str(s), quote=True)


def abs_url(path):
    if not path:
        return SITE["base_url"] + "/"
    if str(path).startswith("http"):
        return path
    return SITE["base_url"].rstrip("/") + path


def wa_link(text):
    return f'https://wa.me/{SITE["whatsapp"]}?text={quote(text)}'


WA_GENERIC = "Hello Al Jawareh Auto Spare Parts, I'd like to enquire about a spare part."


def tel_link():
    return f'tel:{SITE["phone_href"]}'


def media(path, alt, ratio="4x3", label=None, icon_name="box", cls="", logo_brand=None, tag=None):
    """Real photo when it exists in the build; otherwise a designed art panel.
    Never emits a request for a missing file."""
    if path and path in AVAILABLE_IMAGES:
        return (f'<figure class="media media--{ratio} {cls}">'
                f'<img src="{esc(path)}?v={ASSET_VER}" alt="{esc(alt)}" loading="lazy" decoding="async"></figure>')
    if logo_brand:
        centre = f'<span class="art__logo">{brand_logo(logo_brand, "art")}</span>'
    else:
        centre = f'<span class="art__ic">{icon(icon_name, "art__icon")}</span>'
    tag_html = f'<span class="art__tag">{esc(tag)}</span>' if tag else ""
    return (f'<figure class="media media--{ratio} art {cls}" role="img" aria-label="{esc(alt)}">'
            f'<span class="art__grid" aria-hidden="true"></span><span class="art__glow" aria-hidden="true"></span>'
            f'<span class="art__mark" aria-hidden="true">{icon(icon_name, "art__watermark")}</span>'
            f'{centre}{tag_html}</figure>')


def logo_slot(brand, size="md"):
    """Brand logo upload slot — shows the marque name as text until a logo file is added.
    No manufacturer logos are reproduced."""
    slug = brand["slug"]
    name = brand["name"]
    return (
        f'<span class="logoslot logoslot--{size} ph" data-ph title="{esc(name)}">'
        f'<img src="/assets/images/brands/{slug}-logo.svg" alt="{esc(name)} logo" loading="lazy" '
        f'onload="this.closest(\'[data-ph]\').classList.add(\'is-loaded\')" '
        f'onerror="this.closest(\'[data-ph]\').classList.add(\'is-fallback\')">'
        f'<span class="logoslot__text" aria-hidden="true">{esc(name)}</span>'
        f'</span>'
    )


def monogram(name):
    """Neutral text initials used as a placeholder tile in dense grids (not a logo)."""
    words = [w for w in re.split(r"[^A-Za-z0-9]+", name) if w]
    if len(words) >= 2:
        m = (words[0][0] + words[1][0]).upper()
    elif words:
        m = words[0][:2].upper()
    else:
        m = "?"
    return f'<span class="mono" aria-hidden="true">{esc(m)}</span>'


def brand_logo(b, size="sm"):
    """Real brand logo on a white badge; clean name badge if no logo file exists."""
    slug, name = b["slug"], b["name"]
    path = f"/assets/images/brands/{slug}-logo.png"
    if path in AVAILABLE_IMAGES:
        return (f'<span class="blogo blogo--{size} is-loaded" title="{esc(name)}">'
                f'<img src="{path}?v={ASSET_VER}" alt="{esc(name)} logo" loading="lazy" decoding="async"></span>')
    return (f'<span class="blogo blogo--{size} is-fallback" title="{esc(name)}">'
            f'<span class="blogo__text">{esc(name)}</span></span>')


def title_of_brand_cat(brand, cat, loc="Sharjah & UAE"):
    return f'{brand["name"]} {cat["name"]}'


# ---------------------------------------------------------------------------
# JSON-LD SCHEMA BUILDERS
# ---------------------------------------------------------------------------
def store_schema():
    a = SITE["address"]
    obj = {
        "@context": "https://schema.org",
        "@type": "AutoPartsStore",
        "@id": SITE["base_url"] + "/#store",
        "name": SITE["name"],
        "url": SITE["base_url"] + "/",
        "image": abs_url(SITE["og_image"]),
        "telephone": SITE["phone_intl"],
        "email": SITE["email"],
        "priceRange": SITE["price_range"],
        "currenciesAccepted": "AED",
        "paymentAccepted": "Cash, Card, Bank Transfer",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": a["line1"] + ", " + a["line2"],
            "addressLocality": a["city"],
            "addressRegion": a["region"],
            "addressCountry": a["country_code"],
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": SITE["geo"]["lat"],
            "longitude": SITE["geo"]["lng"],
        },
        "areaServed": [{"@type": "City", "name": l["name"]} for l in LOCATIONS],
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": h["days"],
                "opens": h["opens"],
                "closes": h["closes"],
            }
            for h in SITE["hours_schema"]
        ],
    }
    obj["logo"] = abs_url("/assets/images/site/logo.png")
    obj["hasMap"] = "https://www.google.com/maps/search/?api=1&query=" + quote(SITE["maps_query"])
    obj["brand"] = [{"@type": "Brand", "name": br["name"]} for br in BRANDS]
    obj["hasOfferCatalog"] = {
        "@type": "OfferCatalog",
        "name": "Genuine & OEM auto spare parts",
        "itemListElement": [
            {"@type": "OfferCatalog", "name": c["name"], "url": abs_url(f'/parts/{c["slug"]}/')}
            for c in CATEGORIES
        ],
    }
    sameas = [v for v in SITE["social"].values() if v]
    if sameas:
        obj["sameAs"] = sameas
    return obj


def breadcrumb_schema(items):
    elements = []
    for i, (label, path) in enumerate(items, start=1):
        el = {"@type": "ListItem", "position": i, "name": label}
        if path:
            el["item"] = abs_url(path)
        elements.append(el)
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def article_schema(post):
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["title"],
        "description": post["excerpt"],
        "datePublished": post["date"],
        "dateModified": post["date"],
        "image": abs_url(f'/assets/images/blog/{post["slug"]}.jpg'
                         if f'/assets/images/blog/{post["slug"]}.jpg' in AVAILABLE_IMAGES else SITE["og_image"]),
        "author": {"@type": "Organization", "name": SITE["name"]},
        "publisher": {
            "@type": "Organization",
            "name": SITE["name"],
            "logo": {"@type": "ImageObject", "url": abs_url("/assets/images/site/logo.png")},
        },
        "mainEntityOfPage": abs_url(f'/blog/{post["slug"]}/'),
    }


def fit_title(t, n=60):
    """Keep titles inside Google's ~60-char display width, shortening progressively."""
    segs = t.split(" | ")
    while len(" | ".join(segs)) > n and len(segs) > 2:
        segs.pop(-2)
    if len(" | ".join(segs)) > n and len(segs) > 1 and segs[-1].startswith("Al Jawareh"):
        segs[-1] = "Al Jawareh"
    if len(" | ".join(segs)) > n:
        segs[0] = segs[0].replace(" in Sharjah & the UAE", " in Sharjah").replace(" in Sharjah & UAE", " in Sharjah")
    if len(" | ".join(segs)) > n and len(segs) > 1:
        segs = segs[:1]
    return " | ".join(segs)


def clip_desc(d, n=158):
    d = " ".join(str(d).split())
    if len(d) <= n:
        return d
    cut = d[:n - 1].rsplit(" ", 1)[0].rstrip(",;:-–— ")
    return cut + "…"


def jsonld_tags(objs):
    out = ""
    for o in objs:
        out += '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>\n"
    return out


# ---------------------------------------------------------------------------
# HEAD + PAGE SHELL
# ---------------------------------------------------------------------------
def render_head(title, description, path, jsonld_objs, og_type="website", image=None, preload=""):
    title = fit_title(title)
    description = clip_desc(description)
    canonical = abs_url(path)
    if image and image not in AVAILABLE_IMAGES:
        image = None
    img = abs_url(image or SITE["og_image"])
    og_dims = ('<meta property="og:image:width" content="1200">\n'
               '<meta property="og:image:height" content="630">\n') if not image else ""
    lat, lng = SITE["geo"]["lat"], SITE["geo"]["lng"]
    return f"""<!DOCTYPE html>
<html lang="en-AE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="theme-color" content="#0f1318">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="format-detection" content="telephone=no">
<meta name="geo.region" content="AE-SH">
<meta name="geo.placename" content="Sharjah">
<meta name="geo.position" content="{lat};{lng}">
<meta name="ICBM" content="{lat}, {lng}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(SITE['name'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(img)}">
{og_dims}<meta property="og:image:alt" content="{esc(SITE['name'])}">
<meta property="og:locale" content="en_AE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(img)}">
<link rel="icon" href="/assets/images/site/favicon.svg?v={ASSET_VER}" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/images/site/apple-touch-icon.png?v={ASSET_VER}">
<link rel="preload" href="/assets/fonts/sora-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="/assets/css/style.css?v={ASSET_VER}">
{jsonld_tags(jsonld_objs)}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def render_page(title, description, path, body, jsonld_objs, active="", og_type="website", image=None,
                priority="0.7", changefreq="monthly", lastmod=None, preload=""):
    doc = (
        render_head(title, description, path, jsonld_objs, og_type, image, preload)
        + nav(active)
        + f'<main id="main">{body}</main>'
        + footer()
        + whatsapp_widget()
        + '<script src="/assets/js/main.js?v=' + ASSET_VER + '" defer></script>\n</body>\n</html>\n'
    )
    write_page(path, doc, priority=priority, changefreq=changefreq, lastmod=lastmod)


def write_page(path, doc, priority="0.7", changefreq="monthly", lastmod=None):
    # path like "/brands/range-rover/" -> dist/brands/range-rover/index.html
    rel = path.strip("/")
    if rel == "":
        out_dir = DIST
    else:
        out_dir = os.path.join(DIST, *rel.split("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append({"loc": abs_url(path if path.endswith("/") or path == "/" else path + "/"),
                  "priority": priority, "changefreq": changefreq, "lastmod": lastmod or TODAY})


# ---------------------------------------------------------------------------
# HEADER / NAV
# ---------------------------------------------------------------------------
def nav(active=""):
    def act(key):
        return " is-active" if active == key else ""

    # Brands mega panel
    brand_links = "".join(
        f'<a class="mega__item" href="/brands/{b["slug"]}/">'
        f'<span class="mega__name">{esc(b["name"])}</span>'
        f'<span class="mega__sub">{esc(b["origin"])}</span></a>'
        for b in BRANDS
    )
    # Parts mega panel
    cat_links = "".join(
        f'<a class="mega__item mega__item--icon" href="/parts/{c["slug"]}/">'
        f'{icon(c["icon"], "mega__ic")}'
        f'<span><span class="mega__name">{esc(c["name"])}</span>'
        f'<span class="mega__sub">{esc(c["short"])}</span></span></a>'
        for c in CATEGORIES
    )
    # Locations dropdown
    loc_links = "".join(
        f'<a class="dd__item" href="/locations/{l["slug"]}/">{esc(l["name"])}</a>'
        for l in LOCATIONS
    )

    # Mobile accordion sections
    m_brands = "".join(f'<a href="/brands/{b["slug"]}/">{esc(b["name"])}</a>' for b in BRANDS)
    m_parts = "".join(f'<a href="/parts/{c["slug"]}/">{esc(c["name"])}</a>' for c in CATEGORIES)
    m_locs = "".join(f'<a href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCATIONS)

    return f"""<header class="site-header" data-header>
  <div class="topbar">
    <div class="container topbar__inner">
      <span class="topbar__item topbar__loc">{icon('location','ic ic--sm')} {esc(SITE['address']['line2'])}, {esc(SITE['address']['city'])}</span>
      <span class="status" data-hours-status role="status" aria-live="polite">
        <span class="status__dot"></span>
        <span class="status__text">Sat–Thu 8AM–9PM &middot; closed Fri</span>
      </span>
      <span class="topbar__spacer"></span>
      <a class="topbar__item topbar__link topbar__wa" href="{wa_link(WA_GENERIC)}" target="_blank" rel="noopener">{icon('whatsapp','ic ic--sm')} WhatsApp</a>
      <a class="topbar__item topbar__link" href="{tel_link()}">{icon('phone','ic ic--sm')} {esc(SITE['phone_display'])}</a>
    </div>
  </div>
  <div class="nav">
    <div class="container nav__inner">
      <a class="brand" href="/" aria-label="{esc(SITE['name'])} home">
        <img class="brand__logo" src="/assets/images/site/logo-full.png?v={ASSET_VER}" alt="{esc(SITE['name'])}" width="495" height="160">
      </a>
      <nav class="nav__links" aria-label="Primary navigation">
        <a class="nav__link{act('home')}" href="/">Home</a>
        <div class="nav__group has-mega">
          <button class="nav__link nav__toggle{act('brands')}" aria-expanded="false" aria-haspopup="true">Brands {icon('chevron','ic ic--xs')}</button>
          <div class="mega mega--brands" role="menu">
            <div class="mega__grid">{brand_links}</div>
            <a class="mega__all" href="/brands/">All brands {icon('arrow','ic ic--sm')}</a>
          </div>
        </div>
        <div class="nav__group has-mega">
          <button class="nav__link nav__toggle{act('parts')}" aria-expanded="false" aria-haspopup="true">Parts {icon('chevron','ic ic--xs')}</button>
          <div class="mega mega--parts" role="menu">
            <div class="mega__grid mega__grid--icon">{cat_links}</div>
            <a class="mega__all" href="/parts/">All part categories {icon('arrow','ic ic--sm')}</a>
          </div>
        </div>
        <a class="nav__link{act('contact')}" href="/contact/">Contact</a>
      </nav>
      <div class="nav__cta">
        <a class="btn btn--ghost btn--sm nav__call" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>Call</span></a>
        <button class="btn btn--wa btn--sm" data-enquiry-open>{icon('whatsapp','ic ic--sm')}<span>Request a Part</span></button>
        <button class="nav__burger" data-menu-open aria-label="Open menu" aria-expanded="false">{icon('menu','ic')}</button>
      </div>
    </div>
  </div>
  <div class="mobile" data-mobile hidden>
    <div class="mobile__scrim" data-menu-close></div>
    <div class="mobile__panel">
      <div class="mobile__head">
        <img class="brand__logo" src="/assets/images/site/logo-full.png?v={ASSET_VER}" alt="{esc(SITE['name'])}" width="495" height="160">
        <button class="mobile__close" data-menu-close aria-label="Close menu">{icon('close','ic')}</button>
      </div>
      <div class="mobile__status"><span class="status" data-hours-status role="status"><span class="status__dot"></span><span class="status__text">Sat–Thu 8AM–9PM &middot; closed Fri</span></span></div>
      <div class="mobile__body">
        <a class="mobile__link" href="/">Home</a>
        <details class="mobile__acc"><summary>Brands {icon('chevron','ic ic--xs')}</summary><div class="mobile__sub">{m_brands}<a href="/brands/">All brands</a></div></details>
        <details class="mobile__acc"><summary>Parts {icon('chevron','ic ic--xs')}</summary><div class="mobile__sub">{m_parts}<a href="/parts/">All part categories</a></div></details>
        <a class="mobile__link" href="/contact/">Contact</a>
      </div>
      <div class="mobile__foot">
        <button class="btn btn--wa btn--block" data-enquiry-open>{icon('whatsapp','ic ic--sm')} Request a Part</button>
        <a class="btn btn--ghost-light btn--block" href="{tel_link()}">{icon('phone','ic ic--sm')} {esc(SITE['phone_display'])}</a>
      </div>
    </div>
  </div>
</header>
"""


# ---------------------------------------------------------------------------
# BREADCRUMBS
# ---------------------------------------------------------------------------
def breadcrumbs(items):
    """items: list of (label, path|None). Returns HTML string."""
    parts = []
    for i, (label, path) in enumerate(items):
        last = i == len(items) - 1
        if last or not path:
            parts.append(f'<span aria-current="page">{esc(label)}</span>')
        else:
            parts.append(f'<a href="{esc(path)}">{esc(label)}</a>')
    sep = f'<span class="crumbs__sep">{icon("chevron","ic ic--xs")}</span>'
    inner = sep.join(parts)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><div class="container">{inner}</div></nav>'


# ---------------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------------
def footer():
    a = SITE["address"]
    brand_cols = "".join(f'<li><a href="/brands/{b["slug"]}/">{esc(b["name"])}</a></li>' for b in BRANDS)
    cat_cols = "".join(f'<li><a href="/parts/{c["slug"]}/">{esc(c["name"])}</a></li>' for c in CATEGORIES)
    loc_cols = "".join(f'<li><a href="/locations/{l["slug"]}/">{esc(l["name"])}</a></li>' for l in LOCATIONS)
    hours = "".join(f'<li><span>{esc(d)}</span><span>{esc(t)}</span></li>' for d, t in SITE["hours_display"])

    socials = ""
    labels = {"facebook": "Facebook", "instagram": "Instagram", "tiktok": "TikTok",
              "youtube": "YouTube", "google_business": "Google"}
    for key, url in SITE["social"].items():
        if url:
            socials += f'<a class="soc" href="{esc(url)}" target="_blank" rel="noopener" aria-label="{labels.get(key,key)}">{labels.get(key,key)}</a>'

    return f"""<footer class="footer">
  <div class="container footer__grid">
    <div class="footer__col footer__brand">
      <a class="brand brand--footer" href="/">
        <img class="brand__logo" src="/assets/images/site/logo-full.png?v={ASSET_VER}" alt="{esc(SITE['name'])}" width="495" height="160">
      </a>
      <p class="footer__blurb">Genuine &amp; OEM spare parts for premium European and American vehicles — supplied across the UAE from our shop in Sharjah.</p>
      <div class="footer__contact">
        <a href="{tel_link()}">{icon('phone','ic ic--sm')} {esc(SITE['phone_display'])}</a>
        <a href="{wa_link(WA_GENERIC)}" target="_blank" rel="noopener">{icon('whatsapp','ic ic--sm')} WhatsApp us</a>
        <a href="mailto:{esc(SITE['email'])}">{icon('mail','ic ic--sm')} {esc(SITE['email'])}</a>
        <span>{icon('location','ic ic--sm')} {esc(a['line1'])}, {esc(a['line2'])}, {esc(a['city'])}</span>
      </div>
    </div>
    <div class="footer__col">
      <h3 class="footer__h">Brands</h3>
      <ul class="footer__list">{brand_cols}</ul>
    </div>
    <div class="footer__col">
      <h3 class="footer__h">Parts</h3>
      <ul class="footer__list">{cat_cols}</ul>
    </div>
    <div class="footer__col">
      <h3 class="footer__h">Areas we serve</h3>
      <ul class="footer__list">{loc_cols}</ul>
      <h3 class="footer__h footer__h--mt">Company</h3>
      <ul class="footer__list">
        <li><a href="/about/">About us</a></li>
        <li><a href="/blog/">Blog &amp; guides</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/request-a-part/">Request a part</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div class="footer__col">
      <h3 class="footer__h">Opening hours</h3>
      <ul class="footer__hours">{hours}</ul>
      <div class="footer__socials">{socials}</div>
    </div>
  </div>
  <div class="footer__bar">
    <div class="container footer__bar-inner">
      <p>&copy; <span data-year>{date.today().year}</span> {esc(SITE['name'])}. All rights reserved.</p>
      <p class="footer__note">Genuine &amp; OEM parts. Brand names are used for reference only; all trademarks belong to their respective owners.</p>
      <button class="footer__top" data-scroll-top aria-label="Back to top">{icon('chevron','ic')}<span>Top</span></button>
    </div>
  </div>
</footer>
"""


# ---------------------------------------------------------------------------
# WHATSAPP ENQUIRY ASSISTANT (floating button + drawer) — on every page
# ---------------------------------------------------------------------------
def parts_catalog_json():
    import json as _json
    cat = [{"cat": c["name"], "icon": c["icon"], "items": c["items"]} for c in CATEGORIES]
    return _json.dumps(cat, ensure_ascii=False)


def parts_builder():
    cat_opts = "".join(f'<option value="{esc(c["name"])}">{esc(c["name"])}</option>' for c in CATEGORIES)
    return f"""<div class="pb" data-parts-builder>
      <span class="field__label">Parts you need <b>*</b></span>
      <div class="pb__pickrow">
        <div class="pb__field">
          <select class="pb__select" data-pb-cat aria-label="Part category">
            <option value="" disabled selected>Choose a category</option>{cat_opts}
            <option value="__other">Something else / not sure</option>
          </select>
        </div>
        <div class="pb__field">
          <select class="pb__select" data-pb-part aria-label="Select part" disabled>
            <option value="" disabled selected>Select a category first</option>
          </select>
        </div>
        <button type="button" class="pb__add" data-pb-add aria-label="Add part">{icon('plus','ic ic--sm')}<span>Add</span></button>
      </div>
      <input type="text" class="pb__other" data-pb-other placeholder="Type the exact part or describe the fault" hidden>
      <ul class="pb__list" data-pb-list aria-live="polite"></ul>
      <p class="pb__empty" data-pb-empty>No parts added yet — pick a category and part above, or type your own.</p>
      <input type="hidden" name="parts" data-pb-hidden>
    </div>"""


def whatsapp_widget():
    make_opts = "".join(f'<option value="{esc(b["name"])}">{esc(b["name"])}</option>' for b in BRANDS)
    return f"""<nav class="mbar" aria-label="Quick actions">
  <a class="mbar__btn mbar__btn--call" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>Call</span></a>
  <a class="mbar__btn mbar__btn--chat" href="{wa_link(WA_GENERIC)}" target="_blank" rel="noopener">{icon('chat','ic ic--sm')}<span>Chat</span></a>
  <button class="mbar__btn mbar__btn--wa" data-enquiry-open>{icon('whatsapp','ic ic--sm')}<span>Request a Part</span></button>
</nav>
<button class="wa-fab" data-enquiry-open aria-label="Request a part on WhatsApp">
  {icon('whatsapp','wa-fab__icon')}
  <span class="wa-fab__label">Request a Part</span>
</button>
<div class="enquiry" data-enquiry hidden>
  <div class="enquiry__scrim" data-enquiry-close></div>
  <aside class="enquiry__panel" role="dialog" aria-modal="true" aria-labelledby="enq-title">
    <header class="enquiry__head">
      <div>
        <p class="enquiry__eyebrow">{icon('whatsapp','ic ic--sm')} WhatsApp enquiry</p>
        <h2 class="enquiry__title" id="enq-title">Request a part / get a quote</h2>
      </div>
      <button class="enquiry__close" data-enquiry-close aria-label="Close">{icon('close','ic')}</button>
    </header>
    <p class="enquiry__intro">Add one or more parts to your list, tell us your vehicle, and we'll open WhatsApp with everything ready to send. We confirm the exact parts and quote you.</p>
    <form class="enquiry__form" data-enquiry-form>
      <label class="field"><span>Your name</span><input type="text" name="name" placeholder="e.g. Ahmed" autocomplete="name"></label>
      <div class="field-row">
        <label class="field"><span>Vehicle make <b>*</b></span>
          <select name="make" required>
            <option value="" disabled selected>Select brand</option>
            {make_opts}
            <option value="Other">Other</option>
          </select>
        </label>
        <label class="field"><span>Model</span><input type="text" name="model" placeholder="e.g. Sport / C 200"></label>
      </div>
      <div class="field-row">
        <label class="field"><span>Year</span><input type="text" name="year" inputmode="numeric" placeholder="e.g. 2019"></label>
        <label class="field"><span>VIN / chassis no.</span><input type="text" name="vin" placeholder="Helps us match exactly"></label>
      </div>
      {parts_builder()}
      <label class="field"><span>Notes (optional)</span><textarea name="notes" rows="2" placeholder="Anything else that helps"></textarea></label>
      <button type="submit" class="btn btn--wa btn--block btn--lg">{icon('whatsapp','ic ic--sm')} Send my list on WhatsApp</button>
      <p class="enquiry__fine">No account needed. Opens WhatsApp to <b>{esc(SITE['phone_display'])}</b>.</p>
    </form>
    <script type="application/json" data-parts-catalog>{parts_catalog_json()}</script>
  </aside>
</div>
"""


# ---------------------------------------------------------------------------
# REUSABLE UI SECTIONS
# ---------------------------------------------------------------------------
def section_header(eyebrow, title, sub=None, center=False, light=False):
    c = " sec-head--center" if center else ""
    l = " sec-head--light" if light else ""
    subhtml = f'<p class="sec-head__sub">{sub}</p>' if sub else ""
    return (f'<div class="sec-head{c}{l}">'
            f'<span class="eyebrow">{esc(eyebrow)}</span>'
            f'<h2 class="sec-head__title">{title}</h2>{subhtml}</div>')


def btn_enquiry(label, make=None, cls="btn btn--wa", icon_name="whatsapp"):
    data = f' data-make="{esc(make)}"' if make else ""
    return (f'<button class="{cls}" data-enquiry-open{data}>'
            f'{icon(icon_name,"ic ic--sm")}<span>{esc(label)}</span></button>')


def btn_wa_link(label, message, cls="btn btn--wa", icon_name="whatsapp"):
    return (f'<a class="{cls}" href="{wa_link(message)}" target="_blank" rel="noopener">'
            f'{icon(icon_name,"ic ic--sm")}<span>{esc(label)}</span></a>')


def hero_quick_form():
    make_opts = "".join(f'<option value="{esc(b["name"])}">{esc(b["name"])}</option>' for b in BRANDS)
    return f"""<form class="quickform" data-quick-form>
      <p class="quickform__title">{icon('vin','ic ic--sm')} Quick part enquiry</p>
      <div class="quickform__fields">
        <select name="make" required aria-label="Vehicle make">
          <option value="" disabled selected>Brand</option>{make_opts}<option value="Other">Other</option>
        </select>
        <input type="text" name="model" placeholder="Model &amp; year" aria-label="Model and year">
        <input type="text" name="part" placeholder="Part or fault" required aria-label="Part needed">
      </div>
      <button type="submit" class="btn btn--wa btn--block">{icon('whatsapp','ic ic--sm')} Get a quote on WhatsApp</button>
      <span class="quickform__hint">Prefer the full form? <button type="button" class="linkbtn" data-enquiry-open>Open the request assistant</button></span>
    </form>"""


def brand_card(b):
    return (f'<a class="bcard" href="/brands/{b["slug"]}/">'
            f'<span class="bcard__logo">{brand_logo(b, "card")}</span>'
            f'<span class="bcard__txt"><span class="bcard__name">{esc(b["name"])}</span>'
            f'<span class="bcard__sub">{esc(b["origin"])}</span></span>'
            f'<span class="bcard__go" aria-hidden="true">{icon("arrow","ic ic--sm")}</span></a>')


def brands_grid(limit=None, ids=None):
    items = BRANDS if ids is None else [BRAND_BY_SLUG[i] for i in ids]
    if limit:
        items = items[:limit]
    return f'<div class="grid grid--brands">{"".join(brand_card(b) for b in items)}</div>'


def category_card(c, brand=None):
    href = f'/brands/{brand["slug"]}/{c["slug"]}/' if brand else f'/parts/{c["slug"]}/'
    name = f'{brand["name"]} {c["name"]}' if brand else c["name"]
    tag = brand["name"] if brand else None
    img = media("/assets/images/categories/" + c["slug"] + ".jpg", name, "16x9", c["name"], c["icon"], "ccard__img", tag=tag)
    return (f'<a class="ccard" href="{href}">'
            f'<span class="ccard__media">{img}</span>'
            f'<span class="ccard__body"><span class="ccard__name">{esc(name)}</span>'
            f'<span class="ccard__desc">{esc(c["card"])}</span>'
            f'<span class="ccard__go">Browse parts {icon("arrow","ic ic--sm")}</span></span></a>')


def categories_grid(brand=None, limit=None):
    items = CATEGORIES[:limit] if limit else CATEGORIES
    return f'<div class="grid grid--cats">{"".join(category_card(c, brand) for c in items)}</div>'


def features_why():
    feats = [
        ("shield", "Genuine &amp; OEM only",
         "Manufacturer parts and top OEM suppliers — Bosch, Mahle, ATE, Sachs. No mystery-brand gambles."),
        ("vin", "VIN-matched accuracy",
         "Send your chassis number and we match the exact part number, so it fits the first time."),
        ("truck", "Fast UAE-wide delivery",
         "Based in Sharjah, delivering to Dubai, Ajman, Abu Dhabi and beyond — often same or next day."),
        ("money", "Fair, honest pricing",
         "Genuine and OEM side by side, so you choose the right balance of budget and quality."),
        ("headset", "Real parts expertise",
         "We know these cars — from Range Rover air suspension to BMW cooling. Ask us anything."),
        ("box", "Hard-to-find parts sourced",
         "Not on the shelf? We source it through our supplier network with a realistic timeline."),
    ]
    cards = "".join(
        f'<div class="feature"><span class="feature__ic">{icon(i,"feature__icon")}</span>'
        f'<h3 class="feature__t">{t}</h3><p class="feature__p">{p}</p></div>'
        for i, t, p in feats
    )
    return f'<div class="grid grid--features">{cards}</div>'


def steps_order():
    steps = [
        ("Send us the details", "Message your vehicle make, model, year, VIN and the part you need — or just describe the fault. Use the Request a Part button anywhere on this site.", "chat"),
        ("We source &amp; quote", "We confirm the exact part, tell you whether it's genuine or OEM, and send you a clear price. No obligation.", "quote"),
        ("You approve", "Happy with the part and price? Give us the go-ahead and choose delivery or collection.", "check"),
        ("Delivered or collected", "Collect from our Sharjah shop, or we deliver anywhere in the UAE — often same or next day.", "truck"),
    ]
    items = "".join(
        f'<li class="step"><span class="step__num">{n}</span>'
        f'<span class="step__ic">{icon(i,"step__icon")}</span>'
        f'<h3 class="step__t">{t}</h3><p class="step__p">{p}</p></li>'
        for n, (t, p, i) in enumerate(steps, start=1)
    )
    return f'<ol class="steps">{items}</ol>'


def faq_block(faqs, eyebrow="FAQ", title="Common questions", center=False):
    items = "".join(
        f'<details class="faq"><summary class="faq__q">{esc(q)}{icon("chevron","faq__chev")}</summary>'
        f'<div class="faq__a"><p>{esc(a)}</p></div></details>'
        for q, a in faqs
    )
    return (f'<div class="faqs">{section_header(eyebrow, title, center=center)}'
            f'<div class="faqs__list">{items}</div></div>')


# Curated high-intent brand x category internal links (SEO)
POPULAR_COMBOS = [
    ("range-rover", "suspension-air-struts"), ("range-rover", "brakes"),
    ("land-rover", "engine-parts"), ("mercedes-benz", "suspension-air-struts"),
    ("mercedes-benz", "brakes"), ("bmw", "cooling-ac"), ("bmw", "brakes"),
    ("audi", "transmission-drivetrain"), ("audi", "engine-parts"),
    ("porsche", "brakes"), ("volkswagen", "filters-service-parts"),
    ("jaguar", "engine-parts"), ("gmc", "suspension-air-struts"),
    ("mercedes-benz", "filters-service-parts"), ("range-rover", "cooling-ac"),
    ("porsche", "suspension-air-struts"),
]


def popular_links():
    tags = "".join(
        f'<a class="poptag" href="/brands/{bs}/{cs}/">'
        f'{esc(BRAND_BY_SLUG[bs]["name"])} {esc(CAT_BY_SLUG[cs]["name"].lower())} '
        f'<b>Sharjah</b></a>'
        for bs, cs in POPULAR_COMBOS
    )
    return f'<div class="poptags">{tags}</div>'


def coverage_block():
    chips = "".join(f'<a class="areachip" href="/locations/{l["slug"]}/">{esc(l["name"])}</a>' for l in LOCATIONS)
    return f"""<div class="coverage">
      <div class="coverage__text">
        {section_header('UAE-wide', 'Delivering parts across the Emirates')}
        <p>We're based in Industrial Area 12, Sharjah, and deliver genuine &amp; OEM parts right across the UAE. Nearby emirates are often same or next day.</p>
        <div class="areachips">{chips}</div>
      </div>
      <div class="coverage__map">
        <iframe title="Al Jawareh Auto Spare Parts location" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          src="https://maps.google.com/maps?q={quote(SITE['maps_query'])}&output=embed"></iframe>
      </div>
    </div>"""


def blog_card(p):
    _ic = {"Buying Guide": "tag", "Fitment Guide": "wrench", "How-To": "vin", "Maintenance": "gauge"}.get(p["category"], "layers")
    _img = media("/assets/images/blog/" + p["slug"] + ".jpg", p["title"], "16x9", p["category"], _ic, "pcard__media")
    return (f'<article class="pcard"><a class="pcard__link" href="/blog/{p["slug"]}/">'
            f'{_img}'
            f'<span class="pcard__body"><span class="pcard__cat">{esc(p["category"])}</span>'
            f'<span class="pcard__title">{esc(p["title"])}</span>'
            f'<span class="pcard__excerpt">{esc(p["excerpt"])}</span>'
            f'<span class="pcard__meta">{esc(p["read_time"])} {icon("arrow","ic ic--sm")}</span></span></a></article>')


def blog_cards(limit=3):
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)[:limit]
    return f'<div class="grid grid--posts">{"".join(blog_card(p) for p in posts)}</div>'


def cta_banner(title, text, make=None, label="Request a Part"):
    return f"""<section class="cta">
      <div class="container">
        <div class="cta__card" data-reveal>
          <span class="cta__photo" aria-hidden="true" style="background-image:url(/assets/images/site/shop-counter.webp?v={ASSET_VER})"></span>
          <div class="cta__glow" aria-hidden="true"></div>
          <div class="cta__inner">
            <div class="cta__text"><h2 class="cta__title">{title}</h2><p class="cta__p">{text}</p></div>
            <div class="cta__actions">
              {btn_enquiry(label, make=make, cls="btn btn--wa btn--lg")}
              <a class="btn btn--ghost-light btn--lg" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>{esc(SITE['phone_display'])}</span></a>
            </div>
          </div>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------------------
# PAGE: HOME
# ---------------------------------------------------------------------------
def trust_strip():
    items = [
        ("shield", "Genuine &amp; OEM", "Manufacturer &amp; top OEM brands"),
        ("vin", "VIN-matched", "The right part, first time"),
        ("truck", "UAE-wide delivery", "Often same or next day"),
        ("headset", "Real parts experts", "We know these cars"),
    ]
    cells = "".join(
        f'<div class="trust"><span class="trust__ic">{icon(i,"trust__icon")}</span>'
        f'<span class="trust__tx"><b>{t}</b><span>{s}</span></span></div>'
        for i, t, s in items
    )
    return f'<section class="trustband-sec"><div class="container"><div class="trustband">{cells}</div></div></section>'


def specialist_block():
    return f"""<section class="section section--feature">
      <div class="container feature-split">
        <div class="feature-split__media" data-reveal>
          <picture>
            <source srcset="/assets/images/site/shop-counter.webp?v={ASSET_VER}" type="image/webp">
            <img src="/assets/images/site/shop-counter.jpg?v={ASSET_VER}" alt="Al Jawareh Auto Spare Parts shop counter in Industrial Area 12, Sharjah, with Range Rover and Land Rover parts" width="720" height="465" loading="lazy" decoding="async">
          </picture>
          <span class="feature-split__badge">{icon('location','ic ic--sm')} Visit the shop &middot; Industrial Area 12, Sharjah</span>
        </div>
        <div class="feature-split__text" data-reveal>
          <span class="eyebrow">Range Rover &amp; Land Rover specialists</span>
          <h2 class="sec-head__title">A real parts shop in Sharjah, stocked for the cars you drive</h2>
          <p class="feature-split__lead">Walk in, call or WhatsApp. Our shelves carry the fast-moving parts for Range Rover, Land Rover and the German marques, and what isn't on the shelf we source through our supplier network with a clear timeline.</p>
          <ul class="ticklist">
            <li>{icon('check','ic ic--sm')}<span>Air suspension: struts, EAS compressors and height sensors</span></li>
            <li>{icon('check','ic ic--sm')}<span>Engine, timing and cooling parts</span></li>
            <li>{icon('check','ic ic--sm')}<span>Brakes, filters and complete service kits</span></li>
            <li>{icon('check','ic ic--sm')}<span>Matched to your VIN so it fits the first time</span></li>
          </ul>
          <div class="feature-split__stats">
            <div><b>{len(BRANDS)}</b><span>premium marques</span></div>
            <div><b>{len(CATEGORIES)}</b><span>part categories</span></div>
            <div><b>{len(LOCATIONS)}</b><span>emirates &amp; cities served</span></div>
          </div>
          <div class="feature-split__actions">
            {btn_enquiry('Request a Range Rover part', make='Range Rover', cls='btn btn--wa btn--lg')}
            <a class="btn btn--ghost btn--lg" href="/brands/range-rover/">Range Rover parts {icon('arrow','ic ic--sm')}</a>
          </div>
        </div>
      </div>
    </section>"""


def build_home():
    chips = "".join(f'<a class="marquee__item" href="/brands/{b["slug"]}/" tabindex="-1">{brand_logo(b, "chip")}</a>' for b in BRANDS)
    marquee = chips + chips  # duplicated for a seamless loop
    hero = f"""<section class="hero">
      <div class="hero__bg" aria-hidden="true">
        <picture>
          <source media="(max-width: 700px)" srcset="/assets/images/site/hero-mobile.webp?v={ASSET_VER}" type="image/webp">
          <source srcset="/assets/images/site/hero-900.webp?v={ASSET_VER} 900w, /assets/images/site/hero-1600.webp?v={ASSET_VER} 1600w" sizes="100vw" type="image/webp">
          <img class="hero__photo" src="/assets/images/site/hero.jpg?v={ASSET_VER}" alt="" width="1600" height="613" fetchpriority="high" decoding="async">
        </picture>
        <span class="hero__scrim"></span><span class="hero__grid"></span><span class="hero__glow"></span>
      </div>
      <div class="container hero__inner">
        <div class="hero__content">
          <span class="hero__eyebrow"><span class="hero__eyebrow-dot"></span> Trusted Range Rover &amp; Land Rover spare parts in Sharjah</span>
          <h1 class="hero__title">Genuine &amp; OEM car parts for <span class="grad">Europe's finest</span>, in stock in Sharjah</h1>
          <p class="hero__lead">Range Rover, Land Rover, Mercedes-Benz, BMW, Audi, Porsche and more. Send your vehicle and the part on WhatsApp. We match it to your VIN, quote you honestly and deliver across the UAE.</p>
          <div class="hero__actions">
            {btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}
            <a class="btn btn--ghost-light btn--lg" href="/brands/">Shop by brand {icon('arrow','ic ic--sm')}</a>
          </div>
          <ul class="hero__chips">
            <li>{icon('check','ic ic--sm')} Genuine &amp; OEM</li>
            <li>{icon('check','ic ic--sm')} VIN-matched</li>
            <li>{icon('check','ic ic--sm')} UAE-wide delivery</li>
          </ul>
        </div>
        <div class="hero__aside">{hero_quick_form()}</div>
      </div>
      <div class="hero__marquee"><div class="marquee">{marquee}</div></div>
    </section>"""

    brands = f"""<section class="section section--brands">
      <div class="container">
        {section_header('Shop by marque', 'Parts for the cars you drive', 'Pick your brand to see what we stock, or send your VIN and we will match it for you.', center=True)}
        {brands_grid()}
      </div>
    </section>"""

    cats = f"""<section class="section section--alt">
      <div class="container">
        {section_header('Part categories', 'Whatever your car needs', 'From engines and air suspension to brakes, filters and body panels, all genuine or quality OEM.', center=True)}
        {categories_grid()}
      </div>
    </section>"""

    steps = f"""<section class="section section--dark section--steps">
      <div class="container">
        {section_header('How ordering works', 'From WhatsApp to your door in four steps', center=True, light=True)}
        {steps_order()}
        <div class="section__cta">{btn_enquiry('Start your request', cls='btn btn--wa btn--lg')}</div>
      </div>
    </section>"""

    why = f"""<section class="section">
      <div class="container">
        {section_header('Why buy from us', 'The right part, without the runaround', center=True)}
        {features_why()}
      </div>
    </section>"""

    popular = f"""<section class="section section--alt">
      <div class="container">
        {section_header('Popular searches', 'Frequently requested parts')}
        {popular_links()}
      </div>
    </section>"""

    blog = f"""<section class="section">
      <div class="container">
        {section_header('Guides', 'Parts buying &amp; fitment advice')}
        {blog_cards(3)}
        <div class="section__cta"><a class="btn btn--ghost btn--lg" href="/blog/">Read all guides {icon('arrow','ic ic--sm')}</a></div>
      </div>
    </section>"""

    coverage = f'<section class="section section--alt"><div class="container">{coverage_block()}</div></section>'

    faq = f'<section class="section"><div class="container container--narrow">{faq_block(FAQS[:6], center=True)}<div class="section__cta"><a class="btn btn--ghost btn--lg" href="/faq/">All questions {icon("arrow","ic ic--sm")}</a></div></div></section>'

    cta = cta_banner("Can't find your part?",
                     "Send us your vehicle and the part on WhatsApp. Genuine or OEM, we'll track it down and quote you.")

    body = hero + trust_strip() + brands + specialist_block() + cats + steps + why + popular + blog + coverage + faq + cta
    title = "Genuine & OEM Car Spare Parts in Sharjah | Al Jawareh"
    desc = ("Genuine & OEM spare parts for Range Rover, Land Rover, Mercedes-Benz, BMW, Audi, Porsche & more. "
            "Shop in Sharjah, delivery across the UAE. Request a part on WhatsApp.")
    ld = [store_schema(),
          {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"],
           "alternateName": "Al Jawareh", "url": SITE["base_url"] + "/", "inLanguage": "en-AE"},
          faq_schema(FAQS[:6])]
    preload = (
        f'<link rel="preload" as="image" type="image/webp" href="/assets/images/site/hero-mobile.webp?v={ASSET_VER}" media="(max-width: 700px)" fetchpriority="high">\n'
        f'<link rel="preload" as="image" type="image/webp" href="/assets/images/site/hero-1600.webp?v={ASSET_VER}" '
        f'imagesrcset="/assets/images/site/hero-900.webp?v={ASSET_VER} 900w, /assets/images/site/hero-1600.webp?v={ASSET_VER} 1600w" '
        f'imagesizes="100vw" media="(min-width: 701px)" fetchpriority="high">\n'
    )
    render_page(title, desc, "/", body, ld, active="home", og_type="website",
                priority="1.0", changefreq="weekly", preload=preload)


# ---------------------------------------------------------------------------
# PAGE: BRANDS INDEX
# ---------------------------------------------------------------------------
def build_brands_index():
    body = f"""{breadcrumbs([('Home', '/'), ('Brands', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">Brands we stock</span>
        <h1 class="pagehead__title">Spare parts for 9 premium marques</h1>
        <p class="pagehead__lead">We specialise in genuine and OEM parts for premium European and select American vehicles. Pick your marque to see the parts we supply — or just send us your VIN on WhatsApp.</p>
        <div class="pagehead__actions">{btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}</div>
      </div>
    </section>
    <section class="section"><div class="container">{brands_grid()}</div></section>
    {cta_banner('Not sure which part you need?', 'Describe the fault and your vehicle — we speak these cars fluently and will point you right.')}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Brands', '/brands/')]),
          {"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i, "name": b["name"],
                                "url": abs_url(f'/brands/{b["slug"]}/')} for i, b in enumerate(BRANDS, 1)]}]
    render_page("Car Brands We Stock Parts For | Al Jawareh Auto Spare Parts, Sharjah",
                "Genuine & OEM spare parts for Range Rover, Land Rover, Jaguar, Mercedes-Benz, BMW, Audi, Volkswagen, Porsche and GMC — supplied in Sharjah and across the UAE.",
                "/brands/", body, ld, active="brands", priority="0.9", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: PARTS INDEX
# ---------------------------------------------------------------------------
def build_parts_index():
    body = f"""{breadcrumbs([('Home', '/'), ('Parts', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">Part categories</span>
        <h1 class="pagehead__title">Every part your car needs</h1>
        <p class="pagehead__lead">From engines and air suspension to brakes, filters, electrical and body panels — all genuine or quality OEM, matched to your vehicle. Browse a category or send us the part on WhatsApp.</p>
        <div class="pagehead__actions">{btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}</div>
      </div>
    </section>
    <section class="section"><div class="container">{categories_grid()}</div></section>
    {cta_banner("Can't find the category?", "Tell us the part or the symptom on WhatsApp and we'll sort it — genuine or OEM.")}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Parts', '/parts/')]),
          {"@context": "https://schema.org", "@type": "ItemList",
           "itemListElement": [{"@type": "ListItem", "position": i, "name": c["name"],
                                "url": abs_url(f'/parts/{c["slug"]}/')} for i, c in enumerate(CATEGORIES, 1)]}]
    render_page("Car Spare Part Categories in Sharjah & UAE | Al Jawareh Auto Spare Parts",
                "Browse spare part categories — engine, suspension & air struts, brakes, filters, electrical, body panels, transmission, cooling and steering. Genuine & OEM, delivered across the UAE.",
                "/parts/", body, ld, active="parts", priority="0.9", changefreq="monthly")


# ---------------------------------------------------------------------------
# helpers for brand/category pages
# ---------------------------------------------------------------------------
def brand_faqs(b):
    n = b["name"]
    return [
        (f"Do you stock genuine {n} parts?",
         f"Yes. We supply genuine {n} parts and premium OEM-supplier equivalents. Tell us your budget "
         f"and we'll show you both so you can choose."),
        (f"Can you get a {n} part that isn't in stock?",
         f"Almost always. If it's not on the shelf, we source it through our supplier network — genuine "
         f"or OEM — and give you a realistic timeline before you commit."),
        (f"Do you deliver {n} parts across the UAE?",
         f"Yes. We're in Sharjah and deliver {n} parts to Dubai, Ajman, Abu Dhabi, Ras Al Khaimah and "
         f"beyond, often same or next day."),
        (f"How do I order a {n} part?",
         f"Send your {n} model, year and VIN or chassis number on WhatsApp with the part you need. "
         f"We'll confirm the exact part, quote you, and deliver or hold it for collection."),
    ]


def category_faqs(c):
    n = c["name"].lower()
    return [
        (f"Are your {n} genuine or OEM?",
         f"Both. We stock genuine (manufacturer) {n} and premium OEM-supplier equivalents. We'll tell "
         f"you which is which and let you choose on price and warranty."),
        (f"Can you match {n} to my exact car?",
         f"Yes — send your VIN or chassis number and we'll match the correct part for your specification, "
         f"so it fits the first time."),
        (f"Do you deliver {n} across the UAE?",
         f"Yes. From our Sharjah shop we deliver across Dubai, Ajman, Abu Dhabi and the rest of the UAE, "
         f"often same or next day."),
    ]


def related_categories_chips(brand, current=None):
    chips = "".join(
        f'<a class="chip" href="/brands/{brand["slug"]}/{c["slug"]}/">{esc(c["name"])}</a>'
        for c in CATEGORIES if c["slug"] != current
    )
    return f'<div class="chips">{chips}</div>'


def related_brands_chips(cat, current=None):
    chips = "".join(
        f'<a class="chip" href="/brands/{b["slug"]}/{cat["slug"]}/">{esc(b["name"])}</a>'
        for b in BRANDS if b["slug"] != current
    )
    return f'<div class="chips">{chips}</div>'


def items_list(items, cols=True):
    lis = "".join(f'<li>{icon("check","ic ic--sm")}<span>{esc(x)}</span></li>' for x in items)
    cls = "ticklist ticklist--cols" if cols else "ticklist"
    return f'<ul class="{cls}">{lis}</ul>'


# ---------------------------------------------------------------------------
# PAGE: BRAND
# ---------------------------------------------------------------------------
def build_brand(b):
    crumbs = [('Home', '/'), ('Brands', '/brands/'), (b["name"], None)]
    faqs = brand_faqs(b)
    models = "".join(f'<li>{esc(m)}</li>' for m in b["models"])
    body = f"""{breadcrumbs(crumbs)}
    <section class="brandhead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container brandhead__inner">
        <div class="brandhead__text">
          <span class="eyebrow">{esc(b['origin'])} &middot; Genuine &amp; OEM</span>
          <h1 class="brandhead__title">{esc(b['name'])} Spare Parts in Sharjah &amp; the UAE</h1>
          <p class="brandhead__lead">{esc(b['intro'])}</p>
          <div class="brandhead__actions">
            {btn_enquiry(f'Request a {b["name"]} part', make=b['name'], cls='btn btn--wa btn--lg')}
            <a class="btn btn--ghost btn--lg" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>{esc(SITE['phone_display'])}</span></a>
          </div>
        </div>
        <div class="brandhead__media">{media(f'/assets/images/brands/{b["slug"]}-hero.jpg', f'{b["name"]} spare parts in Sharjah', '4x3', b['name'], 'box', logo_brand=b, tag='Genuine & OEM parts')}</div>
      </div>
    </section>
    <section class="section">
      <div class="container split">
        <div class="split__main">
          {section_header('Popular parts', f'{esc(b["name"])} parts we supply most')}
          {items_list(b['popular'])}
          <p class="note">{icon('shield','ic ic--sm')} {esc(b['note'])}</p>
        </div>
        <aside class="split__aside">
          <div class="panel">
            <h3 class="panel__t">Models we cover</h3>
            <ul class="panel__list">{models}</ul>
            <p class="panel__note">Don't see your exact model? Message us — we cover more than we can list.</p>
            {btn_enquiry('Check my model', make=b['name'], cls='btn btn--wa btn--block')}
          </div>
        </aside>
      </div>
    </section>
    <section class="section section--alt">
      <div class="container">
        {section_header('By category', f'Browse {esc(b["name"])} parts by category')}
        {categories_grid(brand=b)}
      </div>
    </section>
    <section class="section"><div class="container container--narrow">{faq_block(faqs, eyebrow='FAQ', title=f'{esc(b["name"])} parts — questions')}</div></section>
    {cta_banner(f'Need a {b["name"]} part today?', f'Send your VIN and the part on WhatsApp. We stock the fast-movers and can source the rest — genuine or OEM.', make=b['name'])}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Brands', '/brands/'), (b['name'], f'/brands/{b["slug"]}/')]),
          store_schema(), faq_schema(faqs)]
    title = f'{b["name"]} Spare Parts in Sharjah & UAE | Genuine & OEM | Al Jawareh'
    desc = (f'{b["name"]} spare parts in Sharjah and across the UAE — {b["popular"][0].lower()}, '
            f'{b["popular"][1].lower()} and more. Genuine & OEM, VIN-matched. Request a part on WhatsApp.')
    render_page(title, desc, f'/brands/{b["slug"]}/', body, ld, active="brands",
                image=f'/assets/images/brands/{b["slug"]}-hero.jpg', priority="0.8", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: CATEGORY
# ---------------------------------------------------------------------------
def build_category(c):
    crumbs = [('Home', '/'), ('Parts', '/parts/'), (c["name"], None)]
    faqs = category_faqs(c)
    body = f"""{breadcrumbs(crumbs)}
    <section class="pagehead pagehead--cat"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container pagehead__cat-inner">
        <span class="pagehead__ic">{icon(c['icon'],'pagehead__icon')}</span>
        <div>
          <span class="eyebrow">Part category &middot; Genuine &amp; OEM</span>
          <h1 class="pagehead__title">{esc(c['name'])} in Sharjah &amp; the UAE</h1>
          <p class="pagehead__lead">{esc(c['intro'])}</p>
          <div class="pagehead__actions">{btn_enquiry(f'Request {c["name"].lower()}', cls='btn btn--wa btn--lg')}</div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container split">
        <div class="split__main">
          {section_header("What's included", f'{esc(c["name"])} we supply')}
          {items_list(c['items'])}
        </div>
        <aside class="split__aside">
          <div class="panel panel--accent">
            <h3 class="panel__t">{icon('vin','ic ic--sm')} Match it to your VIN</h3>
            <p>{esc(c['name'])} vary by model and year. Send your chassis number and we'll confirm the exact part before you buy.</p>
            {btn_enquiry('Send my VIN', cls='btn btn--wa btn--block')}
          </div>
        </aside>
      </div>
    </section>
    <section class="section section--alt">
      <div class="container">
        {section_header('By brand', f'{esc(c["name"])} for the marques we stock')}
        {brand_grid_for_category(c)}
      </div>
    </section>
    <section class="section"><div class="container container--narrow">{faq_block(faqs, eyebrow='FAQ', title=f'{esc(c["name"])} — questions')}</div></section>
    {cta_banner(f'Need {c["name"].lower()} for your car?', 'Send us your vehicle and the part on WhatsApp — genuine or OEM, matched to your VIN.')}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Parts', '/parts/'), (c['name'], f'/parts/{c["slug"]}/')]),
          store_schema(), faq_schema(faqs)]
    title = f'{c["name"]} in Sharjah & UAE | Genuine & OEM | Al Jawareh Auto Spare Parts'
    desc = (f'{c["name"]} for Range Rover, Mercedes-Benz, BMW, Audi, Porsche and more in Sharjah and '
            f'across the UAE. {c["card"]} Request a part on WhatsApp.')
    render_page(title, desc, f'/parts/{c["slug"]}/', body, ld, active="parts", priority="0.8", changefreq="monthly")


def brand_grid_for_category(c):
    cards = "".join(
        f'<a class="minicard" href="/brands/{b["slug"]}/{c["slug"]}/">'
        f'<span class="minicard__logo">{brand_logo(b, "mini")}</span>'
        f'<span class="minicard__name">{esc(b["name"])} {esc(c["short"].lower())}</span>'
        f'{icon("arrow","ic ic--sm")}</a>'
        for b in BRANDS
    )
    return f'<div class="grid grid--mini">{cards}</div>'


# ---------------------------------------------------------------------------
# PAGE: BRAND x CATEGORY (programmatic SEO)
# ---------------------------------------------------------------------------
def bc_intro(b, c):
    n, cn = b["name"], c["name"].lower()
    variants = [
        (f"Looking for {esc(b['name'])} {esc(cn)} in Sharjah or anywhere in the UAE? We keep genuine "
         f"and OEM {esc(cn)} for {esc(b['name'])}, matched to your exact VIN so the part fits the first time."),
        (f"{esc(b['name'])} {esc(cn)} shouldn't be a guessing game. We supply genuine and quality OEM "
         f"{esc(cn)} for {esc(b['name'])} across Sharjah, Dubai and the wider UAE — send your chassis "
         f"number and we'll confirm the right part."),
        (f"From our shop in Industrial Area 12, Sharjah, we supply {esc(b['name'])} {esc(cn)} — genuine "
         f"and OEM — with fast delivery across the UAE. Tell us your model and VIN and we'll quote you honestly."),
    ]
    idx = (len(b["slug"]) + len(c["slug"])) % len(variants)
    p1 = variants[idx]
    it = c["items"]
    p2 = (f"That covers {esc(it[0].lower())}, {esc(it[1].lower())} and {esc(it[2].lower())}, and more — "
          f"all matched to your {esc(b['name'])}'s specification. If it isn't on the shelf, we source it "
          f"through our supplier network with a realistic timeline before you commit.")
    return f'<p class="brandhead__lead">{p1}</p><p class="lead-2">{p2}</p>'


def bc_faqs(b, c):
    n, cn = b["name"], c["name"].lower()
    return [
        (f"Do you have genuine {n} {cn} in stock?",
         f"We stock the fast-moving {n} {cn} and can source the rest quickly — genuine or premium OEM. "
         f"Send your VIN and we'll confirm availability and price."),
        (f"Can you match {n} {cn} to my exact car?",
         f"Yes. {n} part numbers change between models and years, so we use your VIN or chassis number to "
         f"match the correct {cn} the first time."),
        (f"Do you deliver {n} {cn} to Dubai and across the UAE?",
         f"Yes. We're in Sharjah and deliver {n} {cn} to Dubai, Ajman, Abu Dhabi and the rest of the UAE, "
         f"often same or next day."),
    ]


def build_brand_category(b, c):
    crumbs = [('Home', '/'), ('Brands', '/brands/'), (b["name"], f'/brands/{b["slug"]}/'), (c["name"], None)]
    faqs = bc_faqs(b, c)
    models = "".join(f'<li>{esc(m)}</li>' for m in b["models"])
    body = f"""{breadcrumbs(crumbs)}
    <section class="brandhead brandhead--bc"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container brandhead__inner">
        <div class="brandhead__text">
          <span class="eyebrow">{icon(c['icon'],'ic ic--sm')} {esc(b['name'])} &middot; {esc(c['name'])}</span>
          <h1 class="brandhead__title">{esc(b['name'])} {esc(c['name'])} in Sharjah &amp; the UAE</h1>
          {bc_intro(b, c)}
          <div class="brandhead__actions">
            {btn_enquiry(f'Request {b["name"]} {c["short"].lower()}', make=b['name'], cls='btn btn--wa btn--lg')}
            <a class="btn btn--ghost btn--lg" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>Call us</span></a>
          </div>
        </div>
        <div class="brandhead__media">{media(f'/assets/images/categories/{c["slug"]}.jpg', f'{b["name"]} {c["name"]}', '4x3', f'{b["name"]} {c["short"]}', c['icon'], tag=b['name'])}</div>
      </div>
    </section>
    <section class="section">
      <div class="container split">
        <div class="split__main">
          {section_header('What we supply', f'{esc(b["name"])} {esc(c["name"].lower())} we stock &amp; source')}
          {items_list(c['items'])}
          <p class="note">{icon('shield','ic ic--sm')} Genuine and OEM options side by side — we'll tell you the difference and let you choose.</p>
        </div>
        <aside class="split__aside">
          <div class="panel panel--accent">
            <h3 class="panel__t">{icon('vin','ic ic--sm')} Send your VIN</h3>
            <p>The fastest way to the right {esc(c['name'].lower())} for your {esc(b['name'])} is your chassis number. Send it on WhatsApp and we'll confirm the exact part.</p>
            {btn_enquiry('Get a quote', make=b['name'], cls='btn btn--wa btn--block')}
          </div>
          <div class="panel">
            <h3 class="panel__t">{esc(b['name'])} models we cover</h3>
            <ul class="panel__list">{models}</ul>
          </div>
        </aside>
      </div>
    </section>
    <section class="section section--alt">
      <div class="container">
        {section_header('Keep browsing', f'Other {esc(b["name"])} parts')}
        {related_categories_chips(b, current=c['slug'])}
        <div class="crosslink">
          <h3 class="crosslink__h">{esc(c['name'])} for other brands</h3>
          {related_brands_chips(c, current=b['slug'])}
        </div>
      </div>
    </section>
    <section class="section"><div class="container container--narrow">{faq_block(faqs, eyebrow='FAQ', title=f'{esc(b["name"])} {esc(c["name"].lower())} — questions')}</div></section>
    {cta_banner(f'Need {b["name"]} {c["short"].lower()} now?', f'Send your VIN and the part on WhatsApp — genuine or OEM, delivered across the UAE.', make=b['name'])}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Brands', '/brands/'), (b['name'], f'/brands/{b["slug"]}/'),
                             (c['name'], f'/brands/{b["slug"]}/{c["slug"]}/')]),
          store_schema(), faq_schema(faqs)]
    title = f'{b["name"]} {c["name"]} in Sharjah & UAE | Genuine & OEM | Al Jawareh'
    desc = (f'{b["name"]} {c["name"].lower()} in Sharjah and across the UAE — {c["items"][0].lower()}, '
            f'{c["items"][1].lower()} and more. Genuine & OEM, VIN-matched. Request a part on WhatsApp.')
    render_page(title, desc, f'/brands/{b["slug"]}/{c["slug"]}/', body, ld, active="brands",
                image=f'/assets/images/categories/{c["slug"]}.jpg', priority="0.6", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: LOCATIONS INDEX + LOCATION
# ---------------------------------------------------------------------------
def location_card(l):
    tag = "Our shop" if l.get("is_home") else "Delivery"
    return (f'<a class="loccard" href="/locations/{l["slug"]}/">'
            f'<span class="loccard__ic">{icon("location","loccard__icon")}</span>'
            f'<span class="loccard__name">{esc(l["name"])}</span>'
            f'<span class="loccard__tag">{tag}</span>'
            f'<span class="loccard__go">Parts in {esc(l["name"])} {icon("arrow","ic ic--sm")}</span></a>')


def build_locations_index():
    body = f"""{breadcrumbs([('Home', '/'), ('Areas', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">Areas we serve</span>
        <h1 class="pagehead__title">Auto spare parts across the UAE</h1>
        <p class="pagehead__lead">We're based in Sharjah and deliver genuine &amp; OEM parts right across the Emirates. Pick your area or send us your VIN on WhatsApp.</p>
        <div class="pagehead__actions">{btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}</div>
      </div>
    </section>
    <section class="section"><div class="container"><div class="grid grid--locs">{"".join(location_card(l) for l in LOCATIONS)}</div></div></section>
    <section class="section section--alt"><div class="container">{coverage_block()}</div></section>
    {cta_banner('Anywhere in the UAE', "Tell us where you are and the part you need — we'll get it to you.")}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Areas', '/locations/')]), store_schema()]
    render_page("Auto Spare Parts Across the UAE | Sharjah, Dubai, Ajman & More | Al Jawareh",
                "Genuine & OEM auto spare parts delivered across the UAE — Sharjah, Dubai, Ajman, Abu Dhabi, Ras Al Khaimah, Umm Al Quwain, Fujairah and Al Ain. Request a part on WhatsApp.",
                "/locations/", body, ld, active="locations", priority="0.7", changefreq="monthly")


def location_faqs(l):
    n = l["name"]
    return [
        (f"Do you deliver car parts to {n}?",
         f"Yes. {l['delivery']} Send your vehicle details and the part on WhatsApp and we'll quote and dispatch."),
        (f"Can I collect my part instead of delivery to {n}?",
         f"Absolutely. You're welcome to collect from our shop in Industrial Area 12, Sharjah — often the "
         f"same day for in-stock parts."),
        (f"How do I order parts from {n}?",
         f"Message us your make, model, year and VIN with the part you need. We confirm the exact part, "
         f"quote you, and deliver to {n} or hold it for collection."),
    ]


def build_location(l):
    crumbs = [('Home', '/'), ('Areas', '/locations/'), (l["name"], None)]
    faqs = location_faqs(l)
    areas = "".join(f'<span class="tagpill">{esc(a)}</span>' for a in l["areas"])
    body = f"""{breadcrumbs(crumbs)}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">{icon('location','ic ic--sm')} {esc(l['name'])}, UAE</span>
        <h1 class="pagehead__title">Auto Spare Parts in {esc(l['name'])}</h1>
        <p class="pagehead__lead">{esc(l['intro'])}</p>
        <div class="pagehead__actions">
          {btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}
          <a class="btn btn--ghost btn--lg" href="{tel_link()}">{icon('phone','ic ic--sm')}<span>{esc(SITE['phone_display'])}</span></a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container split">
        <div class="split__main">
          <p class="prose">{esc(l['detail'])}</p>
          <h3 class="mini-h">Areas we cover in {esc(l['name'])}</h3>
          <div class="tagpills">{areas}</div>
          <p class="note">{icon('truck','ic ic--sm')} {esc(l['delivery'])}</p>
        </div>
        <aside class="split__aside">
          <div class="panel panel--accent">
            <h3 class="panel__t">Fast parts in {esc(l['name'])}</h3>
            <p>Genuine &amp; OEM parts for Range Rover, Mercedes, BMW, Audi, Porsche and more — matched to your VIN.</p>
            {btn_enquiry('Send my VIN', cls='btn btn--wa btn--block')}
          </div>
        </aside>
      </div>
    </section>
    <section class="section section--alt">
      <div class="container">
        {section_header('Brands', f'Popular marques we supply to {esc(l["name"])}')}
        {brands_grid()}
      </div>
    </section>
    <section class="section"><div class="container">{coverage_block()}</div></section>
    <section class="section section--alt"><div class="container container--narrow">{faq_block(faqs, eyebrow='FAQ', title=f'Parts in {esc(l["name"])} — questions')}</div></section>
    {cta_banner(f'Need a part in {l["name"]}?', 'Send us your vehicle and the part on WhatsApp — we deliver across the UAE.')}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Areas', '/locations/'), (l['name'], f'/locations/{l["slug"]}/')]),
          store_schema(), faq_schema(faqs)]
    title = f'Auto Spare Parts in {l["name"]} | Genuine & OEM | Al Jawareh'
    desc = (f'Genuine & OEM auto spare parts in {l["name"]}, UAE — for Range Rover, Mercedes-Benz, BMW, '
            f'Audi, Porsche and more. {l["delivery"]} Request a part on WhatsApp.')
    render_page(title, desc, f'/locations/{l["slug"]}/', body, ld, active="locations", priority="0.7", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: ABOUT
# ---------------------------------------------------------------------------
def build_about():
    stats = [("9", "premium marques"), ("UAE-wide", "delivery network"),
             ("Genuine &amp; OEM", "no mystery brands"), ("Sharjah", "walk-in shop")]
    stat_html = "".join(f'<div class="stat"><span class="stat__n">{n}</span><span class="stat__l">{l}</span></div>' for n, l in stats)
    vals = [
        ("shield", "Honesty first", "We tell you whether a part is genuine or OEM, what it costs, and what the warranty is — before you buy. No surprises."),
        ("vin", "Right the first time", "We match parts to your VIN so you don't lose days to returns and wrong-fit parts."),
        ("headset", "We know these cars", "Range Rover air suspension, BMW cooling, Mercedes AIRMATIC — we deal with them every day and we'll steer you right."),
        ("truck", "Fast across the UAE", "Based in Sharjah, delivering to Dubai, Ajman, Abu Dhabi and beyond — often same or next day."),
    ]
    val_html = "".join(f'<div class="feature"><span class="feature__ic">{icon(i,"feature__icon")}</span><h3 class="feature__t">{t}</h3><p class="feature__p">{p}</p></div>' for i, t, p in vals)
    body = f"""{breadcrumbs([('Home', '/'), ('About', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">About us</span>
        <h1 class="pagehead__title">Your parts partner in Sharjah</h1>
        <p class="pagehead__lead">Al Jawareh Auto Spare Parts supplies genuine and OEM parts for premium European and American vehicles — from a Range Rover air strut to a Mercedes service kit — with fast delivery across the UAE.</p>
      </div>
    </section>
    <section class="section"><div class="container"><div class="statband">{stat_html}</div></div></section>
    <section class="section">
      <div class="container split">
        <div class="split__main">
          {section_header('Our story', 'Built on getting the right part, fast')}
          <p class="prose">We started with a simple frustration shared by every European car owner in the UAE: finding the correct part shouldn't take a week of phone calls and a wrong-fit return. So we built a shop that does the opposite — deep stock on the parts these cars actually need, an honest choice between genuine and OEM, and a WhatsApp line where you can send your VIN and get a straight answer.</p>
          <p class="prose">Today we supply parts for Range Rover, Land Rover, Jaguar, Mercedes-Benz, BMW, Audi, Volkswagen, Porsche and GMC. Air suspension, brakes, cooling, service parts and hard-to-find components — matched to your chassis number and delivered anywhere in the Emirates.</p>
          <p class="prose">Whether you're a workshop that needs parts on a deadline or an owner fixing your own car, you get the same thing from us: the right part, a fair price, and no runaround.</p>
        </div>
        <aside class="split__aside">
          <div class="panel panel--accent">
            <h3 class="panel__t">{icon('location','ic ic--sm')} Find us</h3>
            <p>{esc(SITE['address']['line1'])}, {esc(SITE['address']['line2'])}, {esc(SITE['address']['city'])}, UAE.</p>
            <p class="panel__note">Daily 8AM–1PM &amp; 4PM–9PM &middot; closed 1–4 PM</p>
            {btn_wa_link('Message us', WA_GENERIC, cls='btn btn--wa btn--block')}
          </div>
        </aside>
      </div>
    </section>
    <section class="section section--alt"><div class="container">{section_header('What we stand for', 'How we do business', center=True)}<div class="grid grid--features">{val_html}</div></div></section>
    {cta_banner('Ready when you are', 'Send your vehicle and the part on WhatsApp — genuine or OEM, matched to your VIN and delivered across the UAE.')}"""
    ld = [breadcrumb_schema([('Home', '/'), ('About', '/about/')]), store_schema()]
    render_page("About Al Jawareh Auto Spare Parts | Sharjah Parts Specialists",
                "Al Jawareh Auto Spare Parts supplies genuine & OEM parts for Range Rover, Mercedes-Benz, BMW, Audi, Porsche and more — from our shop in Industrial Area 12, Sharjah, across the UAE.",
                "/about/", body, ld, active="about", priority="0.6", changefreq="yearly")


# ---------------------------------------------------------------------------
# shared enquiry form (inline version for the Request page)
# ---------------------------------------------------------------------------
def enquiry_form_inline():
    make_opts = "".join(f'<option value="{esc(b["name"])}">{esc(b["name"])}</option>' for b in BRANDS)
    return f"""<form class="enquiry__form enquiry__form--inline" data-enquiry-form>
      <label class="field"><span>Your name</span><input type="text" name="name" placeholder="e.g. Ahmed" autocomplete="name"></label>
      <div class="field-row">
        <label class="field"><span>Vehicle make <b>*</b></span>
          <select name="make" required><option value="" disabled selected>Select brand</option>{make_opts}<option value="Other">Other</option></select>
        </label>
        <label class="field"><span>Model</span><input type="text" name="model" placeholder="e.g. Sport / C 200"></label>
      </div>
      <div class="field-row">
        <label class="field"><span>Year</span><input type="text" name="year" inputmode="numeric" placeholder="e.g. 2019"></label>
        <label class="field"><span>VIN / chassis no.</span><input type="text" name="vin" placeholder="Helps us match exactly"></label>
      </div>
      {parts_builder()}
      <label class="field"><span>Notes (optional)</span><textarea name="notes" rows="2" placeholder="Anything else that helps"></textarea></label>
      <button type="submit" class="btn btn--wa btn--block btn--lg">{icon('whatsapp','ic ic--sm')} Send my list on WhatsApp</button>
      <p class="enquiry__fine">No account needed. Opens WhatsApp to <b>{esc(SITE['phone_display'])}</b>.</p>
    </form>
    <script type="application/json" data-parts-catalog>{parts_catalog_json()}</script>"""


# ---------------------------------------------------------------------------
# PAGE: REQUEST A PART
# ---------------------------------------------------------------------------
def build_request():
    body = f"""{breadcrumbs([('Home', '/'), ('Request a part', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">{icon('whatsapp','ic ic--sm')} WhatsApp enquiry</span>
        <h1 class="pagehead__title">Request a part / get a quote</h1>
        <p class="pagehead__lead">Fill in the details below and we'll open WhatsApp with your message ready to send. We confirm the exact part, tell you whether it's genuine or OEM, and quote you — no obligation.</p>
      </div>
    </section>
    <section class="section">
      <div class="container split split--form">
        <div class="split__main">
          <div class="formcard">{enquiry_form_inline()}</div>
        </div>
        <aside class="split__aside">
          <div class="panel">
            <h3 class="panel__t">What happens next</h3>
            <ol class="ministeps">
              <li><b>You send</b> — vehicle, VIN and the part (or the fault).</li>
              <li><b>We confirm &amp; quote</b> — exact part, genuine or OEM, clear price.</li>
              <li><b>You approve</b> — pick delivery or collection.</li>
              <li><b>Delivered</b> — anywhere in the UAE, often same or next day.</li>
            </ol>
          </div>
          <div class="panel panel--accent">
            <h3 class="panel__t">{icon('vin','ic ic--sm')} Have your VIN ready</h3>
            <p>Your chassis number is on your Mulkiya, the windscreen base, or the driver's door jamb. It's the fastest route to the right part.</p>
            <a class="linkbtn" href="/blog/find-the-right-part-using-vin-chassis-number/">How to find your VIN {icon('arrow','ic ic--sm')}</a>
          </div>
          <div class="panel">
            <h3 class="panel__t">Prefer to talk?</h3>
            <p>Call or WhatsApp us directly.</p>
            <a class="btn btn--ghost btn--block" href="{tel_link()}">{icon('phone','ic ic--sm')} {esc(SITE['phone_display'])}</a>
          </div>
        </aside>
      </div>
    </section>"""
    ld = [breadcrumb_schema([('Home', '/'), ('Request a part', '/request-a-part/')]), store_schema()]
    render_page("Request a Part / Get a Quote | Al Jawareh Auto Spare Parts",
                "Request a genuine or OEM car part in the UAE. Send your vehicle, VIN and the part you need — we confirm the exact part and quote you on WhatsApp. Delivery across the UAE.",
                "/request-a-part/", body, ld, active="", priority="0.8", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: CONTACT
# ---------------------------------------------------------------------------
def build_contact():
    a = SITE["address"]
    hours = "".join(f'<li><span>{esc(d)}</span><span>{esc(t)}</span></li>' for d, t in SITE["hours_display"])
    cards = [
        ("whatsapp", "WhatsApp", SITE["phone_display"], wa_link(WA_GENERIC), True),
        ("phone", "Call us", SITE["phone_display"], tel_link(), False),
        ("mail", "Email", SITE["email"], f'mailto:{SITE["email"]}', False),
    ]
    card_html = "".join(
        f'<a class="contactcard{" contactcard--wa" if wa else ""}" href="{href}"{" target=_blank rel=noopener" if wa else ""}>'
        f'<span class="contactcard__ic">{icon(i,"contactcard__icon")}</span>'
        f'<span class="contactcard__label">{lbl}</span>'
        f'<span class="contactcard__val">{esc(val)}</span></a>'
        for i, lbl, val, href, wa in cards
    )
    body = f"""{breadcrumbs([('Home', '/'), ('Contact', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">Contact</span>
        <h1 class="pagehead__title">Talk to us about your part</h1>
        <p class="pagehead__lead">The fastest way to reach us is WhatsApp — send your vehicle and the part and we'll take it from there. Or call, email, or drop by the shop in Sharjah.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="contactgrid">{card_html}</div>
      </div>
    </section>
    <section class="section section--alt">
      <div class="container split">
        <div class="split__main">
          <div class="contactinfo">
            <h2 class="mini-h">{icon('location','ic ic--sm')} Our shop</h2>
            <p class="prose">{esc(a['line1'])}<br>{esc(a['line2'])}<br>{esc(a['city'])}, {esc(a['country'])}</p>
            <h2 class="mini-h">{icon('clock','ic ic--sm')} Opening hours</h2>
            <ul class="footer__hours contactinfo__hours">{hours}</ul>
            <div class="contactinfo__cta">{btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}</div>
          </div>
        </div>
        <aside class="split__aside">
          <div class="mapcard">
            <iframe title="Al Jawareh Auto Spare Parts location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              src="https://maps.google.com/maps?q={quote(SITE['maps_query'])}&output=embed"></iframe>
          </div>
        </aside>
      </div>
    </section>
    {cta_banner('We reply during working hours', "Send your enquiry any time on WhatsApp — we'll get back to you as soon as we're open.")}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Contact', '/contact/')]), store_schema()]
    render_page("Contact Al Jawareh Auto Spare Parts | Sharjah | 050 149 4916",
                "Contact Al Jawareh Auto Spare Parts in Industrial Area 12, Sharjah. WhatsApp or call 050 149 4916 for genuine & OEM parts, delivered across the UAE.",
                "/contact/", body, ld, active="contact", priority="0.7", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: FAQ
# ---------------------------------------------------------------------------
def build_faq():
    body = f"""{breadcrumbs([('Home', '/'), ('FAQ', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">FAQ</span>
        <h1 class="pagehead__title">Ordering, delivery &amp; warranty</h1>
        <p class="pagehead__lead">Everything you might want to know before you send us a part request. Still stuck? Message us on WhatsApp — we're happy to help.</p>
      </div>
    </section>
    <section class="section"><div class="container container--narrow">{faq_block(FAQS, eyebrow='Questions', title='Frequently asked questions')}</div></section>
    {cta_banner('Question not answered?', 'Ask us directly on WhatsApp — real answers, no call centre.')}"""
    ld = [breadcrumb_schema([('Home', '/'), ('FAQ', '/faq/')]), faq_schema(FAQS), store_schema()]
    render_page("FAQ | Al Jawareh Auto Spare Parts | Ordering, Delivery & Warranty",
                "Answers on ordering car parts, genuine vs OEM, VIN matching, UAE delivery, warranty and payment — from Al Jawareh Auto Spare Parts, Sharjah.",
                "/faq/", body, ld, active="faq", priority="0.6", changefreq="monthly")


# ---------------------------------------------------------------------------
# PAGE: BLOG INDEX + POST
# ---------------------------------------------------------------------------
def render_blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{esc(val)}</p>")
        elif kind == "h2":
            out.append(f'<h2 class="post__h2">{esc(val)}</h2>')
        elif kind == "ul":
            lis = "".join(f'<li>{icon("check","ic ic--sm")}<span>{esc(x)}</span></li>' for x in val)
            out.append(f'<ul class="post__ul">{lis}</ul>')
    return "".join(out)


def build_blog_index():
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    body = f"""{breadcrumbs([('Home', '/'), ('Blog', None)])}
    <section class="pagehead"><span class="head__photo" aria-hidden="true" style="background-image:url(/assets/images/site/hero-900.webp?v={ASSET_VER})"></span>
      <div class="container">
        <span class="eyebrow">Guides</span>
        <h1 class="pagehead__title">Parts buying &amp; fitment guides</h1>
        <p class="pagehead__lead">Straight-talking advice on buying the right part — VIN matching, genuine vs OEM, and marque-specific fitment guides from the shop floor.</p>
      </div>
    </section>
    <section class="section"><div class="container"><div class="grid grid--posts">{"".join(blog_card(p) for p in posts)}</div></div></section>
    {cta_banner("Reading up before you buy?", "When you're ready, send us your vehicle and the part on WhatsApp for a quote.")}"""
    ld = [breadcrumb_schema([('Home', '/'), ('Blog', '/blog/')]),
          {"@context": "https://schema.org", "@type": "Blog", "name": f'{SITE["name"]} Blog',
           "url": abs_url("/blog/"),
           "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": abs_url(f'/blog/{p["slug"]}/'),
                         "datePublished": p["date"]} for p in posts]}]
    render_page("Parts Buying & Fitment Guides | Al Jawareh Auto Spare Parts Blog",
                "Guides on buying car parts in the UAE — VIN matching, genuine vs OEM vs aftermarket, Range Rover air suspension, Mercedes service parts and more.",
                "/blog/", body, ld, active="blog", priority="0.7", changefreq="weekly")


def build_post(p):
    crumbs = [('Home', '/'), ('Blog', '/blog/'), (p["title"], None)]
    related = [x for x in POSTS if x["slug"] != p["slug"]]
    related = sorted(related, key=lambda x: x["date"], reverse=True)[:3]
    rel_html = "".join(blog_card(x) for x in related)
    body = f"""{breadcrumbs(crumbs)}
    <article class="post">
      <div class="container container--narrow">
        <header class="post__head">
          <span class="post__cat">{esc(p['category'])}</span>
          <h1 class="post__title">{esc(p['title'])}</h1>
          <p class="post__meta"><span>{esc(p['read_time'])}</span> &middot; <span>Al Jawareh Auto Spare Parts</span></p>
        </header>
        {media(f'/assets/images/blog/{p["slug"]}.jpg', p['title'], '16x9', p['category'], 'layers', 'post__hero', tag=p['category'])}
        <div class="post__body">{render_blocks(p['body'])}</div>
        <div class="post__cta">
          <h3>Need this part for your car?</h3>
          <p>Send us your vehicle and VIN on WhatsApp — genuine or OEM, matched and quoted.</p>
          {btn_enquiry('Request a Part', cls='btn btn--wa btn--lg')}
        </div>
      </div>
    </article>
    <section class="section section--alt">
      <div class="container">
        {section_header('Keep reading', 'More guides')}
        <div class="grid grid--posts">{rel_html}</div>
      </div>
    </section>"""
    ld = [breadcrumb_schema([('Home', '/'), ('Blog', '/blog/'), (p['title'], f'/blog/{p["slug"]}/')]),
          article_schema(p)]
    title = f'{p["title"]} | Al Jawareh Auto Spare Parts'
    render_page(title, p["excerpt"], f'/blog/{p["slug"]}/', body, ld, active="blog", og_type="article",
                image=f'/assets/images/blog/{p["slug"]}.jpg', priority="0.6", changefreq="yearly",
                lastmod=p["date"])


# ---------------------------------------------------------------------------
# PAGE: 404 (written raw, not in sitemap)
# ---------------------------------------------------------------------------
def build_404():
    body = """<section class="notfound">
      <div class="container">
        <span class="notfound__code">404</span>
        <h1 class="notfound__title">This part isn't here</h1>
        <p class="notfound__lead">The page you're after has moved or never existed. Let's get you back on track.</p>
        <div class="notfound__actions">
          <a class="btn btn--wa btn--lg" href="/">Back to home</a>
          <a class="btn btn--ghost btn--lg" href="/brands/">Browse brands</a>
          <a class="btn btn--ghost btn--lg" href="/parts/">Browse parts</a>
        </div>
      </div>
    </section>"""
    doc = (render_head("Page not found | Al Jawareh Auto Spare Parts",
                       "The page you're looking for could not be found.", "/404.html", [], "website")
           + nav("") + f'<main id="main">{body}</main>' + footer() + whatsapp_widget()
           + '<script src="/assets/js/main.js?v=' + ASSET_VER + '" defer></script>\n</body>\n</html>\n')
    with open(os.path.join(DIST, "404.html"), "w", encoding="utf-8") as f:
        f.write(doc)


# ---------------------------------------------------------------------------
# ASSETS, SEO FILES, SITE IMAGES
# ---------------------------------------------------------------------------
def copy_assets():
    """Write CSS/JS/images from the embedded theme module, so the repo needs
    only the .py files. Any real photos placed under ./assets/images are copied
    on top (optional)."""
    import base64
    a = os.path.join(DIST, "assets")
    css_dir = os.path.join(a, "css")
    js_dir = os.path.join(a, "js")
    img_dir = os.path.join(a, "images")
    site_dir = os.path.join(img_dir, "site")
    for d in [css_dir, js_dir, site_dir,
              os.path.join(img_dir, "brands"),
              os.path.join(img_dir, "categories"),
              os.path.join(img_dir, "blog")]:
        os.makedirs(d, exist_ok=True)
    with open(os.path.join(css_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(theme.STYLE_CSS)
    with open(os.path.join(js_dir, "main.js"), "w", encoding="utf-8") as f:
        f.write(theme.MAIN_JS)
    with open(os.path.join(site_dir, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(theme.FAVICON_SVG)
    for name, b64 in theme.SITE_IMAGES_B64.items():
        with open(os.path.join(site_dir, name), "wb") as f:
            f.write(base64.b64decode(b64))
    with open(os.path.join(DIST, "favicon.ico"), "wb") as f:
        f.write(base64.b64decode(theme.FAVICON_ICO_B64))
    for slug, b64 in getattr(theme, "BRAND_LOGOS_B64", {}).items():
        with open(os.path.join(img_dir, "brands", f"{slug}-logo.png"), "wb") as f:
            f.write(base64.b64decode(b64))
    # optional: copy real photos the user has added under ./assets/images/
    local_img = os.path.join(ASSETS_SRC, "images")
    if os.path.isdir(local_img):
        for root, _dirs, files in os.walk(local_img):
            rel = os.path.relpath(root, local_img)
            dest = img_dir if rel == "." else os.path.join(img_dir, rel)
            os.makedirs(dest, exist_ok=True)
            for fn in files:
                if fn == "favicon.svg":
                    continue
                shutil.copy2(os.path.join(root, fn), os.path.join(dest, fn))
    # extra photos embedded later (categories/blog/brands heroes), keyed by path under images/
    for rel, b64 in getattr(theme, "EXTRA_IMAGES_B64", {}).items():
        dest = os.path.join(img_dir, *rel.split("/"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(base64.b64decode(b64))
    # self-hosted fonts (faster than Google Fonts: no third-party round trip)
    fonts = getattr(theme, "FONTS_B64", {})
    if fonts:
        font_dir = os.path.join(a, "fonts")
        os.makedirs(font_dir, exist_ok=True)
        for name, b64 in fonts.items():
            with open(os.path.join(font_dir, name), "wb") as f:
                f.write(base64.b64decode(b64))
    # register every image that now exists, so pages only reference real files
    AVAILABLE_IMAGES.clear()
    for root, _dirs, files in os.walk(img_dir):
        for fn in files:
            full = os.path.join(root, fn)
            AVAILABLE_IMAGES.add("/" + os.path.relpath(full, DIST).replace(os.sep, "/"))


def build_llms():
    """llms.txt — a plain summary that AI search assistants can read."""
    a = SITE["address"]
    lines = [
        f"# {SITE['name']}",
        "",
        f"> Genuine and OEM auto spare parts shop in {a['line2']}, {a['city']}, UAE. "
        "Specialists in Range Rover and Land Rover, also Jaguar, Mercedes-Benz, BMW, Audi, "
        "Volkswagen, Porsche and GMC. Delivery across the UAE. Orders and quotes via WhatsApp.",
        "",
        f"- Phone / WhatsApp: {SITE['phone_display']} ({SITE['phone_intl']})",
        f"- Address: {a['line1']}, {a['line2']}, {a['city']}, UAE",
        "- Hours: Saturday to Thursday 8:00 AM to 1:00 PM and 4:00 PM to 9:00 PM; closed Friday",
        "",
        "## Brands",
    ]
    lines += [f"- [{br['name']} spare parts]({abs_url('/brands/' + br['slug'] + '/')})" for br in BRANDS]
    lines += ["", "## Part categories"]
    lines += [f"- [{c['name']}]({abs_url('/parts/' + c['slug'] + '/')}): {c['card']}" for c in CATEGORIES]
    lines += ["", "## Areas served"]
    lines += [f"- [{l['name']}]({abs_url('/locations/' + l['slug'] + '/')})" for l in LOCATIONS]
    lines += ["", "## Key pages",
              f"- [Request a part]({abs_url('/request-a-part/')})",
              f"- [FAQ]({abs_url('/faq/')})",
              f"- [Contact]({abs_url('/contact/')})", ""]
    with open(os.path.join(DIST, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def build_sitemap():
    urls = "".join(
        f"  <url><loc>{esc(p['loc'])}</loc><lastmod>{p['lastmod']}</lastmod>"
        f"<changefreq>{p['changefreq']}</changefreq><priority>{p['priority']}</priority></url>\n"
        for p in PAGES
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}</urlset>\n")
    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def build_robots():
    txt = (f"User-agent: *\n"
           f"Allow: /\n"
           f"Disallow: /404.html\n\n"
           f"Sitemap: {SITE['base_url']}/sitemap.xml\n")
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


def build_htaccess():
    txt = r"""# ============================================================================
# Al Jawareh Auto Spare Parts — .htaccess
# Generated by build.py. Edit build.py (build_htaccess) to change.
# ============================================================================

Options -Indexes
DirectoryIndex index.html
ServerSignature Off

<IfModule mod_rewrite.c>
    RewriteEngine On

    # Force HTTPS + www (canonical host) in a single 301
    RewriteCond %{HTTPS} off [OR]
    RewriteCond %{HTTP_HOST} !^www\. [NC]
    RewriteCond %{HTTP_HOST} ^(?:www\.)?(.+)$ [NC]
    RewriteRule ^ https://www.%1%{REQUEST_URI} [L,R=301]
</IfModule>

# Custom error page
ErrorDocument 404 /404.html

# ---------------------------------------------------------------------------
# Compression
# ---------------------------------------------------------------------------
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css
    AddOutputFilterByType DEFLATE application/javascript application/x-javascript text/javascript
    AddOutputFilterByType DEFLATE application/json application/xml application/rss+xml
    AddOutputFilterByType DEFLATE image/svg+xml application/xhtml+xml
    AddOutputFilterByType DEFLATE font/ttf font/otf font/woff font/woff2 application/vnd.ms-fontobject
</IfModule>

# ---------------------------------------------------------------------------
# Browser caching
# ---------------------------------------------------------------------------
<IfModule mod_expires.c>
    ExpiresActive On
    # Never cache HTML so content updates go live immediately
    ExpiresByType text/html "access plus 0 seconds"
    ExpiresByType application/xml "access plus 0 seconds"
    ExpiresByType text/xml "access plus 0 seconds"
    # Long cache for static, fingerprint-safe assets
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType text/javascript "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType image/x-icon "access plus 1 year"
    ExpiresByType font/woff2 "access plus 1 year"
    ExpiresByType font/woff "access plus 1 year"
    ExpiresByType font/ttf "access plus 1 year"
</IfModule>

<IfModule mod_headers.c>
    # Cache policy
    <FilesMatch "\.(css|js|jpg|jpeg|png|webp|gif|svg|ico|woff2|woff|ttf)$">
        Header set Cache-Control "public, max-age=31536000, immutable"
    </FilesMatch>
    <FilesMatch "\.(html|xml)$">
        Header set Cache-Control "no-cache, must-revalidate"
    </FilesMatch>

    # Security headers
    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains" env=HTTPS
    Header unset X-Powered-By
    Header unset Server
</IfModule>

# ---------------------------------------------------------------------------
# Correct MIME types
# ---------------------------------------------------------------------------
<IfModule mod_mime.c>
    AddType image/svg+xml .svg
    AddType application/font-woff2 .woff2
    AddType image/x-icon .ico
</IfModule>

# Protect dotfiles (except .well-known)
<FilesMatch "^\.(?!well-known)">
    Require all denied
</FilesMatch>
"""
    with open(os.path.join(DIST, ".htaccess"), "w", encoding="utf-8") as f:
        f.write(txt)


def _find_ttf(bold=False):
    names = (["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf"])
    roots = ["/usr/share/fonts", "/usr/local/share/fonts",
             os.path.join(os.path.dirname(__file__), "assets", "fonts")]
    for r in roots:
        for dp, _, fs in os.walk(r) if os.path.isdir(r) else []:
            for want in names:
                if want in fs:
                    return os.path.join(dp, want)
    return None


def generate_site_images():
    """Generate favicon.ico, apple-touch-icon.png and og-default.jpg if Pillow is available.
    The site works fine without them (favicon.svg is shipped as a vector fallback)."""
    site_dir = os.path.join(DIST, "assets", "images", "site")
    os.makedirs(site_dir, exist_ok=True)
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        print("  (Pillow not available — skipping raster favicon/OG; favicon.svg still shipped)")
        return

    GRAPHITE = (18, 22, 29)
    AMBER = (245, 166, 35)
    WHITE = (246, 247, 249)

    def font(sz, bold=True):
        p = _find_ttf(bold)
        try:
            return ImageFont.truetype(p, sz) if p else ImageFont.load_default()
        except Exception:
            return ImageFont.load_default()

    # favicon.ico + png (rounded amber tile with "AJ")
    def mark(size):
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        r = int(size * 0.22)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=GRAPHITE)
        d.rounded_rectangle([int(size*0.06), int(size*0.06), int(size*0.94), int(size*0.94)],
                            radius=int(r*0.8), outline=AMBER, width=max(2, int(size*0.05)))
        f = font(int(size * 0.5))
        t = "AJ"
        try:
            bb = d.textbbox((0, 0), t, font=f)
            tw, th = bb[2]-bb[0], bb[3]-bb[1]
            d.text(((size-tw)/2 - bb[0], (size-th)/2 - bb[1]), t, font=f, fill=AMBER)
        except Exception:
            d.text((size*0.25, size*0.25), t, fill=AMBER)
        return img

    try:
        ico = mark(64)
        ico.save(os.path.join(DIST, "favicon.ico"),
                 sizes=[(16, 16), (32, 32), (48, 48)])
        mark(180).convert("RGB").save(os.path.join(site_dir, "apple-touch-icon.png"))
        mark(512).save(os.path.join(site_dir, "logo.png"))
    except Exception as e:
        print(f"  (favicon generation skipped: {e})")

    # OG default 1200x630
    try:
        W, H = 1200, 630
        og = Image.new("RGB", (W, H), GRAPHITE)
        d = ImageDraw.Draw(og)
        for i in range(H):  # subtle vertical gradient
            k = i / H
            d.line([(0, i), (W, i)], fill=(int(18+8*k), int(22+8*k), int(29+10*k)))
        d.rectangle([0, 0, 16, H], fill=AMBER)
        d.text((80, 150), "AL JAWAREH", font=font(96), fill=WHITE)
        d.text((84, 262), "AUTO SPARE PARTS", font=font(44), fill=AMBER)
        d.text((84, 360), "Genuine & OEM parts for premium European", font=font(34), fill=(200, 205, 213))
        d.text((84, 404), "& American vehicles — Sharjah, UAE", font=font(34), fill=(200, 205, 213))
        d.text((84, 512), "WhatsApp  050 149 4916", font=font(36), fill=WHITE)
        og.save(os.path.join(site_dir, "og-default.jpg"), quality=88)
    except Exception as e:
        print(f"  (OG image generation skipped: {e})")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    copy_assets()

    build_home()
    build_brands_index()
    build_parts_index()
    for b in BRANDS:
        build_brand(b)
    for c in CATEGORIES:
        build_category(c)
    for b in BRANDS:
        for c in CATEGORIES:
            build_brand_category(b, c)
    build_locations_index()
    for l in LOCATIONS:
        build_location(l)
    build_about()
    build_contact()
    build_faq()
    build_request()
    build_blog_index()
    for p in POSTS:
        build_post(p)
    build_404()

    build_sitemap()
    build_robots()
    build_llms()
    build_htaccess()

    n_bc = len(BRANDS) * len(CATEGORIES)
    print("=" * 60)
    print(f"  Built {len(PAGES)} URLs into dist/")
    print("-" * 60)
    print(f"  Home ............................ 1")
    print(f"  Brand pages ..................... {len(BRANDS)}")
    print(f"  Category pages .................. {len(CATEGORIES)}")
    print(f"  Brand x Category pages .......... {n_bc}")
    print(f"  Location pages .................. {len(LOCATIONS)}")
    print(f"  Blog (index + posts) ............ {1 + len(POSTS)}")
    print(f"  Core (brands/parts/locations idx, about, contact, faq, request) .. 7")
    print(f"  + 404.html, sitemap.xml, robots.txt, .htaccess")
    print("=" * 60)


if __name__ == "__main__":
    main()

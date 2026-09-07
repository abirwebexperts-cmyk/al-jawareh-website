# -*- coding: utf-8 -*-
"""
Embedded site assets for Al Jawareh Auto Spare Parts.

The whole website builds from a few Python files (build.py, data.py, theme.py),
so nothing but these needs to live in the repo — no assets/ folder to upload.
build.py writes these out into dist/assets/ on every build.

Editing:
  - STYLE_CSS  -> the site's design/CSS. Edit freely.
  - MAIN_JS    -> menus + WhatsApp enquiry logic. Edit freely.
  - the *_B64 blobs are binary images (favicon, icons, share image); don't hand-edit.
"""

STYLE_CSS = r"""/* ==========================================================================
   Al Jawareh Auto Spare Parts — style.css
   Industrial-premium: graphite + amber + silver. Sora / Inter.
   ========================================================================== */

:root{
  /* palette */
  --ink:#0b0e13;
  --graphite:#12161d;
  --graphite-2:#161b23;
  --charcoal:#1a1f27;
  --charcoal-2:#222a35;
  --surface:#ffffff;
  --surface-2:#f5f6f8;
  --surface-3:#eceef2;
  --line:#e3e6ec;
  --line-2:#d5d9e1;
  --line-dark:rgba(255,255,255,.10);
  --line-dark-2:rgba(255,255,255,.16);

  --amber:#f5a623;
  --amber-600:#e2900f;
  --amber-700:#c67c08;
  --amber-soft:rgba(245,166,35,.14);
  --amber-glow:rgba(245,166,35,.35);

  --silver:#c3c9d2;
  --silver-2:#9aa2af;

  --ink-2:#1a2030;      /* headings on light */
  --body:#4c5563;       /* body text on light */
  --muted:#6b7480;
  --white:#ffffff;
  --on-dark:#e7eaf0;
  --on-dark-muted:#9aa3b2;

  --wa:#25d366;
  --wa-600:#1ebe5d;

  /* radii */
  --r-xs:8px; --r-sm:10px; --r:14px; --r-lg:20px; --r-xl:26px; --pill:999px;

  /* shadow */
  --sh-sm:0 1px 2px rgba(11,14,19,.06), 0 1px 3px rgba(11,14,19,.05);
  --sh:0 4px 14px rgba(11,14,19,.08), 0 2px 6px rgba(11,14,19,.05);
  --sh-lg:0 18px 44px rgba(11,14,19,.16), 0 6px 16px rgba(11,14,19,.08);
  --sh-amber:0 14px 34px rgba(245,166,35,.28);
  --sh-wa:0 12px 30px rgba(37,211,102,.30);

  /* type */
  --f-head:'Sora',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  --f-body:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;

  --wrap:1200px;
  --gutter:clamp(16px,4vw,28px);
  --header-h:72px;
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{
  margin:0;font-family:var(--f-body);color:var(--body);background:var(--surface);
  font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
  overflow-x:hidden;
}
img,svg,iframe{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit}
ul,ol{margin:0;padding:0;list-style:none}
h1,h2,h3,h4{font-family:var(--f-head);color:var(--ink-2);margin:0;line-height:1.15;letter-spacing:-.02em;font-weight:700}
p{margin:0}
:focus-visible{outline:3px solid var(--amber);outline-offset:2px;border-radius:4px}

.skip-link{position:absolute;left:-999px;top:0;z-index:200;background:var(--graphite);color:#fff;padding:.7rem 1rem;border-radius:0 0 var(--r-sm) 0}
.skip-link:focus{left:0}

/* ---------- layout ---------- */
.container{width:100%;max-width:var(--wrap);margin-inline:auto;padding-inline:var(--gutter)}
.container--narrow{max-width:820px}
.section{padding:clamp(52px,7vw,92px) 0}
.section--alt{background:var(--surface-2)}
.section--dark{background:var(--graphite);color:var(--on-dark)}
.section--dark h2{color:#fff}
.section__cta{display:flex;justify-content:center;margin-top:clamp(28px,4vw,44px)}

.eyebrow{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--f-head);font-weight:700;
  font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--amber-700)}
.section--dark .eyebrow,.sec-head--light .eyebrow{color:var(--amber)}

.sec-head{margin-bottom:clamp(28px,4vw,48px);max-width:720px}
.sec-head--center{margin-inline:auto;text-align:center}
.sec-head__title{font-size:clamp(1.6rem,3.4vw,2.5rem);margin-top:.5rem;font-weight:800}
.sec-head__sub{margin-top:.85rem;color:var(--muted);font-size:1.05rem}
.sec-head--light .sec-head__sub{color:var(--on-dark-muted)}

/* ---------- icons ---------- */
.ic{display:inline-flex;flex:none}
.ic svg{width:22px;height:22px}
.ic--sm svg{width:18px;height:18px}
.ic--xs svg{width:14px;height:14px}

/* ---------- buttons ---------- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;
  font-family:var(--f-head);font-weight:700;font-size:.95rem;letter-spacing:.01em;
  padding:.8rem 1.4rem;border-radius:var(--pill);transition:transform .18s ease,box-shadow .2s ease,background .2s ease,color .2s ease,border-color .2s ease;
  white-space:nowrap;border:1.5px solid transparent}
.btn:hover{transform:translateY(-2px)}
.btn:active{transform:translateY(0)}
.btn--sm{padding:.55rem 1rem;font-size:.86rem}
.btn--lg{padding:.95rem 1.7rem;font-size:1.02rem}
.btn--block{width:100%}
.btn--wa{background:var(--wa);color:#08130b;box-shadow:var(--sh-wa)}
.btn--wa:hover{background:var(--wa-600)}
.btn--ghost{background:transparent;border-color:var(--line-2);color:var(--ink-2)}
.btn--ghost:hover{border-color:var(--ink-2);background:var(--surface-2)}
.btn--ghost-light{background:rgba(255,255,255,.06);border-color:var(--line-dark-2);color:#fff}
.btn--ghost-light:hover{background:rgba(255,255,255,.12)}
.linkbtn{display:inline-flex;align-items:center;gap:.4rem;font-family:var(--f-head);font-weight:700;
  color:var(--amber-700);font-size:.9rem}
.linkbtn:hover{color:var(--amber-600);text-decoration:underline}

/* ==========================================================================
   HEADER / NAV
   ========================================================================== */
.site-header{position:sticky;top:0;z-index:100}
.topbar{background:var(--ink);color:var(--on-dark-muted);font-size:.82rem;border-bottom:1px solid rgba(255,255,255,.06)}
.topbar__inner{display:flex;align-items:center;gap:1.4rem;height:38px}
.topbar__item{display:inline-flex;align-items:center;gap:.45rem}
.topbar__item svg{color:var(--amber)}
.topbar__spacer{flex:1}
.topbar__link:hover{color:#fff}

.nav{background:rgba(18,22,29,.96);backdrop-filter:blur(10px);border-bottom:1px solid var(--line-dark);
  transition:box-shadow .25s ease,background .25s ease}
.site-header.is-stuck .nav{box-shadow:0 10px 30px rgba(0,0,0,.28)}
.nav__inner{display:flex;align-items:center;gap:1.2rem;height:var(--header-h)}

.brand{display:inline-flex;align-items:center;gap:.65rem;flex:none}
.brand__mark{width:40px;height:40px;border-radius:11px;display:grid;place-items:center;
  background:var(--graphite);border:2px solid var(--amber);color:var(--amber);
  font-family:var(--f-head);font-weight:800;font-size:1.05rem;letter-spacing:.02em}
.brand__text{display:flex;flex-direction:column;line-height:1}
.brand__name{font-family:var(--f-head);font-weight:800;color:#fff;font-size:1.12rem;letter-spacing:.04em}
.brand__tag{font-size:.6rem;letter-spacing:.28em;color:var(--amber);font-weight:600;margin-top:3px}

.nav__links{display:flex;align-items:center;gap:.2rem;margin-left:.6rem}
.nav__link{display:inline-flex;align-items:center;gap:.3rem;color:var(--on-dark);font-family:var(--f-head);
  font-weight:600;font-size:.92rem;padding:.6rem .8rem;border-radius:var(--r-sm);transition:color .18s,background .18s}
.nav__link:hover,.nav__link.is-active{color:#fff;background:rgba(255,255,255,.06)}
.nav__link .ic svg{color:var(--on-dark-muted);transition:transform .2s}
.nav__group{position:relative}
.nav__group:hover .nav__toggle .ic svg,.nav__toggle[aria-expanded="true"] .ic svg{transform:rotate(180deg)}

/* dropdown / mega */
.mega,.dd{position:absolute;top:calc(100% + 10px);left:0;background:var(--surface);color:var(--body);
  border:1px solid var(--line);border-radius:var(--r-lg);box-shadow:var(--sh-lg);padding:1rem;
  opacity:0;visibility:hidden;transform:translateY(8px);transition:opacity .2s,transform .2s,visibility .2s;z-index:120}
.nav__group:hover .mega,.nav__group:hover .dd,
.nav__group.is-open .mega,.nav__group.is-open .dd{opacity:1;visibility:visible;transform:translateY(0)}
.mega{width:min(640px,86vw)}
.mega--brands{width:min(560px,86vw)}
.mega__grid{display:grid;grid-template-columns:1fr 1fr;gap:.25rem}
.mega__grid--icon{grid-template-columns:1fr 1fr}
.mega__item{display:flex;flex-direction:column;padding:.6rem .7rem;border-radius:var(--r-sm);transition:background .16s}
.mega__item:hover{background:var(--surface-2)}
.mega__item--icon{flex-direction:row;align-items:center;gap:.7rem}
.mega__ic{width:38px;height:38px;border-radius:10px;background:var(--amber-soft);color:var(--amber-700);
  display:grid;place-items:center;flex:none}
.mega__ic svg{width:20px;height:20px}
.mega__name{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:.95rem}
.mega__sub{font-size:.78rem;color:var(--muted)}
.mega__all{display:inline-flex;align-items:center;gap:.45rem;margin-top:.6rem;padding:.6rem .7rem;
  font-family:var(--f-head);font-weight:700;color:var(--amber-700);border-top:1px solid var(--line)}
.mega__all:hover{color:var(--amber-600)}
.dd{width:220px;padding:.5rem}
.dd__item{display:block;padding:.55rem .7rem;border-radius:var(--r-sm);font-weight:600;color:var(--ink-2);font-size:.9rem}
.dd__item:hover{background:var(--surface-2);color:var(--amber-700)}

.nav__cta{display:flex;align-items:center;gap:.6rem;margin-left:auto}
.nav__call{color:#fff}
.nav__burger{display:none;width:44px;height:44px;border-radius:var(--r-sm);color:#fff;align-items:center;justify-content:center;border:1px solid var(--line-dark-2)}
.nav__burger:hover{background:rgba(255,255,255,.08)}

/* mobile off-canvas */
.mobile{position:fixed;inset:0;z-index:150}
.mobile[hidden]{display:none}
.mobile__scrim{position:absolute;inset:0;background:rgba(6,8,12,.55);backdrop-filter:blur(2px);animation:fade .2s ease}
.mobile__panel{position:absolute;top:0;right:0;height:100%;width:min(360px,90vw);background:var(--surface);
  display:flex;flex-direction:column;box-shadow:var(--sh-lg);animation:slideIn .25s ease}
.mobile__head{display:flex;align-items:center;justify-content:space-between;padding:1rem 1.2rem;border-bottom:1px solid var(--line);background:var(--graphite)}
.mobile__head .brand__name{color:#fff}
.mobile__close{width:42px;height:42px;color:#fff;display:grid;place-items:center;border-radius:var(--r-sm)}
.mobile__close:hover{background:rgba(255,255,255,.1)}
.mobile__body{flex:1;overflow-y:auto;padding:.6rem}
.mobile__link{display:block;padding:.85rem 1rem;font-family:var(--f-head);font-weight:600;color:var(--ink-2);border-radius:var(--r-sm)}
.mobile__link:hover{background:var(--surface-2)}
.mobile__acc summary{display:flex;align-items:center;justify-content:space-between;padding:.85rem 1rem;
  font-family:var(--f-head);font-weight:600;color:var(--ink-2);border-radius:var(--r-sm);list-style:none;cursor:pointer}
.mobile__acc summary::-webkit-details-marker{display:none}
.mobile__acc summary svg{transition:transform .2s;color:var(--muted)}
.mobile__acc[open] summary svg{transform:rotate(180deg)}
.mobile__sub{display:flex;flex-direction:column;padding:.2rem .4rem .6rem 1rem}
.mobile__sub a{padding:.55rem .7rem;color:var(--body);font-size:.92rem;border-radius:var(--r-sm)}
.mobile__sub a:hover{background:var(--surface-2);color:var(--amber-700)}
.mobile__foot{padding:1rem 1.2rem;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:.6rem}

@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes slideIn{from{transform:translateX(100%)}to{transform:translateX(0)}}

/* ---------- breadcrumbs ---------- */
.crumbs{background:var(--surface-2);border-bottom:1px solid var(--line);font-size:.82rem}
.crumbs .container{display:flex;align-items:center;flex-wrap:wrap;gap:.35rem;padding-block:.7rem}
.crumbs a{color:var(--muted);font-weight:600}
.crumbs a:hover{color:var(--amber-700)}
.crumbs span[aria-current]{color:var(--ink-2);font-weight:700}
.crumbs__sep{display:inline-flex;color:var(--line-2)}
.crumbs__sep svg{width:13px;height:13px;transform:rotate(-90deg)}

/* ==========================================================================
   HERO
   ========================================================================== */
.hero{position:relative;background:var(--graphite);color:var(--on-dark);overflow:hidden;isolation:isolate}
.hero__bg{position:absolute;inset:0;z-index:-1}
.hero__grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);
  background-size:48px 48px;
  mask-image:radial-gradient(120% 90% at 78% 8%,#000 0%,transparent 68%);
  -webkit-mask-image:radial-gradient(120% 90% at 78% 8%,#000 0%,transparent 68%)}
.hero__glow{position:absolute;top:-18%;right:-8%;width:min(720px,72vw);height:min(720px,72vw);
  background:radial-gradient(circle,var(--amber-glow) 0%,rgba(245,166,35,.10) 34%,transparent 66%);
  filter:blur(6px)}
.hero::after{content:"";position:absolute;inset-inline:0;bottom:0;height:1px;background:var(--line-dark)}
.hero__inner{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(28px,4vw,56px);align-items:center;
  padding-block:clamp(56px,8vw,104px)}
.hero__eyebrow{display:inline-flex;align-items:center;gap:.5rem;background:rgba(245,166,35,.12);
  border:1px solid rgba(245,166,35,.28);color:var(--amber);padding:.4rem .9rem;border-radius:var(--pill);
  font-family:var(--f-head);font-weight:600;font-size:.76rem;letter-spacing:.08em}
.hero__eyebrow svg{color:var(--amber)}
.hero__title{font-size:clamp(2.1rem,5.2vw,3.7rem);font-weight:800;color:#fff;margin-top:1.1rem;letter-spacing:-.025em}
.grad{background:linear-gradient(100deg,var(--amber) 10%,#ffce6e 55%,var(--amber-600) 90%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.hero__lead{margin-top:1.15rem;color:var(--on-dark-muted);font-size:clamp(1.02rem,1.6vw,1.18rem);max-width:36em}
.hero__actions{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.8rem}
.hero__chips{display:flex;flex-wrap:wrap;gap:.5rem 1.3rem;margin-top:1.8rem}
.hero__chips li{display:inline-flex;align-items:center;gap:.5rem;font-size:.9rem;color:var(--on-dark);font-weight:500}
.hero__chips svg{color:var(--amber)}

.hero__marquee{position:relative;border-top:1px solid var(--line-dark);padding:.9rem 0;overflow:hidden;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.marquee{display:flex;gap:3rem;width:max-content;animation:scroll 34s linear infinite}
.marquee__item{font-family:var(--f-head);font-weight:700;font-size:1.05rem;letter-spacing:.14em;
  text-transform:uppercase;color:rgba(255,255,255,.28);white-space:nowrap}
@keyframes scroll{to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.marquee{animation:none}}

/* hero quick form */
.hero__aside{width:100%}
.quickform{background:rgba(255,255,255,.04);border:1px solid var(--line-dark-2);border-radius:var(--r-lg);
  padding:1.4rem;box-shadow:var(--sh-lg);backdrop-filter:blur(6px)}
.quickform__title{display:flex;align-items:center;gap:.5rem;font-family:var(--f-head);font-weight:700;
  color:#fff;font-size:1rem;margin-bottom:1rem}
.quickform__title svg{color:var(--amber)}
.quickform__fields{display:flex;flex-direction:column;gap:.7rem;margin-bottom:1rem}
.quickform input,.quickform select{width:100%;background:rgba(255,255,255,.06);border:1px solid var(--line-dark-2);
  color:#fff;border-radius:var(--r-sm);padding:.78rem .9rem;font:inherit;font-size:.92rem;transition:border-color .18s,background .18s}
.quickform input::placeholder{color:var(--on-dark-muted)}
.quickform select{color:#fff}
.quickform select option{color:#111}
.quickform input:focus,.quickform select:focus{outline:none;border-color:var(--amber);background:rgba(255,255,255,.1)}
.quickform__hint{display:block;margin-top:.8rem;font-size:.8rem;color:var(--on-dark-muted);text-align:center}
.quickform__hint .linkbtn{color:var(--amber);font-size:.8rem}

/* ==========================================================================
   GRIDS
   ========================================================================== */
.grid{display:grid;gap:clamp(14px,1.6vw,22px)}
.grid--brands{grid-template-columns:repeat(auto-fill,minmax(180px,1fr))}
.grid--cats{grid-template-columns:repeat(auto-fill,minmax(310px,1fr))}
.grid--features{grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.grid--posts{grid-template-columns:repeat(auto-fill,minmax(320px,1fr))}
.grid--mini{grid-template-columns:repeat(auto-fill,minmax(250px,1fr))}
.grid--locs{grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}

/* monogram tile */
.mono{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;flex:none;
  background:linear-gradient(150deg,var(--charcoal),var(--graphite));color:var(--amber);
  border:1px solid var(--line-dark-2);font-family:var(--f-head);font-weight:800;font-size:1.05rem;letter-spacing:.02em}

/* brand card */
.bcard{position:relative;display:flex;flex-direction:column;gap:.15rem;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--r-lg);padding:1.3rem;transition:transform .2s,box-shadow .2s,border-color .2s;overflow:hidden}
.bcard::before{content:"";position:absolute;inset:0 0 auto 0;height:3px;background:linear-gradient(90deg,var(--amber),transparent);opacity:0;transition:opacity .2s}
.bcard:hover{transform:translateY(-4px);box-shadow:var(--sh-lg);border-color:var(--line-2)}
.bcard:hover::before{opacity:1}
.bcard__logo{margin-bottom:.7rem}
.bcard__name{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:1.12rem}
.bcard__sub{font-size:.82rem;color:var(--muted)}
.bcard__go{display:inline-flex;align-items:center;gap:.4rem;margin-top:.9rem;font-family:var(--f-head);
  font-weight:700;font-size:.85rem;color:var(--amber-700)}
.bcard__go svg{transition:transform .2s}
.bcard:hover .bcard__go svg{transform:translateX(4px)}

/* category card */
.ccard{position:relative;display:flex;align-items:center;gap:1rem;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--r-lg);padding:1.2rem 1.3rem;transition:transform .2s,box-shadow .2s,border-color .2s}
.ccard:hover{transform:translateY(-4px);box-shadow:var(--sh-lg);border-color:var(--line-2)}
.ccard__ic{width:52px;height:52px;border-radius:14px;background:var(--amber-soft);color:var(--amber-700);
  display:grid;place-items:center;flex:none;transition:background .2s,color .2s}
.ccard__ic svg{width:26px;height:26px}
.ccard:hover .ccard__ic{background:var(--amber);color:#1a1305}
.ccard__body{flex:1;min-width:0}
.ccard__name{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:1.05rem}
.ccard__desc{font-size:.85rem;color:var(--muted);margin-top:.2rem}
.ccard__go{color:var(--line-2);flex:none;transition:transform .2s,color .2s}
.ccard:hover .ccard__go{color:var(--amber-700);transform:translateX(3px)}

/* feature */
.feature{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:1.6rem}
.section--dark .feature,.section--alt .feature{background:var(--surface)}
.feature__ic{width:54px;height:54px;border-radius:14px;background:var(--graphite);color:var(--amber);
  display:grid;place-items:center;margin-bottom:1.1rem}
.feature__ic svg{width:26px;height:26px}
.feature__t{font-size:1.12rem;font-weight:700}
.feature__p{margin-top:.55rem;color:var(--muted);font-size:.94rem}

/* steps */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(16px,2vw,26px);counter-reset:s}
.step{position:relative;background:rgba(255,255,255,.04);border:1px solid var(--line-dark-2);
  border-radius:var(--r-lg);padding:1.5rem 1.3rem}
.step__num{position:absolute;top:-16px;left:1.3rem;width:34px;height:34px;border-radius:10px;
  background:var(--amber);color:#1a1305;display:grid;place-items:center;font-family:var(--f-head);font-weight:800}
.step__ic{color:var(--amber);margin:.6rem 0 .8rem}
.step__ic svg{width:26px;height:26px}
.step__t{color:#fff;font-size:1.05rem;font-weight:700}
.step__p{color:var(--on-dark-muted);font-size:.9rem;margin-top:.5rem}

/* faq */
.faqs__list{display:flex;flex-direction:column;gap:.7rem}
.faq{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:border-color .2s,box-shadow .2s}
.faq[open]{border-color:var(--line-2);box-shadow:var(--sh)}
.faq__q{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:1.1rem 1.3rem;
  font-family:var(--f-head);font-weight:700;color:var(--ink-2);cursor:pointer;list-style:none;font-size:1.02rem}
.faq__q::-webkit-details-marker{display:none}
.faq__chev{color:var(--amber-700);transition:transform .25s;flex:none}
.faq[open] .faq__chev{transform:rotate(180deg)}
.faq__a{padding:0 1.3rem 1.2rem;color:var(--body);font-size:.96rem}
.faq__a p{max-width:64ch}

/* popular tags */
.poptags{display:flex;flex-wrap:wrap;gap:.6rem}
.poptag{display:inline-flex;align-items:center;gap:.35rem;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--pill);padding:.55rem 1rem;font-size:.86rem;color:var(--body);transition:all .18s;font-weight:500}
.poptag b{color:var(--amber-700);font-weight:700}
.poptag:hover{border-color:var(--amber);background:var(--amber-soft);transform:translateY(-2px)}

/* coverage */
.coverage{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,52px);align-items:center}
.coverage__text p{color:var(--muted);max-width:40ch}
.coverage__map{border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--sh-lg);border:1px solid var(--line);aspect-ratio:4/3}
.coverage__map iframe{width:100%;height:100%;border:0;filter:grayscale(.15)}

/* post card */
.pcard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;transition:transform .2s,box-shadow .2s,border-color .2s}
.pcard:hover{transform:translateY(-4px);box-shadow:var(--sh-lg);border-color:var(--line-2)}
.pcard__link{display:flex;flex-direction:column;height:100%}
.pcard__media{border-radius:0}
.pcard__body{display:flex;flex-direction:column;padding:1.2rem 1.3rem 1.4rem;flex:1}
.pcard__cat{align-self:flex-start;background:var(--amber-soft);color:var(--amber-700);font-family:var(--f-head);
  font-weight:700;font-size:.72rem;letter-spacing:.04em;text-transform:uppercase;padding:.3rem .7rem;border-radius:var(--pill);margin-bottom:.8rem}
.pcard__title{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:1.12rem;line-height:1.3}
.pcard__excerpt{margin-top:.55rem;color:var(--muted);font-size:.9rem;flex:1}
.pcard__meta{display:flex;align-items:center;gap:.5rem;margin-top:1rem;font-family:var(--f-head);font-weight:700;
  font-size:.82rem;color:var(--amber-700)}
.pcard:hover .pcard__meta svg{transform:translateX(4px)}
.pcard__meta svg{transition:transform .2s}

/* ==========================================================================
   MEDIA + GRACEFUL PLACEHOLDER
   ========================================================================== */
.media{position:relative;overflow:hidden;border-radius:var(--r-lg);background:var(--charcoal)}
.media--4x3{aspect-ratio:4/3}
.media--16x9{aspect-ratio:16/9}
.media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .6s ease}
.ph.is-loaded img{opacity:1}
.ph.is-fallback img{display:none}
.ph__fill{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.55rem;
  background:linear-gradient(140deg,#1b212b 0%,#252d39 60%,#1b212b 100%);color:var(--silver-2);transition:opacity .4s}
.ph__fill::after{content:"";position:absolute;top:-40%;left:-30%;width:60%;height:180%;transform:rotate(20deg);
  background:linear-gradient(90deg,transparent,rgba(245,166,35,.06),transparent)}
.ph.is-loaded .ph__fill{opacity:0;visibility:hidden}
.ph__icon{color:var(--amber)}
.ph__icon svg{width:40px;height:40px}
.ph__label{font-family:var(--f-head);font-weight:700;color:var(--silver);font-size:.98rem;text-align:center;padding:0 1rem}
.ph__hint{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--silver-2);opacity:.7}

/* logo upload slot (brand page header) */
.logoslot{position:relative;display:inline-flex;align-items:center;justify-content:center}
.logoslot img{max-height:100%;max-width:100%;object-fit:contain;opacity:0;transition:opacity .4s}
.logoslot.is-loaded img{opacity:1;position:static}
.logoslot.is-fallback img{display:none}
.logoslot__text{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  font-family:var(--f-head);font-weight:800;color:var(--ink-2);white-space:nowrap;letter-spacing:.01em}
.logoslot.is-loaded .logoslot__text{opacity:0}
.logoslot--sm{height:26px;min-width:96px}.logoslot--sm .logoslot__text{font-size:.98rem}
.logoslot--md{height:34px;min-width:130px}.logoslot--md .logoslot__text{font-size:1.2rem}
.logoslot--lg{height:60px;min-width:210px;justify-content:flex-start}
.logoslot--lg .logoslot__text{justify-content:flex-start;font-size:1.9rem}

/* ==========================================================================
   CTA BANNER
   ========================================================================== */
.cta{background:var(--graphite);color:#fff;position:relative;overflow:hidden}
.cta__inner{position:relative;display:flex;align-items:center;justify-content:space-between;gap:2rem;
  padding:clamp(38px,5vw,62px) 0;flex-wrap:wrap}
.cta__glow{position:absolute;top:50%;left:30%;transform:translate(-50%,-50%);width:560px;height:560px;
  background:radial-gradient(circle,var(--amber-glow),transparent 66%);opacity:.5;pointer-events:none}
.cta__text{position:relative;max-width:52ch}
.cta__title{font-size:clamp(1.5rem,3vw,2.15rem);color:#fff;font-weight:800}
.cta__p{color:var(--on-dark-muted);margin-top:.6rem}
.cta__actions{position:relative;display:flex;gap:.8rem;flex-wrap:wrap}

/* ==========================================================================
   FOOTER
   ========================================================================== */
.footer{background:var(--ink);color:var(--on-dark-muted);padding-top:clamp(48px,6vw,74px)}
.footer__grid{display:grid;grid-template-columns:1.7fr 1fr 1fr 1.25fr 1fr;gap:clamp(24px,3vw,40px);padding-bottom:2.6rem}
.brand--footer .brand__mark{border-color:var(--amber)}
.footer__blurb{margin-top:1.1rem;font-size:.9rem;max-width:34ch;line-height:1.7}
.footer__contact{display:flex;flex-direction:column;gap:.6rem;margin-top:1.3rem;font-size:.9rem}
.footer__contact a,.footer__contact span{display:inline-flex;align-items:center;gap:.6rem}
.footer__contact svg{color:var(--amber);flex:none}
.footer__contact a:hover{color:#fff}
.footer__h{font-family:var(--f-head);color:#fff;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;margin-bottom:1.1rem;font-weight:700}
.footer__h--mt{margin-top:1.7rem}
.footer__list{display:flex;flex-direction:column;gap:.55rem;font-size:.9rem}
.footer__list a{color:var(--on-dark-muted)}
.footer__list a:hover{color:var(--amber)}
.footer__hours{display:flex;flex-direction:column;gap:.45rem;font-size:.88rem}
.footer__hours li{display:flex;justify-content:space-between;gap:1rem;border-bottom:1px dashed rgba(255,255,255,.08);padding-bottom:.45rem}
.footer__socials{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.3rem}
.soc{border:1px solid var(--line-dark-2);border-radius:var(--pill);padding:.4rem .9rem;font-size:.8rem;font-weight:600;color:var(--on-dark-muted)}
.soc:hover{border-color:var(--amber);color:var(--amber)}
.footer__bar{border-top:1px solid rgba(255,255,255,.08)}
.footer__bar-inner{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;padding:1.5rem 0;font-size:.8rem}
.footer__bar-inner p{color:var(--silver-2)}
.footer__note{max-width:56ch;opacity:.75}
.footer__top{display:inline-flex;align-items:center;gap:.4rem;border:1px solid var(--line-dark-2);border-radius:var(--pill);padding:.45rem .95rem;color:#fff;font-family:var(--f-head);font-weight:700;font-size:.8rem}
.footer__top svg{width:16px;height:16px;transform:rotate(180deg)}
.footer__top:hover{border-color:var(--amber);color:var(--amber)}

/* ==========================================================================
   WHATSAPP FLOATING BUTTON + ENQUIRY DRAWER
   ========================================================================== */
.wa-fab{position:fixed;right:20px;bottom:20px;z-index:90;display:inline-flex;align-items:center;gap:.6rem;
  background:var(--wa);color:#08130b;border-radius:var(--pill);padding:.85rem 1.25rem;box-shadow:var(--sh-wa);
  font-family:var(--f-head);font-weight:700;transition:transform .2s,box-shadow .2s}
.wa-fab::before{content:"";position:absolute;inset:0;border-radius:inherit;box-shadow:0 0 0 0 var(--wa);
  animation:pulse 2.6s ease-out infinite;z-index:-1}
.wa-fab:hover{transform:translateY(-3px) scale(1.02)}
.wa-fab__icon svg{width:26px;height:26px}
.wa-fab__label{font-size:.92rem}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(37,211,102,.5)}70%{box-shadow:0 0 0 16px rgba(37,211,102,0)}100%{box-shadow:0 0 0 0 rgba(37,211,102,0)}}
@media (prefers-reduced-motion:reduce){.wa-fab::before{animation:none}}

.enquiry{position:fixed;inset:0;z-index:160}
.enquiry[hidden]{display:none}
.enquiry__scrim{position:absolute;inset:0;background:rgba(6,8,12,.6);backdrop-filter:blur(3px);animation:fade .2s ease}
.enquiry__panel{position:absolute;top:0;right:0;height:100%;width:min(460px,94vw);background:var(--surface);
  display:flex;flex-direction:column;box-shadow:var(--sh-lg);animation:slideIn .28s ease;overflow-y:auto}
.enquiry__head{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem;padding:1.4rem 1.5rem 1rem}
.enquiry__eyebrow{display:inline-flex;align-items:center;gap:.4rem;color:var(--wa-600);font-family:var(--f-head);font-weight:700;font-size:.75rem;letter-spacing:.08em;text-transform:uppercase}
.enquiry__eyebrow svg{color:var(--wa)}
.enquiry__title{font-size:1.35rem;margin-top:.45rem}
.enquiry__close{width:42px;height:42px;border-radius:var(--r-sm);display:grid;place-items:center;color:var(--muted);flex:none}
.enquiry__close:hover{background:var(--surface-2);color:var(--ink-2)}
.enquiry__intro{padding:0 1.5rem;color:var(--muted);font-size:.9rem}
.enquiry__form{padding:1.2rem 1.5rem 1.7rem;display:flex;flex-direction:column;gap:.85rem}
.enquiry__form--inline{padding:0}
.enquiry__fine{font-size:.78rem;color:var(--muted);text-align:center}
.enquiry__fine b{color:var(--ink-2)}

/* shared form fields */
.field{display:flex;flex-direction:column;gap:.35rem}
.field>span{font-family:var(--f-head);font-weight:600;font-size:.82rem;color:var(--ink-2)}
.field b{color:var(--amber-700)}
.field input,.field select,.field textarea{width:100%;border:1px solid var(--line-2);border-radius:var(--r-sm);
  padding:.72rem .85rem;font:inherit;font-size:.92rem;background:var(--surface);color:var(--ink-2);transition:border-color .18s,box-shadow .18s}
.field textarea{resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--amber);box-shadow:0 0 0 3px var(--amber-soft)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:.85rem}

/* ==========================================================================
   PAGE HEADERS
   ========================================================================== */
.pagehead{background:var(--graphite);color:var(--on-dark);padding:clamp(44px,6vw,78px) 0;position:relative;overflow:hidden}
.pagehead::before{content:"";position:absolute;top:-32%;right:-6%;width:520px;height:520px;
  background:radial-gradient(circle,var(--amber-glow),transparent 66%);opacity:.55;pointer-events:none}
.pagehead .eyebrow{color:var(--amber)}
.pagehead__title{font-size:clamp(1.9rem,4.4vw,3rem);color:#fff;margin-top:.6rem;font-weight:800;position:relative}
.pagehead__lead{margin-top:1rem;color:var(--on-dark-muted);max-width:62ch;font-size:1.08rem;position:relative}
.pagehead__actions{margin-top:1.7rem;display:flex;gap:.8rem;flex-wrap:wrap;position:relative}
.pagehead--cat .pagehead__cat-inner{display:flex;align-items:flex-start;gap:1.5rem;position:relative}
.pagehead__ic{width:74px;height:74px;border-radius:18px;background:rgba(245,166,35,.14);border:1px solid rgba(245,166,35,.3);
  color:var(--amber);display:grid;place-items:center;flex:none}
.pagehead__ic svg{width:36px;height:36px}

.brandhead{background:var(--graphite);color:var(--on-dark);padding:clamp(40px,6vw,72px) 0;position:relative;overflow:hidden}
.brandhead::before{content:"";position:absolute;top:-30%;right:-4%;width:560px;height:560px;
  background:radial-gradient(circle,var(--amber-glow),transparent 66%);opacity:.5;pointer-events:none}
.brandhead__inner{display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(28px,4vw,52px);align-items:center;position:relative}
.brandhead .eyebrow{color:var(--amber)}
.brandhead__logo{margin-bottom:1.1rem}
.brandhead .logoslot__text{color:#fff}
.brandhead__title{font-size:clamp(1.8rem,4vw,2.8rem);color:#fff;margin-top:.5rem;font-weight:800}
.brandhead__lead{margin-top:1rem;color:var(--on-dark-muted);font-size:1.06rem;max-width:54ch}
.lead-2{margin-top:.9rem;color:var(--silver-2);font-size:.98rem;max-width:58ch}
.brandhead__actions{margin-top:1.7rem;display:flex;gap:.8rem;flex-wrap:wrap}

/* ==========================================================================
   SPLIT / PANEL / LISTS
   ========================================================================== */
.split{display:grid;grid-template-columns:1.6fr 1fr;gap:clamp(28px,4vw,52px);align-items:start}
.split--form{grid-template-columns:1.3fr .9fr}
.split__aside{display:flex;flex-direction:column;gap:1.2rem;position:sticky;top:calc(var(--header-h) + 16px)}

.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:1.5rem;box-shadow:var(--sh-sm)}
.panel--accent{background:var(--graphite);color:var(--on-dark);border-color:transparent}
.panel--accent .panel__t{color:#fff}
.panel--accent p{color:var(--on-dark-muted)}
.panel__t{display:flex;align-items:center;gap:.5rem;font-size:1.12rem;font-weight:700;margin-bottom:.85rem}
.panel__t svg{color:var(--amber)}
.panel__list{display:flex;flex-direction:column;gap:.5rem;margin:.4rem 0 1rem}
.panel__list li{padding-left:1.1rem;position:relative;font-size:.92rem;color:var(--body)}
.panel--accent .panel__list li{color:var(--on-dark)}
.panel__list li::before{content:"";position:absolute;left:0;top:.62em;width:6px;height:6px;border-radius:2px;background:var(--amber)}
.panel__note{font-size:.85rem;color:var(--muted);margin-bottom:1rem}
.panel--accent .panel__note{color:var(--on-dark-muted)}

.ticklist{display:flex;flex-direction:column;gap:.7rem}
.ticklist--cols{display:grid;grid-template-columns:1fr 1fr;gap:.7rem 1.4rem}
.ticklist li{display:flex;align-items:flex-start;gap:.6rem;color:var(--body);font-size:.96rem}
.ticklist svg{color:var(--wa-600);margin-top:.18rem;flex:none}

.note{display:flex;align-items:flex-start;gap:.6rem;margin-top:1.4rem;padding:.95rem 1.1rem;background:var(--amber-soft);
  border:1px solid rgba(245,166,35,.28);border-radius:var(--r);color:var(--ink-2);font-size:.9rem}
.note svg{color:var(--amber-700);margin-top:.1rem;flex:none}

.chips{display:flex;flex-wrap:wrap;gap:.55rem}
.chip{display:inline-flex;align-items:center;background:var(--surface);border:1px solid var(--line);border-radius:var(--pill);
  padding:.5rem 1rem;font-size:.86rem;font-weight:600;color:var(--body);transition:all .18s}
.chip:hover{border-color:var(--amber);color:var(--amber-700);background:var(--amber-soft)}
.crosslink{margin-top:1.7rem}
.crosslink__h{font-size:1rem;margin-bottom:.8rem;color:var(--ink-2)}

.minicard{display:flex;align-items:center;gap:.8rem;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r);padding:.9rem 1.1rem;transition:all .18s;color:var(--ink-2)}
.minicard:hover{border-color:var(--line-2);box-shadow:var(--sh);transform:translateY(-2px)}
.minicard__logo .mono{width:38px;height:38px;font-size:.88rem;border-radius:10px}
.minicard__name{flex:1;font-family:var(--f-head);font-weight:600;font-size:.92rem}
.minicard>svg,.minicard .ic svg{color:var(--amber-700);flex:none}

.statband{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.stat{background:var(--surface);padding:1.7rem 1.2rem;text-align:center}
.stat__n{display:block;font-family:var(--f-head);font-weight:800;font-size:clamp(1.3rem,2.4vw,1.9rem);color:var(--ink-2)}
.stat__l{display:block;margin-top:.35rem;font-size:.85rem;color:var(--muted)}

.prose{color:var(--body);font-size:1.02rem;margin-bottom:1.1rem;max-width:68ch}
.prose:last-child{margin-bottom:0}

/* locations */
.loccard{position:relative;display:flex;flex-direction:column;gap:.15rem;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r-lg);padding:1.3rem;transition:all .2s}
.loccard:hover{transform:translateY(-4px);box-shadow:var(--sh-lg);border-color:var(--line-2)}
.loccard__ic{width:46px;height:46px;border-radius:12px;background:var(--amber-soft);color:var(--amber-700);display:grid;place-items:center;margin-bottom:.7rem}
.loccard__ic svg{width:24px;height:24px}
.loccard__name{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:1.15rem}
.loccard__tag{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--amber-700);font-weight:700}
.loccard__go{display:inline-flex;align-items:center;gap:.4rem;margin-top:.9rem;font-family:var(--f-head);font-weight:700;font-size:.85rem;color:var(--body)}
.loccard:hover .loccard__go{color:var(--amber-700)}
.loccard__go svg{transition:transform .2s}
.loccard:hover .loccard__go svg{transform:translateX(4px)}

.mini-h{display:flex;align-items:center;gap:.5rem;font-size:1.06rem;margin:1.7rem 0 .8rem;color:var(--ink-2)}
.mini-h:first-child{margin-top:0}
.mini-h svg{color:var(--amber-700)}
.tagpills,.areachips{display:flex;flex-wrap:wrap;gap:.5rem}
.tagpill{background:var(--surface-3);border-radius:var(--pill);padding:.42rem .95rem;font-size:.84rem;color:var(--body);font-weight:500}
.areachip{background:var(--surface);border:1px solid var(--line);border-radius:var(--pill);padding:.5rem 1rem;font-size:.85rem;font-weight:600;color:var(--body);transition:all .18s}
.areachip:hover{border-color:var(--amber);color:var(--amber-700);background:var(--amber-soft)}

/* request + contact */
.formcard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-xl);padding:clamp(1.3rem,3vw,2rem);box-shadow:var(--sh)}
.ministeps{display:flex;flex-direction:column;gap:.75rem;counter-reset:m}
.ministeps li{position:relative;padding-left:2.1rem;font-size:.92rem;color:var(--body)}
.ministeps li b{color:var(--ink-2)}
.ministeps li::before{counter-increment:m;content:counter(m);position:absolute;left:0;top:.05rem;width:24px;height:24px;border-radius:7px;background:var(--amber);color:#1a1305;font-family:var(--f-head);font-weight:800;font-size:.78rem;display:grid;place-items:center}

.contactgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(14px,2vw,20px)}
.contactcard{display:flex;flex-direction:column;align-items:flex-start;gap:.15rem;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:1.4rem;transition:all .2s}
.contactcard:hover{transform:translateY(-4px);box-shadow:var(--sh-lg)}
.contactcard--wa{background:var(--graphite);border-color:transparent;color:#fff}
.contactcard__ic{width:48px;height:48px;border-radius:12px;background:var(--amber-soft);color:var(--amber-700);display:grid;place-items:center;margin-bottom:.7rem}
.contactcard--wa .contactcard__ic{background:rgba(37,211,102,.16);color:var(--wa)}
.contactcard__ic svg{width:24px;height:24px}
.contactcard__label{font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:600}
.contactcard--wa .contactcard__label{color:var(--on-dark-muted)}
.contactcard__val{font-family:var(--f-head);font-weight:700;color:var(--ink-2);font-size:1.05rem}
.contactcard--wa .contactcard__val{color:#fff}
.contactinfo__hours{margin:.6rem 0 1.5rem}
.contactinfo__hours li{color:var(--body);border-bottom:1px dashed var(--line)}
.contactinfo__cta{margin-top:.5rem}
.mapcard{border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--sh-lg);border:1px solid var(--line);aspect-ratio:3/4;min-height:340px}
.mapcard iframe{width:100%;height:100%;border:0}

/* ==========================================================================
   BLOG POST
   ========================================================================== */
.post{padding:clamp(36px,5vw,64px) 0}
.post__head{text-align:center;margin-bottom:1.8rem}
.post__cat{display:inline-block;background:var(--amber-soft);color:var(--amber-700);font-family:var(--f-head);font-weight:700;font-size:.74rem;letter-spacing:.06em;text-transform:uppercase;padding:.35rem .9rem;border-radius:var(--pill)}
.post__title{font-size:clamp(1.7rem,3.6vw,2.6rem);margin-top:1rem;font-weight:800}
.post__meta{margin-top:.8rem;color:var(--muted);font-size:.9rem}
.post__hero{margin-bottom:2rem;border-radius:var(--r-xl)}
.post__body{font-size:1.06rem;color:var(--body);line-height:1.8}
.post__body>p{margin:0 auto 1.2rem;max-width:70ch}
.post__h2{font-size:clamp(1.3rem,2.6vw,1.7rem);margin:2.1rem auto 1rem;max-width:70ch;color:var(--ink-2)}
.post__ul{display:flex;flex-direction:column;gap:.6rem;margin:0 auto 1.4rem;max-width:70ch}
.post__ul li{display:flex;align-items:flex-start;gap:.6rem}
.post__ul svg{color:var(--wa-600);margin-top:.28em;flex:none}
.post__cta{margin-top:2.4rem;padding:clamp(1.4rem,3vw,2rem);background:var(--surface-2);border:1px solid var(--line);border-radius:var(--r-xl);text-align:center;max-width:70ch;margin-inline:auto}
.post__cta h3{font-size:1.3rem}
.post__cta p{color:var(--muted);margin:.6rem 0 1.2rem}

/* 404 */
.notfound{min-height:58vh;display:grid;place-items:center;text-align:center;background:var(--graphite);color:var(--on-dark);padding:4rem 0}
.notfound__code{font-family:var(--f-head);font-weight:800;font-size:clamp(4rem,14vw,9rem);line-height:1;color:transparent;
  background:linear-gradient(100deg,var(--amber),#ffce6e);-webkit-background-clip:text;background-clip:text}
.notfound__title{font-size:clamp(1.6rem,3vw,2.2rem);color:#fff;margin-top:.5rem}
.notfound__lead{margin-top:.8rem;color:var(--on-dark-muted)}
.notfound__actions{margin-top:1.8rem;display:flex;gap:.8rem;flex-wrap:wrap;justify-content:center}

/* ==========================================================================
   RESPONSIVE
   ========================================================================== */
@media (max-width:1024px){
  .hero__inner,.brandhead__inner,.coverage{grid-template-columns:1fr}
  .hero__aside{max-width:520px}
  .split,.split--form{grid-template-columns:1fr}
  .split__aside{position:static}
  .steps{grid-template-columns:repeat(2,1fr);gap:26px 20px}
  .step__num{top:-14px}
}
@media (max-width:980px){
  .nav__links,.nav__call{display:none}
  .nav__burger{display:flex}
  .statband{grid-template-columns:repeat(2,1fr)}
  .contactgrid{grid-template-columns:1fr 1fr}
}
@media (max-width:760px){
  :root{--header-h:64px}
  .topbar__item:first-child{display:none}
  .field-row{grid-template-columns:1fr}
  .ticklist--cols{grid-template-columns:1fr}
  .contactgrid{grid-template-columns:1fr}
  .pagehead--cat .pagehead__cat-inner{flex-direction:column;gap:1rem}
  .cta__inner{flex-direction:column;align-items:flex-start}
  .footer__grid{grid-template-columns:1fr 1fr}
  .steps{grid-template-columns:1fr}
  .mapcard{aspect-ratio:4/3;min-height:280px}
}
@media (max-width:560px){
  .footer__grid{grid-template-columns:1fr}
  .statband{grid-template-columns:1fr 1fr}
  .btn{padding:.78rem 1.15rem}
  .wa-fab__label{display:none}
  .wa-fab{padding:.95rem;border-radius:50%}
  .cta__actions,.hero__actions,.pagehead__actions,.brandhead__actions,.notfound__actions{width:100%}
  .cta__actions .btn,.hero__actions .btn,.brandhead__actions .btn{flex:1 1 auto}
}
"""

MAIN_JS = r"""/* ==========================================================================
   Al Jawareh Auto Spare Parts — main.js
   Vanilla JS. No libraries, no storage. Progressive enhancement.
   ========================================================================== */
(function () {
  "use strict";

  var WA_NUMBER = "971501494916";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- sticky header shadow ---------- */
  var header = $("[data-header]");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-stuck", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- body scroll lock ---------- */
  var lockCount = 0;
  function lockScroll(on) {
    lockCount = Math.max(0, lockCount + (on ? 1 : -1));
    document.body.style.overflow = lockCount > 0 ? "hidden" : "";
  }

  /* ---------- mobile menu ---------- */
  var mobile = $("[data-mobile]");
  function openMenu() {
    if (!mobile) return;
    mobile.hidden = false;
    lockScroll(true);
    var b = $(".nav__burger");
    if (b) b.setAttribute("aria-expanded", "true");
  }
  function closeMenu() {
    if (!mobile || mobile.hidden) return;
    mobile.hidden = true;
    lockScroll(false);
    var b = $(".nav__burger");
    if (b) b.setAttribute("aria-expanded", "false");
  }
  $$("[data-menu-open]").forEach(function (el) { el.addEventListener("click", openMenu); });
  $$("[data-menu-close]").forEach(function (el) { el.addEventListener("click", closeMenu); });
  // close the mobile menu when a real link inside it is tapped
  if (mobile) {
    $$("a", mobile).forEach(function (a) { a.addEventListener("click", closeMenu); });
  }

  /* ---------- desktop dropdown / mega (touch + keyboard) ---------- */
  $$(".nav__group").forEach(function (group) {
    var toggle = $(".nav__toggle", group);
    if (!toggle) return;
    toggle.addEventListener("click", function (e) {
      e.preventDefault();
      var open = group.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      // close siblings
      $$(".nav__group").forEach(function (g) {
        if (g !== group) { g.classList.remove("is-open"); var t = $(".nav__toggle", g); if (t) t.setAttribute("aria-expanded", "false"); }
      });
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".nav__group")) {
      $$(".nav__group.is-open").forEach(function (g) {
        g.classList.remove("is-open"); var t = $(".nav__toggle", g); if (t) t.setAttribute("aria-expanded", "false");
      });
    }
  });

  /* ---------- enquiry drawer ---------- */
  var enquiry = $("[data-enquiry]");
  var lastFocused = null;
  function openEnquiry(make) {
    if (!enquiry) return;
    enquiry.hidden = false;
    lockScroll(true);
    lastFocused = document.activeElement;
    // preselect make if provided
    if (make) {
      var sel = $('select[name="make"]', enquiry);
      if (sel) {
        var found = false;
        $$("option", sel).forEach(function (o) { if (o.value === make) found = true; });
        sel.value = found ? make : "Other";
      }
    }
    var first = $("input, select, textarea", enquiry);
    if (first) setTimeout(function () { first.focus(); }, 60);
  }
  function closeEnquiry() {
    if (!enquiry || enquiry.hidden) return;
    enquiry.hidden = true;
    lockScroll(false);
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }
  $$("[data-enquiry-open]").forEach(function (el) {
    el.addEventListener("click", function () {
      closeMenu();
      openEnquiry(el.getAttribute("data-make") || "");
    });
  });
  $$("[data-enquiry-close]").forEach(function (el) { el.addEventListener("click", closeEnquiry); });

  /* ---------- esc closes overlays ---------- */
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { closeEnquiry(); closeMenu(); }
  });

  /* ---------- WhatsApp message builder ---------- */
  function val(form, name) {
    var f = form.querySelector('[name="' + name + '"]');
    return f && f.value ? f.value.trim() : "";
  }
  function buildMessage(form) {
    var name = val(form, "name");
    var make = val(form, "make");
    var model = val(form, "model");
    var year = val(form, "year");
    var vin = val(form, "vin");
    var part = val(form, "part");
    var notes = val(form, "notes");

    var vehicle = [make, model, year].filter(Boolean).join(" ");
    var lines = ["Hello Al Jawareh Auto Spare Parts,", "", "I'd like to enquire about a spare part."];
    if (name) lines.push("Name: " + name);
    if (vehicle) lines.push("Vehicle: " + vehicle);
    if (vin) lines.push("VIN / Chassis: " + vin);
    if (part) lines.push("Part needed: " + part);
    if (notes) lines.push("Notes: " + notes);
    return lines.join("\n");
  }
  function submitToWhatsApp(form) {
    if (form.reportValidity && !form.reportValidity()) return;
    var text = buildMessage(form);
    var url = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text);
    window.open(url, "_blank", "noopener");
    closeEnquiry();
  }
  $$("[data-enquiry-form], [data-quick-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      submitToWhatsApp(form);
    });
  });

  /* ---------- back to top ---------- */
  $$("[data-scroll-top]").forEach(function (el) {
    el.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  /* ---------- footer year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });

  /* ---------- smooth in-page anchors ---------- */
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var target = document.getElementById(id.slice(1));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: "smooth", block: "start" }); }
    });
  });
})();
"""

FAVICON_SVG = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Al Jawareh">
  <rect width="64" height="64" rx="14" fill="#12161d"/>
  <rect x="5" y="5" width="54" height="54" rx="11" fill="none" stroke="#f5a623" stroke-width="3"/>
  <text x="32" y="43" text-anchor="middle" font-family="'Segoe UI', Arial, sans-serif" font-weight="800" font-size="30" fill="#f5a623">AJ</text>
</svg>
"""

# --- binary assets (base64) -------------------------------------------------
FAVICON_ICO_B64 = (
"AAABAAMAEBAAAAAAIABpAgAANgAAACAgAAAAACAASQUAAJ8CAAAwMAAAAAAgAF8IAADoBwAAiVBORw0KGgoAAAANSUhEUgAAABAA"
"AAAQCAYAAAAf8/9hAAACMElEQVR4nKWTP0jVURTHP+fe+0wDdbGMDB/PHlEI/fGJoUNDCmLRIFGBS20REU4NjTYF1pDQ0NjgnFAE"
"0VaDQ/kiQlqEl4KDoZj45733+/3uPQ0/fZXWEB24cJfz/XfOESMQtO1CodOMd+fMidgDIPy5NGPhQyl8mZkNd40svhJoGxo+516M"
"DlpbLAX1AZG/tCtgBe3KGXn82vvnb5NLrtBpJ0YHnb3+NPLzS2qxgEhNgqqmHxFEQGOVbKv4Zzfr7MKKTrhCTvLFktf5JbWHWwQf"
"oJpAFIOz0FAnKFCJUpzGZmF+SW2x5LWQk7yJE1LZDoLC6hYMnTS8Gctwe8CyVoatKjwacTy45lgrg3GCD0icoE4k9awqOx651W/p"
"6zC07xcmpz2Lq9CXF6oJJCHNQiR1ZXYCEkmZzmSFrqxw5WGMkVSNryhbEWxU947nN4ByBMPdBudSpnKkXO0xIGC23+6qAQSvHGyC"
"y92GhRXlzoDh+xb0HTMcbzdsVlOS3eUAjAGqcPaooaVZuDge8+5z4Mgh4f1YHT0dQuyV+kya0x4FGoB98PFr4NS9iNlF5UCLsFmF"
"3vsR/Z2G86cNLz+Fmt2aAlU0KCIG1isQ+3T+YZtqowILy8qNJwlTxUBjPSyvK6qgirqMQ6xBNUHqM2nzzvJZl+7v2JTHGWhqgIwF"
"TcAaNOMQN1PSuZFel8+2+p+rvNunESIP39YVEsi2iu/KWTs5Hc/92zFpyvzrMcn/nvMP46cGkLk82LMAAAAASUVORK5CYIKJUE5H"
"DQoaCgAAAA1JSERSAAAAIAAAACAIBgAAAHN6evQAAAUQSURBVHiczZdbbJRFFMd/Z+b7tu32kpbSEuRSA4jaVkUuxgINXoBiBOEB"
"HtQ3g0/GmIYXTUiICYkPxmDCiwmoLxoSSQwJGlovwdrSFwMSU9TWBLU2QKqVXre7+30z48PslkLYFgoJnmR2Nt+ZOec/5zojeNKA"
"WbNmTdg/MLh/aNw+ba1qBmcBxZ2RBVFK2c7qMnV66eLag2fPno3yOgX2aDhuamuXbk4Zty+2atvWRtjwoBBlQeTOtDsHYQLO9Dq+"
"6oFA2baklvcGB/u/gT1aAGoWLt3gHJ1FgciRV1T03Eal7SjK2rsDQClQFdhTXda8+pENM7FzIjT/fbn/jNTV1VX+M2ZPVJaqTefe"
"1tlkQhKH2g1HvzNEFu5QPw4IFex9StPaokllXXb1AZMYnrAd88vVLqlZsOjNsWzwzonXVbR+pQpX7c9ycdBRkRQkJ2CuIPJ7HTCa"
"ciyrFc4fTNDdZ6Ndh21YnojfUkPjsqOlEduyUetDbYaLg46FVUKoIVD4eY5juoyFVcLFQcehNkPLRq1bGrFD47JDWSvrm1eKikad"
"OtphqEgK2dj7zuV8mB9KQKtrA3c93zl/4jw/f3rnIBtDRVI42mGIRp1qXinKWlkfgLOTEUpZiE1hc4vAcAqiOP8BKpOgxSvJrxnP"
"QDrj+SUJSBZ5ALktxAaUhckIwNkAUEo8t1DEi3jFLz2pqF/sLWQMfNxpGE6B1r5YTGRga6OwfqUvHd/9bOn41VFadD1IxFsTUMFs"
"gSTiUc8rg3dfDKipBbJACVwadnz4vaW61K+dzMLWRsVruzVY4Bi0/WQoLwFjby5/1iqnxJ9sS4OiqgxG/oXRCYjGYOdqTXEIxl2z"
"4HgG4mGIR/y+2VJoVgDWQVHglQUJGBqHc384AoGmFUL9fUJ6WsVUci0L1C3k74wAlEA6Cw8vEpoe8NJO/2J4vz3GOKgqh+2rFOlo"
"7g1jxn0ikI5h+2OKqnKwEXT1Obp6HQNDgMDzq7xr4jmW7RkBxAaqkl6JCFwYcHz+g2Vo0PFptwGgfpHQtEKYyNyayW+kglmgBUYz"
"sKVRaFwiZLKQjuCNFk1soG6+MJ6CsqSPj28vxFOpdlcAIL6A7HxcU1wEqUlY16BYtyZnNANuxJHJ+NRbPA/6LrnbbhwFAWRiWDQP"
"NjcKJob+IcdnpwzW5oIzgqYVii2PiF/XoOj73aDvBgCtfNl9uUlzf41AAF+ctxz4xKByRcemYe1DlmcbQlQAu9dpPvjaFiw4twXA"
"Wkgm4Jl6YSztU7Gz11FaCRUlvjbYMvhryPHjn45HlwjLFwiLa6E49DKc9VaczSA3BeCARAD7jsXsO+ZjYSIDRaEXmicD7DkcURRC"
"qIW1dYqdqxWTaUhouDBgSQS5m+XtAACvdDjl/+db7I0kwEQWIgtftgY8sVz8xwQc77R09DrKin2pLlQjZmxGoWLKhq5Ajmnx68IA"
"rozAb1cs7T2OI6fNLSXEjADc1E9hvoh3ywuHIgBSWRidhPJi3w8KAZ8OwFqHyt9u5kpjaT9rBVWlPpBvJs85j9x6ng1AVEkIVuUQ"
"zxFAkHeXK9z7HV6HVVASgn+wKNfd2edsWCF27ybNaMqRCLxphdx8C2PK4TfycjISgb8Z792kCSvEdvY5q5TrVtVl7mR7D6q9y5jW"
"bZpltcLlq47I+A4XGd+U5jKmy7h81V/LW7dp2ruMae9BVZe5k/f+YQL3+Gn2v3iccg+f5/8BkpiYtJ9T0dMAAAAASUVORK5CYIKJ"
"UE5HDQoaCgAAAA1JSERSAAAAMAAAADAIBgAAAFcC+YcAAAgmSURBVHic3ZprjJxVGcd/zznnfWdmd9st7qW3pbYKhbYsUGiJlepS"
"0FoDiRgIJSQSJUD8ABr5sCTVRD8YEvaD0dgYQgwgMYQSMUgwaapcCtVGbi0sxYSglLJAabe0e52d93IeP5yZ3S4suLtsd63/5E1m"
"Z+fN/P/v838u55wRxkOgw8LubEHzoq+CI3Ky3YhpV/UeMMwOvIgxXn13multkHGi9/Cz0OFgdw7oSYRHYQAP0LKw7Xsq9r7cw+CI"
"J80VGffRUw9FiazQUDRYA6L5TUc/6Ln/o1zl5DfmN7WtLxXsL1R140iiOeC7rndudRsyPAJ2lp5/7qGuCK/3oJ0PZxlgirFYEdlT"
"ruR39B/reaHGWaoiTNOitovw8kw5M3XDfbnedpWVu653RALF5tl9+jWM9CqpwraHM7Y/kWtdo5WS88MYvezY4Z6XqwI6HOzOWha2"
"vTSc2ou+slKTzWtN9MPLrZgI8HDXn3KSDMws6fAKsYNt37JgwKfwq6dy3bXPp8+9IXFdlL989IOei6HDOditza1LbzHGrhjqy9Mr"
"10bRbddY6T+iPPKs57dP57x40JNns0O+Buvg8Zc8N2+yXLfB8KNrnETk0c4X0rSh1a5obl16S++R3ffJgua2jsjZZ0Yyz3c3Gr37"
"BieawYU/SXj/BIyk0NQwu+RrODYIxQgWL4D9P48RB3c+lOkDe7wUnSHN8stMFPu+XEEg7drqpBQJD+31HO4LYTyjHtJ8bq4z6gOH"
"w33w0F5PKRK6tjoRSHOFKPZ9Bm8fHCh7urY6p0Cmyr1PZ5QTcCZUhLlC7gOHcgL3Pp2RqaJA11bnBsoevH3QGJH2NIP2NqTUInQ9"
"lvPKQaWpAbI5JF9D5oOFXzmodD2WU2oR2tuQNAMj0u5U1YtgBivhhjSHJJ3alxjDx9qcaqgmnwSp3ncyvD+pxX4ESRq4AQxWQARU"
"1Tuq40GtREqtM0wSqjBQ/ghZhUIULp2AkQCph3L5pO9SqCsEy0woQqrcGFfOjZs81YkROfjSMqEuDiJUwTnoOQYHjyqR+7iIzENT"
"PaxaKWR50GAtvNaj9A1/iogJMG0B1kDfMHyjXXj0BxFRHZATJpQG2Pk35Tv3pHjPuIgagYEEtrQLD/84goHqP0rwzZ+lPHlAWVA/"
"+eIxbQG1cG5abbExfPjh2KxkhmDDWcKqJcILbykNhfEWE4Ekg6wP+oeCvnlVj8sUu/20xjMRGK7A8ha4Yo3gU4htqNmxAwQa6+Hy"
"NeYT7SACzga7OBNeT5X89AUQfLz284bzlwnlSvB9OYFKGgglKVy7zlBfCNXlVGFaAnKFooNr15vR0leM4f5nc159RykWg0XOWihc"
"erahcgoHwWkJ8B6WngGXrTJUEijEcOQE/P7vnr1vKupD5YkdXHuJIcmmZ4/JYMoCrIHhBL693tJYClYqWOjuUQ68q+x8NWekEpqU"
"KqxfYTh3cbDWqYjClAQIoZrUx7Cl3RBVEy/J4Yl9oU2+/q6y/5ASWxhKYEUrfP08w0BV1EyvTKckwJjQdTeeE0rkSDVh+8uw6zWl"
"sQSVHB7f54kKoZZbF6zW0lAtkzPLfxo5IHDFasPnGsNaoRDBH57Peb3Hc3wI+k7AH1/Mea9XKUUwNAwdqwznLBHKyczbaNKNzEgo"
"k19oEa5YY0iTkA9JBh3nGp7aFmMkVKTIgqsy9Rp6wtfWGPYdzFGd2ShMqRNnHi5cBu1nCgPlIKCSwRdbhVVLxhqWahCb+arIBK5Z"
"Z7jnyZxKPoPsmYKF/Gjtt/jqUxSB+XUQFwELUr2Mg/oGKEVBVJ4HkRvOFtJsDiIgAlkOZzYJHasMSRpa/+AIbHskY/8hpS4ODQ7A"
"CgyMwB1bLFetNZQTqC/CdZdYntif4WZwf2lSAkx19rn6YqGxFJK3vgjvvKf8bo+nv7rpVRubjUClAsuaPFvON4iE5rduubB6idB9"
"SGessU1KgPcwrwRXXmCJopC4xsArh5SBEWiZ9/HxNy/AP/7lGSjDgvpwz4rFhs3nCfvf9BTi8WGodW+Y/FoAJpED1oQl3JfPNixr"
"EvoGQ+IeH4Rdr3liF+yV+/EXQO8gPPeGJ82DpdQrG1da6huExY0yytSaYMfag5mKgv8agdxDXQzP/9uz/qcJSkhCJYwHxeiT175G"
"4PsPZEQ2/P3hULjxrEVw46WhFAsQR3DgsHJ0gNHPzpgACEmcZlDRMfITLconQpaHiDmBmzsMy5uFy1eb0U7uFVwMT/3T81avMr84"
"VgxmTEBNhJ1G4okEnzoLt2+2rFwmVAaDXUpxWEfsOeDZ/pec2Fbz4FQImAlIlVghgrQCb/cqfz3gufvPnt7+8P6nbcVMhFkRIBKI"
"/eZJT9M86B9W3u+DfW8rbxxW6gshD6ZKHmZLAIHcL3fl4YUIzobisKCuuqE1DfIwyxZqnc/oUVVt5+6z7r06wk6OqYVvqkk0FWSf"
"ZZDTsSidZDVvRMSoQkMhvBPZ4Mf/NcTRWI9oKAQxEo4ytTty0N2Dlo8qnVdbLlguHBtkRoeu6cKZcNBxwXKh82pL+ajS3YNGDrxq"
"t8HkN84rGTp3ZJkAToRbNzlK8dg8P1ewJnAoxXDrJoeTkEGdO7JsXsmAyW80aWIabRhLos4dmZZT5YYNhkWNodkcHwqhm4vr+FDg"
"sKgRbthgKKdK545MFSIrkCamUQDb3Lr0Jmvd3R8cyRt+fWvkRg/59s7tId+65Wb0kG9+q7D90VxvvzfNFrbawTzP7uw98u59p/0x"
"6//DQTdwmv/UoIbT+sceNZx2P7f5D40XMc9nrmALAAAAAElFTkSuQmCC"
)

SITE_IMAGES_B64 = {
    "apple-touch-icon.png": (
        "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"
    ),
    "logo.png": (
        "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"
        "gRg3SLHA2B4AAAAASUVORK5CYII="
    ),
    "og-default.jpg": (
        "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAQDAwMDAgQDAwMEBAQFBgoGBgUFBgwICQcKDgwPDg4MDQ0PERYTDxAVEQ0NExoTFRcY"
        "GRkZDxIbHRsYHRYYGRj/2wBDAQQEBAYFBgsGBgsYEA0QGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgY"
        "GBgYGBgYGBj/wAARCAJ2BLADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUF"
        "BAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVW"
        "V1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi"
        "4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAEC"
        "AxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVm"
        "Z2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq"
        "8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD16iiiv5hP2Q/PP4j/APJZPFv/AGGrz/0e9czXTfEf/ksni3/sNXn/AKPeuZr+m8B/u1L/"
        "AAr8j8cxP8afq/zCiiiuswCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKAP0yooor+WT9qPzz+I//JZPFv8A2Grz/wBHvXM103xH/wCSyeLf+w1ef+j3rma/pvAf7tS/wr8j8cxP8afq/wAwooorrMAo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKK"
        "ACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9MqKKK/lk/aj88/iP"
        "/wAlk8W/9hq8/wDR71zNdN8R/wDksni3/sNXn/o965mv6bwH+7Uv8K/I/HMT/Gn6v8wooorrMAooooAKKKKACiiigAooooAKKKKA"
        "CiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiii"
        "gAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK"
        "KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9MqKKK/lk/aj88/iP/AMlk8W/9hq8/9HvXM103xH/5"
        "LJ4t/wCw1ef+j3rma/pzAf7tT/wr8j8cxP8AGn6v8wooorqMAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig"
        "AooooAKKKKACiiigAooooAKKKKACiiigD9MqKKK/lk/aj88/iP8A8lk8W/8AYavP/R71zNdN8R/+SyeLf+wzef8Ao965mv6dwH+7"
        "U/8ACvyPxzE/xp+r/MKKKK6zAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooA/TKiiiv5XP2o/PX4jf8lj8W/wDYZvP/AEe9czXTfEb/AJLH4t/7DN5/6PeuZr+m8B/u1L/CvyPxzE/xp+r/ADCiiius"
        "wCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP0wooor+WT9qPz1"
        "+I3/ACWPxb/2Gbz/ANHvXM103xG/5LH4t/7DN5/6PeuZr+m8B/u1L/CvyPxzE/xp+r/MKKKK6zAKKKKACiiigAooooAKKKKACiii"
        "gAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK"
        "KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKA"
        "CiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/TCiiiv5ZP2o/PX4jf8lj8W/9hm8/9HvXM103xG/5"
        "LH4t/wCwzef+j3rma/pzAf7tS/wr8j8cxP8AGn6v8wooorqMAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig"
        "AooooAKKKKACiiigAooooAKKKKACiiigD9MKKKK/lk/aj89fiN/yWPxb/wBhm8/9HvXM103xG/5LH4t/7DN5/wCj3rma/p3Af7tS"
        "/wAK/I/HMT/Gn6v8wooorrMAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigD9MKKKK/lc/aj89fiN/yWPxb/ANhm8/8AR71zNdN8Rgf+Fx+Lf+wzef8Ao965nBr+ncB/u1L/AAr8j8cxP8afq/zCijBo"
        "wa6zAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBo"
        "AKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKM"
        "GjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBo"
        "AKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKM"
        "GjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBo"
        "AKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoA/TCiiiv5XP2o/Pf4jf8"
        "lj8Wf9hm8/8AR71zNdN8Rv8Aksfiz/sM3n/o965mv6bwH+7Uv8K/I/HMT/Gn6v8AMKKKK6zAKKKKACiiigAooooAKKK/Rn4Rfsif"
        "Caf4JeHL3x/4PfUPEV3aLd3krahdQFTJ86x7I5VUFFZVPHVTSbsNK5+c1Ffqf/wyB+zt/wBE8/8AKtff/H6T/hkD9nb/AKJ5/wCV"
        "a+/+P0udByn5Y0V1XxL8GXPw8+LviHwZdbydMvHhjd+skR+aJ/8AgSMjfjXK1QgooooAKK+2f2TfgH8JviZ8CbnxF438Kf2pqSav"
        "NarP9vuYMRrHEwXbFIq9WbnGea92/wCGQP2dv+ief+Va+/8Aj9S5JDsflhRX2X+178C/hZ8LvhDo2t+BfC39lX1zrCWss3265n3R"
        "mCViuJZGA5RTkDPFfGlNO4mrBRRRTAKKKKACiiigAooooAKK/QP9nz9mz4K+OP2bfC/irxR4L+36tfRTNcXP9o3cW8rPIg+VJVUf"
        "KoHAHSvTP+GQP2dv+ief+Va+/wDj9TzIdj8sKK+of2yPhH8PfhVf+Do/APh/+yF1GO8a6H2ue48wxmHZ/rXbGN7dMdea+XqpO4mF"
        "FFFABRXpHwG+HafFH4/eH/Cd1C8mmvN9p1AKxX/Roxvcbhyu7AQEcguK/Qf/AIZA/Z2/6J5/5Vr7/wCP0nKw0rn5YUV+p/8AwyB+"
        "zt/0Tz/yrX3/AMfryv8AaI/ZV+Gfh/8AZ+1nxL8OfCr6ZrGk7b12W+uZ/Nt1OJVKyyMAApL5Az8nXk0uZBynwJRRRVCCiu8+C2ne"
        "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"
        "KqwPG/hDSPH3w81fwfrsQex1K3aBzjJjPVZF/wBpWCsPdRUxdhtXPxgorb8YeFtV8EePNW8Ja3F5d/ply9tKB0baeGX/AGWGGB7g"
        "isStiD6y/YC/5Lt4j/7ALf8ApRDX6GV+ef7AX/JdvEf/AGAW/wDSiGv0MrGe5cdjj/itreqeGvgX4w8Q6JdfZdS0/R7q6tZ9iv5c"
        "iRMyttYFTggcEEV+cH/DX/7RP/RQ/wDyk2P/AMYr9EPjn/ybL4//AOxfvf8A0Q1fkBVQSsKR7f8A8Nf/ALRP/RQ//KTY/wDxij/h"
        "r/8AaJ/6KH/5SbH/AOMV4hRV2RNzs/iF8WPH/wAVLuxuvHuv/wBrS2CPHbN9lgg8tWILDESLnJUdc1xlFFMD0L4D/wDJzvgD/sPW"
        "f/o1a/XyvyD+A/8Ayc74A/7D1n/6NWv18rOoVEK/NT4h/tVfHvQ/i94q0TSvHn2exsdYu7W2h/suyfy40ndVXLQknAAGSSa/Suvx"
        "x+LP/JffHH/YwX//AKUyUoIJHf8A/DX/AO0T/wBFD/8AKTY//GKP+Gv/ANon/oof/lJsf/jFeIUVpZE3P0s/Y9+Kfjz4p+B/Emoe"
        "PNd/ta5s76OGB/ssMGxDHkjESKDz65r6Sr49/wCCfn/JNPGH/YTi/wDRVfYVZS3LR87fttf8mm33/YRtP/QzX5lV+mv7bX/Jpt9/"
        "2EbT/wBDNfmVVw2JkFFFFWIKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/S6iiiv5XP2o/Pf4jf8lj8Wf9hm8/9HvX"
        "M103xGH/ABeLxZ/2Gbz/ANHvXNYr+ncB/u1P/CvyPxzE/wAafq/zEopcUYrruYCUUuKMUXASilxRii4H1X+wp4A/t74zaj45u4d1"
        "p4etdkDEcG5nBQY9cRiX6Flr9Eq8S/ZR8Af8ID+zLoiXMPl6jrIOr3eRg5lA8tT6YiEYI7HNe21jJ3ZaOA+NXxFHwq+B+u+NY47e"
        "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"
        "x20RcqPU46D3PFarEUnB1FJcve6t95n7KfNycrv26mdRXoy/Ab4svD5o8IS7cZwbu3B/IyZrC1j4bePdBhebVfCWqwQoMvMIDJGo"
        "9S65A/OuWlm2Bqy5KdeDfZST/U3ngcTBc06ckvRnLUUUV6ByhRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRR"
        "QAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUU"
        "UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH6WUUUV/K5+1H58fEX/ksXiz/sM3n/o965qul+Iv/JYv"
        "Fn/YZvP/AEe9c1X9O4D/AHal/hX5H45if40/V/mFFFFdZgFFFFABRRRQAV6F8E/Cv/CWfGbSrWWPfaWbfb7nIyNkZBAPsXKL+Nee"
        "19Y/su+Ff7P8DX/iu4jxNqc3kwEj/ljGSCR9XLA/7gr53irMv7PyyrUT95+6vV/5K7+R62SYT61jIQey1fov6se7vPBHPFBJKiyS"
        "58tCcF8DJwO+BXzN+1T4V8q/0jxlbx/LMpsLlgP4hloyfcjeP+Airnxb+JzaH+0t4aihnIs9BK/awD188ASj3xEVx7k17F8TfC6+"
        "NPhPq+ixKJJ5IPOtSOf3qfOmD7kY+jGvyrK6dXIcVg8bVfuVVr6N2/Jxkfa42cMzoYjDQ+KD09Vr+d0fAVfoL8N/+SN+E/8AsD2n"
        "/ola/PoggkEYI7Gv0F+G/wDyRvwn/wBge0/9ErX13iT/ALrQ/wAT/I8LhH+NU9F+Z8V/Fj/kt/in/sIy/wDoVeq/sof8jT4j/wCv"
        "SL/0M15V8WP+S3+Kf+wjL/6FXqv7KH/I0+I/+vSL/wBDNern3/JNv/BD84nFln/I3X+KX6nVftWf8k80P/sIn/0U1TW37Ufw/hso"
        "YW0fxKWRFUkW8GMgY/57VD+1Z/yTzQ/+wif/AEU1fJ9eRw3kOEzbJ6KxSfuudrO27/4B3ZvmdfA4+p7G2qje/kj9BPAXjzSPiJ4Y"
        "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"
        "VXFOEEpUp6atvf1u4/fY3xP9t0eaV1OPkl+Vk/zPAKKUgqxVgQQcEHtSV+vnwYUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAF"
        "FFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFA"
        "BRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+llFFFfyuftR+fHxF/5LF4s/7DN5/6"
        "PeuarpfiL/yWLxZ/2Gbz/wBHvXNV/TuA/wB2pf4V+R+OYn+NP1f5hRRRXWYBRRRQAUUUUAWdPsbnVNXtdMsozJc3UyQRIP4nYhQP"
        "zIr9D/Deh23hrwhpugWePJsbdIA2MbiBgsfcnJP1r44+Adv4fX4sxa14l1nTNNtdMiaeI31ykIkmPyqBuIzjJbjoVFe4/Gv4r6NY"
        "/Cya38HeLbC41W8mSBJNKvkeWBM7mfMbZXhduf8Aar8w41hiMzx9DLaEXbq7O1339Fr8z7Lh6VLB4api6j16LrZf5v8AIta7+zj4"
        "L8ReJr/XdS1rxG13eztPLsuIQoLHOFBiOAOgHoBXqekacmj6BZaTFcT3EdpAluk1wQ0jhVCgsQACcDk4FfAv/CxfiD/0Pfib/wAG"
        "k/8A8VXsX7P/AMV7iLxHqmleOvFsr208CzW91rN8SsbocFA8jcbg2cZ/grhzzhbNVg+etX9oqe0Un5LT0X5HTludYJ4jlp0uRy3d"
        "/wAzzr41+Ff+ES+M2q2sUey0vG+3W2BgbJCSQPYOHX8K+ufhPexX/wAEPC08LBlXTooCR/ejXy2H5qa8Z/aSuvB3ibwvpmuaF4o0"
        "O/1GxmMLwWl9FLI8L99qsSdrKP8AvomuU+Cnxsi8B2z+HPEcU02iySGWKaEbntWP3vl/iQ9cDkHJGc125hhMVnmQUZwi3VpvVPd2"
        "Vnv1as/+Cc+Fr0ctzOpGTXJPZ9FfX/NHK/GzSrvSfjr4gS6iZBc3H2qJiOHRwGBHrzkfUGvVf2UNKu1k8R628TLassNtHIRw7Asz"
        "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"
        "N/FHImZ5CMqzAjgg/jXz58ddT07V/jpq9/pOoWt/aSJAEuLWVZY2xCgOGUkHBBH4V8twvh6sOIsXOUWk/aa20+NHs5zVhLKqEU1f"
        "3f8A0lnnNbmo6B4q8IXkFzqGnajpUpAkgucMgbIyCkg4PHoaw6+yvCvx3+F+q+GrTS9U1BrCVIEhkg1G2OxiqgH5l3LjjuRX2WfZ"
        "nisBGE8Ph3Vi78yV7ra2yfn0PAyzB0cU5Rq1eRq1r/0vzPnnQ/jl8TtCZBH4mmvoV6w6iouA3sWb5/yYV9n+EtZufEPgTSNcvLI2"
        "dxe2sc8kBz8hYZ4zzjuPYiuQh1X4DLOt/DdeAEmB3CUfZVkB9fXNYvjf9ojwV4f0iaPw5eprmqlSsKQKfJRuzO5wCB6Lkn261+Z5"
        "xfO5wp4HAOnO+rtb77JL5s+wwFsujKeJxKlHor3+7W/yR8xfFGC1tvjR4ohs1VYhqU2FXoCWJYD8c1yVTXl3cahqNxf3krS3FxI0"
        "0sjdXdjkk/Uk1DX7LhaTo0YUpO7ikr+iPgK01UqSmla7bCiiitzIKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKK"
        "ACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9LKKKK/lc/aj8+PiL/wAli8Wf9hm8/wDR71zVdP8AEUf8"
        "Xi8Wf9hm8/8AR71zOK/p3Af7tS/wr8j8cxP8afq/zEopcUYrrMBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKX"
        "FGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopc"
        "UYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilx"
        "RigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXF"
        "GKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcU"
        "YoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxR"
        "igD9K6KKK/lc/aj8+viL/wAlh8Wf9hm8/wDR71zVdL8Rf+Sw+LP+wzef+j3rmq/p3Af7tS/wr8j8cxP8afq/zCiiiuswCiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK"
        "KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKA"
        "CiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiii"
        "gAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP0qooor+Vz9qPz6+Iv8AyWHx"
        "Z/2Gbz/0e9c1XS/EX/ksPiz/ALDN5/6Peuar+ncB/u1L/CvyPxzE/wAafq/zCiiiuswCiiigAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig"
        "AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP0qooor+Vz9qPz6+Iv/JYfFn/AGGbz/0e9c1XS/EX/ksPiz/s"
        "M3n/AKPeuar+ncB/u1L/AAr8j8cxP8afq/zCiiiuswCiiigAooooAKKKltrW6vbpLaztpriZzhYoULs30A5NAEVFdM/w5+IUdsbi"
        "TwJ4mSEDPmNpc4X89uK5yWGW3naGeJ4pEOGR1Ksp9CD0oAZRRRQAUUUUAFFFFABRRRQAUUV6FoHwO+KPijwlb+J9C8L/AGvSrhHe"
        "K4+228e4KxVjtaQMMFSOR2oA89ooooAKKKKACiiigAooooAKKciPJIscaM7scKqjJJ9AK6Jvh74+SzF2/gfxItuRkSnTJghHrnbi"
        "gDm6KdJFJDM0U0bRyKcMjjBB9xTaACiiigAord03wT4z1m0F1o/hLXdQgIyJbSwllU/iqkVn6lpGraNd/ZdY0u90+fGfKu4Gib8m"
        "ANAFKiiusHwu+JjKGX4deLCDyCNIuOf/ABygDk6K6z/hVvxO/wCic+Lf/BRcf/EVgS6Rq0Ovf2JNpd7HqfnC3+wvAwn8wnATy8bt"
        "xJAxjNAFKiupm+GXxIt7eSef4feKooo1LvI+kzqqqBkkkpwAK5agAorf0rwL4313TV1HQ/B2v6nZsSq3Nlp800bEHBAZVIyDWfq+"
        "h614f1D7Br2j3+l3ZQSfZ763eCTaejbXAODg8+1AFCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooqSCCe6uo7a1hknnlYJH"
        "FGpZnYnAAA5JJ7UAR0V6lZ/s5fGi+tEuIfA86o4yBPd28LfiryAj8RXnOraVf6Fr17ouqwfZ76yne2uItyvskRirLlSQcEHkEigC"
        "nRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRXc+D/g78RvH2gPrXhPw7/aFikzW7Tfa4IsSAAkYkdT0ZecY5rj"
        "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"
        "aN8JSs7M7aihZick5znNAHeftO/CfQ/h/wCINL1zwva/Y9M1XzEks1JKQTJg5XPRWDdOxU44IA8Cr7J/bN/5EDw0f+ohJ/6Lr5z8"
        "KfBb4l+N/Dia94X8Nfb9Pd2jWb7ZbxZZTgja8in9KAOCoqW5tprO9mtLlNk0LtHIuQdrA4IyOOoqKgD7Y/Y3/wCSNa1/2Gn/APRE"
        "NfNXx2/5ON8Xf9fx/wDQVr6D/Yz1e2k8EeJNA8wC5gvkvNhPJSSMJkfQxfqPWvNvj18IvH83x21jV9G8Lapq2n6nKtxBcWFu04BK"
        "KGV9oOwhgeuOMGgD6J/Zk/5Ng8O/791/6VS18PXmj3niD4vXOhaem+6vtXe2iH+08xUZ9ua++PhBoFz8Ov2eNH0zxKUtJ7C2murz"
        "cwIgDSPMwJHHyhsH6Gvm39l3wz/wlvx61TxtcQH7LpYkuU3DI8+csEH4L5h9iBQB778V/EUfwa/ZuSHw/IILm3ig0rTiRzuwAWPv"
        "sR2+oqH4taTafFr9lebVNLj8yVrKPWrEDkh1TeV/3ihkTHqa6L4nfCTQPivZ6daeIdU1i0gsHeSOPT5Y0DswAy2+NskAHGMfeNbn"
        "gfwbp/gPwLaeE9Mvb+8sbTeInv3R5ArMWKkqqggFjjjpQB+X9fp54v8AC/8Awmnwr1Hwr9u+w/2jaCD7T5Xm+XnBztyM9OmRX58/"
        "FzwefAvxl13w6kZS1juDNacceRJ86AeuA236qa+9fiZ/bv8AwonXP+EZ/tD+1/sH+i/2dv8AtG/jHl7Pmz9OaAPBf+GKf+ql/wDl"
        "G/8Auivl7XtM/sTxVqejef5/2G7ltfN27d+xyu7GTjOM4ya9I/4ya/6qz/5UK811i11iy126t9ftr631MSFrmO+Rkn3t8xLh/myc"
        "5565zQBRooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP0oooor+Vz9qPz8+In/JYfFn/YZvP/AEe9c1XS/ET/AJLD4s/7DN5/"
        "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"
        "4brV1DxN4k1bR7XSdU8QarfWFoALa0ubuSWKABdoCIxIXA4GB04oApX94+oatdX8iqr3EzzMq9AWJJA/Oq9FFAG/4N8aeIvAXiuH"
        "xD4Zvja3kYKMCNySoeqOv8SnA/IEYIBr6GsP20dVjslXU/ANnc3GPmkttQaFCf8AdaNyPzr5aooA9l+Jn7SHjT4i6JLoMdtbaJpE"
        "3E1vaszyTjOdryHqvTgAZ75q58If2g7P4TeB5tCg8Df2ncXFy1zPeHUvJLkgKq7fJbAAX16knvXh1FAG/wCNvFV743+IOreK9QTy"
        "5tQuDKIt27yk6IgOBkKoVc47V0vwe+K978JPGF1rEOmf2pbXdsbeeyNx5AY5DK+7a2CCD26Ma87ooA9L+MvxWs/i14h07Wo/Cv8A"
        "Yl3a27W0r/bftHnpu3J/yzTG0l/XO7tivY4v20/KgSP/AIVrnaoXP9s9cD/rhXyjRQB9Y/8ADa3/AFTT/wArP/3PXzp8QvF3/Cef"
        "EvVvF39n/wBn/wBoSLJ9l83zfLwirjdtXP3c9B1rmaKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/Siiiiv5XP2o/Pz4i"
        "f8lh8Wf9hm8/9HvXNV0vxE/5LD4s/wCwzef+j3rmq/p3Af7tS/wr8j8cxP8AGn6v8wooorrMAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig"
        "AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9KKKKK/lc/aj8/PiJ/yWHxZ/wBhm8/9HvXNV0/xE/5L"
        "B4r/AOwzef8Ao965qv6dwH+7Uv8ACvyPxzE/xp+r/MbRTqK6zAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6ig"
        "BtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOo"
        "oAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRT"
        "qKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0"
        "U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igB"
        "tFOooA/Saiiiv5XP2o/P74if8lg8V/8AYZvP/R71zVdL8RP+SweK/wDsM3n/AKPeuar+ncB/u1L/AAr8j8cxP8afq/zCiiiuswCi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP0mooor+Vz9qPz++In"
        "/JYPFf8A2Gbz/wBHvXNV0vxE/wCSweK/+wzef+j3rmq/p3Af7tS/wr8j8cxP8afq/wAwooorrMAooooAKKKKACiiigAooooAKKKK"
        "ACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9JqKKK/lc/aj8/viJ/wAlg8V/9hm8/wDR71zVdL8R"
        "P+SweK/+wzef+j3rmq/p3Af7tS/wr8j8cxP8afq/zCiiiuswCiiigAooooAKK9s/ZN8Uf8Iv+1d4bMkmy31MyaXLz97zUIjH/f0R"
        "19Gft9eF/tfw68LeMIo8vp9/JYysBzsmTcCfYNDj/gXvUt62HbQ+B6K+6v2CvD8Om+A/GXjy+KxRTXEdis0nARIUMkhz6fvVz/u1"
        "S/b98Mq9p4N8bQICoabTJ5ByDkCWIZ/Cajm1sFtLnxFU9nZ3mo6jb6fp9rPd3dzIsMFvAhkkldjhUVRyzEkAAckmv0A/YN8L/wBm"
        "/BjXfFUse2XV9SEKNj70UCYB/wC+5JR+FeDeNfFH/CWf8FM7C/STfBa+L9O06LByAtvcRRHHsWRj+NHNrYLHiuufDzx/4Y0v+0/E"
        "vgbxJo1lvEf2rUdMnt49xzhdzqBk4PHtXN1+lP7a9nd6h+zZbWNhazXV1PrlrHFBAhd5GKyAKqjkk+gr4xk/Zi+PMegnWG+G+p/Z"
        "wm8ossLT4/64h/Mz7bc0KV0DR5JRT5YpIJ3hmjeORGKujjBUjggg9DXqei/s1fHTxBaJc6d8ONUWJwGVrxorTIPIOJnU1VxHlNFe"
        "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"
        "2/ZJ/Zv0Xx7p0nxH8e2ZvNGjnaDTtNckJdOn35ZMdUU/KFzywbPAwW3YSVz5Jor9J/EX7VPwA+Gusz+ENM025vFtHNvNH4e06EW0"
        "TA4KZZ0VsH+7kV82/tPeL/gj4+8N+HvFHwwtdPtdYkuZY9TijtPslxt2qVMqABW5z84z6Z7UlK/Qdj5qoooqhBRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRR"
        "RQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+k1FFFfyuftR+f3xE"
        "/wCSweK/+wzef+j3rmq6X4if8lg8V/8AYZvP/R71zVf07gP92pf4V+R+OYn+NP1f5hRRRXWYBRRRQAUUUUAXtE1a60HxNp2uWLbb"
        "qwuoruE+jxuGX9QK/Uf4+6Va/Eb9jzxHPp6+ckulJrNowGSRGFuBj3KqR/wKvyqr9Sv2Xtfg8a/sieHYL3bObS3k0e5jbkbYiUVT"
        "/wBsjH+dRPoykeb2H/FqP+CWElx/qb3VNJZ89GZ7+TapHuI5V/74p3xCP/C2P+CYWn+IF/f32n6dbXpfr+9tW8mdv++RMazP26ta"
        "ttA+EHg34fabiKGe6MwiU/dhtohGqn2zKP8Avj2q5+xLqlj4v/Zz8U/DzWFFzb2t1JFLAT1tbqLBX8WWb86XS4eR698LbS3+E/7G"
        "ujT3sYjGk6A+q3SHjDsjXMin33Mwr84PhRd3F/8AtOeCL67kMlxceKLCWVz1Zmu0JP5mv0B/a/8AEq+F/wBk/WLWBhFLq00GlQhe"
        "OGbe4A/65xyD8a/Pf4Of8nF+AP8AsZNO/wDSqOiOzYM/T/41/EfT/hR8Ib3xteaZHqNxaSIljbPxvuHyi/Nj5QAWJI52hh3rzf8A"
        "Zi/aK13423fiDTPE2i6bYXumpFPFJp29Y5I3LKQyuzEMCBznnPQY5rftxf8AJrqf9hm2/wDQZK8d/YA/5KL4x/7BsP8A6NNJL3bj"
        "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"
        "oAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRT"
        "qKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0U6igBtFOooAbRTqKAG0"
        "U6igBtFOooAbRTqKAG0U6igD9JKKKK/lc/aj8/8A4if8lf8AFf8A2GLv/wBHvXN10nxE/wCSv+K/+wxd/wDo965uv6dwH+7Uv8K/"
        "I/HMT/Gn6v8AMKKKK6zAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKK"
        "ACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo"
        "oooA/SSiiiv5XP2o/P8A+In/ACV/xX/2GLv/ANHvXN10nxE/5K/4r/7DF3/6Peubr+ncB/u1L/CvyPxzE/xp+r/MKKKK6zAKKKKA"
        "CiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiii"
        "gAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoo"
        "ooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK"
        "KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/SSiiiv5XP2o/P/4if8lf"
        "8V/9hi7/APR71zddJ8RP+Sv+K/8AsMXf/o965uv6dwH+7Uv8K/I/HMT/ABp+r/MKKKK6zAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiig"
        "AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA/SSiiiv5XP2o/P/wCIn/JX/Ff/AGGLv/0e9c3XSfET/kr/"
        "AIr/AOwxd/8Ao965uv6dwH+7Uv8ACvyPxzE/xp+r/MKKKK6zAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooA/SSiiiv5XP2o/P/AOIn/JX/ABX/ANhi7/8AR71zdFFf07gP92pf4V+R+OYn+NP1f5hR"
        "RRXWYBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRR"
        "RQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU"
        "UUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH//2Q=="
    ),
}

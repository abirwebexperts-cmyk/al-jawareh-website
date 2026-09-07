# -*- coding: utf-8 -*-
"""
Embedded site assets for Al Jawareh Auto Spare Parts.

The whole website builds from a few Python files (build.py, data.py, theme.py),
so nothing but these needs to live in the repo. build.py writes these into
dist/assets/ on every build.

Editable: STYLE_CSS (design/CSS), MAIN_JS (menus + WhatsApp logic).
Do not hand-edit the *_B64 blobs (binary images: logo, favicon, share image).
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
.brand__logo{height:46px;width:auto;display:block;filter:drop-shadow(0 2px 6px rgba(0,0,0,.35));transition:opacity .18s,transform .18s}
.brand:hover .brand__logo{opacity:.9}

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
.mobile__head .brand__logo{height:34px;filter:none}
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
.brand--footer .brand__logo{height:56px}
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
  .brand__logo{height:38px}
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
  .nav__cta .btn--wa{display:none}
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
    "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"
)

SITE_IMAGES_B64 = {
    "apple-touch-icon.png": (
        "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"
    ),
    "logo.png": (
        "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"
        "gRg3SLHA2B4AAAAASUVORK5CYII="
    ),
    "logo-full.png": (
        "iVBORw0KGgoAAAANSUhEUgAAAe8AAACgCAMAAAASLhTyAAABBGlDQ1BJQ0MgUHJvZmlsZQAAeJxjYGA8wQAELAYMDLl5JUVB7k4K"
        "EZFRCgxIIDG5uIABN2BkYPh2DUQyMFzWxaMOF+BMSS1OBtIfgFilCGg50EgRIFskHcLWALGTIGwbELu8pKAEyA4AsYtCgpyB7BQg"
        "WyMdiZ2ExE4uKAKp7wGybXJzSpMR7mbgSc0LDQbSHEAsw1DMEMTgzuCE8H/+IgYGi68MDMwTEGJJMxkYtrcyMEjcQoipLGBg4G9h"
        "YNh2HiGGCJOCxKJEsBALEDOlpTEwfFrOwMAbycAgfIGBgSsaFhA43KYAdps7Qz4QpjPkMKQCRTwZ8hiSGfSALCMGAwZDBjMAHn8+"
        "VlqfzkYAAAMAUExURV5cVVYlFmdlV1taV2dZJmlnVCUhFGJbJp2RXZucmiYgEyUfE+Hg3iUqGqWilpeSad/TndiVHlhPL8+lVjJM"
        "KCsrW/DjMVBOMbGZJZFdH0gkDci5kb7AwpR1XNbY2cC+w4ZzXzs9QUg4JIh5T5ubme3tqUY4F5OUkT1BNjBQUaJnIZePZPz8AYB+"
        "g3uBevnveNvUZD1BQaKhH0s1SnWcZr3At0I+QwD/AOutbXNzi6sYEzs7QQAA/zxCKj1CQnednYJ7YJKPbbjosdG2m87NzD49QYZy"
        "PK7s7NU3N/92dkA/QmqcF5doKqFdoba20bHLWztDMD9ERgD//0E/Q39/g35+g39//2+De36Fg3Gqxn//f3///4B+gIyDP7WswL7C"
        "VslQNcJ+LP9/qv+/P8y5ktq22snJxwAAAAUDAhYWEzg5NcfHyfj4+La2uKeoqtbW19SWCufn6JWWlygoKIeIilVWVeunC31+fTY2"
        "NXV2dioYBc2JBUdISPG3EGdnaRgYCQgHBfjoTlZXV/LGL/jXL/nmMjElDO24LTY3MSonDSspKeaZBu3HTPXGEEhISDc3DQkIBAkH"
        "BK92DE03DfXYTtOnL/z6jBUVEKZqBcyYLZRmDPfWFvjobM24bv7//tikESYJAfz4cmhnaCwqKa2ILtW3TRUWE0kpB/HXbs6oSJB2"
        "LmtJEElHMXFWExgYEgsIBLSVMRYWE1VFENi1NU1GMFVVAhUVEeipKem5SXFoTRcYCmtZLX9/AOnJbo5ZDNTEcdPHiQoHAyomEb29"
        "wDY2NHRlLrSGEfbnjQgGAykoJ/rzUIppKEhISLKoa66XTS0ZC1VWMp2doe7ZibWmUZKGTyYnJlZXU/8AACcnJ6h4Kjk0E5eFL5d1"
        "FTY1NUdFNWdnZ5iYmKmpqd3d4fnkGbq0bFZXVXt8gScnKFhUMsN7BZ2hojQ1NGY4C2toMYp5Sx0dIdfEUTU2NDY3M0c7KCgoKEhI"
        "SaiZav38pzYAACUaDVxdYSsmFColEXR2c32BgismE0XOPXoAAAEAdFJOU6EP6V3nG+EY9xmiXvse9iD8/KH8Fg38W/z68Pr8Ggn8"
        "9vpcsaMHqVr4DwuqAfz8B/z6ChIM/PABBxsIXQFYYwdQUg8Ol6KmCBIEtAlxBAoKhI0BfEawAmfOCQICjbD9/RP9BgSdB30A+/kN"
        "/Pv8/Pz8/Pz6/Af8BPr7+/z7/PsO0fz6/Pz8+/wqERD8/PwODI6v/Pv8/PuL/Pz8/Pz8Avz8+wsr/Pxx/Pz8/PwR/FFv/K/7/PsE"
        "0fz8+yz7Avz8/PxQKvxM+/z7LU/8/Cz8/BAM/Pz8+20tAZH8+/z80SsvDAj8/PxO/ND7/Pyw/Av7+fxvjfmw0Pv7BTH7S44v+3G9"
        "03q5AABu0ElEQVR42u29B0AbV7Y3LiRENRjcS5J18tI328vb19v33te/7997b5qRLAlUUEEWQmBRTBcyAdNM780YsDG2wYCNwRhj"
        "IO4tbnHv2bjE/3POnZFEceLs2+zbzfrYgMrMnXvP79Q7956RKF7RHxNJXrHgFd6v6BXef4z00Su8/5jpE/j3Cu/vEpUqlivTFAkH"
        "dkYMDOw8sBPpQETEB/9jaGnpK/3+Q6aAgF8HBAjaej4re+eB/tbWnNxch8PB80G8P3Ec/nLk5ubktPb3HxhIn/iRiH3Ar3/961d4"
        "/0HAzbS5QnkAgM7J7eKtrhP3O69e3TEVcuji3r17o/ZP7o+KmoyK2rv34qGQKemO3qud9/Uuq5XjuC4E/ouBAHnpK/3+Q4CaVPJX"
        "wREAdHtQkPnqkPRWyCFAOOrzzxd9TrR5NrEPPwcBiELwA69e7Tzh6nLk5rSGB1TK36BWv2U9B0Py62z4Cfhw+/btr/B+Wdol8Gpn"
        "TU6uw3ViaOrQ2qgFIZ5DW4u3bt3qe7t/f1Tkoamh+6DtgHp46uvfZowYMOeDv3yl3y8TWZcKEVfAE7Dfa3pvPboYFbWfcN5aXCyg"
        "uH//ZB1QX9+ePSV72M+ePfBB8f79AtLFSAz5z/fv31tyaGpHp9WBoA98+O1IqELx5xEH+vvDW1vDcsLC3n0X/hcoX+H9FVBDFvWJ"
        "EcF+PXjlksDAoanIvZNeAAHBPXeq206eCmxu7HAD1dbWWoHKifAVfNbY2FzUUDV+tP4OQC+iXiwq++TeQ1O9Lt7hKKiJWPxbh/v1"
        "JYHNgQ0nx4+WiDRudRx4hfeL4f4kAExi6c+bVi5ZHTJevad48+cMsrq+kvrxkIbRQLfLWs4xslpdLrPLff/+iRMnXC4Wn4lUbj3R"
        "0Ts02jC+FHS+mOyCT9t/fHSq12115Ba0DEz89uK47aXBSxr219Xl5+dnZPSkpHQXxsQULq3lWl/h/SK4/xz9nxw1+9ahyf3Fm9ER"
        "76+rrh9vaHa7GMZ6c6fUHqKLVKtU2kWxsbHrvRS7SKtdq9bo1u2w3dd7sbe6O5obqo5W91FrWwF38u77o/Y+kna4OEdO/xdCaPjJ"
        "P3N+JuCdJSdCivOTk5I2pHTHbdoUD/RZ4WouN3tu0Bbw4a92vcJ7ezb8+s/Bby1ZfWu8pA5U8mBxfn71eAOoIgHd6dyxTqdRLfJD"
        "GCHWqhjBq0WLYkXoVWs1BrsUgOeZutc2jlahhQe0ixMTE5mBnyyZ6u105eb09zdRXP3n/xzEA14PXuK+mJ8EcBPeMfHDgHd8CMcN"
        "LJRffvjHjTcY8r9UvLF45ZJbIfU9daCFdRnVbaDVADWvt9kNkWqtiKVKHakzWOxOp62z02zW64WpFj2Q2WZzOqX2H+g0ahUdH6uN"
        "ijRYbGZSd6vL3QuoZ9Qx046hH8SAJYduXXU5csLf+rc4sfObavknn2z/1Zk1HXXJyZkIeBziTVTo5go+zJ4dw3/4H/7DrxR//hJX"
        "+k7r98233g2UHposRpOYUpjXXIsY6Z2WSH+k19ltgsp+DfFmm9Oi07BzF6l19k4903RXc0NbdR3BLYRyn+8vmeoEyPsjPqTs4DcL"
        "PD78v1e6mouTtgh4xwh4x+zmugZmR6TB744u/X6w4o8a74CAt97tBTMOsU5P4cerb0Dc7bKtiwQtZWqq1lmc5pdDehbqALvdoInS"
        "gu2HNuw2cg28uyOwqjofDTtQfj4q/J7xBndQbs5bAd8kgPvEB/f24J8usTbko36npPjw/iy+ysqFf+Q9NEDxq/Cg0aV99YHhAvp/"
        "jHgD2O5be/fX9WUkxeTtvrEG0ixbpNbri3V2Mz8fSTDfZnOnzUud75uR0MDPO1jvNKjIuS/SWJieW2sbT9XX5TPAkeqKJ/eGdFgd"
        "OTsVr5MAvsw0L/P4APeu4GB5EH8U8E6ahXfeZx43F/YjchUBOB2zOMw6Ndld2BPVmxMAtv2rAf9O4v3OF2+tW/docn9dRoonb3fj"
        "mtob69atZVFZrBaxng1dEMJsW5CcAtEbs57dQPGS3mbRqBF0baSUxe+ujtGj1fmEeAb8q6urm+wb7z0RFNa/8+vRzla8HhCKUf0n"
        "pN7Z77xlrc2Yg/dnn32WV9jAOfoVi5kIfRTRfmK8LiUmPialLzCo/+8V3vtAfyx4y/vDOkP2Rk32VRfmFa1uvHFjXWRULCg1qKL2"
        "msVfr3neZTa/T1AC3p22lyLzbCfAmx/rVKjn2iOP9SyG62hYVU0pM1Ff33705l25rV/8X95YemE6EBb4Tx8qIkyffPLRJ9vT/mNp"
        "GLeuDrOxOXjHF64LdHXltD6B4OBH4VxgXUbMpk2bYmI8xSWdBR8qlv1R6XdEf1jvrZL9fdX1xxvdtWsC14UQ2PCjjbz8pj9QLr15"
        "Nr3fCfE5mPBO/Avks+viWwzfEXJSZd5Pzy9fQ1+h1QniZO1oqEese+A/UMbk5snxwM41Ya1f/Ijy8gX99uLwNSFRIe8GK7J3fbQL"
        "4u/g8C7uUXHyPP0GwPsmq1cF9taGtYY/dQ0B3DGbIHyPiyvLL24Ie/KVAeJ3CW+TQlGZE7RuaVTd5NLVzRifrY5EM75oEQTiGj8r"
        "LuRalG99YwKB4AljM57vU3Mpg/wXOhvHLHtDIcCdgohXV1eDnu8pGe8Nym0Nfkeh+LdzvKzJqFCEh03Vba4rbgh6S7Hrp4B2gSNI"
        "+mgyfwG8P8sDFd+2LaN6fNTtri5OKYvzUkpfiDtcsTzgj0O/D+S4dqyNmuyp2r2mHJSMfHbsIgjIVQafGfcD+wX0dYjrCV/xTRDv"
        "hdyijsUpG7WFRKt8zY2iQlLw6uqelG3bUjLq6koe9VpzWw/P7Xip4nBOx6H9GOQVT7mev/POQI7jasie/ZtRvcmgx/njDQRpWRk0"
        "mJGfmBLnT93FezpaP/yj0O/+dvc4BOT1o24Au/x+5KLYRTQ9ptU5vZAg2i791yL+1dJA6m02C+/0/uF7p0GtRchVDHLO1dhQ35PR"
        "s83jSen2AFX31e15BIY4PGJWBvbz8DWPoiCVSAIfUHzUFeRwNSDYAD+DGxQc51sAcNBtAe5NcWVlSSmQmc+hjLqGsJ3ffbz7w+4/"
        "itpfcrIZZ8Wt0rWYKQHcsVrdLNWeRXq9y+X6xngHUTo2m1xeyHl7JKbmoOVOMwvfGqvqPdWAeKGnsLCwzVNfMjlZ39gRVnMAHRBm"
        "VYrsgo61UX09gGsGIF5X0ntrcnOxmNWxeyUoLYWF8fHDw/HCrAv46w0LUlJxW9AX32m8Sw+0BnU+iiqZGnLjejObQQVgx0KQplVb"
        "fB5WUO9/FokuG3Ta5WIfubyQCxdy2SxqrRa8iPaa/X26seZubmsjvAQCNV86Hng1qKD1CzlOk4dzrkDy9qjKAHhdHep1cj4iXu1p"
        "q2pY3QhpBlJj4+rR41WrYspiYnxwZ/pRUmbmhqTE6jX9y767eCe0OqRro0qGaikF3qEGg3rhAqAdq7IHfdVE2W9IpN4v/IoF7JZf"
        "QEJAibmTXaxjtKq+3gt4YXRhfR/eW4H47UCpYvFTnK3Z3ZaB90bIqCclAdrFdfUn8W7tnI5DwhdYVQgW3ot0kj/B2+QM94vumf7h"
        "430gJ2hH5F5wisSLHZGL0JouurB+vcrysrOl3xRu7qu/RTJbokDBtbE40f4+fVLr3l1FJr0wGmm4rbAaIuxDU4G5rf0rl6Bg1jYP"
        "byPIMZWry2hraHRbX9Bhq3v3cDdAu2VL8hxKQlE5xXGOiO8k3q25nSEXD00xxuh1KkBbu2jRBQyS9dy3Rq6XECTeqYmNvYB3V7Rq"
        "A4Pc2jHUUFVYWBUdDX54eLitrbC++k51/fhoYNCawBN0k7U5pJ6SuMKiDutXtw+QV6UAwFvmY97jBryzv3t4H2jFmbRDxCpA266i"
        "QEkLTBbj42+H+JezG28atNgdmuvROYVJdndzw/EqJAA8pg1+PEkZfX3jQ81uJkTWxqKq+qW7a61+FyPDwd+m3/4rbtbsXpW0MXke"
        "3olt8GXOd8ieGwns/tzOHYcibzGwufsGyn1BpS5oVYZvUbdZ6Pdyxzl1gDcGjoi7zi5A7nI3joKaF8aAZS+MAYIArq5vz6FbHWzF"
        "DedvxnmX+Zc2p9Rut1guX7bYnW+yhJ+6UF5+o8iTvHGuemc0w3ctf5/9HdLvA/1PlzilISG9AofM65huE2M1Tv73Am7sF6k4LZrB"
        "FM3gZCEFhOyNow1VCDoCXgaIb8vom4wab+i97+cr2K3XtapYDP60KtU+tVpzTWex2zr1PBmZcuuNokI06skbkQT19gBTHAFpyu8E"
        "3qVNB/rDl0h37JCGeGH9pY7NrWghQvrW0f5GeHOck+I2RoAb+HL7fT1TXNDz3UWnwI97BOrpqdtftwcXOQPofOeOdTr12ii1JjIy"
        "UhcZqdHodDqDwWIx6OCVxW7mg/RWq7X2xu7CjMSNjBD2xPxRNOcTacY/eLyNiqyW5w9O25w7pFJhFgV+2wyL1i8SWaqyBHH/cnDj"
        "+lbclwTiCOS0mUHTnFpv5wjz9esXfc/gu/1urSVVL1xaj3OuPdu2ZdQV768rCbkVOLSj0+yN+Pnb+jdtTrvlS4Phyx9aDJEqvCGg"
        "xyW0a27szstITBYQ35iYuA0yFUdlU8J3wH+n5jowdrEKWLtcvGuHRkULDBnahje53yEJ287A1ACBFkauXbv20KNHU7du7Rjq7TS7"
        "eN68Qxflw1qlFbq6aBHgZfBbSFUOqBedWlVVWL3Ns60nI6OvbjJqD+5hcc1bZ2F2WkDRdRp1lFpnxkXTa9bUNnvyBRVPPJjYVs5x"
        "uU0By/6A8WYrglJlEu+sJc5c28zvO9WxsSrvctJv35QzjDuHph4dKinZMzk5uV+gyb1rH+2Q4s4yX/DO29UQnHvBnkXwwYULALta"
        "Z3+T98+rO3pB26uX9vXhYglot2RKTMz8DrPZ1WvVuH7aYtajUbd2tNFCKlTv/AY44vnNPxi8xdVepcZ0DMwO9Pe31hQUtLcH6W8j"
        "xk4wagZwYRo1LhiNZWz8HpBq3zfJuBeYKGX3u978ibCyhe54379/Hz7D7QedQztuPTq0dq+IMGCN+47qj46fbGjumDcJprdZVLG0"
        "gF01H2zqMsOcIkxA/TIquygq5dbaxuZTVfUAO2F+qKHjhBW+ve2b0dE7I7GBWJVdT4i7TuYn5hPeiSdxsuXm9sW/v3iblH6x5Hll"
        "OoIMGD+4chqXA9vtiK9aWGhIi8SZwkC0qvYjnd3pfGy3Q+qCZPGSgRHaQI3G7wzRCSwiopevqTEqMvzQLpVKe4F2SG+BJgPGm/cX"
        "F/f19WXQXEhGdXX9+FRDb+f8uU4hrLbTXTItxo8q1Ty0UTgh2N7n1fULbGQgvBqdwSLtFPc2WO/3NtTfycjIB4++9FYvTtgH3RYh"
        "h2QP2o9dr/llEHbDepKiNsC7roNbIg8I/vD3EW+TUSliXRqaurMFdPnYg+sPMTKxEMh+uz3Yfg/knnoWAYYEJNsbMuuEFxIl6tQS"
        "Rr0/tEBoZWaWGIKCjqu9Qw0hR0tIlevqAN9tQNVA9fWFbVUNQy+a5+SZrdVdILC9dlzL1BlBBpRFor5/TzTuYvzOcI/S6EIsUlrk"
        "brU2niysvgOQ7y9pCIQ+WkGdhVl8qQbGvF4l1aOAoIYj4Mlb97iCguU3d/3e4L3LBECbTEajkDGUzgxO1xTk5l55+NhiOKLep2Y8"
        "uODzfX5ECoKJKNNVzVxCLr6mmsVGRsx0UharEXYX4MpT77RGp1S67hFEXHv31hFlZNwBlCFL2oYq3VM4PNob6K71bjWb7x4oV9Cp"
        "aU5tjtMmWNX7QLNFoJmk0m+fntPhUVFRKq+gqCGquw9JV2OeB9S87schh3qtHCAu3IG1WnDaYZEFPuEB8OJEzMjyi0OCnr5T8dPf"
        "B7wB5YoKZZb83L8upXdjg9MFD66fRp+MaopGlqlspL/t9VrCfaJGaygbZcRsNVLkNX+D/Qs/1IHlDGVQGr+b1VyQubN36BbAvHeS"
        "UV0fqjNLh7cJtrutobnxRUD7Y27D9S2x88IzCs0uCJ/s2/c9oXv75np0tTpqrfoXUWo/KVajpESpI0N2uF3u5rYM8OZ9JQ0uDoIN"
        "HAWImE2Dtkqnd0Ea6loFeCdvTPzx/qv8XcXE9oXWsUl+p8YbrHeWKRTo2dlLsnvXT5+2gXP2YYZu9rIIn+baLJ31AX1EOEGgyzjR"
        "eBkd9Zdf+lw1+erISJygsDttnWa91S90t57o7JWGHIoEVYqarBPVmaw2gJxCC5DgfX3VqUb37E2iRA5Gs++gUF4ohI8+y/KLX5BL"
        "ttveNLMFMbdv3xYixNvwmkWJNttjJu8k2aDe39P8b9R9nTCYSByO7lazu6geb45HPTrBbroj4kEWuOp6TRDKsNvDXHhxVGfQSkVw"
        "wAIr3n+XeBvP/8+lpaHvvfe2RBIIkZgTo2yaMbLbfTGWwYuZV211R44Q0JFHRKAZvt7zZpPwlZNWDs9aOuwy378qDdkbhUUd9u8v"
        "TswXVg3jgkIEOyUlhdaT4vbR3oV8tCM3p2B6pJJocHBwevrevbAu3HtAt8K0PqBRW7/x/hWAD8C3W3Ro6QQbRhKLbAkJ0UVGruvs"
        "qPJsyy+OmjKztRc4l75DhRoOH3DljRkHQcPz8+se8bgj4V/WnpeWlprGZBKpdAf0H/VP9xWIgZozbdVdO+JV9EivZv9gLt6PH1Nc"
        "/hjXh2NOyvuvMe+8OjQVArkUAk2VHIqL63xrw5KSEGrEvdrjGa86vrqxdgGVzs2pCQ+vrExNhQBTmQ4/qQFjM7LpY1dsECdr/fyv"
        "WofbCfX/rJkAwBIST8w7BesHYwU7BVYgZGjoZFt13+TeW4KOu3jOpl6kjY3EZZTlRTiq/OT8/bcgBQ++Gfzn/8e/+Tf/5sPDv2u8"
        "KQQ3tuS0n3biRmu1hvZjCng5IaVeAPEvffrtNexHgBjiP5iNt5SwftO3WBTnRTqllpBHFwHlKG99lq1bEw8eTCwu9q4MI8rPT1qx"
        "bVXVaLN7IaALalrCB1KVAenZaelp6enp2QnZAHfWudDU1twrFg2F35R5gQA7bV81B+CYT1+HPO5QdQpGD6IPp1NqsUgb2lYUF5f0"
        "WglxF8eZ1YtUi35IAVwbyXF+/v5erCEm0FP571y/lf057WCpMAzToYFahzbK4tVSH+IW5sDJdKMpvzYr+o48IrruyxZ/P2B3ms3C"
        "0pMTnTukU4BzCaTNItBb2cZ8/HUQ8Pbb4lVX11d9tK2ht3FeLu3Amms1LU8GUtOVacqEtISEhMPpaUpGNKDTdojGab+4+ogBeqBf"
        "GOKu9tz2goKCGqIWL4W31AgEX7bnOrq6HF0vNPR6NhEBY5aCfdwxNN52Z3/dlMtKXhwA18RGLbJw0IHGnowkXPqWv2dqHLgQQjS0"
        "UqHc9TvEOwF4Y9FRwMXu8KxbhxDRliz97KVgt9k8Fybghmvzki2NqN3MgYtwO83sJqLraoi3OAsVXihOFIpuIMwMdLaDkz7Nv+Op"
        "KlpgbgzddE1N+JNUIGV6elrCYfiXkC5OFBhLFa/351wBsFWxi1Qag+XxAkiDtADINeE1LSODg9jQcvwF/gD+CZTKaPnyMfgSooGR"
        "6elpwr69/QWKjzvdnFIpBidXm4fv1O3p5dYwwPW4QtKJLnw0g9Y6JucXUwUi/LU5JGixIvt3hveBmgdOg0aFWF9Gj8Riqa91cHwQ"
        "xC6XdbPVe1a4ZmG67WT3mlxDj/bA4Irr6vLRQgMlitgm+uggyUFd3Z36tqJmt6t8PtS5APVAagAgMTCQBnQYNTtdme033dtfEIgz"
        "aLEUkvHzkG4HpKdHRgYZngK66V9FKAYiDTLoaxD33AVwB768Cc79asfQ+OTkEK2nBpxt+8DKYLxe68kXw5KMjBSijJD3l7yx/dvH"
        "G/WBWT3Sa9RLQFr/jW5Y8rdtdh2bWImMBOftteUEN/ywe0yuqcioyb6+jDsr2Go/f7y9REqdUb2qqqjDPS/LQqDDWyAiq1RmZ6dl"
        "A87padmHExANpfdOcgStj3xo0YCzngs12n8w2oI6M9uA/9LpJ105j3xwK4UYkI6s9BkBEJZwMvsFOXOR50HRdwwdjRpnC+g57jFE"
        "EQYIX8qLMpL9l6si4IknQcGNvwP97j/20K6DiFVnYHmwfsEIBiKKdiIWXcwPZMx2QyQqt4g3Q/sy/KNVYa7Oqb378+9AkM2kOonW"
        "aObT8u1in5rnQ0YdMhpoXTAmC39SORDBgm/kfbYSUTAaTbQrzd9YHQO0524fJ5WuGfEBLcKpDPBibZxLdJBRPDQrK8snBkpBCuA/"
        "Qz01dWRwOvzYLH3n9Z1XOw5FhWCcDjjzwGetjeM5d32+P9aEd9uJlYJB//bwLj3QimCDgyOs5ykD2Dyv0SOZFkzaMviXOjgygr6s"
        "3Ts+vhNSuEjCW7gNYr982YmmonPH2snJak80mytJSWFDxZCFdBxj8Yw71W0NQ42ueXNkmGY9fz5CLK0cYHqWoMxCMAjrOYvmDrRK"
        "nBadxcb7WYX2nLDpQVGnfbqrVB5GgfnA+JWTjUhGE5tbJuiNWVnp6dADoZUElvopRa8wOHh32p8rro7Avb84YaX8U39ErdKBsbM2"
        "ZMxGG6i64+lPv2V7fgAMuVqrxnkTu22OMhSEj6SOjY35nJvPuykFwW5SLjPKnz2TXVp5rL2Lxa1mqUFj8N32uiw1oxgcmpzsafN4"
        "yso8nnqaMREQT0bFBqi3QUzWWMsvMHWCKknCllqZns1Mr3J5ulL54jjktNPi22VKVmFEEFafZcBfpKsgMCbFf/VNJyAF1cffPwtI"
        "z6IGl4ttVzI/Pzg4DZgLetBx8aLL6nJBVmZTaV7DkM3tyZgFdveGsoxOLlix69vD+1x/gRRniQwUTfH+cW/LCNPjdH83thxYlBWh"
        "jIgA9YrIBnY1ZTUZf5Y1M3NWJrskW7nk+mkz8vm2zaITEZeCELmGSvr6lhYW4lYdmvBmk2Qsqa4+Cgk1pln8Ahl1zZMnlQFjoEtp"
        "kGFlpx9OWJYewIzui4a0cxr6wIwUOerw8BEytZWCvSaLzAZFmP12ZiQR+/QPfvYByVD6BySVhHnlyHR4O0N86tAJLOINFh3CHBdX"
        "bq3yh7s7Li6uLKOBe/7Tb0+/+3NtOCEIls8XhTsKasB8p84Ipor9yTLOdm3w5ry43mHgrZGn7WFhQYFSWi4UIpXe53HPrc4itVt+"
        "6ATDdWuyLsMTQwt6CXMEvIdNfBc1uudbbw5S4YLn4eGDqWNnBH/ZpMwiP03a9VUZZY6DDQWNU3h45fLlkEPREJanf0Bt0CjQNH8b"
        "N5lMjDfG9HTGt2U/U/5sbGxwmml5R4iL19/GkE2jtnHl5btTkjYA0ljTiVFMyipX+4cf7fqW8M4xGzAtdXrBBo2aFjy1UrB3WSxa"
        "MTIfxoRZKfAqQPbWu0ukO0Lw7uTaqKi9a/fC37XwJjJynZm3gXI/DuJco5N128pwMW9cGel2dX19/dKlx0c7FlyFAF6k5jmEC4MB"
        "AWfOnAH7AVA3AejMU38NSgmtDmadQKdTx2Z56ixBYE0ifVv3FcHPe6M8uTHrZ8qAsTNnBu+Sjpt38LdBwfW4cNVaXl7roV3CAthl"
        "QDFJbkeT4tvBO0cPaFu8oThiXenHoSwISYwVBLTCnzv0MiFipUwitazDxX8hO3o73W43rsjDW1reWwocb7dxrnVYnwVxBq2uqqpq"
        "aAhsXvjmNIYLBdNCQFUZEKAMCACllhvlwLybSuVLIJTQkuvIae0fyMpiRgF/mlClSVj8Gvi2wPbnEYqU0mQELhqVWU2A+MpjDtq/"
        "eBvvvh/Rqe+Dguel+MAm+xeTVMSFK7b/9vEu7b9iV2m8wbgjt4b0IR1MXlZ6QpbSWIE3RUFUTfMWrYUaZ2SSh06LJWSH+ev2Z7lu"
        "PVrXOzTUC7o8zz/PCr5bn6TOgB6g4QaYm5ZlBRiXyyuUFabzHwDjlr8MQsqdLZVvKEor5ORCYQjg9UFMEOpS07cO8cJhnem8qcKU"
        "bqwA2FPH3ipwiAsuIDq2kEHvFjQ7RqAyjzWnNPu3jXfpgRynzsD2uVNwNkJ6TVqB0xaEcqliPpdKs5SVI/ck73c+PH2FPTHEyvO/"
        "6R0mzIbbC46BBwHLfSYgldw0QN20nDlapShvLwcWHpQgJMg/80vLTf9yz7MoZYlcBSi50QiJzmBYF1vJaDeEaPRc+Y3ubj+skeJ7"
        "3Llf/E/Zv2W8D1wx6Oy8EJ5NDwpgs7jVl8/Od3MmE6SdkFzibQScRb537Ni9Y0+PhT0NCysoeNEkzMIaTVn94EqZDJBediYroCnr"
        "Z01NTRNKb0zlc7MvhRjyVZkONglZC56IuaJvwz+bvunxJuU5I4I+A4gfo02FnE1n0Tg5rrbQ40OaaNjTzPXjUzckvx37wsLyhwbK"
        "tCEUHxnxplykEabZh7OnDYhDLDUKEXLpG+dNpooK+czMjFx+Vn4JRzIGGkop+pOWJ+zG0pORu3en7959/hxyIoi24Qde1ICkAKWe"
        "AfeBc99jYwCNHAyeMiArK0DpF5UhgpjpyOFlamoWKoufKo+1tHwRCi67pbLUbw2WUQm6VHEOqAIYbFoQALD8mLqfh+sqjN/Io+Pg"
        "S5ElL53ECewyZQHewLCxsZl22kiqN1gMFo4rr0qZjfYw1ujLUSS8DN6+LuN68ITQ0NlfgT8jXpaW1jgtiHYuWPExDMDTMaBZIPg1"
        "na+AtrKyTKXC+NKJo2x2CdUIQqmKsRm57G/PyiGuwgCPjAR+h3FKlnzm0spLcvlM8ETwhNE4AVELnYYHNjGDglhXYtNZf4b4mOYs"
        "oTOFSh7apLIZyKj14RUmkc1woOyh3ckfuxtkk+pzs/xPAY8tT0/YWZn1+oJ4Q5vP7l3Rtw/KpDab5KzCpExIUChDjcaXANx4ruJ8"
        "6LOxVOO5N4wvq90V5yuAX2fPmUJDz549++yZfCyXypXYf3AZ8OZGU7xYE955ecNtvCM47cV4l86aSCSqkCC9/R4EC+yi52X4/u1/"
        "9R6ayYoavR6DceayGdcrFjJ9plJsSCp9++2K0EuShw+lD//dMWUpS78rjOSS5CZcBhO5CFqWoxVVemeX8YXxjMQSEilZOQOGGoJt"
        "IIzG4DtIsibwshB9G+WSh1LpQ8mxnaXpcwSu1PjfnZUYtIt05isG1SLNlcFQo9crynALuU5v1qxfr9a3+820gYWCHkFnJeHpC41J"
        "qTgrsai0OrNdo9IaTl96j3glMSm/Hm/Tn1WE/qvISKlUKpkxvSzeoW/jCZGS0P8PtzEteltmDBf20llw10VjilhcN0+g4VUuLvyF"
        "8ZpRUXGg9dJ5hal/5L03wEbBEI0KmR0X9NofynbSnS+j4tlpFe1yfftZRZaiFTS7dSfYX8xXUOWVL0hrjYoZG56nsh8LfWDAxbt2"
        "rqbUN+NSARgvDlJjScRFb5+VgwhMMN9JIgQ/pnuWRYBK2JgcYrCmLLDXWU0oJigXxgoko/H8oE2NGzf0ufOnukznZBZc5m2Q4m+7"
        "5By7/wVKMyPV4EcW+trCtZBFY+qrkD3UYF+dXM0CVtqUpZA4teKpWvNDCx6skj5Tfv2zZZSllRId7TIx51S8nDUPVb5nwL0Gar1E"
        "hxeKtVzfOeZAvMGgY6WD2m2A9zCYcZGOVzW4qKSLZOEbmZX3pDqdZPqYRaOKlCnOQ8ZXUXqP2GDmTk+XopmqKJ25QhUFnU6J0ViZ"
        "k9OSGmpkUylZWRWAdemC0lpaUXrJhuep+S5JlwGX1zu5gnPgktCrUxwif+MSr8IvIkFuIfFZjsmPkSawwOSfl9nxdJX+rilBOWFc"
        "jpHzBOL9gWhpTaY/Mx2ja6hcXZXA0Dm+75mE4W3Akjr207JlFczNmC4RZustOvzCAsgmmES8syR6NXbJxrUr5hlpsG5GiT12fex6"
        "g4YGZLZpCHdZ6NchWHo+vTT8tDAix9hL4V1hmpFIcWuChnPadHShrpGKAqpAZbHjDL/VExOf56OPq443Wjku58OF8QbFlGB/DTw2"
        "prFBr02mc6CMDG+z5FwFCIDxjUuEt4rnH85kpaaCsxSmzL4qgAXBeUPijCW8r0h5Ae/2LC8qGE6dl/AkSTabTD57khJMfugxJ/ZD"
        "Y/7lWYVxwZmtUlPo2TCGN88Nls52osZz8mdS7IDKjO1o9VYZOmegCpPsJzhstZ6+/glXUCrc+YZOy6+LeHfNwxsnvmSnzXhBpx1P"
        "1fN6hjfYDtPcNZtz2QED4p0qwpuTYfBY+rXh8c9lZmKhhjebCW89P3KukhQc8LYB7IUxef5ERem4nJsvwFsxSCxV21BkwWiEAtw+"
        "vPWSZ+CZlaHnZALe3MNLoNBsOjzL+NXpCrgeE6oCCqfeSQKFOoMGwcu8itB7gHcsDkMCEZt/e8DZs4zzdu70WYV/gOCz24Dd2XZb"
        "LOvb3TeUsyw6NC+Tun6oVTvxlrFKynGSmSwUmmWgNXqzTqsxQ9ijgq+5sFLR0pvkZ6/zAt4Ohck4L3yqkHVxFq3WwusNKpWd8+Id"
        "WnF+dtpcapqFOIoZ4s30G4SzgqzcV5vzigqJXsCbN9OF9FxLqLIAMbU47VgBrKoMtJoIjbmbpautC+GNKvPGPeKWwYxc13FXLpmM"
        "oRWhXQQOcOPeM4hpIUSUmZmewgEsiKaA/CvhBv2s+Pl1wlvH8TaesYXryqoQVAlNY0XoA73AAMlZ0bGzVs9XVJx9wJkNWCLz9qAC"
        "50NFKfEKq8kUcG7GQX3bx3P3ziuDWXx5XmTws/c5nhVBoYVnx86mk3pXzEhoQSjtO0HbGB4KYoh9hphC9sCsYn11lGL+aZyNt3HM"
        "gQvCqdImTnwwvPWnQ7O8sw7nTeIqfL+8X3ku1BR6nSP0mH6H+qTJaCwVbP5sb2sy3eMp9gAWevE+p2zBjuPaT/iT1y3iPVx0g81F"
        "5/YfnhufE19Dz5mMErMmdr3KxmnWx8Jv7q7JeM70rEvD8OYA7wrQx1CJeT3Dm5eh/4Q4CTihnI23UTkreysNrah4dp3cpw6Ek3QG"
        "8U41iouGwKya/kzAm0e8TUqfm0ExO3tP3CA5+EmW6LHP037DA6kmiC6V57NCLzmYbQK8Q0vhoufeoYS/FCLpv5GfvUd7+/Rs1rfr"
        "bkU6cyMzstkLRKfPVWSR/y09NyNrJ3uNfS2tIOhCoV/pbyDTAG7jWPvsZcQ0MP2V90R7jpC9cR646zfxQGn3uQo/vO++EfpzDHEi"
        "Eg6nMyHFvByOewMjx+Uig55d5+0UgXgvxLW8oaz0w/tUyseId1FRXpFw5yFnZ9rhefEaNA4tG8Gw6e1YTYj9Bp6dCz0r6xKa5u69"
        "Fxr6xrmzoRKngDc3CMHSudBz5xYbxcmX83Kw+edxCqICpegcxICQxELcDoJzXScKpxfvMabfpW+cB8fx7L0rZsEaXz9rPGc8D2nm"
        "+XOlKNjnwfxJzDbzm4DVlTGT6F8rTKGYwUFKI5G9EWDMOncJWUh4S967BGnjfwtfhFILr/+N6Rk4W7sBl8rYzTwPl8DpUeN/xCxQ"
        "b3YK+1OkEIbeTa2A5FipHBt7JusS8Xb8J3mF4o1n05BKnr5S0D+DrVYYs+52sUlsPdXtZM5ez8uE6YsKRWio7O23IQtl/TAS3KGh"
        "8gr43A9vMKN//99jtip9eH26ZTEeGQqiBSN4+PDNBzWppWTKzs7Hu+aNrEqcfnSS/+aKUki5i4qKfMqdPff+d6kM6b33ZGdnCbre"
        "9hDTbhmBA53iJG9LJP8LpN2Idyw4EY4bwYhFcu8ecFVJ0jt29xjQ9M7Sc5fwxbG7qQrl9LGwB2HHps/KTl9jeIObU7Hedo0Z00FU"
        "FFksxZectgme4oEMJ0HoU1kFpAUArERqUKu0Ko2TrzlXymbkzytCJZZIlXa9Vq1zHqtQZJ2/xGHyCDEC91BigeNVmiOXpbJQxfLz"
        "f2MK/bnEqWOPMtGqLXyXDDUVLZhJdtpm0Hq3DGsNfAEEG5LrSBIf3qFy4JQU156rdHa9o6UUk8ksmaSLt6jUGrWFCzKLeHMy1O9S"
        "MD+Lodsa2n3yA4skFKfSTAqav5C8/fZpL973zp9/73/4IbSsVUHbtusyfNB86XtSiw53lhk6ra1GhVJulF/n0UTGevHmIaNVprcT"
        "3k7Cu4fhfbxXVO6Iw/PwTpXixiWVRnJX9sDvZoUT97Gpnadv4/5kxNus0X5PpdWd1gNPtShkgLdJZsfDdGbMoErTr9Nqc5tj+tIV"
        "XOdyRN8lK3DiTm0790ByRYNygufpMUBQCXibFKHTcMw+lU6vF7Uz7NJMaYuUVq6bc86er1CGSi7TnnC4skHfqjwPLg6gkr2t0Qrb"
        "utW2HOO5UBnirY2FmNAiPEBqfaz68elBRcXfhIa+J9XECnvA12t1vGMEjTKo/jOJXbveW9YLslqu69I9m0alVl8DxSUHgX1FE2PR"
        "CPvMVXZ9DvQCDLrsCgcJ3vpYtFsMhguAtykd+nfedFZiUMd65ej0f22EULDi7kMI7lQXLLwP79C3dWrv4+9iNV9er8kqfdt7sUU6"
        "fW5laYVx5jomNthBvFAsGkLAu6lgPt55iHdu+BeHExIC5qxvMSqmWZ7kNDtksmPtDkf7sXthYVe6yHSApvDa2EWx6ttgtTQsUgW8"
        "tVoUMm5QbrprZ0prvvSBMTSVgpv1No4/zWmZCus5YRaDe2imPayX8Ua9gHc7ptDGUtMV4Rj+saCdYZfO/utj1DKM6VhoeqjEIKCt"
        "xQy5FcOF8+feo3kSBhI01z7zTILRslar0etE8PAAe5fsDYRb7UVVi/GoI1WRZQI/SnmDePwiLa72lPBkabQ4dSWIe1fFM8mXrOR1"
        "LItDcs9VyLPGLj3gDdCtC6h0DAY46y/OL4fAoPTSFYv/Qww1fA7EOzNhZrUQEYl4S942qMWCBOQrb/Oytw1iaTmWo6eaZgBvnCIg"
        "vFUi3unyloXxbv0iIu1wwrz9RErFMdIJHQ8hjGyQ6C/Avj+wgEgiqjxyEKMzCD5j0bLxdjA7eFHH4EzFPcHC8BLweYNk/HAkPH+B"
        "gcUz6YejzXo18GURzvO+qaWED/GGKPidsS4L1mcAvO1evGdCGd5w4fbQCoSbqs8xSWunZD9UolvvxRsNxz0Z4q1SaTWaWFY3QWCX"
        "+cqzUFAh78G0ldPM1aBjr5DZ1D7lxr29wDgbL8Z9nFNLE3ZclxxnXbU+ObJwBRijyBne2ll43y1NB/Mzdt2uXe//YNLL3PQbr18K"
        "Mgspnhfvh3bNrDIUmtucROO9GDah5nPlZy+d9uJtRmFAvN9Ir3gB3uEDadlp8/ePGRXtFkFfHXdly5ePjeFWlzGZw7L+AmSWMIpY"
        "4OARGPltNcObs4M/0toR77GzYQahBw/Ozjy7a74g4A1nCTEdRwfYMeNRoR7AK852IfZCLHyZi+F9lklG8y/rIcC0I0o6hne7BeGB"
        "MOHKfyOT7ltPVhi36AGju8ZAe86xfB5SCR0ZTbDQEgln0Kppe64KC+aoLjC81fz19yQWksVYNTpgGIDKAuJmqsgKfWhgSKuxjggM"
        "GfXb7I374MUFnMEEGy/RULFtLDYSy6YkRkopT9Qhh74EheDMahgYWLXp/zdBqTjbblbh45G0+8T6JMCZwfMyB1n99X546w2Cl6Bn"
        "V5LEo3bjDrV9WhLz9XYu7JnsCq9D0XqMeIMyMnteMeLgOdx9ifl3CsvH0H+HZwckLLBfMKu03XABLsTwHlMupwlrwPsyVrxCnGL3"
        "QRRBeOM19NiX7zG8/xrw1oEJvAB4txPe9CQ2AW/GL45E0kl4o+4h3s4LwENAsh3vexlD76LYEt5gjVWLCO+zf8bwBkG78jZNWoL9"
        "cur1ZgPKoMykrDBdt5Ne4o0CvVOlgas+PM0D3kJdCJ39lza7mgEOJlNqIVgNWBwBy0mowKAPYrBmI2OgclL6jGM2M7xjRf3WqhBv"
        "XiI167RYF8lM06BoUHJNWRBEcYZFcBbhTfu5AO+CUqWydITj31THYnluns2k4UxJ7iUZP0+/KW1fr7VAmG9hEyoAoAGLMPG3bTp8"
        "XMN6dRAnQ7wBKhUw6k0VM7qQj2UB3rzFSfpd5QG88/Lyqho57ovgtIX2A2eZHDoITVSXEe8x4f5WVpbMAZzDOAucLRZBouQSdAZG"
        "zum+p9bgRcGen+3S4AjtDO9jb8ayeAXOWi/ifWR97KILAt7q1/A8zn4BWoJBhWVlgXr/2V0ePQXKhAEVE6714NJZWTsZBhA0vfQ0"
        "hinrtayGvA1nBiDnRy8AFk/NQkx6WNRDM4djUe9TCc+OAc2JZdqBM86xZC7Q5GgJb64G1FPiVMWqGNwcr9HOwxudlxbDF8lD3iws"
        "Q6d5MVSvkXOQJHEkYwYBbzia8DYi3rzZICxcR4dL1vHeP/K/VPnwJi9M3ng93VYWJtDAN5iFIfAsFrFx1yVXWAfR4agYB2sEvH/g"
        "xGX5XJsnj26NVbkR7+zl8/E2Kiscmn0ajQr9sWwM91jQLYpLIAU6neYxBiwQX1NUvU/EW6PRvIZ4y2YuXSHrCG/aZTNnj9nIxSLe"
        "4P8WUc7GabAEAnQxSI+ltBjeeA5objtWdakwTfPkQeEYUKB9aGlEvC+gcddLWaSn8yUPd7PAC3CINx7t3WrzS7Neo6ICGXbvZyqs"
        "TP1D3gxKxQQT6AcA0D44sWDGeFbyGM2OxsymS1Tq7+0jvOmmIOINAYFaqwkCvK/4LoSieEF7G9NfsOcGFeMQ2nMcGcM7dHDWyqzH"
        "VNDHxj34R96G8DK8WSxI8SuZRY5y3WuzS7Hi41gwa5DoYXj7iIU2LAaEeIcC3l08b3DicrLy+hi6FRqPU6kDNxfA22ScmHHgflvk"
        "kOPSGC3VNYHayRw6tcFwBJp2vga4I5/Mr4FWYOCGNXNwotlxCfDeh7aR8JbLjjnXCyYfh6JFYwxHx5JP5PggFWZmToHfqF8FWTih"
        "WnGMh9hEi+M9AjZFJeDdpVvPwgq9E+ydkBEI/JYZs0yDnB0RVPsYc/ohMARkV33Er+AinYrGVi24PtRvAEhjQbzHZA+daPw17PEk"
        "6n0gLHrEG+N8sgakvID3bT+8ORteGRSz4PzZsw940Ixr2BzijSINeOPsvey0P+DgcS+gX7tyGo07E28SKsIbozLqAvgoLc5R+J9J"
        "9cgAgeu39bjfluHNjC7Yc+MIugEnbqlb0yM+WraWcwz4Pzzaq9/KrJ85NEcMBlz/1HVpRv5vceF/qcn01126a18a8CFqTsBdhyjZ"
        "9mF9EZ67rdEZdGobHn9Wpte+phbwhpjeLvABh8IiL/D6F5gJuh20DwRFYyN7CqDAl8fAuiiNZ49RJIeRP2onWprrsmeyIIhNVJjm"
        "mG0UpsTSTA3NVT+4BPZ8EGQK4zezWIhe/1Cq10PSH6m+7MctUWp49M2Cfhv2MREuGGN4Q5pPzH5zH+4+Jrwp5o4k2VBrXgO8u2T/"
        "5ZV5eIeFPpOdvq1T63RHBLzVJDAFbyzH1Px6l/9UK8Nbf5pzYrBFgS8GsGrCGzqJ+s1bBLz99k3rMXAjvCFFQpVBUFBiGd6mET7I"
        "bLE7b+Ouf2G9Q6Gb68q+uQDeJqU8tUtjMFzG4XfJZGMf4N3ND8Yu3eMNOosF69Darxm+ZHirjxzRoD8FATAgbl1/LbtnvqBmeHdJ"
        "ZJIr9vUqCiPADIp4U5SmQlBuq+fiHSbPylLKAW+qaA18hk91auDcaWhMf20RCyPNNg6h16qxIMDD011dD+7O4O0uUBm0LWoLqw0C"
        "bHuIeOsiUdfESnguFCXMHzh1LGsO1++qQWIfi3irBR4KXBTwRkesY7bgmvoaJqv3RPh43h7L8O66e/deEK8DBuos2LIZ6+2ozYB3"
        "utEIQe8DLHTLnk/nRP2GEAS8POJ9AfG2YDpAeGNQaCdPAX6CzUH62XMVk9Qrt83EQszcVUcY3qGQj/F6J7AAuD6aIaxe83RwXQGv"
        "B3y4AN6mEU5juGwx6Myc/srp0zSL+OD0Fb1Ug5vzsFOGLy2EtxO4hNdAvL/UGfT6n8A4LFocoQHLjUCIqKFqcRBG2yizUb95W2/H"
        "BAmCVLNZqoqEBrCSMYUGwPpjpiz5B6jfVPImiOENJv8nWKXGgnqnUtt+ie2SJquoXJ7T2dVOeJvtaqqtKRRK1oA06B9rwTdpDOJj"
        "f532EEq2dbb3nVjG7jX1Y6yQodYYdAZgYBjgfdoMQmxAkNBIgmFGkTBTXkd4o/Je09h/YnP6Hh5sYGXxHpvNb9psbz5WU00paPhN"
        "i0qn0SHe76RD5vFMctuu1vomcuAUGwJpVy1SaS/YEG/mSliYp/3S9qaNHmmldvo/qhjDXHB/+NqyD8udEN7AKMT7XHrWtF4fwqbP"
        "6wHvOAS8sKSXywnGhanz9buFo+2XRzT+1c1AgWnDFmZf8C09HJMMO+qbGu8sCKUXXrsG3NCIpS5VrJocFsTEInNUXBC/AzuNXlDo"
        "LKfbJ+BdgaHhswdmLQtzCO8jVHwPRvgaTfP6SiCpqXaqGnPDQcghLtkgumPVq6iKl1CuDYu/7PMveucl6gfWL92HABlAhGsQb70O"
        "3BmE9QbdPjwZjcNtPW6r3qcS8dZpXptV5Fis16tm9ROPYGEdDWYFKjpYz+X8p3TjB88kWK9rVhk+EAXCGycHUJXAGSLeeDUq/oNC"
        "/RqrxCl0HgRDJdaO3Kd+DXdZIwultAMX8DYp06f1Zh1tYHXtScJdY7gEvWfyVnnuwEL+21jp0OnwzpDhiO6IAOI16DXeQbdjioDl"
        "s3Q/Qbw1YAV+gFkqq0frq3J4RCMkvWpWDVYcIN3gYAU51FRzzXAZHzECsEIoCHydrvjAWJH1rN2sxQqKPMMbbAfV2mP19jQqoUYu"
        "VndiVfgw/64wzkgwchaq/7MSXqDaBgu+xXGovycIn0ooVfyar+gqHPIDA4hwzbLUwdO8XYO809CWdUKLuwKJj4pyLBB3NZWC0/gK"
        "PoqDU++DfxoMfmhzOhbRQoUwQAu555UVY/9Oqor1K5aL8o/Y6jE92UcuzkIyqGczWKz91+jHvyanOkrsONU9uEwstKNPhTCl36Ss"
        "fKB3GnbsCOK4wDrhoaJlcTGeuqX3HTXBCuVcvNNTHTYdK2XmV10Y76fiw1JwwPCatBItvAGtne6y90gqkKdDTrOCiBi8iVquInOr"
        "EatgUkUOHUpQkFpweNO4M6bibPtPcNyU/Kh1Ytk9jYaVn6MClEKVRRIwjDTuzpyV2bXoSo5ovOU18RkAVGtRhxZYAOg1QTNfEwp2"
        "agQhtUBi7GhJTR28zpmP+Bm2a+hFT1+hyPF7Bq9V89ZY9iuDSe0dYcaFceNLJnaQaJ7Lkt9zqmNnFwTdp7rM4yMKLfB+H+GNZg/x"
        "NuvUYkXJfWIB5TnFgcmMwRiB5yA0FsTbAiMwKVP1ertlBzrcqXzfI4NjPH19V7mCn8/T7/SsXM5psD+eXUyaamVZmPG1S6X0wq6x"
        "E96c7ZqFHXtZLGN57Zq3ACbaYqB9atWcmqdw5JeXyTHo1bofGDRevOXtkOIzvIN0Yi3JI2JdXGIx8ktzjVXURETuXpJJdFqMxTVU"
        "kw6YgJZOrNVHp6tFM4ia8prQmWveqpw6PecYqUwdfABhucZrIq5h2OO4B3jDwaTfQYYj9MUcvL/nhcFXeoIV9kT7UxA6E34Fp1mx"
        "EKpGLBSp0enpkZQGckt61G8UarR4Tgvrr6jmYn1d9kfDOk5i+uURlEgL+FSIQBwtFcq7eojO8YmK/NH8Df4bRLdNhvC5O+fNtxhr"
        "cP0ylk9iGHoLKRgMFLRqgJ/XCG8dHkERI9ZcYqXxroGf91U7hajpS5ElBoMg1hqdWP70yDWaIjPTR9D4iAn3CMx02bVHKNODr75k"
        "wnGNmvtS51df9jVWxJpOBLxPYyp6RCfWkOAt14TSbbpZBXdnlbH1lz/gWm6lMjV1GvMwHRkgcNU059EuC+Mp0P4Bm6JTq6+xAfpX"
        "uRUa9KsWxsySGi1YQcVMgV6DVktleFPP3xbLp6LtgNgAxfs1gPlLPCJSTyusbMRGC0UvKvFK+5i2a3SiaQKnixKJGYYOUmhHi3Hn"
        "MTDnTilWOKmj/f4bBNA3eDx11S7HgTn6naBMxX2Gtsd2rHfo9COBlfgZpYYGg4g3FwTRqngUhJe2x9LH3ndmp/SxFE/hzU70Ejae"
        "h+Bdil8Kj3DgH7PWHSMVH8iNJlmXDhiq1rCHrOl9oSk24Reo0u+f2Mxw4l9ckmAqqvNlXjACv5BW7JvN6RfpziLMb3NSlcrUwVxW"
        "qh6N2vs8g1v2QK/VMM9B8jn3ZCzdafZegQrK+RrGM8LHBtttagwvDHPKUukfmnkN5TRwIIzpffZYcfHppGbVPohRLXOfPK4X2n/z"
        "Jz9hUw2sfCjiPdJlNlgIoKlisb4Dgzyl21MXwjHA/ey5UtnieJn9l3YNRHAG52/xmSBdg/KKN86PFThjwQ1THtT1cide+WtIz3V+"
        "iPxmZUtbQ7Emzsic0QdduiRzQGLF5hh+I8qVpw522Uj35/CLPy3hzVpM+zS8fyFF0UxBBAd+xP6yz0pypKYe09sMTtyt6e7LmI33"
        "hrhufGZRzuz7JRVGZWpN7gu3XnrLukP2jYGbHstjeIuBsVlI82+4hTfsA+PgsbAHTg1lMTiB0+7wFRBlD167vdCJ92SD/8gbEG8D"
        "K6Zp+PI3QeWAMiE9XVlZMwtw/kp7+2m7Cl3DEf38Z0jaBC/3lftVw5Vj011mch3CJLBZuPeBz5fSaIW0zw8+i449JEFN+YzZezFx"
        "3+0LqMDY4tBbpFLs0i1BvX1PBI9LqSrn2BOD/dY7pKOMFzgWKt/Z1f6UJAFEVf0Lgx1yNuxl+7F2Qhxv1lh43sLmJV6WyQVh4qUK"
        "BsdGTms0+yhp1aHha5+eZk3fhjQMmtZptd9b4IGgNYNjgxIefa4BvHmQ2QIRov2bw93CSkKlV077Fpl2hfFS9NM05eikwc7ijE3L"
        "bgZ8FbW3KNOXT3fpweEeueaduCPczDpczKZjkzI+CcMJF6xypNbuo9krAWOzdhFbHzK3xJT3SiNjBbyg3tY9+XPg3lCW0QtHHzDN"
        "Xu+gVKbBmFtaanLEuro5BQU5OTlYZ2eksrImpwuif3yyHXhvekBnDXweXtCu1+EyF5szFnIdA1W0KSioaRUrwdbMfiFSS0RlZQsc"
        "FV5TM5J6ZgYicwiGDKLtLMCakuFP2znD+guxsRZL7AUV3rDuKmCUk0OttaRmLU+V8BaKyEFcXlO9ptNBdE89mE01c19CE6xLLS1Y"
        "I1WZhjWPUwda8Lka7biL/Biv+4Vaw4IvDNVHRlpqhFbaw7p4jMFiNWiJCuYTNg4tV0LDqdNdtw10X+k1ncWAtxBIgR+zJ6cYKDvh"
        "hDbu4ooJzT5KQyguRFZ0dXEUx6vUQVw7A4RRa2sLYNXaSkNIbQkyX7Y/xjnLoeJts8BG9a5Hc56QPnu9opHKCk40pVYORAxUYrnB"
        "iAhW2ZGKolWOtPMGVqKW5We5WAw8dSYMJ5t1KgumEPuAA+2DT1hlWC9FQDt+76ionlDNJfWDgKasiYmVLI8E1tINTAeVqj0zU+DC"
        "ocfq1NrX1PuAT+1PqNkI/B1A5VOyzoAbVOu8VfINui/hsBHhUsuWLTsDP+zlmdQzZ+AH/nnLmtIedXlWAk7upWWnNSmV2UJPlw3m"
        "8hrDD2n2hCSwRukbwchdhxlDMIQubHBkztBSB6jtiGxWL2+ki3Pu09ETlvbh0z81eMuI17GpVwOpcK5Qomywi2cejaUfmM9xuceO"
        "dcHRmkj1tSAupxKGHhExMDCw84vKLypZlcJK5GNl2O3Hl52Pwem57mRE+2ONlIJPmARjM2d9qgnGm42DVjY1NdG2XhiCt0xa5WCu"
        "WcdyNd19sqZ4ROVMjg1djcqGCwz24c1U6D2ekJaejoVIs71V6Iiykbzv4DrLArKa5Hd5DZug05Cbak/Fr1LluTxNyTp12n37cDVL"
        "bupARFpaWgQMMX0Z7Q42pq7sovn8EDbNEYlxRfsgqw60zK9Y6TJ2tSal3xesJ8uzlEbTru1GpbwpAD8g3JZNA6Q//KElBEyOjeIh"
        "diJ+X5k67XDphBt47SuR5ekwzjS/KqmVwMO0tOx0ZYRy0IF1k0gUaUKGUORpogmUnpS9ZhnxuhICRouKkjpM54gVjprppzxnVzP0"
        "cyp3RqSnpQHcwAeqxS7U3awI582XH1Nx0alij7daj5B/d3vweeBpy5Sz8d5lMm7PvpmWHZy9DBiTHgB9zhZ3XTcBZKkOW2QIldqn"
        "6CwHuJ7dlG4qAN1Ug5yaIZdEM5/7JEK5QHVY4jZStliAkHjflNW0Xfn6czNLKi3k5NoHzxA0z3I5nIH6Epretw9jl5zUNDS8aVQl"
        "r6kpApvBjR02gzB1YqAHqxecoa41iXjDcJb58G4KDg5muENL2RET2bj4H3ccwOcT8AX0b1n6sukuu5omZNgd9JoscQxCJG8D14t8"
        "KDjDUM4WKlnQu7S0dCy5qzTCx6m5OJlwTaf78ksLzlLQ4hW9+ghmFawyZ26qIIIoGhbSbpycpYC+YGTwOXxqiNQgawvSIyLSsBI7"
        "QJ12OCI9nSo3Kz9Qpj4IsjO4ayeryzxls8nTANFaDsjyvP0lf/nRLtP2xdD75UrlTeXExATY9+XK5fB/e1ZWpUO/w+4tepsLPJ1Q"
        "LleajuGkEHbcTLfiuAJBn7NFAhUKwLdYFnL5hFHpVXBBvyaUi1v1TrwTxlp2PDmDFVeaml6vgQDnspM1jfF5TVM6XBH+EYuXK4NN"
        "2ctSBx00LQVo/5DxzwE9C5jIzprAa9wUxe3m8uU3b/rVqEVhhuuDan8kDH65yai8mY1Knt2UNc3hpIG9k3UJxjTRBD2VG5ugX4Qh"
        "TwunuCdZyizCGMa3PH051opcTkqXvdy4S2FMzw6YdlCVwGvXcGpB5xTSZpziENKZlgmIm9KDA5RYowHnRLHKEvuuHbzaiMN7u78F"
        "8MbGE7ITEojHWGgXi4Ae4+2XaZ0it7QvJmZOrZ4YTyOZ8+wX11c0bd+1HUgJP+Dadu0yUh1H/wA1dwSkPXsCbfGcqLElq+mmcvuu"
        "XdQC/YVx76L3+FG2+DEdADbFOBEcWuMf1Y4Eg6A1wX/54Ow03DGSBYAbAwK2M8KNShPG4OfiIz+ElCncuEz5s5u0L9lvuzBcEt8Y"
        "he14rIXZWxuX/yV0yUjimjUrGS9IVU4sNxq3o9igFJ0J83b2DCo8DIxGa4RLEM+U4m44MGKpYfSAApvTKXW+b57/gOEalD0jmgLj"
        "tFgDXDgCdUo5VuDluRL8A1s67q0jgL392d0gm+4x6eFQXWHMbIqPiamywhDSvqo+spEGYDIBKGDk0bmhCfah4mitzMIyGhPyiaY5"
        "O+XCAQMl4SsQnM74S4hjc34E4wyWy+VjPha0yyqCg2/KJybkN+Uz786a/7g30zQRAAq5y+t/jKBxwTNPZ5XjvXdmosl4U9jTvQAJ"
        "J+/atdAD+D7aRVUFthuX+UbV/vzMMuVEMAqL8vzNCXBuTSsFQcxJhR6ABENTMM5sEl/km1hUwpQ90bRssH3O7NK9B37S/WRmoikY"
        "A0ZgZ+qx2YmiDIsnNK0Uzm8fxP13CxRnGOHNOudjhPvq/ur4mPj4WXjHF+5GLRQWqc7DW+QCWLlsGIDiT5dtX6bYFUC1uMO7qK6k"
        "o2AkNWAiuOnmzYmbExMzKx/g6PkwnDB0hJ1pmgjervhTaCF7QkF/4dVNsfXtglz+Kd2BZSIXfPOmfAmbLnG0P195Bt7eNP48ePFi"
        "efBKyHxAOa7ABRxBS1YGg9FTeB/FYYLrgGhAB653eR8T2HVvZfCEPPimYpnfHkhxA+7NCoVi8TvvvENbsLNnbaFnFZLg8z8FI5nd"
        "NHHmLYHLXQWDqU1NwRPBSsUnH31k2r4sHfAOuPfAgYMdM5kWv4Owbs/etUD1G0DnRz+Xz/wXQbPFVvaWaLeg8TPB8ndo8+o7/zl4"
        "5i/CfBat6/nKs3KTXN505q/CsJbe9ZWgBAnz64OYKh1mfHoKliEs6RuOn03R8cNVkIzlDix7UT3s0nOhoYsXL35dLleUyoHr9DpY"
        "XoERRSWWxNpZCclQ081ghRy/el12aeXKe/fuvbuESCZvapK//jqAtbiUDsBDFIrX8SP47B3F6/SJHL4ubVrODli8+G8lkiVLrl+/"
        "d/evVsr+drFIr8tk0CJ+JcFf0PYzufyMvDRb3F+MB8llspWylcfCch1WK396ybuyGbAX8sW+RuR4teDgM8Fn/kHx798J/bvvf//7"
        "EplM/s7sBzH8w9/BJa4/ff6WXHH+/GL5SplMIllzes1DOPSZHLS7SQltPpO/jo3Lm2YurVzy7rsS2cq33hp8ciYY27oZ8MXOA18M"
        "fAHJ0pOBnTsjAhQJCX+qOBMeHn43LMwLOJ87PTId/vRBkJXnu8Lu/lXwypVvPRl4gv+fvLVSflb+F+1MdINO3wsPf/7kSfhbwcEy"
        "SaCZp/Lbxnklu9IVYw69QUqhj7VkKRZt8aO8zz6LL2zGGWNxDfpcvEuB938C9L/+0xLJW9k/fe//+T6+A148x/ggTTlQOQARckBw"
        "1mLlYuDc9/GrJX91SRIoEKBC5/+JZMlbMvgS/tIroO8jajLJEoHCB0rlrIqR5E+kUmlgUGBY2MqVS5aws4lwh6+Umn1X8v21ISF/"
        "gic//aJUhBuuH0Lfhz0dfGvN/fud9zvXnD4mgU4FBkokgdJAHwUBhZ35uz/5/qHIRyEhtzq7wvoTvBatdLFsydRUiHRHp4vL7Q9I"
        "ffounCGV9l51Xg0MCgt/8vc/n0j7u++/HbKOehP2XD4YtibohNkcRARAtARH5ATNptzwUkVaa9BpOMjlsopFP7vuhud24XvAm3NM"
        "ryx4N3CNeAYiOh1GD4PFA+goq9URJoGODOHz463Que3zXG+ueJuEC5msyptNn332WR6qt2NnWvqCeCsVK3dc3LNnz507R10uviD4"
        "+yWTe0pKSnpr71tzwKRjPp22LDsb4m25XHJoLxxZ0uvSdy1ZM3RxT8nFiyW3XK4T0pI9JXv27LBa7/fuvVhScqgXXt2CT/ZcvGV1"
        "uW+V4GclQzyXe+ape3zPRfwGzj005eL49q4T43uq8YqMeq1D0OqhQy6uc20U9GTPLauVc5B+75oIXXIo6sd4bAjEI0+vuA4dPXr0"
        "4i2+vPPRXmju4lXroYsXL4bg90dDQg4d2sFxa6SHSibx4UX7L/ZiNCTso5pYGSg9umfz5s/hc+xXF3f1Ip4LP0fHpyB3zRlYHBwY"
        "EhUF7V68CO/B6roPeSmkF85xcK5Dh45CV+E0uBwMxtHan8tZQyIvXqSmjk5dxa3Y7Q6u4+jFoyFHj8KguHbO9agEXkLPDx0av3UC"
        "DjjxiB1/CD6B8UCv7+8QO7dDuOnhRwG5+i8Z3PzUZF4R7iqhGh55tL8E63kUYZyRnbDg84lMinfCpjbj05u27kGJWRJSTQ926uDA"
        "oAxM4ON6AHGAe7vyT+XvHsLv9nfAcffdbfSwp80hcN2r+/FVINiXQDhgM77iTuKhm4HJtSX0MLDNU3ibxGH9MXs0GGLw+VEsKuOa"
        "9H2yeX8zN/755q2b91u5jpL9m1n7nKMFt/dBnBe4hx2KXe2yuvAZVJuPwmWP0mU7Xfu9Tx7D91PQn0NRm/HJVAe3bo66BYBnK4wf"
        "7VIsXtkRuJd9fnDr1pOoiVOfbxVO3fz5Xhhg7solHUfZo8w+7yBF7fU+2Gzz51FTiGTH50Kv8cMQoaqCe1J8Ahr8jLMPA4WWqYaO"
        "dY9fF3/ciw1v9aPNQ1z5EHSansBCTO2fXcE0932dnWWGU1FVRR8L9H9ixTWh8BrOtezMnr+fSFDvjuqDG/Gho3ewc4HjfYmJGxOr"
        "XVaQ14GIBJzpyMYwbnuA4i13ydaDGw/ewW7rh4rx2fIbE3GcV3+MnRtCxm9NPJhYjHjDK3bo0GbW9ZPoo7jO4oO+hwdtrYaTA/f7"
        "nh5VDNctgaEW7wG89xRjT4YoPy9Nh7A+eEngVjgbMCqhErvNeGJxA1y2Gs7Zeqe2Fxo/6GusFwVhczGcsGLFisRilNOcYEWaIn2l"
        "K3BSgPvgxsStQncTE4kN+fl1GWAQg9wdUZvZA44Y3if9ulm8/xamQvv9HoV0SvDXnXiY2ImtDeTCjxbn41CKCW93n9/TsrbW1XK3"
        "tvo/UunHHVxj8VbqCvbmxyc4caEKWaYWh1OAm5/aW7VbQDtv9xpwB7Vut7uxsbEZC3GlKRbGu0nxtKF44wokwvv+eB1eywN+hGsf"
        "WJ6O0SHLp9IUz117QDIOHsXjXONbN67ADhFk+fAqGaIEnk5OBAZZ7+ChgLEVDkTC10A76N1BYm7iQWTlus2JK1ZsFJ5Uv8pqrUN2"
        "QKsd+SSGzTS3mQa5y+LgoJCtK9hFqYTGKIkcoOX+MV5sm7UhUeQTXqO4GY5AAThIgG9E5uPWi10rXa49mxnaiTAI7Jlrj3gmPrnt"
        "IIqua0jARcB7nLrIHlaYTz2YKka2bUQoE7EbzAxshR7iQQwuhNhdx94IeE+iHAML6AfE9Vaxt8/JGzeucFlhNNgqHPDpxhXQbosX"
        "rX/d32XRSWmOiX80ebKoSNgDXLRmTh34/sML4x0QsLj9KCL36ZbkbYij+ygN6yTe/S1YlpZtFJPX7emlOdDxTz/duIqeqFB98NNP"
        "kfeI91XEO78RPqU+5nfwnDtj4xYSgVo22I0H26gjIQRicn7iwS1bkjcmwgFTcPlPV6CikRFwI4gb23DJJb5IRmY7zqQFTEwsDudL"
        "4KKfwqcZ2NVyRCAZr+Em0fDUHk1cIWAGEnywuNYKnUSNrabv88d5XOjQdKadG0IWJ2asupO4Edpr40ErN/rhvbGKusokeiPDm6/G"
        "7gjPuspPvHMCPHUi4Y3g5gtCwXENiZ+u+PTgQaElFH3u5NZkaprh3VsnyDY9qj0xhGMKgYfAWYnbrKN4eGJGYXV+8pYt+aOgrN6U"
        "rEZv+dJJhaZcS6PyBGNedGrUNfeGb3rCwni//qPwjjsA4pZPt2xJIbxpWGCdAO+a7HQxOPxoe/bE4tyrdcCeZAwHgGPJjPWI91D+"
        "lk83JoHbOLpxC8CYD69G87ds2bgN+tFbnLwFDtyygvS7/GgifJ7U3BGYBIPZAniXHz0IcpPc1tZWVVXVFgjH4+gbOOHFChxKLuAd"
        "fFMe1lsMXcXLMrxLSErhYlcTobGNbdbx6hXbkjZCH5JXrFp1dBybAMRWucvdyfDhRjRMuTUtT8HAAosTe2o51x3EexVPvdySvKq5"
        "yIOP8krGI10hicmfbhTMFURVd9CYrOroOJWfCBIBeLvvbETDyHoeIrK8LfFTGGBg4KmkZPiX34zeJjEZ4ExOZng31OUjg93NbSQQ"
        "49Brj8cDL4Ffnra2BhccnpzscXNrPMnAy1GcZTMKrtt2xM7W83RO9hV9nCdo9+i8p3n0pysWxHu54qftt4oB7MyNIt4o8snQTZ53"
        "PFFmi3jv2h78enDuEPB1YxLOzfJtB1FEgEcC3ls2prhhZAjilgyAYDw/MzMZIT6aD8qG3Ca8rdWIhgfOqcqHEcJoXPAJYOLtckMi"
        "tgpsGt0KpmIjGZ3cZdnbgxevDBovBtwyNwp41/YhRh4MEQ7iOQ3lVnetdZgJFAnXSVJJkCnrtmQQjVWsGhfPn0AVS7yF3clP2pIE"
        "nwcWYwsgyY1JmfCv3kqOODk5Ex+uTXgHFkPP0UtbVyFO1bXgcLCDq2Zz2loP18+vL+fKj2ckJWXmB2JDAPYKL97jMHBmDFfgQz9D"
        "yq3l5eXNGzOTk5Nqy+E8d10y64rVk5yURHgvxxpApv4uu8FGeT3fMFl9StTuvKJamvhrbc3JEdYxtCoSFsZ7e2k4fxSRK4PBJFmZ"
        "rwEVBg2FZPFJgGjOAe+b/3DGMQV4k0LBWBH5Mnjb42J4J28DDtxJRsAh3LFuS8rMRK67imF0q1D9yEa685NBDtqsbNiI6wlo6dPk"
        "Ni/DxoFfyWgrRhM3gtWgs9ojmoKb5AX360BRostEvDuAMZnJKCknEzOByauZQKEVTKL6gtY+1N47wI7aDFJfcU4OjBPgDTbE1Vec"
        "n198iudWFSdlJmcAsO6MpA0bksZRUbcCHKsSQcUamRxCE4kIQ1tSJozWBZ9ATxIb5uBNV6rnrFxDRmbmBtRvOHNj/irAu456VY9P"
        "d0UT2IEWIJ/OL69KzkxKplFxzWhqUKlcdzB2xDSyCZ98l2v+oZ0ZEVdJnyfPW02xiD7M3cnoAPw/4A/3LLx3oTmHXpcNJwv63UEm"
        "G7CDDHMgLXv7JyLe298Z5FcBX0k5uUB8FRMDiGEsO4QgIgeSkrZkZmb2oOyDllRDT04lgnk8hXgPY7caE0EOkhHEpcmZWzIBl07U"
        "LKb8REeTmewgO+EV3rfnngLeN4MdQ3Bo8jCKJnGmGZDNRI3j2zZCb1KIm27gd+aWDBYZFYPB3+gpF8VMDKG5ocQkds0TDUVFu0fd"
        "uH5b6C/iHZdUVQ6Cj/a4KDETjR32C/DOxJeuauj5FhDZENSMxObZeNeiuCWjvIzjI4Mg/ACjl5mZUSSAzGwgMgv6j8/CpPJZrnq4"
        "fHI1tdBMF0JhDCwqKsJguyDgdWNrkFQoAmBdF1WfJybcH3+8u1aA+0BCgiIhgZak+sPtj7fpR2fCEMOkIpAvhncv9Rcw5bmcgLTs"
        "gAAR7+x3wmGkABEuhOPgrMykxpgkApdrSM7cgOHe0WS2GtbKncwHLanCMD15Q1J0xwpQxGHGaZCHJARxD3Ahs8zKDW1FSxrofS7N"
        "HXwL3Cw/uQLsDjkPwDs7OPg5D74fENgm4M03AEYMgVXQVhLJIQgiSNyWbQzWrTgWNB1F4F0yWeCBNIr2IDl/yPc0nGrUanJNGRsA"
        "7wYUN0BruDmRmSmO+983QhNoAe4Xg0BtWSUEK0nu2Xg305VwgEcR7zIX14GmIwbwTiK8QSAzySrx48ijajq/A6QsJalNxBsOyJjy"
        "tfk8ILzrJ8JNab5hz2S9OL8CeK9ew6qtEdjs4UoJs+dn/PX7R4hhJgQHwDFmz4dQaZLbygHvmuC07QFee579o1ZU2g1Jx/Gqd6BP"
        "KbWFmfgbeANDAxlxr9gQXVaWuaHHSvwr68BICvg17KoGDAjvBuQaghhYBzKSNGxltjgp0OV+v8MNHTgB/ALL2+hu9ICrZux0PI/I"
        "ngjORcufvO3GNvQYLtTqZMQbDjgBzW9IKmRZMgrUliohYwZUk8kAJAuX9eKNgBd7eeoGlMGKw/VXJZWVlSHCKLtJjT6872DPMVig"
        "K4CAsmBlRbO7o6PjhHe6vGHjBnYl1x1cUga4Hs3HD/JAgQnvRhSIpGGcd0EZq2dSittDUhoEiUFXmF88LoY0judP17Dl8Zy1t2R/"
        "9TDNqBHkRR/fQO3LwWprCXOBno/3J4vbm/M3gMpaVwEDktAI3srfgpavHCe1shMUPryDf5ozdDATeoX32gIJrPJ67KWAd2YVN5QU"
        "VzY8nBK3tNx9pyxuA96EHccDm60gvpnotLkqeJG0rdndeQdEJ7MbLOkqgoIe9FoXUs41o7GkR7/i55mktIB38JmVwGi0Ei6wFZno"
        "RKwgU5mZGE240VMmkfbyq/I3iAhxbfnoMjAnzICLkWQyupGSlElXXSVkUR2Id0ogxzdnbIspK4Pg+MSP4YBqazM0nYR2wLWNuuN2"
        "D5ECw2BcK5IpGcH0rNjrj+ppOBD5V2XEgaEoAr+QsiGpbM1xYBFaB47OT6qq7UT1TslgGA/j7s4UJo9uHBdoe129YDqeLjltNuPT"
        "I9+/tXRyaTSz5eK82g0y5gmKwy8sWOzD++c/DeDbUPqarWXYCRd5HXyFmDoG0g774f3T4NyTBwFW6hWELAB8eTXYPrLnGXEAb3nV"
        "hjhPUVlcXH15c0ZM2YYiwU563K6eFIa3dSkKfUpSRh18npK/G/lIrCf2Z6wm1+AjECKGd3jEmTBrH3qNZtedTIb3CYysMgut6IOi"
        "oTXC2IUP2stMYTDWo3AldSCcIKiZnjXeoKpNuGg+880oqdBC4clDfSnQf89xK9O4YevuDKHl+ynQxAZ8zHg0yBbGFx1ix9ELB/o7"
        "hg0pVVXVGbSPy82NQgtJeeXHUwS8G8jnpWTUYUMZpARceRvh7RYi/KRMdkhfL1YouHKaTcMOXZzsW/qxr6I9C84BjZyWw4oExdfj"
        "/VFwaasrAwXfBXgDa6yC18ncRlJz5nBaQIBQ13dX8EfLutqS44BrtUJQU1ZrrcZewvuTiPdq97a4uEJ8jkahdbgHtKQRhTk6bsMq"
        "V21PdxwwD9mBC+vgCjig7lGwIq58YVkluoZAMqOZfostKcTKBbxX5jbXAR88tWR6Ee/ODNwphV6iIaNsg6Ad7hXIbw/jUD42RXMA"
        "eA6THUaNKShNaMMzCPCTtJs2JSPDExMXt6nwBgRw2E4zVwSCQHgPwXvoOIOisFH4BBtByFPE2ZbaOloYDJFe2SaAG2KdeuBNRnP5"
        "cegs4V0lxDgk+MdZwG31pMRsikkRUvjmbbTMFFq5I0QY1sBbj5aW1LeJZtyr30V5oDI1aQlfVTzdi/f2mz/KxbhqQ1u5q0ywzFwJ"
        "jjOmlpaOEd7CXf3Sd564juLoCtegoUROl1vrRbxTgE27e5PiY47fSAK8a/FhWKB51qPILrBp27rjylCU3Rl+qyi7aymxEyQAudZI"
        "AkFjFfZBFTG8n5x5itq6IemUlUwvZvhD+XgiJkiFKWVlcQzj5iQ8uZBmF1352A5eluxPZoPfnGPztkxh4W4PatV43CYgeixfzKbu"
        "1eUQtoFDArOeB4LQjdHXFDYs9otC1oakOK+kbhOjto46WhAMRgKaK2uDaK2uGwxGbfm4YLCBJb6du4IF51w9uPysXpTHwG3RZdRK"
        "CsYpVx8tXVq/tPB40W42feqn3UVFedDXgsOHI14G7+xfDVDMAEx1gRqSPbHewQ9QFbnwgMNpioDtigFK5HOeFwAWjH88GK04OMta"
        "v0nEO35TWfOplPiY1TeS4uOrGj3x8TF5Vs7dE7cpztPIuT2bNhHezRnICPgQqQcjv6Jkwpse4g2QodIK0o+HbCCG5D59vjLM2gOf"
        "gHHuQOywqw1kA8kllJXFlDGM6cO444JTxqZQYkKS4JIpRf4baJo9whLengYeBhLH0KbFQBjyjkM7KXnl3Ck07w0c+yBO3HCbMURP"
        "/MJPaCNP0lIRqiIUaBpeTEy3B/T5JKkGJG9o3TGXqI8W8IajyqqZSrt7UD+iRXnkAz3dKIAAOJwxVN82XLR7927vrTCvcgN9vNrK"
        "5YiVcb8O7+CcQGRJmZuzpgj+w40GN4XCNcA7O8D40/AgNxJ07H4dHgSy3bECDgIbYO0BLol4xxQNx8QX1t5IyYs/nhcT/1l0IxaR"
        "gU4Pwwmo74j3KqoqI66SLoRG28iSwnCaG5sbrWB58RrRH3/WTawto/Ac8A5zNJJDBIXJ2MS6Ok5ngudxJ8XElZW1sXmLFGT2bqbD"
        "SaiRjQQWcC9ldqbsZoBvSoGQ0L0NFTsGgCjzRK8up+A6blP3Da48Dz4uRP1uS8FVoELPt+E9WDRuG2J2N+5ubGy+IbZalUTSjE13"
        "YyU0/g5cGvwCVwXjxh7cry8r21SGLYH+x6T0CtYGvqULiwFldDcZnDhgmruK0C4q8gL+sQ/v3YB37oHsl7Hn2aUDDuTZhrLdjaNi"
        "vNDcIygN4J0WkK3YFZzbUVLX11cyhHdFkNOgJSdRXTbtblydEb8pHq3yyW3xMcOnPMPxheWNgHdeYcxnn1WBPIwDznHDjb3HU2Li"
        "Y6LhAw8qfuHu1XkbUKEKcQYW2dPtHektwvvjNeV5pKhkpB25YU/brdBVEPiiwOMoQyk30OfFkdRxjUlohykFK69PQX4zM3kqRXA3"
        "cCgwzzMnU64t3EAlT8DoNtPD+cpSCttONtcKogLdWx242gN6WohzH6sA+JRVjbtjNoCnLfOgTiLex+dMXLfhleLAVBUeb8ZBDWWg"
        "PWsI7K3HVcKAd2A1XiqvsSgal5V6GN6j28CuRK/2a+dGNHMwoBIusOSrCe9ZiLMPdo/Wco4Du17Kf5e2lveQTUrG8AsI2NSAH3Qj"
        "vxxgzhPSPopwBGKMArLOnUpCaNxozss2bepOSkqJi4+Px2+qPIh3WV70bq4X8e6O/ywGb1tlrIIxQUzUg6XBAG9XBhrM8XKECJdU"
        "uiBTQv54vOMMSWFurbw6EQWhjWd4h6FxhgMhQE5BSwc9rEUQ4+Kt9Gi9+BgPWes1Pd2b4mIYstZCkhiMGsrgnOho0ebe70TiuTVU"
        "0Aj9zkn2MMYq722mQhCbmLikjHx8ilsMiBJZKA8oejNGVmhMejNi4Ppz8LZ6yhCmvKobggSPo6eLgUAQr4B9HO3BgUMHdxci85jN"
        "CfHEUOE0dOXYt/sQ+gyX4apT0O/aBoAb8AYl37169Wy4Ae8bcxdEvAhv07/PbRaKvGxiDrWR5BN45KaNzHI8asBRhRFcYS3HD9N3"
        "tSj8cEq0sBwSheOkBwcxnAdHNXcD3vAxttGQwTziZ6wQXC0IQDyyrxzCXlxDC24Nwnm4eJ7Ir/JCBBEdTEk+MK6sgW2KbA9Cx4y9"
        "BGZuYnh3pHSD8QAXC9yCtmiFPXejByEsJNxq0SnHYb7W2D3LXK6d7AODhdHEBjwYki9U3viYj73zMSAqgCp2msmB8LhG1EbINAHv"
        "U6gZ8dD87rl3S7B78W6rNz3rFh/qKeDdgKwC0eeOdwtcwrllD+oD9XoKOldX4mIPDNxEQdDx3USo3Lu9Ki7gXTTaLGz7/Xr9fhJU"
        "n7LJGytuQryt9EkMzqY6CnJaW/uDn+M8cNwGYFuQB/jX7bHybRuQ5WBw/PHGZ1bGA+uKAG8EfBgMUc+meL9HmKIwZODAAcTRpHgW"
        "0RUh3pt2+/QD/BZe39WH7Ixh4t8VxExyHAMb/VojGBJoGDkIPEa8yQ6Dk4+nzIAFQch7NKoQSEIYJspUH8bcw1ijLgnrlUFWiOoV"
        "X9jozdfQYmyKjxa6j3g3pAi7Nk5hqIKGuYrwbpzjI+iaRd6GelP8l4ZDb61VKJxoaqoI71pBSuA1pYv80Z7u7hR86YZOx8TD+NwN"
        "hHZRY2Oj6MWLvDTaWPuyeP8opyOJQkmIOmOwm3HNEK4h9PFrvI/iBktaDxYUI8wToNabPCFcR4+YvBCMcBZf5WGQ7i7nRrtRmz+L"
        "KeIYuvEYCeES6WGwV8A15CspB0gKmMdhdOSbboh7MGo92I8qzGPj4jdFF3Z4GUcXjYuhCwPeuwnvGA9IiruepIm0twhNe8zHLMdG"
        "TSS825B1haL7rq0uwyiSx+AK5aAX+F0mgCBqaTf2GyBnK/nHYYTbMPAA3lZtgI+XQvgAjQLgtbPxpqqW3b7AMKQ7nnI8bCc+pqwI"
        "BhgzDCYF43RSeqsgJfEkd2gQyuI3dR8vx/r12CfgTGfI6O5At8sKn1mbTyHeqxF/tO4f766l6dSXwjvYQVFad+HwquF4SDs3dQdy"
        "gSsoMe6p3rOnZC8u0QoK4urRt6c0u45SkDvEDfWgducNVx2vwnGAz7a2CXijDWd4I6htKMGFHxcdPzU8zAp7TuFxGOA1oDcAjeNX"
        "kTfu6SspKdmz9xHXSea9CPNYMCDR0bViCYsGVO+4Dd1VGOcC5EUM75j42loStsIiwruK9ImZiw7UNXCV1qEMiud8NhYGW+Zx8x2U"
        "9UK33KjfcUXlvulWlJr4vFN5eSTU4xiuMYkobyuLj45fCqGIB1kW10OLaqN6hTNXd6PR8Upp4NIYcmANVcfRW4Mb6MAOIt4dPSQD"
        "Vjb7I+4Jwag/Ojqm8L61eWkhCiN8rwesvZLY3FBUtJqZd/gr+I2XwdtY2uoi401hYW0S4l2E84pxbKqAZYtYwKM+E5NXCF0QGgh/"
        "KARFUQeLGc/wFvQ7GhLXhjjy1nkUnMFHNDVxEp04MHa8DMewhuGCiu7aFhOzSUx9u3ej5SUrzjfno8fIswp4ky/elJk/TB4gJjoa"
        "D0XguzP6ugVnQXFWHMIizkOT0erpQ7jjy7xKZ6UI2dNTnQGuNL6siOd6MRhL8Zrm8lGyB2h0ykESoqOXQsJWFhMfB2OBgAyuBni7"
        "k5hv6e7u9rMdx2miyav0DT1gDAjINUuZJ8M5qRh0Lc3InZg8NmkgOguKHKKj46N7quuWxkfHlI3Oq/AQiME60Me7d4uXyTnwEnh/"
        "FJzbWY1em3rXmAy9B3NzUsB7kzjXAXi3ZeLM0qZuEA0UCZw1jYtDi4MWM0bUb5Rr7P3JMgzPCsGyD6GW4At81iHFJlijm+Jha9sG"
        "FHM3dwITEfIO8B8iAQqCMHotAmMcveljUeVGKRguWwo6eGoD0+9GfCBuDEYN6IR3syPJlRfeEIKushjBkML/Nt9kaj3bU8e22aHa"
        "NwBK8XFu/2gtnr7grCkgW9Eh5XAxcCLHaW6HKXoj4c0826YYgfXlVb5wkRrqxqyzlhIHNOynUJSgg4EwQIxgytgAx1NgRCx0gxbg"
        "FDD9ZO09/u7C4cCtXeWNo2DKPy5ilpyeM/br9K/FO2D7RxHcyQxSatwI0Yy9Lxtl8/ZCvE6+pb0dRhZN04OYVzZY2QyWh+4PNN8h"
        "ViPe0MEyjGL4tjLy2Te48nEwSDGeG3hnFT6MidnmXlOP3g3iZDSPMWWAN6Q5YjxTBlFrOdkOSNPKUYs3dTd6wzh4G9dddGMNVz68"
        "Ac8ooovGCIB6BGNdXo0FgquE+yKNGd5IqazQL/keSvF9TvegQmZrJeYM8WWUM1jJDo2XQ4S/KX7DbnrsMuAFwrM7RYgdAaqUQkGY"
        "XBjS+jwHRYxxVWzGlKS0/DhYwjKEES3csIfElK/HGLDtBJt6SfHu+qOwUCjbgrHzgX4B8NWrG71otx5I+JqHzZJ+Z/+01VW3IqW7"
        "eykpQzNNc6y2VvekwGdIcSkUvxTkQtcg58UJlrgeiL9de5JSNlB1EDwLGAUq76rv8eDNAZzaaEuJji7sBub19nnKCj3Da5gAR3eX"
        "9TS6ewqjo3t2o5dKiSnbVt0LYRiYDbpcWVn30jW11Snd0XFt5SDmGfBZjzhtFdgHEpdSSMu7osEJlZWhi6/v6Sb36KlusIqmGprq"
        "OS7wwlqVIeyK7m6bNddStVTYQutpA4kqh+7B1UXMuPJ6iA2jmaxZMebzLC0fhQHGeaA798HnezzV1vKGnm6BUXFlPW3lYriG168S"
        "G2rAQbDozdWH0+hVa5Z6gLM4UV6VEV1Y2CPEaMCXFCH5Lz/eHSd0rp664CCoEdWEA/1UrqejV0Tb0Xrg658lLaGNlsG57rZTp/KO"
        "s7WNgbgNqSrQevK4935bFfWzpgAG3VjfA5SSh5MIJ6ZOAVE/OXfVqVN4R846Ci9ONdCE0mhe0cdFo6ut3NDJYfiU8Xno+PG8U1W1"
        "jcdHVx8/jlIxBJdeNQ54C9uf8LGXx1eX196C6DNvNcYl+MVx8QZmR9VwXt4wtc+tplOwc7UN0C+Pp/CUN91d05CXV9Tgw7Zj1bZt"
        "26rrhxtnL+AsX11VD194qoTPR4chMgsUF7eVhwATjh+nr6zjyImG8ubjMCpURmsDfhDihp4XnTp+HM7LO3XqpKiHnVVVxz8+Llol"
        "V8Mq+P4UNeQKoeUJa0ZH4Q965cZTH+c1NJCguhqOH199XGyj/EYhsrt6VQMJgKN/p0+BE/r9q6flvgzaDO/lN/tfqnCVo6UFr2B1"
        "ufyCxN8jstbWfnW3oOcLdtxa63Lxv3fDcYidPuESY4DWBLZGKYF+FAdyvGiD0iteFm9FU87LFSob+CLcwb2i3xHcLXOLHzr6Z3ln"
        "fNNKG/JfUrdFvLMjWv0Dvxd2oH9gYKBl4QqMjpeVg65XAvOyRT539ufM4f+ctaao5f0ORw7pdsLL4x2RdqC/1VvGzfdyNkGckJb2"
        "xUBLgYCtAz8Ua9iFh4dTnTkshNeag4XpwsKePn8aVlDwNOzp07AweFEQBn/vvfXW02PHjoU9eACfhXUhscyC42nLM7iKEyfcJ/Ce"
        "a0dnZ+dVIGmvtLe3d2iHQFLvC6l03bodL0m0k9z7Ctq7KhJepXMBug9kNptP+Mi1IFn5ryBMmxyOXC8RHxfkLvuOfckOw+XjObkO"
        "b1AO/J8PH0RtL2vJ/fQ7ISEtLY2tUE+A4I/o8OE0UOeBNC8FoOM4DC++6G8BCh8IaGravj2YCP80TcD/ieCb8uCbQME3g70kl8tl"
        "K1euBKgJ+ndxN32gdF0I0aNDkRcj164tKYH/e9mub9/+b3pH1AfEfuNfgfqWLp11lPimby5FMdrLyHv+nr2zaC3S3m9Ga9dG4h7w"
        "R48e4WCkTK6cTidIjFko3kuIU1y9M+1wAvwDAgZHYCk5rK21c2cEcj9BIHDLBxIiaFXSgZ07+/tbkfr7dyp+KyRZaJGyKDx+hG/S"
        "oXtpgHh2ANXZShO3g2dnBwgUvH37RLB8oqkpQBmgRHl5Eh7+HABesgQhHmqYmhofHz8K6PTV9dXV7Z+sq4P/SAIuGRnVAtUzWrq0"
        "EMhTOIvaFiY4GKneR2Jj1SXfhLAR+HNoFgGgj8YfTSHdunWL2RnEFg2EWKta70IjZXWJyo1Qk962ohIe+Ea4CNDTn50vXF38G+I9"
        "G9qFKQ3rd2GBBwFmQekDQLFvyhe/U1pa+qsAfAwODKw/PPxp2BLEeN3Uo0eHSkCh6hBfgjXDS3e2+chDhH+q2ev6FxODdSkDuUqg"
        "kycbfDRKVFQEMtZM1ChQB5Dbj2qJ5hhoP/oNgnZRmwHjrwR5PocXOkbx2ybJV3z3a4GwOp2wXxjLeSxLQ4WG/8GLS32FBg4cePIW"
        "ll8BlIeGGk4evbhnD9NdP4SBkmZRRkZPD+TE1QLiCCWDcxyM43gIadPQLelQLxHA1+m+jzid8EHj1aV/sTha9NGsim9Lyxc700hB"
        "mFH850EmmNbfDd4LENaAzQYf/Q+lVHQKlfk5gbwa1ApNdd8kENNkL9LV1Xe8JlqwxqtAMUkTAUrSO7YsjmlVeXn5711yJJI37BJU"
        "uKUFgh4Ic7CGZoK/Ef4t2uDflX4vUHex1KfP4c+XLJFIb92aOlQStX//5uLiurp8ALcHca2u9xSCSUY7i5gODSGgtS4BzPK5JQb/"
        "hTH0J/9ImhEr300EkdUAPjw9XSnEL4cp9qLwK4Ee6kYwp5OrU/xe0jfUb8C55fm7S/7p+yEhSyGYZUFvyaGj4+g+yV02oqrWMmv7"
        "zza0CwAxB435aaNYHbxV/Lsg9Qt/RGJwvpgiMG7auZDDTVAg3hHeT9MVv8/00nib0nb2hy2RhlDuVDIe0tAw1Itay9zoN5gk9IHn"
        "B1Jra6uvFP4C9MXOLxCPL5DoN1nRnREMjIEBeI+V7ih/ZL8T6O1AJdFOVjnal1ymRbA/6GbFT74iWPV508Nzolj4l/77jfA3xduU"
        "rjjQ8nSJMFtxtdPsenHY6lNFL5A+AMMJq4EBBowADeN1OpVLZxW9/UDB5I/ZzMOH06gQNPGYAZWAvwikw/Ng+C1Rmu96RBC7Kv7A"
        "6Wvwxok3B8e5/A3zLAPLPFz4kydP8KEX9CwD4WkGVHUaM3Wse58dINbHDmaZerZfCi9gy1D1/wB/FkKBAE+HPyQhaQrlAhqmpNrB"
        "igW/+CMmyVeDPcdnoscLR/0MoPm0gIAIgC4iwlvqnGltNs3CHE6bhR6BC7/oQ79TANE0Np8nzDuRvmenM3HIzhaqpGcz7Cgx/LXi"
        "FX27/jttO2hocPZEQJOSni4wj7y17RHVgDRMzw9nRxzOTsjOBpO7LGFZ0/btAWlpExPs7F/7LGNEBFYOh8Mili1bBq+N21+B8vsQ"
        "r4mz6oIWMqX0xxv1mpQyO/vXWEs7G0tOZ7/i8B9wPkaWVrCvv1ZkC9Nvr5j4XcX7Fb3C+xW9wvsVvcL7Fb3C+xW9wvsVvcL7Fb3C"
        "+xW9wvsVvcL7Fb3C+xXer+gV3q/oO0j/P2vTLgavgYSoAAAAAElFTkSuQmCC"
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
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKUKx6AmgBKKXafSk"
        "wT0FABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRR"
        "RQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH6YUUUV/LJ+1H56/Eb/AJLH4t/7DN5/6PeuZrpviN/yWPxb/wBhm8/9"
        "HvXM1/TuA/3al/hX5H45if40/V/mFFFFdZgFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAF"
        "FFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUU+OKSV9saM59FGaG7bglcZRXp3gb4EePvHSxz2Okz2tmxH+lXMbRxYPf"
        "eRiva9M/Ze8A+FFW5+I3xAt4k67IdqDPpl+D9RXi47iDA4N2qTu+y1f4HZQwFat8KPkyG1ublttvbyyn0RSa39F+Hfj3xG4Xw/4N"
        "1zU8nk2lm8gX3JAwB7mvsG0+Jv7Ofw6tF0zwb4OuPFOpKQoNla/aJHb6sPX0robf40/HvxBCkHgH9ny+060cYFzrJ+ypj1A4FeZD"
        "P8ZiZf7Lhny927G08DGmv3krM+ZdG/ZM+OetKrr4WttOjJwX1C9jhZfrGTur07Q/2EPEU9tFceJvHOnacOskdnA0pX8W4r1C78F/"
        "tT63aNc+I/ip4S8G2r/M0cCu8iL1xuHHHua4jV/A3gHTwZfiD+2Fqlxcf8tILG5iH5DO4flV3zitvKMPvYnDDR2bZbX9jz4NaT8/"
        "iH4pX5VeH3SW9sM+x6ira/BD9jXTMf2j4yt7og4/e+ImH6K1ea6lrH7GGhk/2jrvjfxrcLzn7S6o36gH/wCvWUvxq/ZA09gLL9nn"
        "UdRwPvXt1Gf/AEJiaUctx8v4mJfyX/BE6lFbRPcbbwj+w9pTAG78MXBH8VxqLTH8STzVgzfsNWzkG1+HzZ7vGJDXgv8Aw0x+z9bf"
        "Jpv7L+iAZOBKUY/yqCT9qL4Wk/uP2XfBxT/poi5/9BrOWR1pfFiJffYPa0v5T337V+w3NuRbb4ej5u0AFObwr+xJqygxHwdF5nCm"
        "C78j+vFfPf8Aw0p8G5yxv/2WfCZ3dTEQv/stN/4Xn+zJeREal+zMluxHJ0+9EWPoaX9gVV8OIkvncaq0nvE+hh8BP2RtaQ/YNSsF"
        "J5AtPETcfhuqtcfsafBHV0D6D4l16BT/AM+9+lwv/j1fOT+M/wBj3VXPmeAPiB4fZj96z1NJQPoCa19LtP2ar9ydF+PnxC8Mk/dh"
        "vYVZV/4EDR/ZGPh/DxT+4bq0X9k9c1D9g/Q2DHSfiNfwnHyreWUTD6ZXk155r/7EHxMsYnfw9r3h/WtoyFeRrVj7fPxXS6N4X8Tn"
        "a3w0/bH0O/hAyltqkzrJ/unGfaurXWv2yPCxWZdL8PePrFcYk02ZZSw+gO41m6ed0PgnGa+4FGhLyPm7WP2Y/jrokZe5+H13dr1H"
        "9lzx3hP0EZJrznWfC/ibw5N5XiHw3q+kNnAF/ZvBk/8AAhX2k/7Xvizws5j+I3wU8QaMU4aaJXVc+vzjGPpXb6D+1V8FvG9ktpqe"
        "pQWRlO022swqQD6E9KynxDmmF/3jC3Xdal/Uqc/hkfnCo3puT5l65HNFfpnd/Cn9nj4jWb3Np4c8NXsr8m60aUROD1zmM8deleW+"
        "JP2H/CF201x4V8cavp8rD93bXkKXEQP+996uqhxpgJvlq3g/Myll1RfDqfD1Fe9+L/2Rfix4bDTaPFp3imADJOmSlJAP+ucmGP0F"
        "eL614c8Q+G7k2/iHQdS0qUclb23aL+Yr6LD5lhcT/CqJ/M5pYarHeJmUUEEdRRXaYNWCiiigAooooAKKKKACiilAycUAWLXT76+L"
        "CztJpyvXy0LY/Ktmy8AeOtSGdO8Ha5dA9DDZSP8AyFfRP7IWkE+MNW1YR4/s+xVTlc/vJmx+ezmvqPU7m6KFjcSD2XgV+dZ/x3/Z"
        "mLeFhTUn6nvZfkrxUeZysfnUnwY+LbSKn/CtvE67jgF9PkUfmRWN4k8DeLvCFlBd+J/D1/pMNxJ5UT3cZQO2M4GfavujXr25Z3Q3"
        "MxGTwXNeT/FzQT4n+EGsWSK8lzaIL+3AyzZj++B9UzXHlviDUxWIhTqU1GLdup6OI4ZjTpylGbbSPk+imRSCW3ST1HP1p9fqCd1c"
        "+RatoFFPiieaZIo1LM7BVA7k9BXceMvhL4v8D+GtM13WrFo7S/XcvylWjPZXB6HHNY1MTSpzjTnJJy2XcuNGc4uUVojhKKKK3Mwo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9MKKKK/lc/aj89fiN/wAlj8W/9hm8/wDR71zNdN8R"
        "gf8Ahcfi3/sM3n/o965nBr+ncB/u1L/CvyPxzE/xp+r/ADCijBowa6zAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMG"
        "jBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoAKKMGjBoA"
        "KKMGtfw/4W8SeK782fhvQ77U5V+/9miLLH7u3RR7nFTOcYK8nZDSb2MirOn6dqGralHp+lWF1f3kn+rtrWIyyP8ARRya9Stvh/8A"
        "DbwVaG9+LHjqKS/T5l8P+HZFuZG/2ZJ1JVCf9k5612ng34ifE7xRpEnhn9nX4SW+haW58qXVUg3M3p510/Bbvyf5V5tbMJPTDQ5n"
        "3ei+/wDyOqGGSXNUdvzM/wAMfsx6tBa2+s/FDX9N8IaZkNLFcyh7gLjI4B2ox9HxXcab42+A/g7VrfS/hl4Cbxd4iDbbeeSAzlnH"
        "8S54Vup+Wuz8MfsdTeIJk1345fEDVNd1NiHfTLOYrEv+yZM9f93ivW9R8RfA79nXwc0Yj0HwxFtx9ktED3tzjuR952/2jXDVwGKx"
        "K5sRU0fSOi/zf4HXDE0KK/dw17s4eDw5+0R4/tEudS+y+CbKYbgZZNsqqe2xfn6diKmu/gl8G/A+mHxB8VfGFzqZyGebVL4W0ZP+"
        "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"
        "WrMS5s9YtdyqSc7VeLJI+tcjffs0fFWz1O2t7XQ01a3mlEQutNuEmUZONzgHMa9yW6V6d4K+PHwu1W5jivdTm0iduq3alkJ9N68D"
        "6mvonw9Po2tacs+ialaXsAGS9tOJEJ6ckHk1rieMM8yd8uKptx6XX6o4pZRgcUva0pnkXwz+CGjfDGO31bU47bWvFyNvWYjfa2AP"
        "aJf45PVz07V6BcWA1Gyv7DV4U1Kw1BSt1Z3S70m78+hHUHsa7mHRwAQQPxp50fjoK+DxvEGOxuI+sVKj5ulunoerhqGFw9L2KV09"
        "/M+N/ir+zXPYxT+IvhrFd31hHG0t1pD/ADz2ajklG6yp/wCPDvxXziQQcEYNfqsmlvEwdDhgdwI7GvkP9sXRPA/h+50rWbW3+z+K"
        "dRYvdR26hYpohx5jqOBJnGSOvev1Tg3jetjKscDjItye0l+v+Z8vm2UU6Ufa0Hp2PmSigZIBwRnnmjBr9WufNBRRg0YNABRRg0YN"
        "ABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRR"
        "g0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YNABRRg0YN"
        "ABRRg0YNABRRg0YNAH6YUUUV/K5+1H57/Eb/AJLH4s/7DN5/6PeuZrpviN/yWPxZ/wBhm8/9HvXM1/TeA/3al/hX5H45if40/V/m"
        "FFFFdZgFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFLtb0NGDnGKAEop/kzBd3lPj12mt"
        "PT/DHiHVjjTNGvbw+kERc/kKLhYyaK73T/gr8U9RZQngfWbZW6SXts1uh/4E+BXWWf7L/wASZ0DXc/hyxzzibV4N3/fIbNLmQ+Vn"
        "i1FfQun/ALJviCaTZe+O/DVufRVmlx+Krg11umfsbaRIFbWPihGFI/5cLJiR/wB/MUudD5WfJtFfcFj+xn8KgQLv4g+IrkccC3gj"
        "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"
        "vjf6dp1+9vb3ROTIgORk9yM4z3xXP1ad1cgiW2JmErzSFh0Knb2pyWlrHj9wrMP4n+Yj863fDWnW2pa/bW98X8iSRIzsOCSzhQM/"
        "jn8K+nvi7+yHonwv+D+t+PI/F1/qIsIBKtk1uqBiTgAvnOBUNxT1LSbPkveR0AGPTikMhPeo0fzIlfGMgHFLVokcWyc0mTSVLBEZ"
        "p0jHG4gZ9KYiPNJX2n8Mv2VPhn42/Z3HjO/1q9TUJYp3S5tph5NuY92NwPDfdyQfXHatHw3+zF8MdV/ZhHjW5vSdROlyXf2mGbFv"
        "EwGfmH8Xpz0rP2iK5GfDdFfSHwK/Zy8NfG3RL25h8V3WmS2ITzTFEsqsX6AZPb1715v8Z/h1Y/DP4n6l4S0+9nvU05khkuZgAZGa"
        "MPnA6fexVKaegnFo83oooqhBRRRQAUUVLFGG3M/CINzH0HegCKivtPwL+yJ4H+JPwr03xXpPiLU9NEsbrKGQS+Y6HBYZPAOK+Q/E"
        "9ha6Z401jSbJXEOn30tmGc5LbGxu/HGalTT0G4tGRRRRVCCjJoooAM0ueaSgcmgCQORyKc6w3CbLiFZAfXr+Br339n/4D6B8YYtR"
        "07UdVu7C+ghW5WaHDBULbQpX1Oc59Kf8S/gz4K+GPxl0zwTeX+pX0RsBf3FwGWNpd0gRYlGeDz1rNyjsylc8E0+XUNEju4tJnDWd"
        "2nl3FjcEtHKucj/gQIBDdQRUNnq97o2vWPiDTp2gv9MlWdXHVSpzj6V9nfEz9lrwH8MPgtrHjy+1XVr37NDGYbZWCbHkIAye4G4V"
        "8R36n7SLhcqswKuR2PY1lyxV3EtPufT3xgEPxK+Alt4xto0e+sYI9TDoc7on+SWNe+Ax3Y9q7f8AZw8Vyap8A4LaectLp121sueu"
        "wjIya8c+FOqNqvwSvtCuSXaFpdO+qyxswH6VY/ZY1iSFvGGgOTt8iO6VfdJAn8ia+P43wUcRlk521jZ/oe7keJ9nX9m9mfVE+rd9"
        "3PrmsyfV/V+O9cxca0N7BX4zxmqEmpStkhsj2FfitPCyep9srHn/AO0xpsV/4U0PxbCf31hcvp9xj+KOQb1J/wB0rj8a+b695+MH"
        "j/wxH8PtW8JSX63epXqpsjg+YQMrhss3QHjGK8Dhcy20chAG5QeK/deC1Wp5fGlWTVm7X6rc+BzxQ+sNw+Y+iiivrjxQooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigD9LqKKK/lc/aj89/iN/yWPxZ/2Gbz/wBHvXM103xG/wCSx+LP+wzef+j3rma/p3Af"
        "7tS/wr8j8cxP8afq/wAwooorrMAooooAKKKKACiiigArrfDvwz8b+K9JOp+H/Dt9qFqrbDLbxGQA+hx0NcmoLMAO/FffP7JOsQ6D"
        "+zpBK7BG1HVJXyOCQh8r+aVMm1sVFXPjnVvAniLwPrNtH4q0x7KVh5ixlgX4GcEdQenBr2LxX+27f6p+zufh3beEpbPWH09dMl1B"
        "pgUCKoUsq9cnb0PSvMPjjrd5qn7WnirzLp5IY7tzGhbIT5QDj0rgpJI2mLtGhbP3iOai3MV8J9E67+2vqWtfs7W/wy0/wfLBrE+l"
        "po8+otLhNuwJvRBzk46GuAt/gR8Vp9Fjvb7wzfRxwxb3upoWjj8oDhi5GMYxzmvP7abeDsjRpdyBGK5Od6iv0X+OHjWG1+APi/Q7"
        "aTabfRpLfbuyAFUL/SlZxYaM4r9hOyjs9K8dTuyELeW1ssiEMpxCrkAjr1r56/agnl1L9vLW4YXUGSO3g5OAQIlHNeufsVakuk/A"
        "HWrskI914g4JOAVW2UfzzXgnxbvH1b9ui+wFlNxqNtAcc44UY/Sp63H5Fq+/Z++JenQ3eo6p4fl0+ytFMs1xdgwxoo65ZsDPtX11"
        "+xPBa6d8KPENx56lbjWUUOOQdsCqAPbg1rftY+JDP+yf4yt8uCRDHw3QF8V5p+yhqb6R+zVp7SzZku76WZQeCQrbPx6U27glY+cf"
        "2jtUZ/20fHKwzl4pbkxMPXao4/A1yvhvwH4v8ZLcP4Z0G+1X7PjzVtImlZAehIUcD3qX4vXDX37WHjS45wdTnA9wOK+rv2IJBpul"
        "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"
        "jjIYA4Jxn1FerfFb47eD/g7ounNrtreXElyTHbWVgijCjqcEgACvlf8AYh1a0tNX8YWEpPnz2sLxjIGQr89a9y+NHwk0b4x+GIYp"
        "NQaw8QWCMbG8kG6FyTkxygfwn1HStc2pYfD5xRyzFzaw8F33vrd/NhhqcquHdaEby7HqN7qOmeNvhfcCW136brGnFjb3C5JjdMjc"
        "vTd/KvymsWIubq3A+RJG285wM4r1nxf8Uv2ifh/qMngnxF4h1DThDCIUtxs2ND90eW38S44yK8w02ygtLPzdVu4rLzGyWY73x67R"
        "ya+94PySplEaspVOaE2nGzbstf8AgHkZjWhWsoxs1uSpHJLNHDDFJLLIwSOONSzOx6BQOSfau3h0nw54Dji1Xx08d7qRQS22hQkP"
        "5T9QbnH/AKAPxIPFReDNA+Inilri2+FvhiV96mOXWljJKKfvfv3AWIEdQOfevT/CH7OnhbSJX1f4o+I/+Egv1+YaLpEzBS55PnTk"
        "c/8AAM/Wvo8dnWFwkW6s9unU5cNgauIuoI8+0Xw78RP2hvE8zwBNM8P25DXWpXWVtbRFGMFgPmIHRFGfbvXuthZeH/Bvg4+EfAqX"
        "Fvpz7ft99PxcapIv8cn91PRB0Fat/qmdOh0rTbSHSdGtlCW2lWa+XDCPoOpzySc5NYk7gxPgZOD19a/Ns34lq45+zpq1P8/U+swG"
        "UQw1pz1kUL/VLLSNLn1DUJ1gghGWZjyf9lfU+1fPfiT4v+K9X12V/D1/e6XZqf3UFu+OPVvU074t+IdY1nx3deH8tFaWExjjhHt/"
        "EfUmuXtrWO2h2p949W9a+s4d4dpUqXt6yUpS+aSPNzbNantJUqbskaqfFP4lwyKz69fShRjEqgiszXPFHibxnc2i69cvMttuCZXb"
        "gE5NSFaUKBX09PLsPTmpwgk12SPCnjK048spNoAAFAHQcCloorvOUKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "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"
        "fQY4rrNV/a0eeyYaR4At4LjkpNdXrTIpxwSm0bvpmvEXtoX+9Gp+opi2VspysCD8K4K3C2XVqzrzormevU6I5viox5FPQNb13xD4"
        "48STa14hu3ubiVtzSN0UZ+6g6KPalSzgQDbEo/CplUKMAAU6vepUIUoqMVZI8+dWU3dsZ5agY2jH0qgYrvTL9NR0uZ4Zo23qUOCp"
        "9q0qQgGrnTU1ZijNxd0V9Z8R+K/Fd152q3ski9AmdqKPZRVe30qGMhpP3jj16VoBQO1LUUqEKatFWRVStOo7ydxFUKMAYpaKK2Mg"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9LKKKK/lc/aj8+PiL/yWLxZ/2Gbz/wBHvXNV0/xF"
        "H/F4vFn/AGGbz/0e9cziv6dwH+7Uv8K/I/HMT/Gn6v8AMSilxRiuswEopcUYoASilxRigBKKXFGKAEopcUYoASkJCjJOKdijAoAr"
        "PewI235yfZCafbXlm7Brk3EcecEJEWfH04H61NgUY9zUyTezGmjStrrwb5ivO/iWQDkxpZRJu9txkOPyrdi8U/DW1jURfC3WtRkH"
        "/LS613yQf+ArEf51yGPc0uPc1jKhzfFJ/fb8i41Euh3Y+KOiWrA6V8EPC0eOh1CaS7P45K1oWn7QHjTTkK6T4I8D6fk5HlaSjY/F"
        "mNeZ4FGKweXUXvd+rb/U1WKmtvyPVh+058blTZaaho2nL6WlikePyqhdftD/AB6vMmTx7IuT0UY/pXnOPeis3lGElrKmn8kJYmot"
        "mdjcfGT403QPm/EW+56hSoH/AKDWfJ8SfixOhSb4haqQeyy4/kK56kxVxyvCx2pR+5f5DeKqv7T+805/GPxEuQBP481h8c4+0NVG"
        "XVfFdwSbjxdqshPJzcOf61FgUYrWOBoR+GCXyRDxFR/aZFL/AGpOSZ9cvZCeCWkY/wDs1VH0ySQ5fUJm+uf8a0MUYrVUILZC9tPu"
        "Z/8AZUY/5eZaX+ybY/ekkJ9Tir+KMVXsoi9pLuZ39j2meWkP5f4Uv9j2frJ+daGKMU/ZonmZQ/sex/uuf+BUf2RZf3H/AO+qv4ox"
        "RyIXMyiNJsl6I/8A31ThptoP4G/OrmKMUezQ+ZlT+zrT/nmfzo/s2z6+T+tW8UYo5ELmZU/s6z/54j8zR/Z1n/zwWreKMUciDmZU"
        "/s6z/wCfdKP7Ps+9ulW8UYp8iC7KosLQdIFpfsNp/wA+6VZxRijlQXK32Gz/AOfdKPsNp/z7p+VWcUYo5UFyt9hs/wDn2Sj7Faf8"
        "+6flVnFGKfKguVvsVp/z7R/lS/Y7X/n3j/KrGKMUcqC7K/2O1/54R/lR9jtv+eCflVjFGKXKg5mQfZLb/nhH+VKLaAf8sk/KpsUY"
        "p8qC5F5EP/PJPypfJi/55r+VSYoxRyoLkflR/wBxfyp21QOFAp2KMUcqFcbgUtLijFFgE/E0UuKMUWASilxRinYBKKXFGKAEopcU"
        "YoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxR"
        "igBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFG"
        "KAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUYoASilxRigBKKXFGKAEopcUY"
        "oASilxRigD9K6KKK/lc/aj8+viL/AMlh8Wf9hm8/9HvXNV0vxF/5LD4s/wCwzef+j3rmq/p3Af7tS/wr8j8cxP8AGn6v8wooorrM"
        "AooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooo"
        "oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK"
        "KKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAC"
        "iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9KqKKK/lc/aj8+v"
        "iL/yWHxZ/wBhm8/9HvXNV0vxF/5LD4s/7DN5/wCj3rmq/p3Af7tS/wAK/I/HMT/Gn6v8wooorrMAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9KqKKK/lc/aj8+viL/yWHxZ/2Gbz/wBHvXNV0vxF"
        "/wCSw+LP+wzef+j3rmq/p3Af7tS/wr8j8cxP8afq/wAwooorrMAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA"
        "KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKK"
        "ACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigD9KqKKK/lc/aj8+viL/wAlh8Wf9hm8/wDR71zVdL8Rf+Sw+LP+wzef+j3rmq/p3Af7"
        "tS/wr8j8cxP8afq/zCiiiuswCiiigAooooAKKKKACiu4+Hfwm8afE6/ki8Naev2WFgs9/dMY7eI+hbBJPIO1QT3xXuNr+xXqD2oa"
        "9+IVtDNjlIdNaVQf94yKf0oA+VqK9w+In7MPjHwH4YvPEkOr6Zq+mWaeZO0ZaGZFzjdsbgjnsxPtXh9ABRRRQAUUUUAFFFFABRRR"
        "QAUV7n+z18GPC/xZtfEEviO/1e1OnPbrD/Z8sabvMEmd2+Ns/cGMY71598VvCWneBfjDrfhTSJ7qaysZI0ikumVpCGiRzuKqo6se"
        "gFAHG0UUUAFFFFABRRRQAUUVoaFoeqeJfEdnoOiWj3eoXkoihhTgsx9zwABkkngAEmgDPor6j039i7WptMSXVvHVlZ3ZXLQW9i06"
        "KfTeXTP/AHzXlPxf+DGrfCG60sahrNlqUGp+d5DwIyMvl7N25TwP9YuME9DQB5lRRRQAUVNaWd1qF/DY2NtLc3U7iOKGFC7yMTgK"
        "oHJJPavofwv+x94z1bTY7vxJr1hoLSDcLZYzdSp7MAVUH6MaAPnKivpjX/2NfFFlYPN4d8W6dq0yjIguLdrQv7KdzjP1IHvXztrW"
        "i6r4d1650XXLCaxv7Z9k1vMuGU/1BGCCOCCCKAKFFfQfww/Zh/4WR8MNP8Yf8Jv/AGZ9saVfsv8AZnnbNkjJ9/zlznbnp3rr/wDh"
        "ij/qpn/lG/8AuigD5Nor0v4zfCT/AIVF4k07Sf8AhIP7Y+22xuPN+yfZ9mHK4xvfPTOcivTvCX7I3/CU+AtG8S/8LB+yf2lZRXn2"
        "f+yfM8rzEDbd3nDOM4zgfSgD5morr/ib4Bvvhp8SL3wpe3P2sQqkkF2I/LFxGwyHC5OOcgjJ5U12HwX+A198XdP1TUW13+xLGykS"
        "BJzafaPOkIyygb0xtG0nn+IUAeQUV7T8ZvgB/wAKj8LafrP/AAln9sfbLv7L5X2D7Ps+Rm3Z8x8/dxjFeLUAFFFFABRRRQAUUUUA"
        "FFFFABRW34R8L3/jTxtp3hfS5raG8v5fKikuWZY1OCfmKgnHHYGut+J/wT8VfCew0678Raho90l/I8cQ0+WRypUAndvjX1HTNAHm"
        "9FFFABRRRQAUU5EeWVY41LOxCqoGSSe1fW2kfsleDtI8HJq3xI8aXdjKsavcvbzw21vbk4+UySq2cE4zxn0oA+R6K9F+MnhLwH4O"
        "8a2WnfD7xN/b+nS2Szy3P22G62SmR1KbolCj5VU4PPPuK86oAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoor1f4A/"
        "DHQfip4/1HQ/EN3qNtb22ntdo1hIiOXEka4JdGGMOe3pQB5RRXp3x2+HOifDD4nw+HNAutQubV7CO6L3zo8m5ncEZRVGPlHb1rzG"
        "gAooooAKKKKACiiigAooooAKK+r4v2K/NgST/hZWNyhsf2N0yP8ArvT/APhij/qpn/lG/wDuigD5Norf8beGv+EO+IeseFvtv23+"
        "zrlrf7T5fl+Zt77cnH0yawKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAK"
        "KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD9KqKKK/lc/aj8+viL/AMlh8Wf9hm8/9HvXNV0/xFA/"
        "4XD4s/7DN5/6PeuZwK/p3Af7tS/wr8j8cxP8afq/zEopcCjArrMBKKXAowKAEopcCjAoASnRxvLMkUYy7sFUepNJgVJBK1vdRXEf"
        "343Dr9Qc0AfpDHDo3wU/Z+kNraq9voenmRlT5TczAckn1dz17Z9q+LLr4tfG/wCIHimQaRr3iSW6fdImneH/ADYxGg9I4eSBxycn"
        "1Nfa/iO0tfi1+z9eW+jXMYj13TPMtZGPyq5AZA3phgAe4wa+F/DWr+Ovgb8TG1F/Dq2+rQxyWxt9Ut5DGwbGSu1l3dOCCQfegDqr"
        "vxJ+0o/gTVfD2vaF4u1DR7u2aO4Op6PM5jQclxKUDDGO5I9q5T4QfCnVPix42bSbW4+xafaoJr69K7vKQnAVR3djnA9ie1fc1lru"
        "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"
        "M9R/7F6L/wBFpQB+e9Fexfs/fCjw78VvEWs2HiK91S2jsrZJozYSRoxLMQd29G4+mKwfjZ4C0f4b/FmfwvodzfXFnHbxTB711eTL"
        "rk8qqjH4UAed17/+yAQPj1e5PXRZv/RsNeAV6L8D/HVr8PfjRpmu6kzLp0ge0vGUZKRyDG7HorBWPsDQB6v+2d/yO/hc/wDTjL/6"
        "MFaP7FQ/0rxqf9my/nPXr3xV+Enh344+HtJv7bxALWW2DPaajaKtzFJG+MggMNw+UEEMMc+tS/DP4a+GPgR4H1Sa78QLKJ2We+1O"
        "8C26BUBCqFydoG5u5JLH2FAHy/8AtUo837SVxFEpeRrK2VUUZJJXgY9a+no0h+CH7KB+4lzpGllieMPeSfzBmfH0rwDwe8Pxv/bf"
        "m8Txwu2jWMovlEi4/dW4VIcg9CzhGKn1b0r6K+Jvxv8AB/wp1Kw0/wAQW+qXdzexNMkWnxRuY0BwC+91wCcgYz909KAPPP2Q/GD6"
        "x8ONV8LXk7SXOlXXnx7zkmKbLfjiQSE/74r5m+M3g7/hBvjZruhxReXZmf7VZgDA8mT51A9lyV+qmvrXw1+1R8OfFHi/TvDtrp3i"
        "G0uL+dbaKa8ghWJXY4UMVlYjJwOh5IrjP2xvB32jQtE8dWsWZLVzp92wHPlvloyfYMHH1cUAei/sxf8AJsPh/wD66XX/AKUyVg6h"
        "8Qf2UYdXuodRsPCxvEmdZy/hl3YyBiGy32c5Oc855re/Zi/5Nh8P/wDXS6/9KZK831X9jf8AtPXr7Uv+FjeV9quJJ/L/ALI3bdzF"
        "sZ88ZxnrQB4d8c9Y8Aa38UUvfhtDYRaMLKNCtjYmzj80M+75Ci84K84rzSvU/jT8G/8AhUF/o9t/wkf9s/2jHLJu+x/Z/L2FRjHm"
        "PnO726V5ZQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAfpRRRRX8rn7Ufn58RP8AksPiz/sM3n/o965qul+In/JYfFn/AGGbz/0e"
        "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"
        "RQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2i"
        "nUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUAN"
        "op1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FA"
        "DaKdRQA2inUUAfpNRRRX8rn7Ufn98RP+SweK/wDsM3n/AKPeuarpfiJ/yWDxX/2Gbz/0e9c1X9O4D/dqX+FfkfjmJ/jT9X+YUUUV"
        "1mAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU"
        "UUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUA"
        "FFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+k1FFFfyuftR+"
        "f3xE/wCSweK/+wzef+j3rmq6X4if8lg8V/8AYZvP/R71zVf07gP92pf4V+R+OYn+NP1f5hRRRXWYBRRRQAUUUUAFXNJ099W16x0q"
        "O4gtnu7iO3Wa4JEcZdgu5yASFGcnAJx2NU6UEqwIJBHIIoA95+I/7JPxL+GPw3v/ABtreq+Gr3T7ExiaPTrid5QHkWMEB4VGAWGe"
        "a8p8A+CNZ+I/xG0vwV4fa2TUdRdkie6ZliTajOzMVViAFUngGv0++X4z/sddprjxF4a+u25aH+ayj9K+Rv2EvCx1L466x4lmiJi0"
        "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"
        "/wC1NYbTgWJk8zaRKm/gJnrjjpmrXuoT1Z9efscf8mg+Hf8Arvef+lMlfnF49/5Kt4n/AOwtdf8Ao5q/UDwb4y/Z6+H/AIPtvC3h"
        "H4ieCNO0m2Z2itv+Ejhm2l2Lt80krMcsSeTXg/xl8DfsmD4V+LvEfhfVfCVz4re3lurZrXxQ08slwzbsrF9oIYkk/LtI9qmL1G0a"
        "H7AN7byfDDxdpysv2iHVIpnHcK8QC/rG9Z/7VH7R3xL+HHxltfCPgi+ttLtILGK6mle0jne5dy3GZFICgKB8uDndz0x84fs9/Gm5"
        "+CvxQOrzW0t5ol/GLbU7SIjeUzlZEzxvQ5IB4ILDIzkfa+veJP2SPjTHYeIPFmveFLy4to9sTanftp1xGud3lspeNmAJPynIyTjq"
        "aGrO4LY9C8HX8Pxj/Zn0y98VafCieItH230Cj5MupVioPQZyy85HHPGa/I1hhiAQcHqO9ff/AMb/ANqv4e+F/hhc+BvhNe22palN"
        "af2fDNp6bbTTYduzKtgBmC8KEyB1J4wfz/pwQmFFFFWIKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii"
        "igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo"
        "oooAKKKKACiiigAooooAKKKKACiiigAooooA/Saiiiv5XP2o/P74if8AJYPFf/YZvP8A0e9c1XS/ET/ksHiv/sM3n/o965qv6dwH"
        "+7Uv8K/I/HMT/Gn6v8wooorrMAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAr6O/Yq8TeH"
        "PCvx/wBW1HxR4g0vRLN9AmhS51K7jto2c3FuQgZyAWIVjjrgH0r5xopNXA+n/wBtzxV4X8WfFbw5d+FvEmka5bw6SY5JtMvI7lEb"
        "znO1ihIBwQcGvmCiihKwM6/4U3lnp3x68EahqF1BaWltr9hNPcTuI44kW4Qs7MeFUAEkngAV9oftjfEPwB4n/ZxXTPDXjnw3rN7/"
        "AGtbyfZdO1OC4l2hZMttRicDI596+AKKGru47hRRRTEFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRR"
        "QAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUU"
        "UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAF"
        "FFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+k1FFFfyuftR+f3xE/5LB4r/7DN5/6PeuarpviJ/yV/wAV/wDYYu//AEe9"
        "c3X9O4D/AHal/hX5H45if40/V/mNop1FdZgNop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADa"
        "KdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA"
        "2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUU"
        "ANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1"
        "FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUANop1FADaKdRQA2inUUAfpJRRRX8r"
        "n7Ufn/8AET/kr/iv/sMXf/o965uuk+In/JX/ABX/ANhi7/8AR71zdf07gP8AdqX+FfkfjmJ/jT9X+YUUUV1mAUUUUAFFFFABRRRQ"
        "AUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUU"
        "UAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFF"
        "FFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAB"
        "RRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+klFFFfyuftR+f/AMRP+Sv+K/8AsMXf"
        "/o965uuk+In/ACV/xX/2GLv/ANHvXN1/TuA/3al/hX5H45if40/V/mFFFFdZgFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABR"
        "RRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQA"
        "UUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUU"
        "AFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFF"
        "FABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAfpJRRRX8rn7Ufn/APET/kr/AIr/AOwxd/8Ao965uuk+In/JX/Ff/YYu"
        "/wD0e9c3X9O4D/dqX+FfkfjmJ/jT9X+YUUUV1mAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRR"
        "RQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAU"
        "UUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUA"
        "FFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFF"
        "ABRRRQAUUUUAFFFFABRRRQB+klFFFfyuftR+f/xE/wCSv+K/+wxd/wDo965uuk+In/JX/Ff/AGGLv/0e9c3X9O4D/dqX+FfkfjmJ"
        "/jT9X+YUUUV1mAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAF"
        "FFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFA"
        "BRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRR"
        "QAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB+k"
        "lFFFfyuftR+f/wARP+Sv+K/+wxd/+j3rm6KK/p3Af7tS/wAK/I/HMT/Gn6v8wooorrMAooooAKKKKACiiigAooooAKKKKACiiigA"
        "ooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo"
        "AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK"
        "KACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi"
        "iigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD/9k="
    ),
}

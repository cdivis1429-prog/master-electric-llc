#!/usr/bin/env python3
"""Builds the static Master Electric website into ../site/.

Every page shares one header, footer and SEO block, so edit content here and
re-run:  python3 tools/build_site.py
The generated .html files in site/ are plain HTML and can also be edited by hand.
"""
import json, os, html, datetime

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
DOMAIN = "https://masterelectricdenver.com"
PHONE = "720-456-1384"
TEL = "+17204561384"
EMAIL = "masterelectricllc@outlook.com"
WEB3FORMS_KEY = "f6d660bf-8cb6-4e6b-89b0-79c853fcf957"  # public form key (Web3Forms), safe to commit
LICENSE = "EC.0103012"
GOOGLE_REVIEWS = "https://g.co/kgs/PxdCw6w"
AREAS = ["Aurora", "Denver", "Centennial", "Parker", "Englewood", "Littleton",
         "Lakewood", "Greenwood Village", "Highlands Ranch", "Castle Rock"]

SERVICES = [
    ("basement-electrical.html", "Basement Finish Electrical", "🏠",
     "Full electrical for basement finishes: layout, permits, recessed lighting, circuits and inspections."),
    ("remodel-electrical.html", "Kitchen & Bath Remodels", "🍳",
     "New circuits, lighting, appliance and hood wiring, and code updates for remodels."),
    ("panel-upgrades.html", "Panel Upgrades & EV Chargers", "⚡",
     "Panel replacements, service upgrades, subpanels, EV chargers and surge protection."),
    ("electrical-repair.html", "Electrical Repair & Service", "🔧",
     "Troubleshooting, dead outlets, tripping breakers, lighting, fans and smoke detectors."),
    ("commercial.html", "Commercial Electrical", "🏢",
     "Tenant improvements, retail and restaurant remodels, lighting and service for businesses."),
]
CITY_PAGES = [("aurora-electrician.html", "Aurora"), ("denver-electrician.html", "Denver"),
              ("centennial-electrician.html", "Centennial"), ("parker-electrician.html", "Parker")]

REVIEWS = [
    ("Jim C.", "Highly recommended. Had entire house upgraded... new outlets/switches, new recessed cans and upgrade of older cans to LED, ceiling fans and new exterior lighting and basement lighting repair done. Team was professional and timley and came in on budget. Highly Recommeded!"),
    ("Olivia H.", "I needed help adding a few outlets in our basement, as well as adding a fan to our daughters roome and upgrading some lights throughout our house. We were recommended Master Electric through a local neighborhood Facebook group and will absolutely continue to recommend! Master Electric was timley, professional, and great at staying on budget."),
    ("Lc S.", "Needed an electrician in a hurry and my friend highly recommended them so I gave them a call. Super friendly, reasonable pricing and will be using again."),
    ("Shane S.", "Was punctual and fair on price. we were having our rental property remodeled did a fantastic job will be using for future projects."),
]

E = html.escape


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Electrician",
        "@id": DOMAIN + "/#business",
        "name": "Master Electric, LLC",
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/img/logo-512.png",
        "image": DOMAIN + "/img/share.png",
        "telephone": TEL,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Aurora",
                    "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": a + ", CO"} for a in AREAS],
        "sameAs": [GOOGLE_REVIEWS],
        "priceRange": "$$",
    }


def header(current):
    def link(href, label):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="/{href if href != "index.html" else ""}"{cur}>{label}</a>'
    svc = "".join(f'<a href="/{h}">{t}</a>' for h, t, _, _ in SERVICES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span class="hide-sm">Licensed Colorado Electrical Contractor #{LICENSE} · Serving the Denver Metro</span>
  <span>Call or text: <a href="tel:{TEL}">{PHONE}</a></span>
</div></div>
<header class="site-header"><div class="wrap" style="position:relative">
  <a class="brand" href="/"><img src="/img/logo.png" alt="Master Electric LLC logo" width="56" height="56"><span>Master Electric<small>AURORA &amp; DENVER ELECTRICIANS</small></span></a>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" onclick="var n=document.getElementById('nav');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))">☰</button>
  <nav class="nav" id="nav" aria-label="Main">
    <div class="dropdown"><a href="/#services">Services ▾</a><div class="dropdown-menu">{svc}</div></div>
    {link("service-areas.html","Service Areas")}
    {link("about.html","About")}
    <a href="/#reviews">Reviews</a>
    {link("contact.html","Contact")}
    <a class="btn btn-primary" href="tel:{TEL}">📞 {PHONE}</a>
  </nav>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="/{h}">{t}</a></li>' for h, t, _, _ in SERVICES)
    cities = "".join(f'<li><a href="/{h}">Electrician in {c}</a></li>' for h, c in CITY_PAGES)
    year = datetime.date.today().year
    return f'''<section class="cta-band"><div class="wrap">
  <div><h2>{TAGLINE}</h2><p>Free estimates on basement finishes, remodels and panel upgrades.</p></div>
  <div class="btn-row" style="margin:0"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-outline" href="/contact.html">Request a Quote</a></div>
</div></section>
<footer class="site-footer"><div class="wrap">
  <div class="footer-grid">
    <div>
      <img src="/img/logo.png" alt="" width="64" height="64" style="margin-bottom:12px">
      <p><strong style="color:#fff">Master Electric, LLC</strong><br><em style="color:var(--gold);font-style:normal;font-weight:700">{TAGLINE}</em><br>Faith-driven. Family-owned.<br>Residential and commercial electrical contractor based in Aurora, CO, serving the Denver Metro area.</p>
      <p>Colorado Electrical Contractor #{LICENSE}</p>
    </div>
    <div><h3>Services</h3><ul>{svc}</ul></div>
    <div><h3>Service Areas</h3><ul>{cities}<li><a href="/service-areas.html">All service areas</a></li></ul></div>
    <div><h3>Contact</h3><ul>
      <li><a href="tel:{TEL}">📞 {PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">✉️ {EMAIL}</a></li>
      <li><a href="/contact.html">Request a quote</a></li>
      <li><a href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Google reviews</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom"><span>© {year} Master Electric, LLC. All rights reserved.</span><span>Aurora, Colorado</span></div>
</div></footer>
<div class="callbar"><a class="call" href="tel:{TEL}">📞 Call Now</a><a class="quote" href="/contact.html">Free Quote</a></div>'''


def page(filename, title, description, body, current=None, extra_schema=None):
    url = DOMAIN + "/" + ("" if filename == "index.html" else filename)
    schemas = [business_schema()] + (extra_schema or [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schemas)
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/share.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">
<meta name="theme-color" content="#141b1f">
{ld}
</head>
<body>
{header(current or filename)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(doc)
    return url


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def faq_html(faqs):
    return "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)


def crumbs(*items):
    parts = ['<a href="/">Home</a>'] + [f'<a href="/{h}">{t}</a>' if h else E(t) for h, t in items]
    return '<div class="crumbs">' + " › ".join(parts) + "</div>"


def reviews_html(n=4):
    cards = "".join(f'<div class="review"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div><p>“{E(t)}”</p><cite>— {E(name)}</cite></div>' for name, t in REVIEWS[:n])
    return f'''<section class="section alt" id="reviews"><div class="wrap">
  <div class="center"><span class="eyebrow">Reviews</span><h2>What our customers say</h2>
  <p class="lead">Most of our work comes from referrals and repeat customers.</p></div>
  <div class="grid grid-2" style="margin-top:28px">{cards}</div>
  <div class="center btn-row" style="justify-content:center"><a class="btn btn-dark" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Read more on Google</a><a class="btn btn-outline" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Leave us a review</a></div>
</div></section>'''


def service_cards():
    cards = "".join(f'<div class="card"><div class="icon" aria-hidden="true">{i}</div><h3><a href="/{h}">{t}</a></h3><p>{d}</p><a class="more" href="/{h}">Learn more →</a></div>' for h, t, i, d in SERVICES)
    return cards


TAGLINE = "Done right. No callbacks."

TRUST = '<div class="trust-row"><span>Faith-driven &amp; family-owned</span><span>Licensed &amp; insured</span><span>20+ years in the trade</span><span>Permits &amp; inspections handled</span><span>Colorado Master Electrician</span></div>'


# ---------------------------------------------------------------- Home
def build_home():
    body = f'''<section class="hero"><div class="wrap">
  <div>
    <p class="tagline">{TAGLINE}</p>
    <h1>Electrical for basement finishes, remodels &amp; panel upgrades</h1>
    <p class="lead">Master Electric is a licensed electrical contractor based in Aurora. We wire basements and remodels, upgrade panels and fix electrical problems for homeowners, builders and businesses across the Denver Metro.</p>
    <div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-outline" href="/contact.html">Get a Free Quote</a></div>
    {TRUST}
  </div>
  <div class="hero-photo"><img src="/img/kitchen-pendant-lighting.jpg" alt="New pendant lighting installed over a kitchen island in a Denver-area remodel" width="1000" height="811"></div>
</div></section>

<section class="section" id="services"><div class="wrap">
  <div class="center"><span class="eyebrow">What we do</span><h2>Electrical services for homes and businesses</h2>
  <p class="lead">From a single new circuit to a full basement or a commercial tenant finish, we handle the permits, the wiring and the inspection.</p></div>
  <div class="grid grid-3" style="margin-top:32px">{service_cards()}
    <div class="card" style="background:var(--ink);color:#fff;border-color:var(--ink)"><h3 style="color:#fff">Not sure what you need?</h3><p style="color:#c9d0d2">Call or text a photo of the problem and we'll tell you what it will take.</p><a class="btn btn-primary" style="margin-top:auto" href="tel:{TEL}">📞 {PHONE}</a></div>
  </div>
</div></section>

<section class="section dark"><div class="wrap">
  <div class="stats">
    <div><strong>20+ yrs</strong><span>in the electrical trade</span></div>
    <div><strong>#{LICENSE}</strong><span>Colorado electrical contractor</span></div>
    <div><strong>Residential</strong><span>&amp; commercial work</span></div>
    <div><strong>Permitted</strong><span>work, inspected to code</span></div>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <span class="eyebrow">Basement finishes</span>
    <h2>Finishing your basement? We do the electrical start to finish.</h2>
    <p>Basement finishes are the core of our work. We plan the lighting and outlet layout with you, pull the permit, rough-in for framing inspection, and come back to trim out once drywall is done.</p>
    <ul class="checklist">
      <li>Recessed LED lighting and dimmers</li>
      <li>Bedroom, bathroom, bar and media room circuits</li>
      <li>Code-required smoke/CO detectors and AFCI protection</li>
      <li>Subpanels and panel upgrades when you're out of space</li>
      <li>We work with homeowners, basement companies and remodelers</li>
    </ul>
    <a class="btn btn-dark" href="/basement-electrical.html">Basement electrical details →</a>
  </div>
  <img src="/img/basement-feature-wall-led-shelves.jpg" alt="Basement finish with LED shelf lighting and recessed cans wired by Master Electric" width="1100" height="825" loading="lazy">
</div></section>

<section class="section alt"><div class="wrap">
  <div class="center"><span class="eyebrow">Recent work</span><h2>A few of our projects</h2></div>
  <div class="grid grid-3" style="margin-top:28px">
    <div class="card photo-card"><img src="/img/electrical-panel-install.jpg" alt="New electrical panel and disconnect installation" loading="lazy"><div class="body"><h3>Panel &amp; service work</h3><p>Clean, labeled panel installs and service upgrades.</p></div></div>
    <div class="card photo-card"><img src="/img/commercial-led-lighting.jpg" alt="Custom LED lighting in a commercial space" loading="lazy"><div class="body"><h3>Commercial lighting</h3><p>Custom LED and lighting control for businesses.</p></div></div>
    <div class="card photo-card"><img src="/img/commercial-restaurant-bar-lighting.jpg" alt="Restaurant serving bar with feature ceiling and lighting" loading="lazy"><div class="body"><h3>Restaurant &amp; retail</h3><p>Tenant improvements and remodels for national brands.</p></div></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center"><span class="eyebrow">How it works</span><h2>Simple from first call to final inspection</h2></div>
  <div class="grid grid-3 steps" style="margin-top:32px">
    <div class="step"><h3>Call or request a quote</h3><p>Tell us about the project. For small jobs, a photo is often enough to give you a price.</p></div>
    <div class="step"><h3>Get a clear estimate</h3><p>We walk the job and give you a written price with what's included, so there are no surprises.</p></div>
    <div class="step"><h3>We wire it &amp; get it inspected</h3><p>We pull the permit, do the work, and stay with it until the city signs off.</p></div>
  </div>
</div></section>

{reviews_html()}
'''
    page("index.html", "Electrician in Aurora & Denver, CO | Master Electric, LLC",
         "Licensed Aurora electrician serving the Denver Metro. Basement finish electrical, kitchen and bath remodels, panel upgrades, repairs and commercial work. Call 720-456-1384.",
         body)


# ---------------------------------------------------------------- Service pages
def gallery_html(items, eyebrow, heading):
    figs = "".join(f'<figure><img src="/img/{i}" alt="{E(c)}" loading="lazy"><figcaption>{E(c)}</figcaption></figure>' for i, c in items)
    return f'''<section class="section alt"><div class="wrap">
  <div class="center"><span class="eyebrow">{eyebrow}</span><h2>{heading}</h2></div>
  <div class="grid grid-3 gallery" style="margin-top:28px">{figs}</div>
</div></section>'''


def service_page(filename, h1, title, desc, intro, photo, photo_alt, bullets, sections, faqs, crumb, gallery=None):
    secs = "".join(f"<h2>{E(h)}</h2>{p}" for h, p in sections)
    others = "".join(f'<li><a href="/{h}">{t}</a></li>' for h, t, _, _ in SERVICES if h != filename)
    body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("", crumb))}
  <h1>{E(h1)}</h1>
  <p class="lead">{intro}</p>
  <div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-outline" style="color:#fff" href="/contact.html">Get a Free Quote</a></div>
</div></section>
<section class="section"><div class="wrap split" style="align-items:start">
  <div>
    <h2>What's included</h2>
    <ul class="checklist">{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
    {secs}
  </div>
  <div>
    <img src="/img/{photo}" alt="{E(photo_alt)}" loading="lazy">
    <div class="contact-box" style="margin-top:24px">
      <h3>Get a price for your project</h3>
      <p>Call or text and we'll get back to you quickly.</p>
      <a class="big-phone" href="tel:{TEL}">{PHONE}</a>
      <p style="margin-top:12px"><a href="/contact.html">Or send us the details online →</a></p>
      <p style="font-size:.9rem;color:var(--muted);margin:0">Licensed Colorado Electrical Contractor #{LICENSE}</p>
    </div>
    <div style="margin-top:24px"><h3>Other services</h3><ul>{others}</ul></div>
  </div>
</div></section>
{gallery or ""}
<section class="section"><div class="wrap" style="max-width:860px">
  <h2 class="center">Common questions</h2>
  {faq_html(faqs)}
</div></section>
'''
    page(filename, title, desc, body, extra_schema=[faq_schema(faqs), {
        "@context": "https://schema.org", "@type": "Service", "serviceType": h1,
        "provider": {"@id": DOMAIN + "/#business"},
        "areaServed": [{"@type": "City", "name": a + ", CO"} for a in AREAS]}])


def build_services():
    service_page(
        "basement-electrical.html", "Basement Finish Electrical in Aurora & Denver",
        "Basement Finish Electrician | Aurora & Denver | Master Electric",
        "Licensed electrician for basement finishes in Aurora, Denver and the Denver Metro. Lighting, circuits, permits and inspections. Free estimates: 720-456-1384.",
        "Finishing a basement? We handle the complete electrical: layout, permit, rough-in, inspections and trim-out. We work directly with homeowners and alongside basement finishing companies and remodelers.",
        "basement-finished-room-chandelier.jpg", "Finished basement room with chandelier and recessed lighting wired by Master Electric",
        ["Lighting and outlet layout planned with you", "Electrical permit pulled and inspections scheduled",
         "Recessed LED lighting, dimmers and switches", "Bedroom, bathroom, bar, office and media room circuits",
         "AFCI/GFCI protection and smoke/CO detectors to current code", "Subpanels or panel upgrades if your panel is full",
         "Low-voltage prep for TV, data and speakers", "Exhaust fans, heated floors and dedicated appliance circuits"],
        [("How a basement electrical job works",
          "<p>We start with a walkthrough to plan where lighting, outlets, switches and any dedicated circuits go. After the permit is issued, we rough-in the wiring once framing is up and get the rough electrical inspection passed so drywall can start. After drywall and paint, we come back to install fixtures, devices and trim, then schedule the final inspection.</p>"),
         ("Working with basement companies and builders",
          "<p>If you're a basement finisher, remodeler or builder, we can be your electrical sub. We show up when scheduled, keep inspections moving and price jobs clearly so you can bid with confidence.</p>")],
        [("Do I need a permit to finish my basement electrical?", "Yes. In Aurora, Denver and the surrounding cities, new basement wiring requires an electrical permit and inspections. We pull the permit and schedule the inspections for you."),
         ("How long does basement electrical take?", "Rough-in for a typical basement takes a few days, then trim-out takes a day or two after drywall. Inspection scheduling with the city is usually the biggest variable."),
         ("Will my panel have room for a finished basement?", "Often yes, but not always. We check your panel's capacity and open spaces during the walkthrough and will tell you up front if you need a subpanel or upgrade."),
         ("Do you work with my contractor or basement company?", "Yes. We regularly work as the electrical subcontractor for basement finishers and remodelers, and we also work directly for homeowners.")],
        "Basement Finish Electrical",
        gallery=gallery_html([
            ("basement-framing-rough-in.jpg", "Framing stage, ready for electrical rough-in"),
            ("basement-feature-wall-led-shelves.jpg", "Feature wall with LED shelf lighting and recessed cans"),
            ("basement-led-shelf-lighting.jpg", "Built-in shelves with LED strip lighting"),
            ("basement-wet-bar-recessed-lighting.jpg", "Wet bar with recessed lighting and appliance circuits"),
            ("basement-led-mirror-wall.jpg", "Home gym with backlit LED mirrors and TV wall"),
            ("basement-finished-room-chandelier.jpg", "Finished room with chandelier and dimmable lighting"),
        ], "Recent basement work", "From framing to finished space"))

    service_page(
        "remodel-electrical.html", "Kitchen & Bathroom Remodel Electrical",
        "Kitchen & Bath Remodel Electrician | Aurora & Denver | Master Electric",
        "Electrical for kitchen and bathroom remodels in Aurora and the Denver Metro: lighting, appliance circuits, hoods and code updates. Call 720-456-1384.",
        "Remodels usually mean new lighting, new appliance circuits and bringing older wiring up to code. We coordinate with your contractor or work directly with you to get it done right and inspected.",
        "bath-vanity-sconce-wallpaper.jpg", "Bathroom remodel with new vanity sconce lighting",
        ["Recessed, pendant and under-cabinet lighting", "Dedicated circuits for ranges, ovens, microwaves and dishwashers",
         "Range hood and exhaust fan wiring", "GFCI and AFCI protection to current code",
         "Island and peninsula outlets", "Bathroom fans, heated floors, vanity lighting and lighted mirrors",
         "Whole-house updates: outlets, switches, fans and LED upgrades", "Permits and inspections"],
        [("Remodels done right the first time",
          "<p>Remodel electrical has to be planned before cabinets and drywall go in. We walk the space with you, flag anything that needs upgrading to pass inspection, and give you a clear price before work starts.</p>")],
        [("Do kitchen remodels need a permit?", "Most kitchen and bathroom remodels that add or change circuits require an electrical permit. We handle permits and inspections."),
         ("Can you update the wiring in an older home during a remodel?", "Yes. Remodels are the best time to replace outdated wiring, add grounding and GFCI protection, and add circuits for modern appliances."),
         ("Do you work with general contractors?", "Yes. We work with remodelers and general contractors as their electrical sub, and directly with homeowners.")],
        "Kitchen & Bath Remodels",
        gallery=gallery_html([
            ("bath-remodel-vanity-mirror.jpg", "Bathroom remodel: vanity lighting, recessed cans and exhaust fan"),
            ("bath-shower-lighting.jpg", "Shower with recessed lighting and fan"),
            ("bath-powder-room-wallpaper.jpg", "Powder room remodel with new lighting"),
            ("kitchen-remodel-range-hood.jpg", "Kitchen remodel: range, hood and lighting circuits"),
            ("kitchen-pendant-lighting.jpg", "Kitchen pendant lighting over the island"),
            ("bath-remodel-shower-fan.jpg", "Full bathroom remodel, wired to code"),
        ], "Recent remodels", "Kitchens and bathrooms we've wired"))

    service_page(
        "panel-upgrades.html", "Electrical Panel Upgrades, EV Chargers & Surge Protection",
        "Panel Upgrade Electrician | Aurora & Denver | Master Electric",
        "Electrical panel replacements, service upgrades, subpanels, EV charger installs and whole-home surge protection in Aurora and the Denver Metro. Call 720-456-1384.",
        "An outdated or full panel limits what you can add to your home. We replace panels, upgrade service, add subpanels and install EV chargers and surge protection, all permitted and inspected.",
        "service-exterior-panel-meter.jpg", "Exterior meter and new panel installed by Master Electric",
        ["Panel replacements and service upgrades", "Subpanels for basements, garages and additions",
         "Level 2 EV charger installation", "Whole-home surge protection", "Breaker replacement and installation",
         "Grounding and bonding corrections", "Aluminum wiring repair and rewires", "Coordination with Xcel Energy when needed"],
        [("Signs you may need a panel upgrade",
          "<p>Breakers that trip often, no open spaces for new circuits, an older or recalled panel brand, flickering lights, or plans for an EV charger, hot tub or basement finish are all reasons to have your panel looked at.</p>")],
        [("How long does a panel replacement take?", "Most residential panel swaps are completed in one day. Service upgrades that need utility coordination can take longer to schedule."),
         ("Can I install an EV charger on my current panel?", "Sometimes. We check your panel capacity and load. If there's room we install the charger on its own circuit; if not, we'll explain your options, including load management or an upgrade."),
         ("Is a panel upgrade permitted?", "Yes. Panel and service work requires a permit and inspection, which we handle.")],
        "Panel Upgrades & EV Chargers")

    service_page(
        "electrical-repair.html", "Electrical Repair & Troubleshooting",
        "Electrical Repair & Troubleshooting | Aurora & Denver | Master Electric",
        "Electrician for repairs and troubleshooting in Aurora and the Denver Metro: dead outlets, tripping breakers, lighting, fans and smoke detectors. Call 720-456-1384.",
        "Something not working? We find the problem and fix it, from a dead outlet or tripping breaker to new lights, fans and smoke detectors.",
        "repair-burned-receptacle.jpg", "Burned-out 240V receptacle found and replaced by Master Electric",
        ["Dead outlets and circuits", "Breakers that trip or won't reset", "Flickering or buzzing lights",
         "Light fixture and ceiling fan installation", "Outlet and switch replacement, USB and smart switches", "Hot tub, sauna and outdoor equipment hookups", "Underground feeds to garages, sheds and detached structures",
         "Smoke and carbon monoxide detector installation", "Exterior, landscape and garage lighting",
         "Rental property and pre-sale repairs"],
        [("Fast answers on small jobs",
          "<p>For many small jobs, you can text us a photo and we'll tell you what it will take. We work for homeowners, landlords and property managers, and businesses that need a reliable electrician.</p>")],
        [("Do you do small jobs?", "Yes. We handle everything from one outlet or fixture to full remodels."),
         ("Do you work on rental properties?", "Yes. We work with landlords and property managers on repairs, turnovers and remodels."),
         ("What should I do if I smell burning or see sparks?", "Turn off the breaker for that circuit if it's safe to do so, and call us. If there's smoke or fire, call 911 first.")],
        "Electrical Repair & Service",
        gallery=gallery_html([
            ("repair-burned-receptacle.jpg", "Burned 240V receptacle found during a service call"),
            ("repair-new-receptacle.jpg", "Replaced with a new receptacle, safe and to code"),
            ("service-panel-breakers.jpg", "Panel troubleshooting and breaker replacement"),
            ("service-subpanel-wiring.jpg", "Clean subpanel wiring for added circuits"),
            ("service-outdoor-sauna-hookup.jpg", "Outdoor sauna and equipment hookup"),
            ("service-underground-conduit-trench.jpg", "Underground conduit for a detached structure"),
        ], "Recent service calls", "Problems found, fixed right"))

    # Commercial
    body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("", "Commercial Electrical"))}
  <h1>Commercial Electrical Contractor, Denver Metro</h1>
  <p class="lead">We work with general contractors and business owners on tenant improvements, retail and restaurant remodels, lighting upgrades and commercial service work across the Denver Metro.</p>
  <div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-outline" style="color:#fff" href="mailto:{EMAIL}?subject=Bid%20invitation">Send us plans to bid</a></div>
</div></section>
<section class="section"><div class="wrap split" style="align-items:start">
  <div>
    <h2>For general contractors</h2>
    <p>We bid and build electrical scopes for retail and restaurant tenant improvements and remodels, including work for national brands. We price from the plans, show up on schedule, and keep inspections and closeout moving.</p>
    <ul class="checklist">
      <li>Retail and restaurant tenant improvements</li>
      <li>Remodels and refreshes for national chains</li>
      <li>Lighting, LED retrofits and lighting control systems</li>
      <li>Power distribution, panels and equipment connections</li>
      <li>Kitchen equipment and hood wiring</li>
      <li>Permits, inspections and closeout</li>
    </ul>
    <h2>For business owners</h2>
    <p>Need a reliable electrician for your shop, office, warehouse or restaurant? We handle repairs, added circuits and equipment, lighting upgrades and troubleshooting.</p>
    <h2>Safety and credentials</h2>
    <p>Owned by a Colorado Master Electrician (ME.3001269). Colorado Electrical Contractor #{LICENSE}. Certificates of insurance are available on request.</p>
  </div>
  <div>
    <img src="/img/commercial-restaurant-bar-lighting.jpg" alt="Restaurant serving bar with feature ceiling and lighting wired by Master Electric" loading="lazy" style="aspect-ratio:4/3;object-fit:cover;width:100%">
    <div class="contact-box" style="margin-top:24px">
      <h3>Invite us to bid</h3>
      <p>Send plans and your bid date to <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{TEL}">{PHONE}</a>.</p>
    </div>
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <div class="center"><span class="eyebrow">Recent commercial work</span><h2>From rough-in to final trim</h2>
  <p class="lead">A look at recent commercial projects, from framing-stage rough-in to finished lighting and rooftop equipment.</p></div>
  <div class="grid grid-3 gallery" style="margin-top:28px">
    <figure><img src="/img/commercial-dining-pendant-lighting.jpg" alt="Dining room with drum pendant lighting and cove lighting" loading="lazy"><figcaption>Dining room pendants and cove lighting</figcaption></figure>
    <figure><img src="/img/commercial-lobby-ceiling-lighting.jpg" alt="Lobby and lounge with large drum ceiling fixtures" loading="lazy"><figcaption>Lobby and lounge ceiling fixtures</figcaption></figure>
    <figure><img src="/img/commercial-metal-stud-rough-in.jpg" alt="Electrical rough-in in a metal-stud commercial build-out" loading="lazy"><figcaption>Rough-in during a commercial build-out</figcaption></figure>
    <figure><img src="/img/commercial-rooftop-unit-disconnect.jpg" alt="Rooftop HVAC unit with new disconnect and wiring" loading="lazy"><figcaption>Rooftop unit power and disconnects</figcaption></figure>
    <figure><img src="/img/commercial-exterior-wall-sconce.jpg" alt="Exterior wall sconce on a commercial building" loading="lazy"><figcaption>Exterior building lighting</figcaption></figure>
    <figure><img src="/img/electrical-panel-install.jpg" alt="New electrical panel and disconnect installation" loading="lazy"><figcaption>Panels and power distribution</figcaption></figure>
  </div>
</div></section>
'''
    page("commercial.html", "Commercial Electrical Contractor | Denver Metro | Master Electric",
         "Commercial electrical contractor for tenant improvements, retail and restaurant remodels, lighting and service in the Denver Metro. Send plans to bid: 720-456-1384.",
         body)


# ---------------------------------------------------------------- City pages
CITY_TEXT = {
    "Aurora": ("Aurora is home base for Master Electric, so we can usually get out to you quickly. We wire basement finishes, remodels and panel upgrades in neighborhoods all over Aurora, from older homes near Colfax to newer builds in Southlands, Tallyn's Reach and Saddle Rock.",
               "City of Aurora"),
    "Denver": ("We work throughout Denver, from older homes that need wiring and panel updates to basement finishes, kitchen remodels and commercial tenant improvements.",
               "City and County of Denver"),
    "Centennial": ("Centennial homeowners call us for basement finishes, kitchen and bath remodels, panel upgrades and EV chargers. We're a short drive from Aurora.",
                   "the local building department"),
    "Parker": ("We serve Parker and the surrounding Douglas County area with basement finish electrical, remodels, panel upgrades and commercial work.",
               "the Town of Parker / Douglas County building department"),
}


def build_cities():
    for filename, city in CITY_PAGES:
        intro, authority = CITY_TEXT[city]
        faqs = [(f"Do you serve all of {city}?", f"Yes. We work throughout {city} and the surrounding Denver Metro area."),
                (f"Do you pull electrical permits in {city}?", f"Yes. We pull permits and schedule inspections with {authority} for work that requires them."),
                ("Do you offer free estimates?", "Yes. Call or text 720-456-1384 or request a quote online.")]
        svc = "".join(f'<div class="card"><div class="icon" aria-hidden="true">{i}</div><h3><a href="/{h}">{t}</a></h3><p>{d}</p><a class="more" href="/{h}">Learn more →</a></div>' for h, t, i, d in SERVICES)
        body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("service-areas.html", "Service Areas"), ("", city))}
  <h1>Electrician in {city}, CO</h1>
  <p class="lead">{intro}</p>
  <div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-outline" style="color:#fff" href="/contact.html">Get a Free Quote</a></div>
</div></section>
<section class="section"><div class="wrap">
  <h2>Electrical services in {city}</h2>
  <div class="grid grid-3" style="margin-top:24px">{svc}</div>
</div></section>
<section class="section alt"><div class="wrap split">
  <div>
    <h2>Why {city} homeowners choose Master Electric</h2>
    <ul class="checklist">
      <li>Licensed Colorado electrical contractor #{LICENSE}</li>
      <li>20+ years in the electrical trade</li>
      <li>Permits and inspections handled for you</li>
      <li>Clear written estimates, on time and on budget</li>
      <li>Residential and commercial experience</li>
    </ul>
  </div>
  <div>{faq_html(faqs)}</div>
</div></section>
{reviews_html(2)}
'''
        page(filename, f"Electrician in {city}, CO | Master Electric, LLC",
             f"Licensed electrician serving {city}, CO. Basement finishes, remodels, panel upgrades, EV chargers and repairs. Free estimates: call 720-456-1384.",
             body, current="service-areas.html", extra_schema=[faq_schema(faqs)])


def build_areas():
    cities = "".join(f'<div class="card"><h3><a href="/{h}">{c}</a></h3><p>Electrical services in {c}, CO.</p><a class="more" href="/{h}">{c} electrician →</a></div>' for h, c in CITY_PAGES)
    others = "".join(f"<li>{a}</li>" for a in AREAS)
    body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("", "Service Areas"))}
  <h1>Service Areas</h1>
  <p class="lead">Based in Aurora, Master Electric serves homeowners, builders and businesses across the Denver Metro area.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="grid grid-4">{cities}</div>
  <h2 style="margin-top:48px">Cities we serve</h2>
  <ul class="checklist cols-2">{others}</ul>
  <p>Don't see your city? Call <a href="tel:{TEL}">{PHONE}</a> and ask. We cover most of the Denver Metro.</p>
</div></section>
'''
    page("service-areas.html", "Service Areas | Aurora, Denver & Denver Metro Electrician | Master Electric",
         "Master Electric serves Aurora, Denver, Centennial, Parker, Englewood, Littleton, Lakewood and the rest of the Denver Metro. Call 720-456-1384.",
         body)


# ---------------------------------------------------------------- About
def build_about():
    body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("", "About"))}
  <h1>About Master Electric</h1>
  <p class="lead">A locally owned electrical contractor in Aurora, Colorado, built on doing the work right, showing up when we say we will and pricing jobs fairly.</p>
</div></section>
<section class="section"><div class="wrap split">
  <div>
    <h2>Local, licensed and hands-on</h2>
    <p>Master Electric, LLC is a licensed Colorado electrical contractor (#{LICENSE}) serving the Denver Metro area. With more than 20 years in the electrical trade, we handle residential work, including basement finishes, remodels, panel upgrades and repairs, along with commercial tenant improvements and service.</p>
    <p>When you call, you talk to the owner. We give clear written estimates, pull the permits, and stay with the job until it passes inspection.</p>
    <h2>Faith-driven. Family-owned.</h2>
    <p>Master Electric is a family-owned company built on faith in Jesus Christ. For us, that isn't about religion. It's about following Him in how we work: being honest about what a job needs and what it will cost, keeping our word, and treating every home and jobsite with respect.</p>
    <p>We try to do every job as if we were doing it for the Lord, not just for a paycheck. That's where "Done right. No callbacks." comes from.</p>
    <h2>Licensing and training</h2>
    <ul class="checklist">
      <li>Colorado Master Electrician, license ME.3001269</li>
      <li>Current on Colorado continuing education, including the 2026 NEC update</li>
      <li>Licensed Colorado electrical contractor #{LICENSE}</li>
      <li>Insured, with certificates available on request</li>
    </ul>
    <div class="btn-row"><a class="btn btn-primary" href="tel:{TEL}">📞 Call {PHONE}</a><a class="btn btn-dark" href="/contact.html">Request a Quote</a></div>
  </div>
  <img src="/img/custom-led-shelving.jpg" alt="Custom LED lighting project by Master Electric" loading="lazy">
</div></section>
{reviews_html()}
'''
    page("about.html", "About Master Electric, LLC | Licensed Aurora, CO Electrician",
         "Master Electric is a locally owned, licensed electrical contractor in Aurora, CO with 20+ years in the trade, serving the Denver Metro.",
         body)


# ---------------------------------------------------------------- Contact
def build_contact():
    opts = "".join(f"<option>{t}</option>" for _, t, _, _ in SERVICES)
    body = f'''<section class="page-hero"><div class="wrap">
  {crumbs(("", "Contact"))}
  <h1>Get a Free Quote</h1>
  <p class="lead">Call or text for the fastest answer, or send us the details below and we'll get back to you.</p>
</div></section>
<section class="section"><div class="wrap split" style="align-items:start">
  <form class="form" action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="New quote request from masterelectricdenver.com">
    <input type="hidden" name="from_name" value="Master Electric website">
    <input type="hidden" name="redirect" value="{DOMAIN}/thank-you.html">
    <input type="checkbox" name="botcheck" style="display:none" tabindex="-1" autocomplete="off">
    <div class="row2">
      <div><label for="name">Name *</label><input id="name" name="name" required autocomplete="name"></div>
      <div><label for="phone">Phone *</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
    </div>
    <div class="row2">
      <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"></div>
      <div><label for="city">City</label><input id="city" name="city" placeholder="e.g. Aurora"></div>
    </div>
    <div><label for="service">What do you need?</label><select id="service" name="service"><option value="">Choose one</option>{opts}<option>Other</option></select></div>
    <div><label for="details">Project details</label><textarea id="details" name="details" placeholder="Tell us about the project, timeline and anything else we should know."></textarea></div>
    <button class="btn btn-primary" type="submit" style="justify-self:start">Send Request</button>
    <p style="font-size:.85rem;color:var(--muted);margin:0">We only use your information to respond to your request.</p>
  </form>
  <div class="contact-box">
    <h2>Talk to us directly</h2>
    <p>Call or text:</p>
    <a class="big-phone" href="tel:{TEL}">{PHONE}</a>
    <p style="margin-top:18px">Email:<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p>Based in Aurora, CO, serving the Denver Metro.</p>
    <p>Colorado Electrical Contractor #{LICENSE}</p>
    <p><strong>General contractors:</strong> send plans and bid dates to the email above.</p>
  </div>
</div></section>
'''
    page("contact.html", "Contact & Free Quote | Master Electric, LLC | 720-456-1384",
         "Request a free electrical quote from Master Electric in Aurora, CO. Call or text 720-456-1384 or send your project details online.",
         body)
    body = f'''<section class="section"><div class="wrap center" style="max-width:700px">
  <h1>Thanks — we got your request!</h1>
  <p class="lead">We'll get back to you soon. For anything urgent, call or text <a href="tel:{TEL}">{PHONE}</a>.</p>
  <a class="btn btn-dark" href="/">Back to home</a>
</div></section>'''
    page("thank-you.html", "Thank You | Master Electric, LLC", "Thanks for contacting Master Electric.", body)
    body = f'''<section class="section"><div class="wrap center" style="max-width:700px">
  <h1>Page not found</h1>
  <p class="lead">That page doesn't exist. Try one of these, or call <a href="tel:{TEL}">{PHONE}</a>.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn btn-dark" href="/">Home</a><a class="btn btn-outline" href="/contact.html">Contact</a></div>
</div></section>'''
    page("404.html", "Page Not Found | Master Electric, LLC", "Page not found.", body)


def build_seo_files(urls):
    today = datetime.date.today().isoformat()
    items = "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    with open(os.path.join(ROOT, "CNAME"), "w") as f:
        f.write("masterelectricdenver.com\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    # Google Search Console ownership verification - do not remove
    with open(os.path.join(ROOT, "googleff62fdcd4ed4133d.html"), "w") as f:
        f.write("google-site-verification: googleff62fdcd4ed4133d.html")


if __name__ == "__main__":
    build_home(); build_services(); build_cities(); build_areas(); build_about(); build_contact()
    pages = ["index.html"] + [h for h, *_ in SERVICES] + ["service-areas.html"] + [h for h, _ in CITY_PAGES] + ["about.html", "contact.html"]
    build_seo_files([DOMAIN + "/" + ("" if p == "index.html" else p) for p in pages])
    print("Built", len(os.listdir(ROOT)), "entries in", os.path.abspath(ROOT))

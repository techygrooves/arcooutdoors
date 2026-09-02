# PROJECT-SPEC.md — Arco Outdoors

**This file is the permanent source of truth for every subsequent session on this
repository. Read it before writing any code. Update it whenever a decision,
route, token, or verified fact changes.**

Last updated: 2026-09-01 (pass 9 — remaining location pages, Areas We Serve)

---

## 1. BUSINESS

**Arco Outdoors** — outdoor remodeling contractor, South Florida.

## 2. DOMAIN

`https://www.arcooutdoors.com/`

Canonical form: `https://` + `www.` + trailing slash on directory URLs.
Every canonical, sitemap entry, Open Graph URL and JSON-LD `@id` must use it —
**including when the site is previewed somewhere else.** Those URLs identify the
production page and must not be rewritten for a preview host.

### 2.1 Where the site can be served

The site is mount-point independent: it renders identically at a domain root
(`https://www.arcooutdoors.com/`) and under a subpath
(`https://techygrooves.github.io/arcooutdoors/`). That is not automatic — see
§8.6. Verify both before shipping.

If GitHub Pages is to serve the production domain, add a `CNAME` file
containing `www.arcooutdoors.com` at the repository root and point DNS at
Pages. Until then the project-page URL is the working preview, and the
canonical tags correctly continue to name the production domain.

## 3. VERIFIED CONTACT INFORMATION

The only contact facts confirmed for this project. Do not alter, embellish, or
add to them without new source material.

| Field | Value |
|---|---|
| Phone | 305-951-8862 (`tel:+13059518862`) |
| Email | jonah@arcooutdoors.com |
| Address | 2940 SW 81st Way, Davie, FL 33328 |
| Contractor license | CBC1269393 |
| Published business hours | Monday–Friday, 8:00 AM – 6:00 PM |

Not supplied, and therefore **must not be invented**: social media profile URLs,
Google Business Profile URL, weekend or holiday hours, service radius in miles,
emergency line, secondary phone numbers, staff names other than the email
local-part, year founded, entity type, insurance carrier or policy numbers.

## 4. CORE POSITIONING

Arco is a contractor capable of **complete outdoor transformations**, not only a
single-trade paver contractor.

> One accountable contractor for coordinated South Florida outdoor spaces —
> hardscaping, outdoor kitchens, shade structures, turf, fencing and related
> improvements.

Every page should reinforce coordination and single-point accountability. The
existing homepage already carries this in "Design-to-build, in-house.", "One
accountable team", and the "Fencing & More" card.

### Claims that must never be written

`#1 contractor` · `best contractor` · `thousands of projects` · `20 years
experience` · `award winning` · specific project counts · specific crew sizes ·
"family owned since …" · guarantees, warranties or financing terms — **unless
verified source material exists in this repository.**

See §12 for claims currently live on the homepage that are *not* backed by
source material and need owner sign-off.

## 5. PRIMARY SERVICES

Canonical list and canonical naming. Use these exact names in navigation, form
selects, schema and headings.

1. Complete Outdoor Remodeling
2. Paver Installation
3. Patios
4. Driveways
5. Pool Decks
6. Outdoor Kitchens
7. Pergolas
8. Tiki Huts
9. Artificial Turf
10. Fencing
11. Impact Windows & Doors

## 6. PRIMARY SEO GEOGRAPHY

The homepage represents **Arco Outdoors and the broader South Florida market**.
It is *not* a Parkland landing page. (Three Parkland-first strings were corrected
during this pass — see §13.)

Priority location pages, in build order:

| # | City | Route |
|---|---|---|
| 1 | Parkland | `/service-areas/parkland-fl/` |
| 2 | Davie | `/service-areas/davie-fl/` |
| 3 | Weston | `/service-areas/weston-fl/` |
| 4 | Plantation | `/service-areas/plantation-fl/` |
| 5 | Fort Lauderdale | `/service-areas/fort-lauderdale-fl/` |
| 6 | Pembroke Pines | `/service-areas/pembroke-pines-fl/` |
| 7 | Coral Springs | `/service-areas/coral-springs-fl/` |
| 8 | Boca Raton | `/service-areas/boca-raton-fl/` |

City slugs carry the `-fl` suffix. Service slugs do not mirror their display
names exactly — see §8 for the three that differ.

Counties named on the homepage: Broward, Miami-Dade, Palm Beach.
The homepage service-area list carries 33 municipalities (Parkland was missing
until pass 2 despite being priority market #1). That list is a coverage
statement, not a claim of completed work in each. The eight priority markets
are hyperlinked to their pages; the remaining 25 are plain text, so the link
affordance itself signals which markets have a page.

**Never claim an Arco project occurred in a particular city unless that project
location is verified.**

## 7. TECHNOLOGY CONSTRAINTS

Static site. Deploys by copying the repository to any static host.

**Allowed:** semantic HTML5, CSS3 (custom properties, grid, flexbox), vanilla
JavaScript (ES2018, no transpiling), self-hosted WOFF2 fonts, WebP images.

**Forbidden:** React, Vue, Angular, Next.js, npm/Node as a runtime or build
requirement, bundlers, server-side rendering, WordPress, jQuery, CSS frameworks,
any client-side router.

**Internal URLs are authored root-absolute and shipped relative.** Write
`/assets/…` and `/services/…`; `tools/sync-partials.py` rewrites them to
depth-correct relative URLs on save (§8.6). Never hand-write `../../` — the
tool computes it, and `tools/check-links.py` proves the arithmetic.

There is no build step and there must never be one. `assets/` is served as-is.
Image conversion and similar one-off authoring chores may use local tooling, but
the tooling must not become a repository dependency.

## 8. SITE STRUCTURE

```
/
  index.html                    ← homepage (live)
  404.html                      ← live
  robots.txt  sitemap.xml  favicon.svg  PROJECT-SPEC.md

  services/index.html                        ← live (hub)
  services/outdoor-remodeling/index.html     ← live
  services/paver-installation/index.html     ← live
  services/patios/index.html                 ← live
  services/driveways/index.html              ← live
  services/pool-decks/index.html             ← live
  services/outdoor-kitchens/index.html       ← live
  services/pergolas/index.html               ← live
  services/tiki-huts/index.html              ← live
  services/turf/index.html                   ← live
  services/fence/index.html                  ← live
  services/impact-windows-doors/index.html   ← live

  service-areas/index.html                   ← live (hub)
  service-areas/parkland-fl/index.html       ← live
  service-areas/davie-fl/index.html          ← live
  service-areas/weston-fl/index.html         ← live
  service-areas/plantation-fl/index.html     ← live
  service-areas/fort-lauderdale-fl/index.html  ← live
  service-areas/pembroke-pines-fl/index.html   ← live
  service-areas/coral-springs-fl/index.html    ← live
  service-areas/boca-raton-fl/index.html       ← live

  assets/
    css/style.css               ← tokens, global nav, footer, homepage components
    css/pages.css               ← shared interior-page components
    js/main.js                  ← nav, current-page, reveal, form, year
    images/  fonts/
    partials/header.html        ← canonical header markup (source of truth)
    partials/footer.html        ← canonical footer markup (source of truth)

  tools/sync-partials.py        ← inserts partials + relativises paths
  tools/check-links.py          ← resolves every link/asset against the disk
  .nojekyll                     ← stops GitHub Pages running Jekyll
```

### 8.1 The partial system — how to build every future page

The header and footer are **generated, not written**. Each page carries markers:

```html
<body data-page="services">
<!-- @partial:header -->
   …generated — do not hand-edit…
<!-- @endpartial:header -->

<main id="main"> … </main>

<!-- @partial:footer -->
<!-- @endpartial:footer -->
</body>
```

Workflow for a new page:

1. Copy `index.html`'s `<head>` block and swap the title, description, canonical,
   Open Graph and JSON-LD. Load `style.css` **then** `pages.css` — every page
   loads both, so the `<head>` boilerplate is identical everywhere.
2. Set `<body data-page="…">` (see the table below). Nothing else drives the
   navigation's current state.
3. Paste the two marker pairs; leave them empty.
4. Run `python3 tools/sync-partials.py` — it fills them from `assets/partials/`.
5. Add the URL to `sitemap.xml`.

To change the navigation or footer **anywhere**, edit the partial and re-run the
script. Never edit the copy inside a page; `python3 tools/sync-partials.py --check`
exits non-zero when a page has drifted, and is the pre-commit guard.

The script is Python 3 stdlib only and touches nothing at deploy time. The
committed HTML is complete and static — §7's "no build step" rule still holds.

| `data-page` value | Marks as current |
|---|---|
| `home` | Home |
| `services` | Services |
| `projects` | Projects |
| `service-areas` | Service Areas |
| `about` | About |
| `resources` | Resources (blog, gallery, reviews) |

`main.js` also sets `aria-current="page"` on any dropdown-panel or footer link
whose `href` matches the current path, so a service page lights up both its
top-level trigger and its own entry.

### 8.2 Canonical routes

Three service slugs deliberately differ from their display names. Use the slug
in URLs and the display name in copy — never the reverse.

| Nav label | Route |
|---|---|
| Complete Outdoor Remodeling | `/services/outdoor-remodeling/` |
| Paver Installation | `/services/paver-installation/` |
| Patios | `/services/patios/` |
| Driveways | `/services/driveways/` |
| Pool Decks | `/services/pool-decks/` |
| Outdoor Kitchens | `/services/outdoor-kitchens/` |
| Pergolas | `/services/pergolas/` |
| Tiki Huts | `/services/tiki-huts/` |
| **Artificial Turf** | `/services/turf/` |
| **Fencing** | `/services/fence/` |
| Impact Windows & Doors | `/services/impact-windows-doors/` |

Plus: `/`, `/services/`, `/projects/`, `/service-areas/` + the eight `-fl` city
routes in §6, `/about-us/`, `/gallery/`, `/reviews/`, `/blog/`, `/contact-us/`,
`/get-a-quote/`, `/privacy-policy/`, `/cookie-policy/`, `/accessibility/`.

**Live as of pass 10 (23 URLs):** `/`, `/services/`, all eleven service pages,
`/projects/`, `/service-areas/`, and all eight city pages — `parkland-fl`,
`davie-fl`, `weston-fl`, `plantation-fl`, `fort-lauderdale-fl`,
`pembroke-pines-fl`, `coral-springs-fl`, `boca-raton-fl`. Everything else is
linked from the global nav or footer and returns 404 until its page is built — a
deliberate, approved state, not a defect. `sitemap.xml` lists only URLs that
resolve; add each entry as it ships.

**The service and location tiers are both complete** — all eleven §5 services
and all eight §6 priority markets have a page — and `/projects/` now anchors the
evidence tier.

**What remains** is `/about-us/`, `/contact-us/`, `/get-a-quote/`, `/gallery/`,
`/reviews/`, `/blog/`, `/privacy-policy/`, `/cookie-policy/` and
`/accessibility/`.

`/projects/` and `/gallery/` are **not** two views of the same content, and must
never converge. Gallery is visual browsing: photography, minimal text, fast to
skim. Projects is evidence: written records of specific work, held to the §11.1
template. A change that makes either look like the other has broken the
distinction the two routes exist to draw.

### 8.3 Navigation model

Six top-level items; three carry dropdowns.

| Item | Route | Dropdown |
|---|---|---|
| Home | `/` | — |
| Services | trigger only | 11 services + View All Services |
| Projects | `/projects/` | — |
| Service Areas | trigger only | 8 cities + View All Service Areas |
| About | `/about-us/` | — |
| Resources | trigger only | Blog, Gallery, Reviews |

The primary CTA (`Get a Quote` → `/get-a-quote/`) and the phone number sit in the
sand bar above the ink nav bar, and both reappear as large actions inside the
mobile drawer.

Dropdown triggers are `<button>` elements, never links — they do not navigate,
so a link would lie to assistive technology. `aria-expanded` on the trigger is
the single source of truth in both presentations; CSS reads it for the chevron
and the hamburger, JS toggles the panel's `hidden` attribute.

Behaviour, desktop (>860px): hover opens; a click on an already-hover-opened
panel keeps it open (a plain toggle would shut the panel the instant the visitor
clicked what they wanted) and a second click closes it; opening one closes the
others; `Escape` closes and returns focus to the trigger; moving focus out of
the group closes it; an outside click closes everything.

Behaviour, mobile (≤860px): the ink bar becomes a fixed drawer offset by
`--header-h` (measured by JS, because the header wraps to two rows on phones).
Panels become accordions and several may sit open at once. Opening the drawer
locks body scroll with `position: fixed` — `overflow: hidden` alone does not
hold on iOS Safari — and restores the exact scroll offset on close, with
`scroll-behavior` forced to `auto` so the restore does not animate. Tab is
trapped inside the drawer. `Escape` closes it and returns focus to the toggle.
Choosing any link closes it. Crossing the breakpoint closes everything, so no
overlay is ever stranded.

Without JavaScript (`html:not(.js)` in `style.css`, not a per-page `<noscript>`):
desktop panels open on `:hover`/`:focus-within`; on mobile the drawer becomes a
static, fully expanded list and the hamburger is hidden. Every destination stays
reachable.

### 8.4 Footer model

Five columns — brand + license, Services (9), Service Areas (6 + View All),
Company (6), Contact — over a legal bar carrying Privacy Policy, Cookie Policy
and Accessibility Statement. Collapses to three columns at 1180px and to
`auto-fit` at 860px.

**No social profile links.** None have been verified for this business (§3). Do
not add them on the strength of an icon looking nice; the four `href="#"`
placeholders that shipped in pass 1 were removed in pass 2.

### 8.5 Interior page recipe

Every interior page shipped so far follows the same skeleton. Copy it rather
than inventing a new arrangement — the point is that a visitor cannot tell which
page was built in which pass.

```
breadcrumb (.breadcrumb)                    ← always, on every page below root
page banner (.page-hero + __media/__scrim)  ← one H1, eyebrow, lead, two CTAs
jump bar (.jumpbar)                         ← optional; long pages only
intro (.prose)                              ← states the page's actual argument
…body sections, alternating .section--sand…
related links (.link-index)
service areas (.link-index)
FAQ (.faq, native <details>)                ← 6 entries, mirrored in FAQPage JSON-LD
closing CTA (.cta-band)
```

Section rhythm alternates `.section` and `.section--sand` so no two adjacent
bands share a ground. Headings inside a section use `.section-head--left`;
centred `.section-head` is reserved for the homepage.

**Structured data per page type**

| Page | `@graph` nodes |
|---|---|
| Hub | `BreadcrumbList` + `CollectionPage` (with `ItemList`) + `FAQPage` |
| Service | `BreadcrumbList` + `Service` + `WebPage` + `FAQPage` |
| Location | `BreadcrumbList` + `Service` (`areaServed` = that `City`) + `WebPage` + `FAQPage` |

**Location pages must never emit `LocalBusiness`, `GeneralContractor`, or any
`address` / `PostalAddress` node.** Doing so implies a branch office in that
city. The business is declared once, on the homepage, at the one verified
address (§3); every location page references it as
`provider: { "@id": "…/#business" }` and expresses the city through
`Service.areaServed` only.

`Service.provider` and `WebPage.isPartOf` reference the homepage `@id`s
(`…/#business`, `…/#website`) rather than redeclaring the business. Every FAQ
answer in JSON-LD must match the visible `<details>` text. Still **no**
`aggregateRating` or `Review` anywhere (§12).

### 8.6 Portable paths — why links are relative

The site must render correctly whether it is served from a domain root or from
a subpath. A GitHub Pages *project* site serves at `/<repo>/`, so a page asking
for `/assets/css/style.css` gets `techygrooves.github.io/assets/css/style.css`,
which does not exist. The symptom is total: no CSS, no JavaScript, no images,
every internal link 404. It looks like the site is broken; nothing is wrong
with it except where it was pointed.

**The rule.** Author internal URLs root-absolute — `/assets/…`, `/services/…` —
because that is easy to write and easy to grep. Then run
`python3 tools/sync-partials.py`, which rewrites them to depth-correct relative
URLs as it saves:

| Page | `/assets/css/style.css` becomes | `/` becomes |
|---|---|---|
| `index.html` | `assets/css/style.css` | `./` |
| `services/index.html` | `../assets/css/style.css` | `../` |
| `services/patios/index.html` | `../../assets/css/style.css` | `../../` |

It covers `href`, `src`, `action`, `poster`, and every candidate inside
`srcset` and `imagesrcset`. It is idempotent, because a relative URL has no
leading slash for the next run to match.

**What is deliberately not rewritten:** `https://` URLs, `#fragments`, `tel:`
and `mailto:`, and therefore the canonical, Open Graph, sitemap and JSON-LD
URLs. Those name the production page and must stay absolute wherever the site
is previewed.

**Verification.** `python3 tools/check-links.py` resolves every relative URL
against the file system from the page that contains it, so wrong `../`
arithmetic is caught here rather than by a visitor. It also fails on any
leftover root-absolute internal URL, any `href="#"`, any fragment without a
matching id, and any canonical or `og:url` not pointing at the production
domain. Links to routes on the map that are not built yet are counted and
reported, not treated as errors.

**Known limitation.** `404.html` uses depth-0 relative paths, so it is styled
for a miss at the site root. A miss at a deeper path (`/services/nope/`)
renders the 404 page unstyled, because its relative paths resolve against the
requested URL rather than the file's own location. That is inherent to a static
404 with relative paths and affects both deployment shapes. It is a deliberate
trade for having the rest of the site work everywhere.

## 9. DESIGN SYSTEM

Extracted verbatim from the original bundled homepage and codified as custom
properties in `assets/css/style.css`. **Change values there and nowhere else.**

### 9.1 Colour

| Token | Value | Role |
|---|---|---|
| `--sand-50` | `#f6f1e8` | page ground |
| `--sand-100` | `#efe6d6` | alternating section ground |
| `--sand-200` | `#cdbfa6` | image placeholder |
| `--white` | `#ffffff` | cards, form fields |
| `--ink` | `#241d15` | primary text, nav bar, dark bands |
| `--ink-800` | `#2b2318` | ground behind hero / CTA imagery |
| `--ink-900` | `#1a150f` | footer ground |
| `--body` | `#5f5544` | body copy on sand |
| `--body-2` | `#443c30` | dense list copy |
| `--muted` | `#8a7a63` | small labels, meta |
| `--gold` | `#e0a94e` | primary CTA fill, accents on dark |
| `--gold-deep` | `#c69749` | hairlines, list marks |
| `--gold-link` | `#b5843a` | links + eyebrows on light ground |
| `--gold-light` | `#e6b661` | headings/accents on dark ground |
| `--cream` | `#fdfaf3` | text on dark |
| `--cream-2` | `#efe6d6` | nav text on ink |
| `--foot-text` | `#cabda6` | footer body |
| `--foot-muted` | `#9a8d76` | footer secondary |
| `--foot-dim` | `#7d715c` | footer legal bar |
| `--star` | `#f5b400` | rating stars |

Overlay recipes: hero scrim `linear-gradient(90deg, rgba(20,16,10,.82), rgba(20,16,10,.55) 45%, rgba(20,16,10,.25))`;
CTA scrim `linear-gradient(180deg, rgba(20,16,10,.85), rgba(20,16,10,.7))`;
caption scrim `linear-gradient(0deg, rgba(20,16,10,.78), transparent)`.
Decorative texture images sit at `.14` (Why Arco) and `.22` (CTA) opacity.

### 9.2 Typography

- **Display** — `Cormorant Garamond`, weights 400–700 + italic 400–500.
  Self-hosted, latin + latin-ext variable subsets. Used for every heading, the
  wordmark, statistics, pull quotes and the phone number.
- **Body** — `Manrope`, weights 400–800. Self-hosted, latin + latin-ext.
  Used for all body copy, navigation, buttons and form controls.

| Role | Spec |
|---|---|
| H1 | display 600 · `clamp(44px, 6vw, 82px)` · lh 1.02 · ls −.01em |
| H2 | display 500 · `clamp(34px, 4vw, 54px)` · lh 1.08 |
| H2 (on dark) | display 500 · `clamp(32px, 4vw, 50px)` · lh 1.1 |
| H3 (card) | display 600 · 26px · lh normal |
| H3 (journal) | display 600 · 23px · lh 1.25 |
| Eyebrow | body 700 · 12px · ls .3em · uppercase, preceded by a 34×1px gold rule |
| Hero eyebrow | body 700 · 12.5px · ls .34em, 52px rule |
| Lead | body 400 · 17px · lh 1.8 (18px/1.7 over imagery) |
| Card copy | body 400 · 14.5px · lh 1.7 |
| Nav | body 600 · 12.5px · ls .16em · uppercase |
| Button | body 700 · 13px · ls .14em · uppercase (12.5px for small) |
| Micro label | body 600–700 · 10.5–12px · ls .16–.42em · uppercase |

Italic display type is the emphasis device (`art form.`, review quotes). Never
italicise body sans.

### 9.3 Buttons

| Class | Look |
|---|---|
| `.btn--gold` | `--gold` fill, `--ink` text, gold glow shadow → hover `--cream` fill |
| `.btn--ghostLight` | 1.5px `rgba(253,250,243,.5)` border, cream text → hover cream fill |
| `.btn--ghostDark` | 1.5px `--ink` border, ink text → hover ink fill |
| `.link-action` | 12px/700/.16em gold-link text + `→`, gap widens 8px→14px on hover |

Padding `18px 38px` (`.btn--sm` `15px 26px`, `.btn--block` `17px` full width).
**Square corners — buttons never have a radius.**

### 9.4 Cards, radius, shadow

The identity is predominantly **square**. Radius is the exception, not the rule.

| Component | Radius | Shadow |
|---|---|---|
| Service / journal card | `0`, 1px `rgba(36,29,21,.08)` border | none → hover `0 26px 50px rgba(36,29,21,.16)` |
| Review card | `12px` | `0 40px 60px -22px rgba(36,29,21,.4), 0 12px 22px rgba(36,29,21,.1), inset 0 1px 0 rgba(255,255,255,.95)`, lifts 8px on hover |
| Form panel | `5px`, 4px `--gold` top border | `0 44px 72px -20px rgba(36,29,21,.4), 0 14px 28px …` |
| Google pill | `60px` | `0 24px 44px -14px rgba(36,29,21,.3), …` |
| About image | `0` | `0 30px 60px rgba(36,29,21,.22)` |
| About badge | `0` | `0 20px 40px rgba(36,29,21,.3)` |
| Avatars, logo mark, social dots | `50%` | logo `0 6px 18px rgba(198,151,73,.28)` |
| Form input | `0` | inset `0 2px 5px rgba(36,29,21,.09)`; focus `0 0 0 3px rgba(198,151,73,.18)` + `--gold-deep` border |

### 9.5 Spacing & layout

- Container `max-width: 1280px`, gutter `40px` (`20px` ≤860px). Consultation
  section narrows to `1200px`.
- Section rhythm `110px` block padding (`56px` ≤860px), via `--section-y`.
  Why-Arco band uses `100px`; footer grid `80px / 40px`.
- Card grids `repeat(auto-fit, minmax(270px, 1fr))`, gap `28px` (reviews `30px`).
- Gallery `repeat(auto-fit, minmax(240px, 1fr))`, rows `210px`, gap `18px`,
  with `--xl` (2×2) and `--wide` (2×1) spans.
- Service-area index `repeat(auto-fit, minmax(160px, 1fr))`, gap `10px 40px`.
- Split layouts `repeat(auto-fit, minmax(320px, 1fr))`, gap `72px` (about) /
  `64px` (consultation).

### 9.6 Responsive breakpoints

| Width | Behaviour |
|---|---|
| `> 1180px` | five-column footer |
| `≤ 1180px` | footer drops to three columns, brand column spans full width |
| `861–1080px` | nav link padding and header phone tighten so six items still fit one row |
| `> 860px` | full desktop: horizontal nav with dropdown panels, header phone block + quote button |
| `≤ 860px` | gutter 20px, section padding 56px; header phone and quote button hide, round call icon and hamburger appear; nav becomes a fixed drawer with accordions; trust strip stacks and dividers hide; gallery becomes one column at 220px rows; about badge un-offsets |
| `≤ 480px` | headings allowed to break long words |

Interior pages add `1024px` only for the `.with-rail` article layout.

`--header-h` is set on `<html>` by `main.js` from the measured height of
`.header-top` (92px on tablet and up, 158–184px on phones where the brand row
wraps). The mobile drawer is offset by it. Never hard-code that value.

### 9.7 Image treatment

Full-bleed photography sits under a dark gradient scrim with cream text over it.
Contained photography is square-cornered with a deep soft shadow. Gallery
captions are bottom-anchored over a bottom-up scrim with a gold uppercase
category line above a display-serif name. Decorative textures are heavily
knocked back (`.14`–`.22` opacity) over `--ink`.

### 9.8 Navigation treatment

Two-tier sticky header: a sand top bar (wordmark, phone, gold CTA) above an ink
bar carrying uppercase tracked links, with the active item in `--gold`. Dropdown
triggers are visually identical to plain links plus a 10×7 chevron that rotates
180° when open.

Dropdown panels are `--ink` with a 2px `--gold` top border and a
`0 26px 50px rgba(20,16,10,.45)` shadow, anchored to the trigger's left edge —
except the last item (Resources), which anchors right so it cannot overflow the
viewport. Services and Service Areas use two 190px columns; a `View All …` link
sits below a gold hairline. Panel links are 13.5px `--cream-2`, going `--gold`
on hover.

On mobile the ink bar becomes a fixed drawer sliding in from the right over
280ms, offset from the top by `--header-h`. Panels become accordions indented
behind a gold left rule. Below them sit a large outlined phone action (display
serif number over a tracked micro-label), a full-width gold `Get a Quote`
button, and the licence and hours in `--foot-muted`. The toggle is a bordered
square hamburger that morphs into an X.

Behaviour, keyboard support and the no-JS fallback are specified in §8.3.
Social dots were removed in pass 2 — the class no longer exists.

### 9.9 CTA treatment

Every major section ends in a route to conversion. The three shapes are: the
gold primary button, the outlined secondary button beside it, and the
`.link-action` arrow link inside cards. Phone numbers are always live `tel:`
links. The closing CTA band is a full-bleed dark section with a centred eyebrow,
display heading, one line of copy and a gold/outline button pair.

### 9.10 Interior-page components (pages.css §14)

Added in pass 3, all built on existing tokens:

| Class | Use |
|---|---|
| `.section-head--left` | left-aligned section header; the interior-page default |
| `.note` / `.note--onDark` | callout with a gold left rule — climate notes, scope caveats |
| `.card--service` | homepage `.card` with a 200px media box, for category grids |
| `.card--feature` | one service across the full grid width, image beside copy |
| `.spec-grid` | hairline-topped definition blocks for comparisons |
| `.jumpbar` | sticky-adjacent anchor row for long pages |
| `.areas-grid--compact` | width cap on the shared `.areas-grid`, so the eight-market *Areas we serve* block on a service page reads as two rows of four |

`.table-wrap` carries `tabindex="0"`, `role="region"` and an `aria-label`
wherever it is used, because the container scrolls horizontally and a scrollable
region has to be operable by keyboard.

### 9.11 Image inventory

All photography is self-hosted WebP except nine service-card images still
hot-linked from Unsplash (§12 item 8). Pass 3 recovered the nine original JPEGs
from the pass-1 bundle in git history (`git show ae67717:index.html`) and
re-derived new crops from them, so no new third-party URLs were introduced.

| File | Source | Used by |
|---|---|---|
| `hero-services-outdoor-remodeling` | modern home exterior | `/services/` banner |
| `hero-complete-outdoor-transformation` | draped shade structures at sunset | `/services/outdoor-remodeling/` banner |
| `hero-paver-installation` | paved terrace beside a pool | `/services/paver-installation/` banner |
| `card-paver-installation` | as above, 3:2 crop | hub card |
| `card-tiki-huts` | shade structures, left crop | hub card, remodel gallery |
| `card-fencing` | white masonry garden walls | hub card |
| `card-impact-windows` | glazed wall, interior to exterior | hub card |
| `card-complete-remodeling` | house at dusk with lawn | hub feature card |
| `hero-patios` | covered terrace and lawn at dusk | `/services/patios/` banner |
| `hero-driveways` | garage and paved approach | `/services/driveways/` banner |
| `hero-pool-decks` | pool, surround and loungers | `/services/pool-decks/` banner, `/services/fence/` pool section |
| `hero-turf` | ground-level turf lawn, screening behind | `/services/turf/` banner |
| `hero-fence` | low white boundary wall dividing lawn from path | `/services/fence/` banner |
| `hero-impact-windows-doors` | dark-framed sliding doors onto a pool terrace | `/services/impact-windows-doors/` banner |
| `hero-service-areas` | draped cabanas beside a lit pool at sunset | `/service-areas/` banner |
| `hero-parkland-fl` | lit rear elevation over a level lawn at dusk | `/service-areas/parkland-fl/` banner |
| `hero-davie-fl` | paved path to a white house entrance, lawn alongside | `/service-areas/davie-fl/` banner |
| `hero-weston-fl` | white rear elevation, covered terrace, pool foreground | `/service-areas/weston-fl/` banner |
| `hero-plantation-fl` | dappled tree shadow across a paved terrace | `/service-areas/plantation-fl/` banner |
| `hero-outdoor-kitchens` | covered terrace, dining and a built-in cooking unit | `/services/outdoor-kitchens/` banner |
| `hero-pergolas` | timber post-and-beam frame with drapes | `/services/pergolas/` banner |
| `hero-tiki-huts` | thatched roof among palms beside a pool | `/services/tiki-huts/` banner |
| `hero-fort-lauderdale-fl` | pool edge meeting open water at dusk | `/service-areas/fort-lauderdale-fl/` banner |
| `hero-pembroke-pines-fl` | rear lawn to a lit elevation at dusk | `/service-areas/pembroke-pines-fl/` banner |
| `hero-coral-springs-fl` | single-storey house, deep overhang, terrace | `/service-areas/coral-springs-fl/` banner |
| `hero-boca-raton-fl` | white rendered volumes against a clear sky | `/service-areas/boca-raton-fl/` banner |
| `hero-projects` | white rendered volumes over a paved path and lawn | `/projects/` banner |

**The nine source photographs are now carrying eleven pages.** Pass 4 believed
the usable material was exhausted; pass 6 found three more frames by going back
to the original JPEGs rather than re-cropping the shipped WebP files. The
manifest in the pass-1 bundle (`git show ae67717:index.html`, §17) still holds
all nine at full resolution, and every crop since has come from there. That is
now the standing method: recover the source, crop, re-encode to WebP, never
introduce a new third-party URL. It is also nearly spent — `hero-turf` is only
900px wide because its source is, and every remaining frame has been used at
least once. Real project photography is still the binding constraint — see §12
item 7.

**Two passes have now declared this material exhausted and been wrong.** Pass 4
said pass 4 had spent it; pass 8 said the same and called real photography a
blocker; passes 6 and 7 nonetheless found eight further usable framings by
going back to the recovered originals. The honest statement is the one above:
every source frame is now used at least once, several are used two or three
times in different bands, and the next page that needs a genuinely new subject
— rather than another crop of a subject already on the site — cannot be served
from this material. That is the real blocker, and it arrives with the first
page whose subject is not already photographed.

Each new crop was reviewed against the service it illustrates. A pool photograph
originally cropped for the fencing card was rejected and re-sourced, because a
card labelled *Fencing* showing a pool is the same category of error as §12
item 6. Alt text describes what is actually in the frame, never what the card is
selling.

### 9.12 Project-index components (pages.css §15)

Added for `/projects/`. All three are generic and reusable.

| Class | What it is |
|---|---|
| `.section--ink` | Dark band with no texture photograph behind it, for sections that need contrast but have no image to carry it. The `.why` band remains the textured variant. |
| `.filterbar` / `.filterbar__chip` | Chip row that filters a following grid. Chips are real `<button>`s carrying `aria-pressed`; the group has `role="group"` and a label. |
| `.work-card` | Text-forward record card — tag row, heading, body, service link. **Deliberately not a photo card**, so `/projects/` cannot be mistaken for `/gallery/`. |
| `.record-empty` | The zero-state panel. Uses `font-feature-settings: "lnum"` because Cormorant Garamond's default old-style figures render a display "0" at x-height. |

**The filter degrades the same way the reveal animation does.** `.filterbar` is
`display:none` until `main.js` adds `.filter-on` to `<html>`, immediately before
it wires the chips — the same gate, for the same reason as §18 of style.css. A
script that fails to load leaves every card visible and no dead control on the
page. `initFilter()` is driven entirely by `data-filter-root`, `data-filter` and
`data-tags`, so any future page gets the behaviour by markup alone.

The live region (`[data-filter-status]`) is left **empty on load** and populated
only after a visitor filters something, so a screen reader is not read a count
nobody asked for on arrival.

## 10. SEO RULES

Every indexable page needs, without exception:

- a unique `<title>` (≤ 60 chars where possible, brand suffix `| Arco Outdoors`)
- a unique `<meta name="description">` (~150–160 chars)
- `<link rel="canonical">` on the absolute www URL
- exactly **one** `<h1>`, matching the page's primary intent
- logical `H2`/`H3` order with no skipped levels
- meaningful internal links (hub → spoke and spoke → sibling, in body copy, not
  only in nav)
- genuinely useful content — never text written to hit a keyword count
- a relevant CTA
- accessible images: real `alt` text, or `alt=""` + `aria-hidden` when decorative
- breadcrumbs on every page below the root (use `.breadcrumb` in `pages.css`,
  plus `BreadcrumbList` JSON-LD)

Homepage JSON-LD is a `@graph` of `GeneralContractor` + `WebSite` + `WebPage`.
Reuse the `@id`s (`…/#business`, `…/#website`) so later pages reference rather
than redeclare the business.

**Do not emit `aggregateRating`, `Review`, or `AggregateOffer` markup** until the
underlying data is verified (§12). Structured data that overstates is both a
policy violation and a manual-action risk.

## 11. CONTENT RULES

Never fabricate: customer names · reviews · project locations · project values ·
completion dates · certifications · awards · warranties · financing · staff
biographies · statistics · permit requirements · code requirements.

If information has not been provided, **write around it**. Concretely:

- Describe *method* ("proper base prep, drainage, compaction"), not *volume*.
- Describe *materials and options*, not *prices*.
- Say "permitting requirements vary by municipality — we handle the process for
  your project" rather than naming a code, fee or turnaround.
- Attribute nothing to a named person.

### Local SEO rule

No doorway pages. A location page that differs from its sibling only by city
name must not ship. Each one needs genuinely differentiated substance, drawn
from things that are true and checkable without client input, e.g.:

- the municipality's actual character (lot sizes, typical home age and style,
  coastal vs. inland exposure, common yard constraints)
- which of the 11 services that area realistically asks for most, and why
- travel/logistics context relative to Davie
- distinct internal links, distinct FAQs, distinct imagery, distinct H2s

Never assert a completed Arco project in that city without verification.

### 11.1 Project record template — the standard for `/projects/`

**Status: no record has ever met this standard, so none is published.** Pass 10
audited the repository for anything that could support a case study and found
nothing: no data file of any kind has ever been committed (`git log --all
--diff-filter=A` returns only `PROJECT-SPEC.md`, `robots.txt` and
`sitemap.xml`); the nine source photographs recovered from the pass-1 bundle
carry no EXIF date, GPS or author; and §12 items 6 and 7 already record that the
photography appears to be stock and that two gallery captions do not match their
own images. There is therefore no verified city, date, duration, cost, material
schedule, constraint or homeowner for any individual job anywhere in this
project. `/projects/` says so on the page rather than filling the gap.

**Three gates. A record is published only when all three are true — not two.**

1. **The work is Arco's.** Built under our own contract, by our crews and
   subcontractors. Not advised on, not quoted, not watched go elsewhere.
2. **The photography is Arco's own,** taken at that property, of that work,
   before and after. A record illustrated with a purchased photograph of
   somebody else's yard is not a record.
3. **The homeowner has consented in writing.** Opt-in, never a condition of the
   contract, revocable, and refusing changes nothing about how the job is run.

**Required sections. A record missing any of these has failed its own test.**

| # | Section | Contains | Never contains |
|---|---|---|---|
| 1 | The site before | What was there, what it was doing wrong, ground conditions. Photographs from before work started. | A rendering presented as a "before". |
| 2 | Constraints | Access, levels, drainage, existing structures, trees, association guidelines, approvals that applied to that property. | Generic municipal rules restated as if they governed this job. |
| 3 | Scope | Which of the eleven §5 build types were in the contract, in what sequence, and what was explicitly **excluded**. | A scope written only as inclusions. |
| 4 | Materials | What was specified, what it was judged against (heat, traction, load, exposure), what was rejected. | A named product without documentation to point at. |
| 5 | What went wrong | The moment every project of any size has, and what was done about it. **Required, not optional.** | A record with no friction in it — that has been edited into fiction. |
| 6 | Outcome | Arco's own photography of the finished work, including the awkward junctions. | Stock, supplier or manufacturer imagery. |
| 7 | Location | City-level by default, reduced further on request, omitted entirely if that is what consent requires. | Street address, homeowner name, or a date that identifies a household. |

**Facts that require a source, and are otherwise omitted entirely:** city ·
project date · duration · cost or budget · crew size · specific materials and
products · square footage · homeowner name or quote · the constraints
encountered · the scope delivered. Writing around a missing fact is the §11 rule
and it applies here without exception; a record that reads well because a gap
was filled with a plausible invention is the single failure mode this whole
section exists to prevent.

**Detail-page architecture, reserved for when a record exists.** Route:
`/projects/<slug>/`, slug derived from the build type and city, never from a
homeowner's name. Page recipe as §8.5, plus: breadcrumb `Home / Projects /
<record>`; a `page-hero` using the record's own photography; the seven sections
above in order; a build-type tag row linking to the governing service pages; a
link back to `/projects/`; JSON-LD `CreativeWork` inside the standard `@graph`,
with `about` pointing at the relevant `Service` nodes. `/projects/` gains a
records grid above the build-type index, and the filter chips then filter
records rather than scopes. **Do not build any of this speculatively** — the
route stays unbuilt until gate 3 is satisfied for a real job.

**Until then `/projects/` publishes the standard instead of the records,** on
the principle that a standard which only exists internally is one that quietly
relaxes. Publishing it while there is nothing to bend it for is the point.

## 12. OPEN ITEMS — unverified content currently live

These predate this pass. They are preserved so the homepage design is unchanged,
but each is a **pre-launch blocker** needing owner confirmation or removal. None
of them may be repeated on any new page until verified.

| # | Location | Claim | Risk |
|---|---|---|---|
| 1 | Reviews section | Three named testimonials — "Danielle R., Parkland FL", "Marcus T., Coral Springs FL", "Sofia & Luis G., Boca Raton FL" | If not real Google reviews, this is deceptive advertising (FTC endorsement rules). Highest risk item. |
| 2 | Reviews section | "5.0" and "Based on **180+ verified** Google reviews" | Specific, checkable, and reproduced in no source material. |
| 3 | About / trust strip | "750+ Projects Completed", "20 yrs In South Florida", "20+ Years of Craftsmanship" | Explicitly on the forbidden-claims list in §4. |
| 4 | Trust strip / Why Arco / consultation | "Transparent, Fixed Pricing", "Fixed, itemized pricing — no surprises" | A pricing guarantee. |
| 5 | Consultation section | "On-site visit within 48 hours" | A service-level guarantee. |
| 6 | Gallery | Captions do not match their photographs — "Travertine pool deck & coping" labels a white stucco stairway; "Patio detail" labels an interior lounge | Misrepresents work as Arco's. The `alt` text describes what is actually shown, so `alt` and caption disagree. |
| 7 | Gallery / About / hero | Photography appears to be stock, not Arco project work | Presented as "our custom outdoor transformations". **Pass 10 confirmed no image carries EXIF date, GPS or author.** `/projects/` now states on-page that all site photography is reference imagery; the homepage heading still says "our" and is the remaining exposure. |
| 8 | Services + journal cards | 9 images hot-linked from `images.unsplash.com` | Third-party dependency, licensing exposure, and they are the only images not self-hosted. |
| 9 | Journal section | Three articles with dates (Jul 22, Jul 08, Jun 24) and no year, linking to `#journal` | Implies a blog that does not exist. |
| 10 | ~~Header + footer~~ | ~~Facebook and Instagram icons link to `href="#"`~~ | **Resolved in pass 2** — the icons were removed rather than pointed somewhere invented. Add them only when real profile URLs are supplied. |
| 11 | Consultation form | No submission endpoint exists | See §14 — currently falls back to a mail draft. |
| 12 | Global nav + footer | 9 of the 32 linked routes do not exist yet and return 404 | Approved and expected: the pages ship in later passes. `sitemap.xml` lists only the 23 URLs that resolve. Do not submit the sitemap or launch until the routes resolve. |
| 13 | `/projects/` | The page exists but holds **zero project records** — see §11.1 | Not a defect; it is the audited state. It becomes one only if a record is ever published without meeting all three §11.1 gates. |
| 14 | `/projects/` hero, and every other banner | `hero-projects` is a new crop of an existing stock frame, like every other banner on the site | Consistent with items 7 and 8. Owner decision needed: supply real project photography, or accept reference imagery site-wide and keep it labelled as such. |

## 13. HOMEPAGE ARCHITECTURE & CHANGE LOG

### 13.1 Section order (set in pass 2)

The homepage runs hero → proof → offer → positioning → evidence → method →
differentiation → geography → social proof → content → objections → conversion.

| # | Section | `id` |
|---|---|---|
| 1 | Hero — core value proposition | `top` |
| 2 | Trust / licensing strip | — |
| 3 | Main services (6 cards + View All 11 Services) | `services` |
| 4 | Complete-outdoor-transformation positioning | `about` |
| 5 | Featured work / gallery | `gallery` |
| 6 | Process — 5 steps | `process` |
| 7 | Why Arco | — |
| 8 | Service areas (33 markets, 8 linked) | `service-areas` |
| 9 | Reviews | `reviews` |
| 10 | Journal | `journal` |
| 11 | FAQs — 6 questions | `faq` |
| 12 | Consultation form | `consult` |
| 13 | Closing CTA | `quote` |

Keep this order. Sections 6 and 11 were added in pass 2; everything else was
reordered, not rewritten.

### 13.2 Pass 1 — de-bundling

Three Parkland-first strings became South Florida (hero eyebrow, services H2,
footer summary). Form select expanded to the canonical service list. The gallery
CTA was relabelled because it scrolled to the section already on screen.

### 13.3 Pass 2 — navigation, footer, architecture

Header and footer replaced by the generated partials (§8.1). Homepage sections
reordered per §13.1.

**Added:**

- *Process* section (`.steps` from `pages.css`): consultation → design &
  proposal → preparation → installation → walkthrough. Describes method only —
  no durations, prices or guarantees.
- *FAQ* section (`.faq`, native `<details>`): service area, licensing,
  single-contractor scope, what the consultation involves, permits, contact.
  Every answer is drawn from §3 and §5 alone. `FAQPage` JSON-LD mirrors it.
- `View All 11 Services` and `View All Service Areas` CTAs.
- Parkland added to the service-area list — it was absent despite being
  priority market #1.

**Copy changed (one string):** the hero lead listed four paver-adjacent trades,
which undersold §4. It now reads "…delivering complete outdoor transformations —
patios, pool decks, driveways, outdoor kitchens, pergolas, turf & fencing,
coordinated by one accountable team."

**Removed:** the four Facebook/Instagram `href="#"` placeholders, and the
per-page `<noscript>` blocks (the fallback now lives in `style.css`).

**Fixed:** `.about__badge` sits at `left: -34px` to overhang its image; on
phones that pushed it past the viewport edge where `overflow-x: hidden` clipped
the text. It now un-offsets at ≤860px. Inherited from the original bundle.

### 13.4 Remaining Parkland references — all intentional

Three, and each is correct: one testimonial location (already flagged in §12)
and two journal headlines targeting Parkland as a market. Parkland is one
important market, never the company's home positioning.

### 13.5 Link inventory

All 32 unique routes on the homepage are on the §8.2 map; zero `href="#"`
remain. Four in-page anchors are deliberate and resolve today:

| Anchor | Used by | Why not a route |
|---|---|---|
| `#main` | skip link | — |
| `#services` | hero "View Our Services" | the section is on screen; scrolling beats a page load |
| `#about` | hero scroll cue | as above |
| `#consult` | hero CTA, gallery/FAQ/closing CTA | the working quote form is on this page |

`/get-a-quote/` is used by the header, drawer and footer CTAs. When that page
ships, decide per-CTA whether the on-page form or the dedicated page is the
better destination; do not blanket-replace.

### 13.6 Pass 3 — services hub and first two service pages

Shipped `/services/`, `/services/outdoor-remodeling/` and
`/services/paver-installation/`, plus the interior-page recipe in §8.5 and the
components in §9.10.

**Content approach.** Every claim is either a verified fact from §3, general
construction practice that is publicly documented, or an observable South
Florida climate fact. Nothing about Arco's volume, history, pricing, timelines
or warranties appears anywhere. Two places deliberately decline to claim:

- *Who performs what.* The remodeling page states plainly that no contractor
  self-performs every trade, that specialist work is separately licensed in
  Florida, and that the split between performed and coordinated work is set out
  in the written proposal. It never asserts Arco self-performs anything.
- *Permitting.* Described only as varying by municipality and reviewed at the
  consultation. No code, fee, timeline or requirement is named.

Word counts: hub 1,508, remodeling 1,912, paver installation 2,150.

**Bug fixed — scroll-reveal could blank a page.** `.js .reveal { opacity: 0 }`
was gated on `.js`, which the inline `<head>` script sets before `main.js`
loads. If `main.js` failed to load or threw, every `.reveal` element stayed
invisible permanently. Harmless-looking on the homepage; on these service pages
`.reveal` carries most of the body content. The gate is now `.reveal-on`, which
`main.js` adds itself immediately before it starts observing, so a failed script
leaves the page fully visible. Regression test: `revealtest.js` step 2 blocks
`main.js` and asserts nothing is hidden.

**Also fixed.** `.table-wrap` scrolls horizontally but was not keyboard
operable; it now carries `tabindex="0"`, `role="region"`, an `aria-label` and a
focus ring.

### 13.7 Pass 4 — patios, driveways, pool decks

Shipped `/services/patios/`, `/services/driveways/` and
`/services/pool-decks/`. Word counts 2,348 / 2,347 / 2,624.

**Differentiation is the point, and it is measurable.** The brief was explicitly
not to build three pages from one template with the nouns swapped. Each page is
organised around a different question, and therefore has a different spine:

| | Organising question | Signature section | Process type |
|---|---|---|---|
| Patios | How will the space be used? | zone-sizing table with furniture clearances | install sequence |
| Driveways | It carries cars *and* fronts the house | pavers-vs-concrete comparison | **replacement** sequence, incl. exposing the sub-grade |
| Pool decks | Wet, barefoot, hot, chemical | scope boundary vs the pool contractor | **overlay-or-rebuild** decision, then remodel sequence |

Measured overlap between the body copy of all six service pages is **zero
shared sentences** (checked at ≥45 characters, chrome excluded). H2 sequences
are unique per page. Re-run that check before shipping any further service page.

**Three claims deliberately not made.**

- *Concrete driveways.* §5 lists paver installation, not concrete. The
  driveways page states plainly that Arco installs paver driveways and that
  concrete appears only because it is what most existing driveways are made of.
  A callout invites the visitor to say so if they have decided on concrete, and
  promises an honest answer about fit. Do not turn this into a service claim
  without verification.
- *Slip resistance.* The pool-decks page says outright that no surface is
  slip-proof and that a contractor claiming otherwise is selling rather than
  advising. It discusses how much traction a finish **retains** when wet, which
  is the honest and useful framing. Never write "slip-proof", "non-slip" or
  "slip-free" as a property of a material.
- *Property value.* No percentage, anywhere. The driveways page says why —
  curb appeal is real, a quoted return figure is not supportable, and a
  contractor offering one is worth treating with caution.

**Scope boundary, pool decks.** The page states explicitly that the pool shell,
interior finish, waterline tile, plumbing, equipment and any structural pool
work belong to a licensed pool contractor; that Arco builds the deck and
coordinates at the coping line; and that where both trades are working, the
pool's finished levels govern the deck's. A three-part panel sets out ours /
not ours / shared. Keep that boundary on any future page that touches water.

**Also.** Two ordinary uses of "guaranteed" were reworded to "a certainty" —
the word reads as warranty language on a contractor site even when it is not
doing that job. One sentence duplicated verbatim across two pages was rewritten
so each answers its own question in its own words.

### 13.8 Pass 5 — the site was mounted at a subpath

**Symptom.** The deployed site at `techygrooves.github.io/arcooutdoors/`
rendered as unstyled HTML: default serif, blue underlined links, bullet lists,
alt text where photographs should be.

**Cause.** Not a defect in the markup. Every internal URL was root-absolute, so
on a GitHub Pages *project* site each one resolved above the mount point —
`/assets/css/style.css` became `techygrooves.github.io/assets/css/style.css`.
Reproduced locally by serving the repository under `/arcooutdoors/`: the page
returned 200 and the stylesheet returned 404.

**Fix.** Internal URLs are now relative and depth-correct, generated by
`tools/sync-partials.py` so the partials stay a single source of truth. Full
rationale and the authoring rule are in §8.6.

**Verified on both mount points.** Seven pages × two deployments: stylesheet
applied (page ground, display face and nav bar all correct), `main.js` running,
hero image loaded, zero 4xx. Plus real navigation on the subpath deployment —
dropdown to a service page, breadcrumb home, footer link, logo home — all
landing on the right URL and styled.

**Also.** Added `tools/check-links.py`, which resolves every relative URL from
its containing page and fails on wrong `../` depth, leftover root-absolute
URLs, bare `href="#"`, dangling fragments, and canonicals not naming the
production domain. Verified it catches both failure modes by introducing them
deliberately. Added `.nojekyll` so GitHub Pages serves the files as-is.

Two test suites asserted on root-absolute selectors and were updated to match
on href suffix, which is deployment-agnostic. That was a test defect, not a
site defect.

### 13.9 Pass 6 — turf, fencing, impact windows & doors

Shipped `/services/turf/`, `/services/fence/` and
`/services/impact-windows-doors/`. Word counts 3,271 / 3,313 / 3,778 (body
copy inside `<main>`, chrome excluded). Three service pages remain: outdoor
kitchens, pergolas, tiki huts.

**Each page is organised around a different question**, per the §13.7 rule that
siblings must not be one template with the nouns swapped.

| | Organising question | Signature section | Layout it introduces |
|---|---|---|---|
| Turf | Does this ground actually suit turf? | side-by-side *strong candidates* vs *think harder about* | two-column `.prose` inside one `.split` |
| Fencing | What is the fence **for**? | pool-area section that refuses a compliance claim | purpose grid before any material table |
| Impact windows | Which document answers this? | *Ask for the document, not the adjective* | the previously unused `.with-rail` + `.rail__card` sticky rail |

Overlap re-measured after writing: **zero shared sentences** at ≥45 characters
between any of the three and any other page, chrome excluded. The licence
sentence had to be reworded three ways to reach zero — `pool-decks` and
`patios` had already fixed two phrasings of it, and it is the one sentence
every service page is tempted to repeat.

**Claims deliberately not made.**

- *Turf — water savings.* No percentage, no gallons, no comparison figure. A
  `.note` on the page says why: the honest number depends on the property's
  irrigation, soil, rainfall, rates and prior lawn care, so a single figure
  quoted to everyone is a marketing number. Do not add one without a cited
  source.
- *Turf — heat.* The page states plainly that synthetic fibre gets hotter than
  living grass in direct sun, and gives the physical reason. It offers shade,
  rinsing and lighter infill as mitigations and explicitly declines to quote a
  temperature reduction for any product sold as cooling.
- *Fencing — pool barriers.* The page says, as its own section and again in the
  first FAQ, that **a fence is not automatically a pool barrier**. It does not
  reproduce any barrier requirement, height, gate rule or code reference.
  Requirements are described as property-specific and confirmed with the
  authority having jurisdiction before anything is built. It also states that a
  barrier is one layer of protection and never a substitute for supervision.
  Never soften this into "our fences meet pool code".
- *Fencing — permits and HOAs.* Municipal, county and association approval are
  described as three separate, property-specific tracks. No height limit,
  setback, fee or turnaround is named anywhere, and the page says outright why
  it does not name them.
- *Impact windows — the whole class of numbers.* No product approvals, no
  approval numbers, no brand names, no wind ratings, no energy-savings
  percentage, no insurance discount, no warranty term, no service life. The
  page turns that into its argument: performance figures belong to a specific
  product in a specific configuration, so the reader is told which document to
  ask for instead. A dark `.rail__card` lists the refusals explicitly. Every
  occurrence of "percentage", "wind rating", "insurance discount" and
  "warranty" on that page is a negation or a reference to the manufacturer's
  own paperwork — check that this is still true before editing it.
- *Impact windows — energy and comfort.* Discussed only in comparative terms
  ("glazing and frames differ measurably, and manufacturers publish the data
  per product"), never as an outcome Arco promises. Insurance is routed to the
  carrier.
- *Impact windows — permitting.* Stated at the general level the brief allows:
  the work is regulated, permitting and inspection are normally part of it, and
  the specifics are confirmed per address. No code, fee or review time.

**This page is not landscape work, and says so.** The impact-windows page opens
by naming itself the exception on a site otherwise about outdoor living — it
changes the building envelope rather than the yard — and closes the loop by
explaining when it is sensibly coordinated with a deck or patio project and
when it simply runs on its own.

**Imagery.** Three new hero crops, all derived from the original pass-1 JPEGs
recovered from `ae67717` rather than from the shipped WebP files, so no new
third-party URL was introduced: `hero-turf` (900×346, its source is only 900
wide), `hero-fence` (1100×423) and `hero-impact-windows-doors` (1100×423), each
with a 700w variant, encoded at q72–80 to land in the same 30–80 KB band as the
existing heroes. Supporting images are existing files, re-alt-texted for what
is actually in the frame at the crop shown. Pillow was installed locally for the
crop and encode; it is an authoring chore, not a repository dependency (§7).

**Verified.** `sync-partials.py --check` and `check-links.py` both exit 0. All
three pages at 390 / 768 / 1440: HTTP 200, zero console errors, zero failed
requests, no horizontal overflow, hero decoded. Scroll-reveal returns every
element to full opacity, and with `main.js` blocked nothing is hidden (§13.6
regression). Mobile drawer opens on tap and closes on `Escape`. Renders with
JavaScript disabled. Served correctly from both a root mount and
`/arcooutdoors/`. FAQ JSON-LD compared programmatically against the visible
`<details>` text on all three pages — exact match, 6 entries each.

### 13.10 Pass 7 — local SEO architecture

Shipped `/service-areas/` and the first four city pages: `parkland-fl`,
`davie-fl`, `weston-fl`, `plantation-fl`. Word counts (body inside `<main>`,
chrome excluded): hub 1,897; Parkland 2,308; Davie 2,466; Weston 2,492;
Plantation 2,420.

**The anti-doorway rule was the whole brief, and it is measurable.** Overlap
re-measured across all 16 pages on the site: **zero shared sentences** at ≥45
characters. Each city page is organised around a different question and leads
with a different section, so the section order itself differs, not only the
nouns:

| Page | Organising question | Leads with | Distinct spine element |
|---|---|---|---|
| Parkland | What do you do with a yard this big? | the seven services, as breadth | zoning-and-phasing section; buried work before later phases |
| Davie | Which of four property types are you on? | what proximity does and does not change | four-lot-type analysis (acreage / ranch / subdivision / zero-lot) |
| Weston | What will the community allow? | the approvals track, before any material | screened-enclosure scope boundary; two parallel approvals |
| Plantation | Why did the existing surface fail? | reading what is already in the ground | mature-canopy and root section; survey-first process |

**What each page refuses to claim.**

- *No project is asserted in any city.* Every location page carries an
  "About these photographs" note stating the images illustrate the type of
  work described, are not presented as completed projects, and are not
  claimed to have been taken in that city — including on the Davie page, the
  town of the published address. Parkland's sixth FAQ answers the "have you
  worked here" question by saying to ask, and the hub's second FAQ says the
  same at the coverage level. §12 item 7 records that the photography appears
  to be stock, so it is never described as Arco's work either.
- *No invented local rules.* No height, setback, permit rule, fee, review
  time, barrier requirement or HOA guideline appears on any of the five
  pages. Weston states outright that it will not quote a rule from memory or
  from another community and that the association is the authority on its own
  guidelines. Every page routes requirements to "confirmed for your address as
  part of the project".
- *No demographics.* No income, price, population or "affluent"-class
  language. City character is described only through property-stock
  observations — housing age, lot size and shape, exposure, canopy, water,
  whether associations are typically involved.
- *No branch offices.* See §8.5: location pages emit no `LocalBusiness` and no
  address node. Davie says "our published business address is in Davie" and
  explicitly adds that we do not maintain premises elsewhere, rather than
  implying local presence in each market.
- *No service radius in miles.* The hub says why: a radius sounds precise and
  decides nothing, when scope, access and schedule are what actually
  determine fit. §3 forbids inventing one in any case.

**Hub.** H1 is `Outdoor Remodeling Service Areas in South Florida`, as briefed.
It links all eight priority markets with a substantive character note each
(`.spec-grid`, not a bare list), states the three-county coverage, and includes
a "what actually changes from one city to the next" section that doubles as the
justification for the location-page architecture. It deliberately does not list
the 33 municipalities the homepage names — that list is a coverage statement in
its own context and would be keyword padding here. A `.note` says plainly which
four city pages are written and which four are still coming, so the four links
that 404 today are disclosed on the page rather than discovered.

**Imagery.** Five new hero crops, again cut from the original pass-1 JPEGs
recovered from `ae67717` (§9.11 method), no new third-party URLs:
`hero-service-areas`, `hero-parkland-fl`, `hero-davie-fl`, `hero-weston-fl`,
`hero-plantation-fl`. `hero-weston-fl` is only 700px wide because its source
is, and `hero-plantation-fl` is a different band of the same photograph that
`hero-impact-windows-doors` crops — the shaded-paving foreground rather than
the glazed elevation. Section and gallery images are existing files, re-alt-
texted for what is in the frame, and the gallery captions describe the frame
rather than naming a client or a place (§12 item 6 is the failure mode being
avoided).

**Verified.** `sync-partials.py --check` and `check-links.py` both exit 0. All
five pages at 390 / 768 / 1440: HTTP 200, zero console errors, zero failed
requests, no horizontal overflow, hero decoded, `Service Areas` showing as the
current nav item. Scroll-reveal returns every element to full opacity; with
`main.js` blocked nothing is hidden. Mobile drawer opens and closes on
`Escape`. Renders with JavaScript disabled. Titles, descriptions and canonicals
are unique across all 16 pages, with descriptions trimmed to 151–161
characters. FAQ JSON-LD compared programmatically against the visible
`<details>` text — exact match, six entries per page — and each location
page's `@graph` asserted to contain no `LocalBusiness` and no address node.

### 13.11 Pass 8 — outdoor kitchens, pergolas, tiki huts

Shipped `/services/outdoor-kitchens/`, `/services/pergolas/` and
`/services/tiki-huts/`, completing the eleven-service tier. Word counts
2,527 / 2,565 / 2,700. Written in parallel with passes 6 and 7 on a separate
branch and merged afterwards; the pass numbering here reflects merge order,
not the order the work was done.

Each page is organised around a different question, as §13.7 established:

| | Organising question | Signature section | Workflow keyed to |
|---|---|---|---|
| Outdoor kitchens | Where do the services run, and where does the cook stand? | four-layout comparison; zones and circulation | rough-in while the ground is open |
| Pergolas | Which hours do you want back? | sun path and orientation; attached vs freestanding | footings before paving |
| Tiki huts | What is the destination in the yard? | placement; seating and bar layouts | position fixed first, planning raised early |

**Claims deliberately not made.**

- *No appliance or product brands.* The outdoor kitchen page plans by appliance
  type and cut-out dimension, and says so explicitly. All eleven service pages
  scanned against a brand list — zero mentions.
- *No wind or structural ratings.* The pergolas page refuses one in a callout
  and in its FAQ: performance figures belong to a specific product or
  engineered design and come from the manufacturer or that engineering, not
  from a marketing page. Zero rating figures anywhere. This is the same
  position §13.9 takes on impact windows, reached independently.
- *No blanket permit statements.* Never that a structure does or does not
  require a permit.
- *No thatch service life in years, and no claim about which thatch Arco
  supplies.* The tiki huts page presents natural and synthetic thatch as the
  two families that exist and what each trades, with the choice settled at
  consultation rather than declared in advance. Apply the same pattern to any
  material question where Arco's actual offering is unconfirmed.

**Two accepted forms of the permitting caution.** These three pages use one
sentence pair verbatim wherever permitting comes up:

> Requirements can vary by jurisdiction and project scope. Arco can discuss
> planning considerations for your specific project.

It appears three times on each of them, and the tiki huts page adds a callout
explaining why the answer is not given on a web page. **Do not paraphrase it on
those pages** — a legal caution phrased differently every time is worse than
one phrased identically.

The pages from passes 6 and 7 answer the same question in their own words,
routing it to "confirmed for your address as part of the project" and, on the
location pages, naming the authority having jurisdiction. Both forms say the
same thing and neither states a requirement. Either is acceptable on a new
page; mixing them within one page is not.

**Exception to the zero-overlap rule.** §13.7 requires zero shared sentences
between sibling pages. These three share exactly two sentence-pairs with each
other, and both are deliberate:

1. the mandated permitting sentences above;
2. *"Which elements are performed directly and which are coordinated is set out
   in your written proposal."* — the scope-boundary statement from §13.6, which
   should read identically wherever it appears.

Everything else is zero, including against all thirteen pages these three were
merged alongside — re-measured after the merge, not assumed. When the overlap
check reports a hit, confirm it is one of these two before treating it as
templated filler.

### 13.12 Pass 9 — the remaining location pages, and one shared component

Shipped `/service-areas/fort-lauderdale-fl/`, `pembroke-pines-fl/`,
`coral-springs-fl/` and `boca-raton-fl/`, completing the eight §6 priority
markets. Word counts 3,083 / 2,576 / 2,919 / 2,802.

**Four more spines, none of them a city swap.** Added to the four from §13.10,
that is eight location pages each led by a different section:

| Page | Organising question | Leads with | Signature section |
|---|---|---|---|
| Fort Lauderdale | How does the work get in, and what does the air do to it? | site access | the access grid, then coastal specification of fixings and hardware |
| Pembroke Pines | What should be built first? | a six-stage order of works | the order itself, as a `.steps` list, with each service mapped onto a stage |
| Coral Springs | Who is using this yard? | four competing users | a table of adults / children / dog / pool and where their needs collide |
| Boca Raton | What should "premium" mean from a contractor? | the refusal to claim it | *Where quality actually shows* — setting out, cuts, edges, junctions, falls, joints |

**Claims deliberately not made.**

- *Fort Lauderdale* declines marine work outright: docks, seawalls and boat
  lifts are named as a separate licensed trade. No claim is made about any
  waterway, neighbourhood or street.
- *Pembroke Pines* was written under an explicit instruction to avoid
  neighbourhood claims, and names no community, development or subdivision.
  Its differentiation comes entirely from the order-of-works argument, which
  needs no local assertion to be useful.
- *Coral Springs* repeats the two standing cautions in its own words — no
  surface is slip-proof, and a fence is not automatically a pool barrier — and
  gives the pavers-versus-concrete answer as a partial one, flagging that Arco
  installs paver surrounds (§13.7).
- *Boca Raton* states plainly that Arco does **not** claim to be a luxury or
  high-end specialist, and that the reader should be sceptical of contractors
  who do. The premium register is carried by craft detail and by a `.note`
  separating what is claimed (licence, written scope, confirmed requirements)
  from what is not (specialisation, a local portfolio, knowledge of a
  community's rules before reading them). It is also the only market outside
  Broward, so the county difference is treated as a practical section rather
  than a boast.
- All four carry the photography note in their own wording: illustrative, not
  presented as completed projects, not claimed to have been taken in that city.

### The "Areas we serve" component

Every service page now ends with the same compact block: the eight priority
markets as plain city-name links in `.areas-grid areas-grid--compact`, under
the page's own H2, above a *View All Service Areas* button.

It replaced ten heavier `.link-index` blocks that each carried eight
hand-written descriptors — those were ten slightly different versions of the
same list, which is exactly the shape of near-duplicate content the §13.7 rule
exists to prevent, and their shared lead sentence ("Broward, Miami-Dade and
Palm Beach counties, working from Davie.") was a genuine cross-page duplicate
that the overlap check had been missing because each unique H2 above it split
the sentence chunk. Anchor text is now the city name alone — deliberately not
optimised. `paver-installation` had no such block at all and gained one; it
sits after its FAQ rather than before, because on that page's rhythm that is
the only position where two adjacent bands do not share a ground.

### Duplication review — the method, and what it caught

Ran before finishing, across all 22 pages, at two thresholds:

1. **Exact** shared sentences at ≥45 characters.
2. **Near-duplicate** sentence pairs by token Jaccard ≥ 0.55 — which is the
   check that matters, because paraphrase is how city pages actually go wrong.

The fuzzy pass found 20 pairs on first run and 13 distinct passages were
rewritten: the salt-air sentence shared between Boca Raton and Fort
Lauderdale, the base-construction list shared between three pages and the
services hub, the pergola-versus-tiki-hut line shared with Parkland, the
footings note and site-assessment step shared with Pembroke Pines, the
poured-slab line shared with Plantation, the slip-proof and turf-odour
sentences shared with the pool-decks and turf service pages, the screened-
enclosure passage shared with Weston, and the closing line of two photography
notes. Three permitting answers that had converged on identical wording were
rewritten so each page answers in its own voice.

**Final state: zero exact overlaps involving any page from this pass, and zero
fuzzy pairs above 0.55.** Four exact pairs remain site-wide, all pre-existing
and all accounted for: three are the §13.11 fixed-text exceptions between
outdoor kitchens, pergolas and tiki huts, and one is a single sentence shared
between the homepage and the services hub since pass 3 ("If your address is
nearby but not listed, call and ask.") — recorded here rather than left as an
unexplained hit for a later session to chase.

**Re-run this two-threshold check before shipping any further page.** Exact
matching alone will pass content that a reader would recognise instantly as
the same paragraph reworded.

**Imagery.** Four new hero crops from the recovered originals (§9.11 method),
no new third-party URLs. `hero-fort-lauderdale-fl` is a lower, water-level band
of the photograph the service-areas hub crops higher; `hero-pembroke-pines-fl`
is a lawn-weighted band of the frame Parkland uses; `hero-coral-springs-fl` and
`hero-boca-raton-fl` are upper bands of two frames previously cropped lower.
Every source frame is now used at least twice.

**Verified.** `sync-partials.py --check` and `check-links.py` both exit 0. The
four new pages plus the hub and two service pages at 390 / 768 / 1440: HTTP
200, zero console errors, zero failed requests, no horizontal overflow, hero
decoded. Scroll-reveal returns everything to full opacity; with `main.js`
blocked nothing is hidden. Drawer opens and closes on `Escape`. Renders with
JavaScript disabled. Titles, descriptions and canonicals unique across all 22
pages. FAQ JSON-LD matches the visible `<details>` text exactly, six per page,
and each location page's `@graph` was asserted to contain no `LocalBusiness`,
no `GeneralContractor` and no address node.

### 13.13 Pass 10 — the Projects hub, and an evidence audit that found nothing

**The brief asked for a decision before it asked for a page:** determine whether
actual project photographs and metadata are available, and if they are not,
build the hub honestly rather than inventing case studies. The audit ran first.

```
any project metadata ever committed?   only PROJECT-SPEC.md, robots.txt, sitemap.xml
EXIF date / GPS / author in any image?  none, in any of the nine source frames
any committed text naming an address,
  completion date or client?            none
```

Combined with §12 items 6 and 7 — captions that do not match their photographs,
and photography that appears to be stock — that settles it: **zero verified
project facts exist.** No detail pages were built, and none should be until the
§11.1 gates are met. That section is the deliverable the brief asked for; this
one records what was shipped.

**`/projects/` — one page, 594 lines, no fabricated facts.**

| Band | What it does |
|---|---|
| Intro | States the Projects/Gallery distinction in the first two sentences: gallery is for looking, projects is for checking. |
| Published records | The zero-state, stated plainly, plus the three gates from §11.1 and an invitation to audit the claim ("count the specific completed projects this website asserts"). |
| The work | 26 scopes of work, filtered by the 11 build types. |
| Record template | The seven required sections, published *before* there is anything to bend them for. |
| Checking our work | Six things a homeowner can verify without trusting any website, this one included — including the licence number and where to check it. |
| Areas, FAQ, CTA | The established components. |

**What the filter actually filters, and why not projects.** A filter over zero
records is a dead control, and a filter over reference photography would have
rebuilt `/gallery/` under a name that promises evidence. So the 26 items are
*scopes of work* — each a real piece of work Arco builds, each written from the
service pages' own verified material, each tagged to one to three build types
and linking to the service page that governs it. Every category returns between
2 and 7 results; none returns one, because a filter that always returns a single
item is a menu wearing a filter's clothes.

**Claims refused on this page, each for a stated reason:**

- **No case studies.** No city, date, duration, cost, materials, constraints,
  scope or homeowner appears for any individual job, because none is verified.
- **No portfolio framing of the photography.** The page states that all site
  imagery is reference imagery. It does not present a single frame as an Arco
  job at an address.
- **No addresses.** The page says explicitly that it will not publish a list of
  completed properties, and why — the people living there did not consent to
  being advertising.
- **No slip-proof claim** (only the denial `/services/pool-decks/` already
  uses), **no wind rating**, **no appliance brands**, **no property-value
  percentage**, **no pricing or guarantee language**.
- **Permitting** uses the mandated wording verbatim: *"Requirements can vary by
  jurisdiction and project scope. Arco can discuss planning considerations for
  your specific project."*

**Projects links added across the site** — 22 pages, each contextual rather than
stuffed:

- **Homepage:** a line in the gallery band naming the distinction and linking
  through, plus a second `Browse Projects` button beside `View All Photos`.
- **11 service pages + 8 city pages:** a `Browse the Work by Build Type` button
  closing the existing `#related` band.
- **`/services/`:** the same button under its areas band.
- **`/service-areas/`:** the FAQ answer *"Have you completed projects in my city
  before?"* — the single most natural place on the site to point at `/projects/`
  — now links to it.

**Also fixed, found by extending the test suite to all 14 interior pages:**

- `/services/fence/` and `/services/impact-windows-doors/` carried 209-character
  meta descriptions (§10 asks for ~150–160); both would be truncated in results.
  Rewritten to 146 and 150.
- `.gallery-cta` had no rule for two adjacent buttons, so the homepage pair sat
  border-to-border. They now gap at 14px and stack below 520px.
- `pagetest.js` hardcoded `BUTTON:Services` as the expected current-nav item, so
  it could only ever test service pages; it now reads the page's own nav key.
  Its 30-character title floor was arbitrary and failed legitimate hub titles —
  lowered to 28.

**Verification.** 441 assertions across seven suites, all passing: 57 new
`/projects/` checks (every category filtered and counted, keyboard operation,
`aria-pressed` exclusivity, the no-JS degradation, the honesty guards), plus
266 whole-page checks now covering all 14 interior pages, 47 navigation, 25
accessibility, 25 subpath-deployment, 11 reveal and 10 form. `check-links.py`
resolves every URL on 24 pages with no root-absolute leftovers; `PLANNED` lost
the 15 routes that have since shipped.

**Two test failures were diagnosed as test artifacts, not site bugs,** and both
were fixed in the test rather than the page: `innerText` skips `[hidden]` cards,
so a content assertion running while the grid was filtered could not see the
permit wording; and `fullPage` screenshots re-run layout, which blanks
`.reveal` blocks that a scrolled viewport shows correctly — confirmed by reading
computed opacity for all six reveal blocks (all `1`) before touching anything.

**One judgement left with the owner** (§12 items 7 and 14). The imagery on this
site cannot be described as Arco's project work on the evidence available, so
`/projects/` labels it reference imagery. If these are in fact photographs of
completed Arco jobs, say so and the framing changes across the site — and item
6's mismatched gallery captions become fixable rather than merely flagged.

## 14. FORMS

`#quote-form` is a real `<form>` with labelled controls, `required` fields,
`autocomplete` hints, an off-screen honeypot (`#qf-company`) and inline errors
wired through `aria-describedby` / `aria-invalid`.

**It has no backend.** `main.js` reads `data-endpoint` on the form:

- **endpoint set** → `POST`s JSON `{name, phone, email, service, details}`,
  shows the success panel on `2xx`, and on failure tells the visitor to call or
  email instead.
- **endpoint empty (current state)** → opens a pre-filled `mailto:` draft to
  `jonah@arcooutdoors.com`.

The mail fallback is a stopgap, not a solution — it loses visitors without a
configured mail client. **Setting a real endpoint is a launch requirement.** Any
handler must be static-host compatible (a form service or serverless function);
it must not turn the site into a Node application.

The success panel must never appear unless a send actually succeeded. The
original bundled page showed "Thank you!" while sending nothing at all; do not
reintroduce that behaviour.

## 15. ACCESSIBILITY

Required on every page:

- semantic landmarks (`header`, `nav[aria-label]`, `main`, `footer`), one `main`
- a skip link as the first tab stop
- keyboard-operable navigation — see §8.3 for the full dropdown and drawer
  contract (`aria-expanded`, `Escape`, focus return, focus trap, scroll lock)
- a CSS no-JS fallback (`html:not(.js)` in `style.css`) that keeps every
  navigation destination reachable when scripting is off
- visible focus (`3px` outline, `3px` offset; cream on dark grounds)
- correct heading order, exactly one `h1`
- meaningful `alt`; decorative images get `alt=""` + `aria-hidden="true"`
- every inline `svg` either `aria-hidden="true" focusable="false"` or
  `role="img"` with a label
- `prefers-reduced-motion: reduce` collapses all animation and transitions and
  forces scroll-reveal content visible
- form errors announced through `role="status" aria-live="polite"`, with focus
  moved to the first invalid field

### Known contrast debt — decision required

Four pairs from the original brand palette fail WCAG AA for normal text. They
were **not** changed, because darkening them would visibly alter every eyebrow,
link and accent on the site — a change to the visual identity, not a bug fix.
Compliant values, hue and saturation preserved:

| Token | Current | Worst ratio | AA-passing value | Then |
|---|---|---|---|---|
| `--gold-link` | `#b5843a` | 2.68:1 on `--sand-100` | `#86612b` | 4.51:1 |
| `--muted` | `#8a7a63` | 3.36:1 on `#ffffff` | `#746653` | 4.50:1 |
| `--foot-dim` | `#7d715c` | 3.79:1 on `--ink-900` | `#8b7d66` | 4.51:1 |

`--gold` `#e0a94e` on `--ink` is **7.89:1 — passes**, so buttons and dark-section
accents are fine; the debt is only gold-on-sand and the two greys.
Swapping the three values above in `:root` is the entire fix.

## 16. PERFORMANCE

Budget and standing rules:

- **No base64 or data-URI images.** Ever. This is what made the original file
  4.7 MB (§17).
- Everything below the fold is `loading="lazy" decoding="async"`.
- The hero image is the LCP element: `fetchpriority="high"`, preloaded with
  `imagesrcset`, never lazy.
- Every `<img>` carries explicit `width` and `height`, and fixed-height media
  boxes use `object-fit: cover`, so cumulative layout shift stays at zero.
- Responsive `srcset`/`sizes` on every photograph with more than one useful size.
- Photographs are WebP. Decorative textures shown at low opacity are compressed
  hard (q≈52–58) because their detail is not perceivable.
- Fonts are self-hosted WOFF2, `font-display: swap`, latin + latin-ext only
  (cyrillic, greek and vietnamese subsets were dropped: 334 KB → 200 KB), with
  the two critical faces preloaded.
- JavaScript is one `defer`ed file. Keep it that way; no third-party tags without
  an explicit decision recorded here.

Current homepage payload (self-hosted, uncompressed, first view):
HTML 57 KB · CSS 25 KB · JS 10 KB · fonts 200 KB · images ~1.7 MB across the
whole page, of which only the hero (~196 KB) is eager.

## 17. WHY THE ORIGINAL index.html WAS 4.7 MB

It was not a hand-written page. It was a **Claude Design canvas (`.dc.html`)
artifact bundle** — a single-file React application that unpacked itself at
runtime.

Composition of the 4,701,895 bytes:

| Part | Bytes | Note |
|---|---|---|
| `<script type="__bundler/manifest">` | 4,602,325 | one JSON line: 28 gzipped, base64-encoded assets |
| `<script type="__bundler/template">` | 80,361 | the real page, as a JSON-escaped string |
| bundler unpack runtime | ~19,000 | blob minting, `postMessage` relay, nested-page protocol |

The manifest decompressed to 3.59 MB: 9 JPEGs (2.91 MB), 17 WOFF2 font subsets
(334 KB), React 18.3.1 + ReactDOM UMD (142 KB) and a `dc-runtime` (66 KB).
Base64 inflates binary by ~33%, which is where the remaining megabyte went.

Consequences that made it unusable as a website — all now resolved:

- `<title>` was `Bundled Page`, and the runtime blanked it. No description, no
  canonical, no Open Graph, no structured data.
- **Zero `<img>` elements.** Every photograph was a CSS `background-image`, so
  none had alt text, lazy loading, or `srcset`.
- Nothing rendered without JavaScript — the page was a spinner reading
  "Unpacking…".
- Markup used non-standard custom elements (`<x-dc>`, `<sc-for>`, `<sc-if>`,
  `<sc-raw-select>`, `sc-camel-view-box`, `style-hover`, `{{ mustache }}`) that
  no crawler or assistive technology understands.
- Every style was inline; nothing was cacheable or reusable across pages.
- React and ReactDOM were shipped to render entirely static content.

The rebuild extracted all 28 assets, re-encoded the photographs to WebP at
responsive widths, kept the latin font subsets, and rewrote the template as
semantic HTML5 + external CSS + one small vanilla JS file. **The original bundle
remains in git history at commit `ae67717` if any asset needs recovering.**

## 18. VERIFICATION CHECKLIST

Run before every commit that touches a page. `python3 -m http.server` from the
repository root is enough to serve it.

- [ ] One `h1`; heading order has no skipped levels
- [ ] Unique title, description, canonical
- [ ] No `href="#"` other than the known social placeholders
- [ ] Every `img` has `alt`, `width`, `height`, and `loading` (lazy below fold)
- [ ] No duplicate `id`s
- [ ] Zero console errors and zero failed same-origin requests
- [ ] No horizontal overflow at 390px, 768px and 1440px
- [ ] Mobile menu: opens, closes on link choice, closes on `Escape`, unlatches on
      resize
- [ ] Skip link is the first tab stop and is visible when focused
- [ ] Renders and navigates with JavaScript disabled
- [ ] `prefers-reduced-motion: reduce` leaves all content visible and still
- [ ] New URL added to `sitemap.xml`
- [ ] `python3 tools/sync-partials.py --check` exits 0
- [ ] `python3 tools/check-links.py` exits 0
- [ ] Page renders correctly served from a subpath, not only from a root
- [ ] `<body data-page="…">` set, and the right nav item shows as current
- [ ] Both stylesheets loaded, `style.css` before `pages.css`
- [ ] Dropdowns open on hover, click and `Enter`; `Escape` returns focus
- [ ] Mobile drawer: opens, accordions expand, body scroll locks, scroll offset
      restores on close, `Escape` closes, Tab stays inside
- [ ] Interior pages follow the §8.5 skeleton and alternate section grounds
- [ ] JSON-LD matches the §8.5 table; FAQ answers match the visible text
- [ ] Any new image crop actually depicts the thing it illustrates
- [ ] Zero shared sentences with sibling pages (see §13.7, re-measured §13.9);
      H2 spine is its own
- [ ] No "slip-proof"/"non-slip" as a material property, no value percentages,
      no service claimed that §5 does not list
- [ ] No water-savings figure on turf content, no blanket pool-code compliance
      claim on fencing content, and none of the impact-window number classes
      listed in §13.9 unless verified documentation is in this repository
- [ ] Content still visible with `main.js` blocked (see `.reveal-on`, §13.6)
- [ ] No claim from §4 or §11 introduced

Additionally, for a location page:

- [ ] No completed project asserted in that city, and the photography note is
      present wherever images appear
- [ ] No local code, permit, fee, timeline, barrier requirement or HOA rule
      stated — requirements are routed to "confirmed for your address"
- [ ] No demographic, income or property-value characterisation of the city
- [ ] `@graph` carries no `LocalBusiness`, `GeneralContractor` or address
      node; the city appears only as `Service.areaServed` (§8.5)
- [ ] Section order, not just wording, differs from every sibling city page
- [ ] Duplication reviewed at BOTH thresholds (§13.12): exact shared sentences
      at ≥45 chars, and near-duplicate pairs at token Jaccard ≥ 0.55. Exact
      matching alone is not sufficient
- [ ] Service pages carry the `.areas-grid areas-grid--compact` *Areas we
      serve* block, with city-name-only anchor text

Additionally, for anything touching `/projects/`:

- [ ] No individual project asserted — no city, date, duration, cost, materials,
      constraints, scope or homeowner — unless all three §11.1 gates are met
- [ ] Site photography still described as reference imagery, never as a
      portfolio of completed Arco work
- [ ] No list of completed addresses, and no homeowner identified
- [ ] Every filter category returns at least two entries; a category returning
      one is a menu, not a filter
- [ ] With `main.js` blocked: every card visible, filter bar hidden (`.filter-on`)
- [ ] Filter chips are `<button>`s, exactly one `aria-pressed="true"` at a time,
      operable by keyboard, and the live region is empty until a filter is used
- [ ] `/projects/` and `/gallery/` have not converged (§8.2)

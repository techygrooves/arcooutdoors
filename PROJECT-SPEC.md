# PROJECT-SPEC.md — Arco Outdoors

**This file is the permanent source of truth for every subsequent session on this
repository. Read it before writing any code. Update it whenever a decision,
route, token, or verified fact changes.**

Last updated: 2026-08-31 (pass 4 — patios, driveways, pool decks)

---

## 1. BUSINESS

**Arco Outdoors** — outdoor remodeling contractor, South Florida.

## 2. DOMAIN

`https://www.arcooutdoors.com/`

Canonical form: `https://` + `www.` + trailing slash on directory URLs.
Every canonical, sitemap entry, Open Graph URL and JSON-LD `@id` must use it.

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

  assets/
    css/style.css               ← tokens, global nav, footer, homepage components
    css/pages.css               ← shared interior-page components
    js/main.js                  ← nav, current-page, reveal, form, year
    images/  fonts/
    partials/header.html        ← canonical header markup (source of truth)
    partials/footer.html        ← canonical footer markup (source of truth)

  tools/sync-partials.py        ← authoring helper, never a deploy step
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

**Live as of pass 4 (7 URLs):** `/`, `/services/`, and the five service pages
`outdoor-remodeling`, `paver-installation`, `patios`, `driveways`,
`pool-decks`. Everything else is linked from the global nav or footer and
returns 404 until its page is built — a deliberate, approved state, not a
defect. `sitemap.xml` lists only URLs that resolve; add each entry as it ships.

**Five service pages remain:** outdoor kitchens, pergolas, tiki huts, turf,
fencing, impact windows & doors.

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

`Service.provider` and `WebPage.isPartOf` reference the homepage `@id`s
(`…/#business`, `…/#website`) rather than redeclaring the business. Every FAQ
answer in JSON-LD must match the visible `<details>` text. Still **no**
`aggregateRating` or `Review` anywhere (§12).

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
| `hero-pool-decks` | pool, surround and loungers | `/services/pool-decks/` banner |

**The nine source photographs are now carrying eight pages.** Pass 4 exhausted
the usable material: `hero-driveways` and `card-fencing` are different crops of
the same building, and `hero-pool-decks` is only 700px wide because its source
is. Real project photography is now the binding constraint on further pages —
see §12 item 7.

Each new crop was reviewed against the service it illustrates. A pool photograph
originally cropped for the fencing card was rejected and re-sourced, because a
card labelled *Fencing* showing a pool is the same category of error as §12
item 6. Alt text describes what is actually in the frame, never what the card is
selling.

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
| 7 | Gallery / About / hero | Photography appears to be stock, not Arco project work | Presented as "our custom outdoor transformations". |
| 8 | Services + journal cards | 9 images hot-linked from `images.unsplash.com` | Third-party dependency, licensing exposure, and they are the only images not self-hosted. |
| 9 | Journal section | Three articles with dates (Jul 22, Jul 08, Jun 24) and no year, linking to `#journal` | Implies a blog that does not exist. |
| 10 | ~~Header + footer~~ | ~~Facebook and Instagram icons link to `href="#"`~~ | **Resolved in pass 2** — the icons were removed rather than pointed somewhere invented. Add them only when real profile URLs are supplied. |
| 11 | Consultation form | No submission endpoint exists | See §14 — currently falls back to a mail draft. |
| 12 | Global nav + footer | 31 of the 32 linked routes do not exist yet and return 404 | Approved and expected: the pages ship in later passes. `sitemap.xml` correctly lists only `/`. Do not submit the sitemap or launch until the routes resolve. |

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
- [ ] `<body data-page="…">` set, and the right nav item shows as current
- [ ] Both stylesheets loaded, `style.css` before `pages.css`
- [ ] Dropdowns open on hover, click and `Enter`; `Escape` returns focus
- [ ] Mobile drawer: opens, accordions expand, body scroll locks, scroll offset
      restores on close, `Escape` closes, Tab stays inside
- [ ] Interior pages follow the §8.5 skeleton and alternate section grounds
- [ ] JSON-LD matches the §8.5 table; FAQ answers match the visible text
- [ ] Any new image crop actually depicts the thing it illustrates
- [ ] Zero shared sentences with sibling pages (see §13.7); H2 spine is its own
- [ ] No "slip-proof"/"non-slip" as a material property, no value percentages,
      no service claimed that §5 does not list
- [ ] Content still visible with `main.js` blocked (see `.reveal-on`, §13.6)
- [ ] No claim from §4 or §11 introduced

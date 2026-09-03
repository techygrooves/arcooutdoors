# PROJECT-SPEC.md — Arco Outdoors

**This file is the permanent source of truth for every subsequent session on this
repository. Read it before writing any code. Update it whenever a decision,
route, token, or verified fact changes.**

Last updated: 2026-09-03 (pass 15 — technical SEO: metadata, share cards, link targets)

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

  blog/index.html                            ← live (resource hub)
  blog/<article-slug>/index.html             ← live × 6

  get-a-quote/index.html                     ← live (primary conversion page)
  contact-us/index.html                      ← live
  privacy-policy/index.html                  ← live
  cookie-policy/index.html                   ← live
  accessibility/index.html                   ← live

  assets/
    css/style.css               ← tokens, global nav, footer, homepage components
    css/pages.css               ← shared interior-page components
    js/main.js                  ← nav, current-page, reveal, form, year
    images/  fonts/
    partials/header.html        ← canonical header markup (source of truth)
    partials/footer.html        ← canonical footer markup (source of truth)

  tools/sync-partials.py        ← inserts partials + relativises paths
  tools/check-links.py          ← resolves every link/asset against the disk
  tools/audit-seo.py            ← metadata, headings, JSON-LD, sitemap (§8.7)
  tools/make-og-cards.py        ← regenerates the share cards (build-time only)
  REDIRECTS.md                  ← 301 map; deliberately empty, see the file
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

**Live as of pass 14 — the route map is complete (38 URLs).** Every route in
§8.2 now exists: `/`, `/services/` and all eleven service pages, `/projects/`,
`/gallery/`, `/reviews/`, `/about-us/`, `/service-areas/` and all eight city
pages, `/blog/` and its six articles, `/get-a-quote/`, `/contact-us/`,
`/privacy-policy/`, `/cookie-policy/` and `/accessibility/`, plus `404.html`.

`tools/check-links.py` reports **zero links to planned-but-unbuilt routes** for
the first time in the project's history, and `sitemap.xml`'s 38 entries were
diffed against the file system — they match exactly. There is no longer any
"expected 404" state to explain: a link that does not resolve is now a defect.

**Three tiers are now complete** — all eleven §5 services, all eight §6 priority
markets, and the whole evidence tier (`/projects/`, `/gallery/`, `/reviews/`)
plus `/about-us/`.

**Nothing remains in §8.** Every remaining launch blocker is in §12 — chiefly
the missing form endpoint (item 11) and the unverified homepage claims
(items 1–7). Those are owner decisions and configuration, not pages to build.

**The three evidence routes are deliberately different from one another and must
not converge.**

| Route | Purpose | Failure mode to avoid |
|---|---|---|
| `/gallery/` | Visual browsing. Photographs, minimal text, fast to skim. | Becoming a portfolio — captioning stock imagery as completed work. |
| `/projects/` | Written records of specific work, held to §11.1. | Becoming a gallery — leading with photographs instead of documentation. |
| `/reviews/` | Third-party word about the work, held to §11.2. | Becoming a testimonial wall — unattributed quotes and a rating with nothing behind it. |

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
| Resource hub | `BreadcrumbList` + `CollectionPage` (`ItemList` of articles) + `FAQPage` |
| Article | `BreadcrumbList` + `Article` + `WebPage`, plus `FAQPage` only where the page carries a visible FAQ |
| Contact / conversion | `BreadcrumbList` + `ContactPage` + `FAQPage` where a visible FAQ exists. `ContactPage.about` (and `mainEntity` on `/contact-us/`) reference the homepage business `@id` — the address is never redeclared |
| Legal | `BreadcrumbList` + `WebPage` with `datePublished` / `dateModified`. No `FAQPage` — these pages answer in prose, not disclosures |
| `404.html` | **None.** An error page is not a document to index; it carries `noindex, follow` and no structured data |

**Article nodes carry organisational authorship, never a person.** `author` and
`publisher` both reference the homepage business `@id`; no `Person` node, no
invented byline, no fabricated credentials (§13.15). `datePublished` and
`dateModified` are the real dates the file was written and last revised —
never back-dated to look established, and never bumped to look fresh.

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

**Known limitation, now mitigated.** `404.html` uses depth-0 relative paths, so
a miss at a deeper path (`/services/nope/`) resolves them against the requested
URL and the external stylesheets 404. That is inherent to a static error page
with relative paths and affects both deployment shapes.

Pass 14 stopped it rendering as raw unstyled HTML: `404.html` now carries a
small inline `<style>` block — ground colour, display face for the `h1`, body
type and link colour — declared **before** the two stylesheet links, so the real
stylesheets override it whenever they do resolve. Verified by loading the page
with both stylesheets blocked: sand ground, serif heading, gold links, every
destination readable and clickable. It is a deliberate, documented exception to
the "no inline styles" habit, and the only one on the site.

### 8.7 Metadata contract

Audited page by page in pass 15 and held by `tools/audit-seo.py`, which exits
non-zero on any breach. Every one of the 38 indexable pages carries, with no
exceptions:

| Tag | Rule |
|---|---|
| `<meta charset>` | first thing in `<head>` |
| `<meta name="viewport">` | `width=device-width, initial-scale=1` |
| `<title>` | unique sitewide, ≤ 62 characters |
| `<meta name="description">` | unique sitewide, 110–160 characters |
| `<link rel="canonical">` | absolute, production domain, trailing slash |
| `<meta name="robots">` | `index, follow, max-image-preview:large` |
| `og:type` / `og:site_name` / `og:locale` | `website` (`article` on the six blog articles) / `Arco Outdoors` / `en_US` |
| `og:title` / `og:description` / `og:url` | mirror the title, description and canonical |
| `og:image` + `:width` + `:height` + `:alt` | the page's own card, 1200×630 |
| `twitter:card` | `summary_large_image` |
| `twitter:title` / `:description` / `:image` / `:image:alt` | mirror the Open Graph values |

`404.html` is the deliberate exception and carries none of the social or
canonical tags: it is `noindex, follow`, it is not a document to share, and a
canonical on an error page would point a miss at itself.

**Description length is a real constraint, not a preference.** Twenty-nine
descriptions ran 161–200 characters before pass 15 and were rewritten; a
description past roughly 160 is truncated mid-sentence in the result, so the
last clause — often the one carrying the phone number or the qualifier — never
reaches the reader.

**Titles must not collide.** `/services/` and `/services/outdoor-remodeling/`
both read "Outdoor Remodeling … in South Florida" and competed for the same
query. The hub is now "All Outdoor Remodeling Services"; the pillar page keeps
"Complete Outdoor Remodeling in South Florida". The eight city titles share the
`Outdoor Remodeling in <City>, FL` pattern **on purpose** — the city is the
differentiator and the pattern is what makes the set legible in a result page.

**Share cards: `assets/images/og/og-<slug>.jpg`, one per page, 1200×630.**
Generated by `tools/make-og-cards.py` (build-time only, §9.11). Before pass 15
`og:image` pointed at each page's hero banner, and 21 of the 27 distinct heroes
were **under** the 1200×630 minimum for `summary_large_image` — `hero-pool-decks`
is 700×326 — at a 2.6:1 ratio nothing renders at. Declaring
`summary_large_image` against an undersized image gets the card downgraded or
dropped, so the site's social previews were broken everywhere despite the tags
being present. The cards cut each page's own photograph to 1.91:1, so the tags
and the asset finally agree.

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
| `.contact-line` / `.contact-line__plain` | a phone number, email or address block set in the display face; the `__plain` variant drops the link colour and a size step for facts that are not links |
| `.field-group` / `.field-choices` | a labelled `fieldset` for radio or checkbox groups inside a form panel |
| `.field-optional` | quiet "(optional)" marker on a label, since required fields carry `*` |
| `.quote-layout` | the form beside its supporting rail on `/get-a-quote/`; collapses at 1024px |

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
| `hero-blog` | open-plan interior with doors folded back to a terrace | `/blog/` banner |
| `hero-projects` | white rendered volumes over a paved path and lawn | `/projects/` banner |
| `hero-gallery` | house, sliding glazing, paved terrace and pool | `/gallery/` banner |
| `hero-reviews` | white rendered volumes against clear sky | `/reviews/` banner |
| `hero-about-us` | dark-clad elevation lit at dusk over a lawn | `/about-us/` banner |
| `gal-*` (14 crops × 3 widths) | see §9.13 | `/gallery/` grid, `/about-us/` proof band |

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

**Share cards — `assets/images/og/og-<slug>.jpg`, 38 files, 1200×630, ~2.5 MB.**
Added in pass 15 and never referenced by a page's markup: they exist only for
`og:image` and `twitter:image`, so no visitor downloads one. Each is cut from
that page's own hero (the mapping is the `HEROES` list in
`tools/make-og-cards.py`, which is the file to edit when a page is added), under
the brand scrim with the wordmark, page name, licence and phone set in the
site's own Cormorant Garamond and Manrope. JPEG, not WebP — WebP share images
are still unreliable on some scrapers, and this is the one place on the site
where an older format is the correct choice.

Regenerating them needs two build-time-only packages beyond Pillow:
`pip install fonttools brotli`, which decompress the site's WOFF2 faces so the
cards are set in the real brand type rather than a substitute. Neither is a
runtime dependency and neither touches the deployed site — §7's no-build-step
rule holds.

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

### 9.13 Gallery and review components (pages.css §16, §17)

| Class | What it is |
|---|---|
| `.photo-grid` / `.photo` | Uniform 4:3 gallery cards. Captions sit **below** the image, not overlaid on it. |
| `.photo__tag` | Build-type chip on a gallery card. |
| `.review-card` | Built, documented, and **rendered nowhere** — see §11.2. |
| `.claim-table` | A practice beside a plain *Yes* or *Never*. Carries its own dark header ground because the shared `.table-wrap thead th` colour is `--sand-100`, which vanishes inside a `.section--sand` band. |

**Why gallery captions are not overlaid.** The homepage `.gallery-item`
overlays them, which looks better and reads worse: white text over an arbitrary
photograph has no guaranteed contrast ratio. On `/gallery/` the caption is the
element making a factual claim about what you are looking at, so it is the one
part of the page that has to be legible.

**The gallery reuses `initFilter()` unchanged.** It was written generically in
pass 10 for `/projects/`, driven entirely by `data-filter-root`, `data-filter`
and `data-tags`. `/gallery/` added no JavaScript at all — which is the test of
whether that component was actually generic.

**Image ladder and the descriptor that pays for it.** Each of the 14 crops ships
at 400w, 600w and 800w (or the source's native width where that is under 800 —
never upscaled), 4:3, WebP. The 400w variant is encoded at quality 80 because it
renders near 1:1 on desktop; 600w and 800w are encoded at 72 because only
high-DPR screens select them and those downscale on the way in. Measured
identical at 800×600 and 25% smaller.

`sizes` is `(max-width: 640px) 92vw, (max-width: 1024px) 46vw, **380px**`. The
final term is a pixel value, not a `vw` value, and that matters: the grid slot
is capped by `.container` at roughly 381px on any desktop width, so a `30vw`
descriptor over-states it on a 1366px viewport (410px), pushes past the 400w
candidate, and makes every browser download the 800w file. That bug shipped in
this pass's first draft and cost 411KB per desktop page view against a true
cost of 96KB. **When a grid's column width is capped by a container, describe
it in pixels.**

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

### 11.2 Review publication standard — the standard for `/reviews/`

**Status: no review has ever met this standard, so none is published.** Pass 11
audited the repository before writing the page and found nothing usable:

```
review or testimonial data files ever committed?   none
Google Business Profile URL anywhere in history?   none — the only google.com
                                                   URL in the entire repo is
                                                   fonts.googleapis.com
review deep-links (g.page, maps.app, place_id)?    none
```

The three testimonials and the "5.0 / 180+ verified" figures on the homepage are
**§12 items 1 and 2** — unverified, flagged as the highest-risk item in this
project, and explicitly barred from reuse. They are therefore **not** reproduced
on `/reviews/`. Copying an unverified testimonial from one page to another does
not make it more true; it doubles the exposure and makes it harder to retract.

**Six gates. All six, or the review does not go up.**

| # | Requirement | Never |
|---|---|---|
| 1 | The customer's own words, unedited | Tightened, trimmed of hesitation, or rewritten into a stronger claim than the person made. A cut for length is marked. |
| 2 | Real attribution — first name and last initial, used with permission | Composites, invented names, or "a homeowner in Weston". |
| 3 | City at the level the customer agreed to, or omitted | Street address, or a date that identifies a household. |
| 4 | The build type the review is about | Filing a driveway review where it reads as evidence about an outdoor kitchen. |
| 5 | The source platform, linked where a link exists | A quote we transcribed with no way to read it at source. |
| 6 | Critical and mixed reviews published as written | Filtering, burying, or answering a critical review combatively. |

**The rating is derived, never asserted.** An average is an arithmetic claim
about a body of reviews. It gets published only when there is a body of reviews
on the page to average, is calculated from exactly those, and moves when they
do. A score above an empty page summarises nothing.

**Structured data is gated on the same condition.** `/reviews/` emits
`BreadcrumbList` + `WebPage` + `FAQPage` and **no `Review` and no
`aggregateRating` node**, and must not until real reviews are visible on the
page. Google requires review markup to describe reviews the visitor can
actually see; emitting it otherwise is both a structured-data violation and, in
the United States, a deceptive-advertising exposure under the FTC's endorsement
rules. The same prohibition already stands site-wide in §8.5.

**How we may ask, which is also published on the page.** Ask once, after the
work is finished. Never offer a discount, rebate or gift in exchange — the FTC
treats an undisclosed incentive as deceptive and the platforms remove such
reviews. Never make a review a condition of anything. Never draft it for the
customer. Let them decline with no consequence, set how much identifies them,
or withdraw later.

**When real reviews arrive:** the `.review-card` component (pages.css §17) is
already built and styled. Render the cards, then — and only then — add the
`Review` nodes and an `aggregateRating` computed from exactly the reviews shown.
Remove §12 items 1 and 2 by resolving the homepage section at the same time, so
the two pages cannot disagree.

## 12. OPEN ITEMS — unverified content currently live

These predate this pass. They are preserved so the homepage design is unchanged,
but each is a **pre-launch blocker** needing owner confirmation or removal. None
of them may be repeated on any new page until verified.

| # | Location | Claim | Risk |
|---|---|---|---|
| 1 | Homepage reviews section | Three named testimonials — "Danielle R., Parkland FL", "Marcus T., Coral Springs FL", "Sofia & Luis G., Boca Raton FL" | If not real Google reviews, this is deceptive advertising (FTC endorsement rules). **Still the highest-risk item.** Pass 11 confirmed no review data has ever been committed; `/reviews/` refuses to reproduce these and says on-page that they are unverified. Resolve the homepage section or the two pages contradict each other. |
| 2 | Homepage reviews section | "5.0" and "Based on **180+ verified** Google reviews" | Specific, checkable, and reproduced in no source material. `/reviews/` publishes neither and explains why (§11.2). No `aggregateRating` markup exists anywhere on the site. |
| 3 | About / trust strip | "750+ Projects Completed", "20 yrs In South Florida", "20+ Years of Craftsmanship" | Explicitly on the forbidden-claims list in §4. |
| 4 | Trust strip / Why Arco / consultation | "Transparent, Fixed Pricing", "Fixed, itemized pricing — no surprises" | A pricing guarantee. |
| 5 | Consultation section | "On-site visit within 48 hours" | A service-level guarantee. |
| 6 | Homepage gallery | Captions do not match their photographs — "Travertine pool deck & coping" labels a white stucco house with no pool; "Patio detail" labels an interior lounge; **and pass 11 found a third — "Paver driveway & walkway" labels a pool and terrace with no driveway in frame.** | Misrepresents work as Arco's. The `alt` text describes what is actually shown, so `alt` and caption disagree. The new `/gallery/` does not repeat any of the three; fixing the homepage is a copy edit to three `<figcaption>`s. |
| 7 | Gallery / About / hero | Photography appears to be stock, not Arco project work | Presented as "our custom outdoor transformations". **Pass 10 confirmed no image carries EXIF date, GPS or author.** `/projects/` now states on-page that all site photography is reference imagery; the homepage heading still says "our" and is the remaining exposure. |
| 8 | Homepage + `/services/` cards | 12 images hot-linked from `images.unsplash.com` — **now disclosed publicly** | Third-party dependency, licensing exposure, and they are the only images not self-hosted. **Pass 12 removed three** — the homepage journal cards now use self-hosted `gal-*` crops. Counted precisely: 6 `<img>` on `/`, 6 on `/services/`, plus a `preconnect` on each. No pass has added a new one. **Pass 14 raised the stakes:** `/privacy-policy/` and `/cookie-policy/` now tell visitors this is the site's only automatic third-party request and that it is being removed. Finishing that work is now a promise on a published page, not just a to-do. |
| 9 | ~~Journal section~~ | ~~Three articles with dates (Jul 22, Jul 08, Jun 24) and no year, linking to a blog that does not exist~~ | **Resolved in pass 12.** The three cards now carry the real titles, real publication date and self-hosted imagery of three articles that exist, and link to them directly. The section heading and lead were corrected at the same time: it described "recent projects", which the site does not publish (§11.1). |
| 10 | ~~Header + footer~~ | ~~Facebook and Instagram icons link to `href="#"`~~ | **Resolved in pass 2** — the icons were removed rather than pointed somewhere invented. Add them only when real profile URLs are supplied. |
| 11 | All three forms | **No submission endpoint exists on any of them** | See §14. Every form falls back to a pre-filled mail draft, which loses any visitor without a configured mail client. Pass 13 made this one change away from fixed: set `data-endpoint` on the three forms. **This is the single largest launch blocker on the site** — the conversion page now exists and still cannot deliver an enquiry. |
| 12 | ~~Footer legal bar~~ | ~~3 of the 32 linked routes do not exist yet and return 404~~ | **Resolved.** The three legal pages shipped, and pass 15 re-verified the whole map: `check-links.py` reports zero unresolved links, and `sitemap.xml`'s 38 URLs were diffed against the file system in both directions with no difference. `audit-seo.py` now fails the build if a sitemap entry loses its page or a page is left out of the sitemap, so this cannot silently regress. |
| 13 | `/projects/` | The page exists but holds **zero project records** — see §11.1 | Not a defect; it is the audited state. It becomes one only if a record is ever published without meeting all three §11.1 gates. |
| 14 | `/projects/` hero, and every other banner | `hero-projects` is a new crop of an existing stock frame, like every other banner on the site | Consistent with items 7 and 8. Owner decision needed: supply real project photography, or accept reference imagery site-wide and keep it labelled as such. |
| 15 | `/reviews/` | The page exists but holds **zero reviews** — see §11.2 | Not a defect; it is the audited state. It becomes one only if a review is published without meeting all six §11.2 gates, or if `Review`/`aggregateRating` markup is added before real reviews are visible. |
| 16 | `/gallery/` | Only 7 of the 11 §5 build types have a filter; driveways, outdoor kitchens and tiki huts have no photograph that depicts them | Stated on-page, with links to those three service pages. Resolves the moment real project photography is supplied. |

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
| `#consult` | nothing, since pass 13 | the section and its form remain; the CTAs that pointed here now go to `/get-a-quote/` |

**Settled in pass 13.** `/get-a-quote/` now exists, and the per-CTA decision it
was waiting for was made rather than blanket-applied: every button whose label
promises a quote or a consultation goes to `/get-a-quote/`; every `tel:` button
stays a phone call; the homepage consultation section keeps its own short form
for a visitor already at the bottom of that page, and simply no longer has a
CTA pointing down at it. A site-wide audit of every `.btn` link (label against
destination) reports zero mismatches — re-run it after adding any CTA.

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

### 13.14 Pass 11 — gallery, reviews, about

Three pages, and one of them could not be built as briefed. The gallery and the
about page are straightforward; the reviews page ran into the same wall
`/projects/` hit in pass 10, and for a sharper reason.

**The audit, again first.**

```
review or testimonial data files ever committed?   none
Google Business Profile URL anywhere in history?   none — the only google.com
                                                   URL in the whole repo is
                                                   fonts.googleapis.com
review deep-links (g.page / maps.app / place_id)?  none
```

The brief said *"reuse only actual reviews that are already supported by the
existing site/repository."* The three homepage testimonials are the only
candidates, and §12 items 1 and 2 already record them as unverified, as the
highest-risk item in this project, and as barred from reuse on any new page.
So the honest count of reusable reviews is **zero**, and `/reviews/` publishes
none. The standard it publishes instead is §11.2.

**`/gallery/` — what the photography can and cannot support.**

Every one of the nine source frames was re-examined before a single caption was
written, and the result reshaped the page:

| Filter shipped | Photographs | Why it is honest |
|---|---|---|
| Pool Decks | 5 | Pools with paved surrounds, actually in frame |
| Patios & Terraces | 5 | Paved terraces, decks, loggias |
| Pavers & Hardscape | 4 | Paths, surrounds, kerbs |
| Turf & Lawn | 3 | Ground-level lawn, level lawns |
| Pergolas & Shade | 3 | Draped timber cabana frames |
| Fencing & Screening | 2 | A slatted screen and a low rendered wall |
| Indoor–Outdoor | 5 | Full-height glazing, sliding doors |

**Three of the brief's suggested categories were refused, and the page says so:**
*Driveways* (no frame contains a driveway — the homepage's "Paver driveway &
walkway" caption is on a pool terrace, which is §12 item 6's third instance,
found this pass), *Outdoor Kitchens* (the one kitchen visible is indoors,
through glass), and *Tiki Huts* (the shade structures are draped timber, not
thatch — filing them under tiki huts would misrepresent a material). Each of
the three links to its service page instead.

No photograph carries a city, a date or any geotag, and every caption describes
what is in the frame. That is 14 captions written against the photograph rather
than against the category.

**`/about-us/` — every section the brief asked for, and four claims refused.**
About / What We Build / Complete Outdoor Transformation / How We Approach
Projects (Planning · Design considerations · Preparation · Construction ·
Finishing) / Licence CBC1269393 / South Florida / Contact / proof / CTA. What is
*not* there: founding year, team count, years of experience, awards, founder
story, certifications — none is in §3 or anywhere else in this repository. The
page states that absence rather than hiding it, under *"What we do not claim"*.
Only the verified §3 facts appear, and `jonah@arcooutdoors.com` is used as a
contact address, never as the seed of a biography.

**Two real defects found by extending the suites, both fixed:**

1. **The current-page marking in dropdowns had been dead since pass 5.**
   `initCurrentPage()` compared `a.getAttribute('href')` against
   `location.pathname`, but pass 5 made every href relative — so
   `"../../services/patios/"` never equalled `"/services/patios/"` and no
   dropdown or footer link had been marked `aria-current` on any page for six
   passes. Now resolved through `new URL(href, location.href).pathname`, which
   is also correct under a subpath deployment. Verified at both mount points.
2. **The gallery `sizes` descriptor over-stated the grid slot,** so every
   viewport downloaded the 800w candidate: 411KB per desktop page view against
   a true need of 96KB. The slot is capped by `.container`, not by the
   viewport, so the final term is now `380px` rather than `30vw`. See §9.13 —
   the general rule is worth keeping.

**Image work.** 14 crops recovered from the pass-1 bundle sources, each at
400/600/800w (or native where smaller — never upscaled), 4:3, WebP, tiered
quality. Three new page banners. All lazy-loaded below the fold with explicit
dimensions, so nothing shifts. Measured: **96KB** for the whole gallery at 1x
desktop, 257KB at 2x tablet, 661KB at 2x phone if you scroll every image into
view. No new third-party URL was introduced.

**Verification.** 587 assertions across eight suites, all passing: 89 new for
these three pages — every gallery filter counted, alt text and lazy-loading and
srcset checked per image, a 200KB transfer budget enforced, no city name in any
caption or alt, the four unverified testimonial names asserted absent from
`/reviews/`, no star widget, no invented Google link, no `Review` or
`aggregateRating` node, every About section present and nine classes of
fabricated claim asserted absent — plus 323 whole-page checks now covering all
17 interior pages.

**One test artifact, diagnosed not patched:** the first run reported images with
`naturalWidth === 0`, which was lazy loading working correctly on images below
the fold. Probing `currentSrc` instead is what exposed the real `sizes` bug
underneath — the assertion that looked wrong was measuring the wrong property,
and fixing the measurement found a genuine defect.

**Still with the owner.** §12 items 1 and 2 remain the launch blocker: the
homepage testimonials and rating are unverified and `/reviews/` now says so in
public. Either confirm them against real reviews or remove the homepage
section — as it stands the two pages contradict each other, and the reviews
page is the accurate one.

### 13.15 Pass 12 — the resource centre and its first six articles

Shipped `/blog/` and six evergreen guides. Word counts (body inside `<main>`):
hub 1,323; pavers vs concrete 1,949; pool deck materials 1,727; outdoor kitchen
checklist 1,596; pergola vs tiki hut 1,177; turf around pools 1,962; complete
backyard remodel 2,382.

**The publishing standard is on the page, not just in this file.** `/blog/` has
a *What you will not find in these articles* section listing six refusals —
costs, timelines, invented statistics, return-on-investment figures, quoted
codes or permits, product ratings, and an invented author. It follows the same
principle as §11.1 and §11.2: a rule that lives only internally is one that
quietly relaxes.

| Article | Category | Layout it uses |
|---|---|---|
| Pavers vs Concrete for a South Florida Driveway | Pavers & Hardscaping | bias disclosure, in-page contents list, failure-mode table, six questions as `.steps` |
| Choosing Pool Deck Materials for South Florida | Pool Areas | five complaints as `.steps`, then a four-material table scored against them |
| Outdoor Kitchen Planning Checklist | Outdoor Kitchens | `.with-rail` sticky rail carrying a consultation list; body is a numbered ordered checklist |
| Pergola vs Tiki Hut | Shade Structures | shortest piece; side-by-side split with images, four questions, quick-reference table |
| Using Artificial Turf Around Pools and Patios | Artificial Turf | problem-led, with a five-junction deep dive on edges and a four-question FAQ |
| How to Plan a Complete Backyard Remodel | Backyard Design | longest; decide-now-vs-later table, seven-step sequence, five-question FAQ |

Layouts deliberately differ — a contents list on two, a sticky rail on one, a
table-led argument on two, an FAQ on three and not on the other three. A visible
FAQ and a `FAQPage` node always appear together or not at all.

**Authorship.** `author` and `publisher` on every `Article` node reference the
homepage business `@id`. There is no `Person` node anywhere, no byline, no
stock portrait, no "20 years of experience" claim. The hub's first FAQ says
this in the open, because inventing a credentialled expert is a common enough
practice on contractor sites to be worth naming. `datePublished` and
`dateModified` are 2026-09-02 on all six because that is genuinely when they
were written — not back-dated to look established.

**Categories without empty shelves.** Six of the seven category names in the
brief are used; the seventh, *South Florida Outdoor Living*, runs through all of
them and is not listed separately. Categories link to in-page anchors on the
hub rather than to `/blog/category/<name>/` routes, because those routes do not
exist and inventing links that 404 to look like a bigger site is the same
failure as a doorway page. **When a category route is genuinely built, move the
anchors to it — do not create the routes to make the list look longer.**

**§12 item 9 resolved, item 8 reduced.** The homepage journal section carried
three fabricated article headlines with dates and no year, pointing at a blog
that did not exist. Its three cards now carry the real titles, the real
publication date and self-hosted `gal-*` imagery, and link to the articles
themselves. The section heading and lead were corrected at the same time — the
lead advertised "recent projects", which this site does not publish (§11.1).
That also removed three of the hot-linked Unsplash images; a precise recount
for item 8 found the previous figure in this file was wrong, and it is now
stated exactly.

**Duplication review — where the risk actually was.** Six articles on topics
that already have service pages is the highest duplication risk this project
has run. The two-threshold check from §13.12 found **32 fuzzy pairs on the first
pass**, sixteen of them between the turf article and `/services/turf/`,
including one identical sentence and several above 0.85. Twenty-four passages
were rewritten — the whole upkeep block and heat section of the turf article,
the concrete-paver row of the pool-deck table, three question prompts shared
between the pavers and remodel guides, four passages shadowing the Coral
Springs, Parkland, Pembroke Pines and Weston pages, and two homepage card
texts that had been lifted from article leads.

**Final state: zero exact and zero fuzzy overlaps involving any blog page.**
Seven exact pairs remain site-wide, all pre-existing and documented — the
§13.11 fixed permitting text (now also on `/projects/`) and the pass-3
homepage/services-hub sentence.

**The lesson for the next writer:** an article about a service you already
describe elsewhere will drift into paraphrasing that page unless it is built
around a different question. The two that needed least revision were the ones
with a genuinely different spine — the checklist, which is ordered by sequence,
and the pool-deck guide, which is organised by complaint rather than by
material.

**Imagery.** One new crop, `hero-blog`, from the interior frame in the
recovered originals that had never been used as a banner. Article banners reuse
the relevant service heroes, and inline imagery uses the `gal-*` crops added in
pass 11 — no new third-party URLs.

**Verified.** `sync-partials.py --check` and `check-links.py` both exit 0. All
seven new pages at 390 / 768 / 1440: HTTP 200, zero console errors, zero failed
requests, no horizontal overflow, hero decoded. Scroll-reveal returns
everything to full opacity; with `main.js` blocked nothing is hidden. Drawer
opens and closes on `Escape`. Renders with JavaScript disabled. Titles,
descriptions and canonicals unique across all 33 pages. FAQ JSON-LD matches the
visible `<details>` text exactly on the three pages that have one, and the
other three were asserted to carry no `FAQPage` node and no visible FAQ. No
`Review` or `aggregateRating` node anywhere (§8.5).

### 13.16 Pass 13 — contact, conversion, and one form engine

Shipped `/get-a-quote/` and `/contact-us/`, the last two routes any visitor
could reach from the navigation or a call to action. Word counts 837 and 1,131
— deliberately short, because both pages exist to be acted on rather than read.

**The form engine was rewritten rather than copied.** `initForm` handled
exactly one form with hard-coded field IDs. Adding two more would have meant
three near-identical blocks of JavaScript, so it became `initForms`: a generic
controller over any `form[data-arco-form]`, with validation rules, labels,
messages, endpoints and panel selectors all declared in markup. The full
contract is in §14. The homepage form was migrated to it by adding attributes
and changing nothing else, and its behaviour was re-tested afterwards.

**Still no backend, said louder.** All three forms carry an empty
`data-endpoint`, so nothing transmits. The mail-draft fallback is unchanged in
substance but its success panel now says what actually happened — that the
message sits in the visitor's mail application and is not with us until they
press send — rather than implying delivery. §12 item 11 was rewritten to make
this the single largest launch blocker on the site: the conversion page now
exists and still cannot deliver an enquiry.

**Connecting a provider is one attribute**, documented in three places so a
future developer cannot miss it: a boxed comment above `initForms`, and a
DEVELOPER CONFIG block beside the form markup on each new page. Each states
that an endpoint URL is public and that no key, token or password may be placed
in markup or in `main.js`.

**Verified contact facts only.** Phone, email, address, hours and licence
number are reproduced exactly as §3 records them, and the page says outright
that no weekend, holiday or emergency availability is advertised *because there
is none to promise*. The address block notes it is an office rather than a
showroom.

**No embedded map, and the page says why.** A Google Maps iframe would load
third-party scripts on every visit for something a visitor needs once, and §7
bars third-party tags without a recorded decision — so the address links out to
Maps instead. If an embed is ever wanted, that is a decision to record here
first, not a widget to drop in.

**Data minimisation is a feature of the page, not an accident.** The quote form
asks for a name, two ways to reply, the project ZIP and a description. It does
not ask for a street address, a budget band or any financial detail, and both
pages say so where a visitor will read it.

**The CTA question from §13.5 was settled.** Every `.btn` link on all 35 pages
was audited by label against destination: quote and consultation labels go to
`/get-a-quote/`, `tel:` buttons stay calls, informational contact links go to
`/contact-us/`. Zero mismatches. The two homepage `#consult` anchors now point
at the quote page; the consultation section and its form remain in place for a
visitor who has already scrolled that far.

**Testing.** A 31-assertion browser suite covers all three forms: empty-submit
error counts, focus moving to the first invalid control, per-rule messages for
phone, email and ZIP, live error clearing, the honeypot short-circuit, the
mail-draft path, the success panel and its focus target, the reset button, and
— with an endpoint injected and the network intercepted — the POST content type,
the exact payload keys, the absence of the honeypot from that payload, success
on 2xx, and on 5xx no success panel, a phone-fallback message and a re-enabled
submit button. All 31 pass. Re-run it after touching `initForms`.

**Duplication.** The two-threshold check found 1 exact and 14 fuzzy pairs on
first run — mostly the permitting caution and the coverage statement, which
these pages naturally restate. Eight passages were revised; final state is zero
and zero. Worth noting for a future pass: some form of the permitting caution now
appears on seventeen pages, most of them paraphrased to keep the checker quiet
(three use the §13.11 fixed text and say so). That is approaching the
point where §13.11's argument applies — a legal caution is better identical
than freshly reworded each time — and formalising a third fixed text may be
the honest answer next time it comes up.

### 13.17 Pass 14 — the legal pages, the 404, and a complete route map

Shipped `/privacy-policy/`, `/cookie-policy/`, `/accessibility/` and a rebuilt
`404.html`. Word counts 1,638 / 637 / 1,325 / 145. **Every route in §8.2 now
resolves** — `check-links.py` reports zero links to unbuilt routes for the first
time, and `sitemap.xml` was diffed against the file system and matches exactly.

**The policies were written from an audit, not a template.** Before a word was
drafted, the source of every page, the stylesheet and the script were searched
for: cookies, `localStorage` / `sessionStorage` / IndexedDB, analytics and tag
managers, advertising and social pixels, social embeds, iframes, video and audio
players, third-party fonts, third-party JavaScript, login or payment paths, and
every external host referenced anywhere. The findings are the content:

| Checked for | Result |
|---|---|
| Cookies, any browser storage | none — nothing is written to the browser |
| Analytics, tag managers | none |
| Advertising / social / conversion pixels | none |
| Social embeds, video, audio, iframes | none anywhere on the site |
| Third-party fonts | none — six self-hosted WOFF2 files |
| Third-party JavaScript | none — one file, from this domain |
| Accounts, logins, payments | none |
| Third-party image requests | **12 images from `images.unsplash.com`, on 2 pages** |
| Outbound map link | a plain link on `/contact-us/`, nothing embedded |
| Form submissions | 3 forms, all with an empty endpoint — nothing transmits |

That audit was re-run mechanically after the pages were written, as a
regression check on the claims themselves. **Re-run it before editing either
policy**: every sentence in them is a factual claim about the codebase, and a
future pass that adds a script or an embed makes the published page false.

**What the policies deliberately do not do.** No claim of compliance with any
named statute. No list of statutory rights we would be asserting apply. No
consent banner, and the cookie policy explains that a banner asking permission
for cookies that do not exist would be theatre. The privacy page instead says:
write to us and we will tell you what we hold, correct it or delete it, no law
needs citing. Both pages name the two changes most likely to make them out of
date — connecting a form endpoint, and removing the last third-party images —
so a reader can see them coming.

**The Unsplash images are now a public commitment.** §12 item 8 has been an
internal to-do since pass 1. Both policies now tell visitors it is the site's
only automatic third-party request, what that necessarily reveals to the
provider, and that it is being removed. Finishing it is no longer optional
housekeeping.

**The accessibility statement claims nothing it cannot show.** It states WCAG
2.1 AA as the *working standard being designed against*, and says explicitly
that it is not claiming "100% ADA compliant", "WCAG certified" or "fully
accessible", that no independent audit has been carried out, and that no
screen-reader user panel has tested it. Twelve built-in measures are listed —
each one testable — alongside four **known shortfalls published on the page**:
the §15 contrast debt in three brand tokens, the absence of an external audit,
the deep-404 styling limitation, and the §12 item 6 caption mismatches. It also
states that no accessibility overlay is installed, and why. A statement that
lists only strengths is marketing.

**The 404 gained the six destinations and lost a limitation.** It now offers
Services, Projects, Service Areas, Get a Quote, Resources and Contact, plus the
homepage and the phone number, and asks anyone who arrived from an internal
link to report it. Its old "completed outdoor spaces" gallery description was
removed — it contradicted §12 item 7. And the §8.6 unstyled-deep-404 problem is
mitigated by a small inline `<style>` block ahead of the stylesheet links: see
§8.6 for the verification.

**Footer.** No change was needed — the legal bar has linked all three routes
since pass 2. They simply resolve now, and `main.js` marks the current one with
`aria-current`, which was confirmed in the browser.

**Verified.** Both tools exit 0. The four pages at 390 / 768 / 1440: HTTP 200,
zero console errors, zero failed requests, no horizontal overflow. Skip link is
the first tab stop and visible when focused. Renders with JavaScript disabled.
`404.html` re-tested with both stylesheets blocked. Duplication review found 2
fuzzy pairs, both revised, ending at zero and zero. Titles, descriptions and
canonicals unique across all 38 indexable pages.

**Also fixed.** The pass-13 rewrite of §14 had left a duplicated
`## 15. ACCESSIBILITY## 15. ACCESSIBILITY` heading in this file. Corrected.

### 13.18 Pass 15 — the technical SEO pass

No page was redesigned. This pass audited all 38 indexable pages plus `404.html`
and fixed what the audit found, then left a guard behind so the same defects
cannot come back silently.

**What the audit found already correct**, and did not touch: every page had a
charset, a viewport, a unique canonical on the production domain, exactly one
`h1`, and a heading order with no skipped levels — 39 for 39, no exceptions.
Every FAQ block matched its `FAQPage` markup entry for entry (30 pages, 6 and 4
and 5 entries respectively, zero mismatches), and the four blog articles and
`/get-a-quote/` that carry no `FAQPage` genuinely have no visible FAQ. All 132
JSON-LD `@id`s parsed and all 177 references resolved. No page anywhere asserted
`aggregateRating`, `Review`, `priceRange`, `foundingDate`, an employee count or
geo coordinates. `sitemap.xml` matched the file system exactly. The business is
declared once, on the homepage, with the §3 address, phone, email and hours, and
the licence expressed as `hasCredential` — not invented, not duplicated onto the
city pages.

**Metadata.** Twenty-nine descriptions ran 161–200 characters and were rewritten
inside 160 without losing their argument; the homepage title came down from 70
characters to 60. `/services/` and `/services/outdoor-remodeling/` shared a title
pattern close enough to compete for the same query, so the hub became "All
Outdoor Remodeling Services". After the rewrite all 39 titles and all 39
descriptions are unique, and a fuzzy check over the descriptions found **zero**
near-duplicate pairs at the §13.12 threshold. Three legal pages carried
`index, follow` without `max-image-preview:large`; all 38 now agree.

**Social metadata was present everywhere and broken almost everywhere.** Each
page pointed `og:image` at its own hero banner while declaring
`twitter:card=summary_large_image` — but the heroes are 2.6:1 page banners, and
21 of the 27 distinct ones are under the 1200×630 minimum a large card needs
(`hero-pool-decks` is 700×326). A card declared large against an undersized
image is downgraded or dropped, so essentially every share of this site
rendered wrong. `tools/make-og-cards.py` now cuts each page's own photograph to
1200×630, lays the brand scrim, wordmark, page name, licence and phone over it
in the site's own WOFF2 faces, and writes `assets/images/og/og-<slug>.jpg` —
38 cards, 2.5 MB, no third-party asset introduced. The three legal pages, which
have no hero, share the homepage photograph. `og:image:alt` and
`twitter:image:alt` are new sitewide.

**A mis-targeted call to action, found by reading the link graph.** Twenty
buttons across the service and city pages read "Browse the Work by Build Type"
and pointed at `/projects/` — a page that by §11.1 holds zero project records
and has no build-type browsing. `/gallery/` is the page with that filter. All
twenty now point there, with the wording varied across five phrasings so the
site is not repeating one exact-match anchor twenty times. The one inline
`style="margin-top:14px"` on `/services/` became `.gallery-cta--stacked`, so
`404.html`'s critical-CSS block really is the only inline style on the site
(§8.6).

**The link graph is otherwise sound and was left alone.** Every indexable page
has contextual inbound links from outside the shared header and footer; the only
page with none is `404.html`, which is correct. The flow runs home → services →
service pages → locations → projects → get-a-quote, locations link to services,
articles link to the services and locations they actually discuss. The remaining
high anchor counts are the "Areas We Serve" grid and the Related Services index
— navigational components where the city or service name is the honest label,
not anchor stuffing.

**`robots.txt`** was already correct; it gained comments recording *why* there
are no `Disallow` rules (blocking `/assets/` would stop rendering) and why
`404.html` is excluded by meta rather than from here.

**`REDIRECTS.md`** is new, and is deliberately empty. No URL this project has
published has ever changed or been removed — the route map has only grown, and
this pass changed link *targets*, not URLs. The repository also contains no
inventory of the previous arcooutdoors.com site: no crawl, no old sitemap, no
logs, and the pass-1 bundle carries no legacy internal URLs. Rather than invent
plausible legacy paths, the file records that, gives the four sources the owner
must pull the real list from, and states the rules for filling it in.

**`tools/audit-seo.py`** is the third guard, alongside `sync-partials.py --check`
and `check-links.py`. It re-runs this entire pass on demand and exits non-zero
on a missing or duplicated title or description, an over-long one, a missing
canonical or social tag, an `og`/`twitter` pair that disagree, a wrong `h1`
count, a skipped heading level, JSON-LD that does not parse, a dangling `@id`,
any of the nine forbidden business properties, an `og:image` with no file behind
it, or a sitemap and file system that have drifted apart.

**It earned its place immediately.** It caught a defect this pass had just
introduced: filling the legal pages' missing `twitter:description` from their
meta description left it disagreeing with their hand-written `og:description`.
It also forced a rule correction — the guard first demanded that
`og:description` equal the meta description, which fourteen pages deliberately
break with a shorter share blurb. That is a legitimate distinction, so the
guard now checks the `og`/`twitter` pair against each other and leaves the
share blurb alone.

**Verified.** All three tools exit 0. Chromium at both mount points (`/` and
`/arcooutdoors/`): one `h1` per page, the retargeted CTA lands on `/gallery/`,
every share card fetches 200 at its production path, no horizontal overflow at
390px, and no same-origin request failures. The only console errors are the
sandbox's egress proxy refusing the twelve known `images.unsplash.com`
hot-links (§12 item 8) — re-counted this pass and still 6 on `/` and 6 on
`/services/`, plus a `preconnect` each.

## 14. FORMS

Three forms exist, and **one engine drives all of them** (`initForms` in
`assets/js/main.js`, rewritten in pass 13 from the single-purpose `initForm`).
A form opts in with `data-arco-form` and declares everything else in markup, so
adding a fourth form never means editing JavaScript.

| Form | Route | Purpose | Required fields |
|---|---|---|---|
| `#quote-request-form` | `/get-a-quote/` | primary conversion — a project enquiry with enough detail to answer usefully | first name, last name, phone, email, project ZIP, project type, description |
| `#contact-form` | `/contact-us/` | general questions that are not yet a project | name, email, question |
| `#quote-form` | `/` (consultation section) | the short in-page form a visitor already at the bottom of the homepage can use | name, phone, email |

**Markup contract.** On the `<form>`: `data-arco-form`, `data-endpoint`,
`data-fallback-email`, `data-subject`, `data-success` and `data-status`
(the last two are selectors). On a control: `data-validate` naming one of
`text | name | phone | email | zip | choice`, an optional `data-error` for a
custom message, an optional `data-label` used in the mail draft, an `id`, and a
sibling `<span id="<id>-error">` wired through `aria-describedby`. The
off-screen honeypot carries `data-honeypot`; the "send another" button in the
success panel carries `data-form-reset`.

**Validation and errors.** Messages are set inline and the field takes
`aria-invalid="true"`; the status region is `role="status" aria-live="polite"`
and names how many fields need attention; focus moves to the first invalid
control; an error clears the moment its field becomes valid on `input` or
`change`. Nothing depends on browser-native validation UI — every form is
`novalidate` so the messages are ours and are announced consistently.

### None of them has a backend

**`data-endpoint` is empty on all three, so nothing is transmitted anywhere.**
On submit the visitor is handed a pre-filled `mailto:` draft to
`jonah@arcooutdoors.com`, and the success panel appears only after that
hand-off. The panel's wording says so plainly — it tells the visitor the
message is not sent until they press send in their mail application, and gives
the phone number for the case where no mail client opened.

**Connecting a provider is a one-attribute change**, documented three times so
it cannot be missed: a boxed comment above `initForms` in `main.js`, and a
DEVELOPER CONFIG comment beside the form markup on `/get-a-quote/` and
`/contact-us/`.

    data-endpoint="https://formspree.io/f/xxxxxxxx"

Set it on all three forms, then send a live test through each. The engine
already POSTs JSON keyed by each control's `name`, disables the submit button
in flight, shows the success panel **only** on a 2xx, and on failure tells the
visitor to call or email instead. No JavaScript change is required to go live.

Any handler must be static-host compatible — a form service or a serverless
function. It must not turn the site into a Node application (§7).

**Secrets.** A form endpoint URL is a public destination, not a credential.
Never put an API key, token or password in the markup or in `main.js`; both
ship to every visitor. Anything that must stay private belongs behind a
serverless function that holds the key server-side.

**The success panel must never appear unless something actually happened.** The
original bundled page showed "Thank you!" while sending nothing at all; do not
reintroduce that behaviour, and do not soften the mail-draft panel's wording
into implying the message has been delivered.

**What the forms deliberately do not ask for.** No street address, no budget
band, no financial detail of any kind, and nothing that could be mistaken for
an account number. The quote page says so on the page. A project enquiry needs
a name, two ways to reply, the ZIP the work is in, and what the visitor wants
done; anything beyond that is collected at the consultation, in person, when
there is a reason for it.

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

**Measured image budgets (pass 11).** `/gallery/` is the heaviest page on the
site and the one worth holding a line on:

| Context | Candidate chosen | Whole-page image transfer |
|---|---|---|
| 1366px desktop @1x | 400w | **96 KB** |
| 820px tablet @2x | 800w | 257 KB |
| 390px phone @2x | 800w | 661 KB |

Phone and tablet select the large candidate because a full-width 4:3 image on a
2x screen genuinely needs ~718 device pixels; that is correct, and lazy loading
means a visitor pays only for what they scroll past. The desktop figure is the
one that regressed once already (411 KB — see §13.14) and the suite now asserts
a 200 KB budget on it.

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
- [ ] Title ≤ 62 chars, description 110–160, both unique sitewide (§8.7)
- [ ] Canonical, Open Graph and Twitter tags complete and agreeing (§8.7)
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
- [ ] `python3 tools/audit-seo.py` exits 0 (metadata, headings, JSON-LD, sitemap)
- [ ] A new page has a share card: add it to `tools/make-og-cards.py`'s
      `HEROES` list and re-run it, or `audit-seo.py` fails on the missing file
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
- [ ] If the change adds a script, embed, font, cookie, storage call or external
      request of any kind: `/privacy-policy/` and `/cookie-policy/` are updated
      in the same commit. Every sentence on those pages is a factual claim about
      this codebase (§13.17), and adding a third-party anything makes a
      published page false

Additionally, for a page carrying a form:

- [ ] `data-arco-form` plus the full §14 markup contract; no bespoke JavaScript
- [ ] Every control labelled, errors wired through `aria-describedby`, status
      region `role="status" aria-live="polite"`
- [ ] Honeypot present, and absent from the submitted payload
- [ ] Success panel gated on a real 2xx (or on the mail hand-off, worded as
      such) — never shown for a send that did not happen
- [ ] No API key, token or password in markup or in `main.js`
- [ ] Nothing sensitive collected: no street address, budget, or financial detail
- [ ] Phone fallback visible on the page and in the failure message
- [ ] Browser form suite re-run after any change to `initForms`

Additionally, for an article under `/blog/`:

- [ ] No cost, timeline, ROI figure, invented statistic, product rating or
      quoted code/permit requirement — regulation is described as varying by
      jurisdiction and scope, and nothing more
- [ ] `Article` node carries organisational `author` and `publisher` (§8.5),
      truthful `datePublished` / `dateModified`, and no `Person` node
- [ ] A `FAQPage` node exists if and only if the page shows a visible FAQ
- [ ] Category links point at anchors or routes that exist (§13.15)
- [ ] Layout differs from the sibling articles where variation aids reading

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
      matching alone is not sufficient — see §13.15 for how badly this fails on
      an article covering a subject a service page already covers
- [ ] Service pages carry the `.areas-grid areas-grid--compact` *Areas we
      serve* block, with city-name-only anchor text

Additionally, for `/gallery/`:

- [ ] Every caption describes what is in the photograph, not what the category
      is selling — checked against the image, not against the filename
- [ ] No city, date or geotag on any photograph, in caption or `alt`
- [ ] A filter exists only where a photograph actually depicts that build type;
      categories with no photograph are named and linked, not padded
- [ ] Every image: `alt`, `width`, `height`, `loading="lazy"`, and a `srcset`
      whose candidates all exist on disk
- [ ] `sizes` describes the real slot — in **px** where a container caps the
      column width (§9.13), and the 1x desktop transfer is under 200 KB
- [ ] No image upscaled beyond its source width

Additionally, for `/reviews/`:

- [ ] No `Review` and no `aggregateRating` node anywhere in the `@graph`
- [ ] No star widget, no rating figure, no review count
- [ ] No quoted customer who does not clear all six §11.2 gates, and none of the
      §12 item 1 names reproduced
- [ ] No Google profile link unless a verified URL exists in this repository

Additionally, for `/about-us/`:

- [ ] No founding year, team count, years of experience, award, certification
      or staff biography — none is verified (§3, §4)
- [ ] Only §3 contact facts, verbatim
- [ ] JSON-LD carries no `foundingDate`, `numberOfEmployees`, `award` or
      `aggregateRating`, and references `#business` rather than redeclaring it

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

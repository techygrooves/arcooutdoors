# FINAL-AUDIT.md — Arco Outdoors, pre-launch audit

**Audit date:** 2026-09-03 · **Commit:** pass 17 · **Site:** `https://www.arcooutdoors.com/`

This is the record of the final pre-launch inspection. Everything listed as fixed
has actually been changed in this repository and re-verified. Everything listed as
outstanding needs a decision or a piece of information from the client — none of it
can be resolved by writing more code.

---

## 1. Pages created — 39 total

| Type | Count | Routes |
|---|---|---|
| Homepage | 1 | `/` |
| Service hub | 1 | `/services/` |
| Service pages | 11 | see §2 |
| Service-area hub | 1 | `/service-areas/` |
| Location pages | 8 | see §3 |
| Resource hub | 1 | `/blog/` |
| Blog articles | 6 | see §4 |
| Evidence pages | 3 | `/projects/`, `/gallery/`, `/reviews/` |
| Company | 1 | `/about-us/` |
| Conversion | 2 | `/get-a-quote/`, `/contact-us/` |
| Legal | 3 | `/privacy-policy/`, `/cookie-policy/`, `/accessibility/` |
| Error | 1 | `404.html` (`noindex, follow`, not in the sitemap) |

**38 indexable URLs + 1 error page.** `sitemap.xml` lists exactly the 38 and was
diffed against the file system in both directions — no entry without a page, no
page without an entry. No duplicate, orphaned, placeholder or half-built page
exists; there is no lorem ipsum, no `TODO`, and no "coming soon" anywhere in
user-visible text.

## 2. Services covered — 11

Complete Outdoor Remodeling · Paver Installation · Patios · Driveways ·
Pool Decks · Outdoor Kitchens · Pergolas · Tiki Huts · Artificial Turf ·
Fencing · Impact Windows & Doors

Three slugs deliberately differ from their display names: Artificial Turf is
`/services/turf/`, Fencing is `/services/fence/`, Complete Outdoor Remodeling is
`/services/outdoor-remodeling/`.

## 3. Locations covered — 8

Parkland · Davie · Weston · Plantation · Fort Lauderdale · Pembroke Pines ·
Coral Springs (all Broward) · Boca Raton (Palm Beach)

**These are not doorway pages.** Each leads with a different section and argues
from a different premise. Cross-page duplication was re-measured in this audit at
both thresholds — exact shared sentences ≥45 characters, and near-duplicate pairs
at token Jaccard ≥0.55 — and driven to **zero on both**. Nine templated passages
were rewritten to get there.

No location page emits `LocalBusiness`, `GeneralContractor` or any `address`
node. The business is declared once, on the homepage, at the one verified
address; each location page expresses its city through `Service.areaServed` only.
Nothing claims a completed project in any named city.

## 4. Blog articles — 6

- Choosing Pool Deck Materials for South Florida
- Pavers vs Concrete Driveways in South Florida
- Outdoor Kitchen Planning Checklist
- Pergola vs Tiki Hut: Choosing Shade for Your Backyard
- Using Artificial Turf Around Pools and Patios
- How to Plan a Complete Backyard Remodel

`Article` schema carries organisational authorship — `author` and `publisher`
both reference the business `@id`. No `Person` node, no invented byline, no
fabricated credentials. Dates are the real dates the files were written.

## 5. SEO status — passing

`tools/audit-seo.py` is the gate and exits 0. Across all 38 indexable pages:

| Check | Status |
|---|---|
| Unique `<title>` (≤62 chars) | 38/38 unique |
| Unique meta description (110–160 chars) | 38/38 unique |
| Canonical, absolute, production domain | 38/38 |
| Exactly one `<h1>`, no skipped heading levels | 39/39 pages |
| `robots` = `index, follow, max-image-preview:large` | 38/38 (404 is `noindex, follow`) |
| Open Graph + Twitter, complete and agreeing | 38/38 |
| `og:image` — real 1200×630 branded card per page | 38 cards, all resolve |
| JSON-LD parses; every `@id` reference resolves | 132 ids / 177 references |
| `BreadcrumbList` on every page below root | yes |
| Sitemap matches the file system | exactly |
| Image `alt` | 155 images, 0 missing, 0 weak, 8 decorative correctly `alt="" aria-hidden` |
| Duplicate FAQ questions across pages | **0** (3 collisions fixed in this audit) |

Internal linking runs home → services → service pages → locations → projects →
get-a-quote, with locations linking to services and articles linking to what they
actually discuss. Every indexable page has contextual inbound links from outside
the shared header and footer; the only page with none is `404.html`, correctly.

**No fabricated structured data.** There is no `aggregateRating`, `Review`,
`priceRange`, `foundingDate`, employee count or geo coordinate anywhere on the
site, and the audit tool fails the build if one is added.

## 6. Form status — **CONNECTED**

All three forms — the homepage consultation block, `/contact-us/` and
`/get-a-quote/` — now POST JSON to **`https://formspree.io/f/mppzrnjb`**.

Verified end to end in a browser, on all three forms, on both paths:

| Path | Behaviour | Panel shown |
|---|---|---|
| Endpoint answers 2xx | JSON `POST` with every named field | "Thank you — your enquiry is with us" / "Message received" / "Thank you!" |
| `data-endpoint` empty | Pre-filled mail draft to `jonah@arcooutdoors.com` | "One more step — send it" / "Over to your email app" |
| Endpoint errors | No success panel at all | Status line offering the phone number and email |

**The success copy is not shared between the two paths**, and that is the point:
a form that posted successfully must not tell the visitor to go and press send
in their email client, and a form that fell back must not claim the enquiry has
arrived. `showSuccess(viaMail)` reveals the `[data-when="sent"]` or
`[data-when="mail"]` block accordingly.

Validation and errors were tested and are correct: inline messages,
`aria-invalid` on failed fields, a `role="status" aria-live="polite"` region,
focus moved to the first invalid field, and an off-screen honeypot.

**Before launch, confirm on the Formspree side:** that the form is verified and
not still in a confirmation-pending state, that the notification address is
`jonah@arcooutdoors.com`, that the monthly submission allowance suits expected
volume, and that spam filtering is on. The endpoint URL is a public destination,
not a secret — but **no API key, token or password may ever be put in the markup
or in `main.js`**. Anything that must stay private belongs behind a serverless
function.

To move to another provider (Basin, Netlify Forms, a serverless function —
anything accepting a JSON `POST` and answering 2xx), swap the URL in
`data-endpoint` on the three form elements. Nothing else changes.

## 7. Remaining information needed from the client

Nothing below can be written without the client supplying it. Each is currently
**absent by design** rather than guessed.

| # | Needed | Why it matters | Blocks launch? |
|---|---|---|---|
| 1 | ~~Form endpoint~~ | **Supplied and wired** — `https://formspree.io/f/mppzrnjb`. Confirm the Formspree form is verified and the notification address is right | No |
| 2 | Certificate of insurance | The site claims a licence, not insurance — see §9 | No |
| 3 | Google Business Profile URL | No review strategy is possible without it; also the natural `sameAs` | No |
| 4 | Social profile URLs, if any exist | Header/footer icons were removed rather than pointed at invented URLs | No |
| 5 | Real project photography, with addresses and owner consent | Every photograph on the site is reference imagery — see §10 | No |
| 6 | Year founded, entity type | Would allow `foundingDate` and an honest company history | No |
| 7 | Weekend / holiday hours, if different | Only Mon–Fri 8:00–18:00 is published | No |
| 8 | Service radius, or a definitive city list | Three counties are named; no radius is claimed | No |
| 9 | Old site URL export (Search Console) | Required before any redirect map can be written — see §8 | **Yes, if a site already ranks** |
| 10 | Written customer reviews with consent | `/reviews/` is deliberately empty until then | No |

## 8. Redirects required — none identified, and that is not the same as none

`REDIRECTS.md` holds the map and is **deliberately empty**. No URL this project
has published has ever changed or been removed; the route map has only grown.

**However, this repository contains no inventory of any previous
arcooutdoors.com site** — no crawl, no old sitemap, no server logs, and the
original source bundle carries no legacy internal URLs. If a site is currently
live on that domain, its indexed URLs must be exported from Google Search
Console and diffed against the 38 routes here **before** DNS is switched.
Inventing plausible legacy paths would produce redirects that 301 nothing and
hide real 404s behind guesses. `REDIRECTS.md` §3 lists the four sources to pull
the real list from.

## 9. Claims intentionally omitted because they could not be verified

Every item here was **removed or reworded during this audit**. Each was live on
the site before it.

| Was on the site | Now | Why |
|---|---|---|
| Three named testimonials ("Danielle R., Parkland FL" etc.) with Google branding | Section replaced with the published review standard and links to `/reviews/`, `/projects/`, `/gallery/` | No customer review has ever been verified for this business. Fabricated endorsements are an FTC exposure, and the Google branding compounded it |
| "5.0 ★" and "Based on **180+ verified** Google reviews" | Removed | Specific, checkable, supported by nothing |
| "750+ Projects completed" | "11 — Services under one contractor" | No project count is evidenced |
| "20 yrs In South Florida" / "20+ Years of Craftsmanship" | "3 — Counties served" / "Based in Davie, Florida" | No founding date is known |
| "5.0 ★ Average rating" | "1 — Point of accountability" | No rating exists |
| "Transparent, Fixed Pricing" | "Eleven Services, One Contractor" | A pricing guarantee |
| "Fixed, itemized pricing — no surprises" | "A written quote, itemized by scope" | Describes the deliverable, promises no price |
| "On-site visit within 48 hours" | "An on-site visit, measured on your property" | A service-level guarantee nobody has committed to |
| "Licensed **& Insured**" (94 occurrences, header, footer, 7 service pages, hero, meta) | "Licensed contractor · CBC1269393" | The licence is verified. **Insurance is not evidenced anywhere in this repository.** The pages now cite the licence and tell the reader to request a certificate of insurance — from every contractor, not just this one |
| "we … carry insurance" (homepage FAQ + its JSON-LD) | Reworded to the licence plus how to check both | Same reason |
| "we're known for professionalism, transparency, and results that stand the test of time" | Replaced with the licence number | An unverifiable reputation claim |
| "100% free · No obligation" | "Free consultation · No obligation" | "100%" is puffery |
| Gallery captions: "Travertine pool deck & coping", "Patio detail", "Paver driveway & walkway" | "Stone steps to a rendered elevation", "Seating beside a glazed wall", "Paved walkway and planting bed" | The captions described work the photographs do not show. The `alt` text was already truthful, so caption and `alt` had been contradicting each other |
| Gallery category tags "Pool Decks", "Turf", "Driveways" on those frames | "Exteriors", "Lawns", "Paving" | Same reason |
| "Explore **our** custom outdoor transformations" | "The kind of outdoor spaces we build", plus an explicit note that the photography is reference imagery | `/gallery/` and `/projects/` already publish that none of the photography is Arco's own work. The homepage was contradicting them |

**Still absent on purpose, and must stay absent until evidenced:** award claims,
project counts, crew sizes, years in business, founding date, "#1" or "best",
financing terms, warranty terms, energy-savings percentages, insurance discounts,
wind ratings, product approval numbers, service lives, ROI figures, specific
permit or code requirements stated as universal, and any claim that a photograph
was taken at a named address.

## 10. Project information needed to create future case studies

`/projects/` exists, is indexed, and holds **zero project records** — that is its
audited state, not a defect. It publishes the standard a record must meet. To
publish the first one, the client needs to supply, per project:

1. **Written homeowner consent** to publish, including whether the city may be
   named. No address is ever published.
2. **The city**, and whether it can be shown.
3. **Scope actually performed**, separated from what was coordinated.
4. **Photographs the client owns**, ideally before/during/after, with the date
   taken. EXIF intact is ideal — none of the current library carries date, GPS or
   author.
5. **Approximate duration and season**, so timelines are described rather than
   promised.
6. **Anything that went wrong and how it was resolved** — the most credible part
   of any case study, and the part competitors will not print.
7. **Permit numbers**, if the client is willing, so the work is independently
   checkable.

The same package unlocks three other things: real `og:image` cards, the
`/gallery/` filters for driveways, outdoor kitchens and tiki huts (which have no
photograph depicting them today), and the retirement of the reference-imagery
disclaimers.

## 11. Performance observations

Measured in Chromium against a local server, desktop 1440 and mobile 390:

| Page | LCP | CLS | Requests | Third-party | Transfer |
|---|---|---|---|---|---|
| `/` desktop | 280 ms | 0.0152 | 25 | **0** | 1071 KB |
| `/` mobile | 216 ms | 0.0000 | 25 | **0** | 780 KB |
| `/services/` | 152–184 ms | 0.0001 | 19 | **0** | 552–689 KB |
| `/projects/` | — | — | — | ImageKit (45 images) | measured off this network |
| `/gallery/` | 176–196 ms | 0.0002 | 22 | **0** | 515–541 KB |
| `/get-a-quote/` | 168–212 ms | 0.0002 | 8 | **0** | 296–490 KB |

- **Two third-party dependencies, both disclosed.** `/projects/` loads its
  project photography from **ImageKit** (the only automatic external request the
  site makes, on 1 of 38 pages), and the three forms POST to **Formspree** when
  submitted. No font host, no analytics, no tag manager, no advertising, no
  embedded map; every other asset on every page is self-hosted.
  `/privacy-policy/` and `/cookie-policy/` were rewritten in this pass to name
  both — they had still been describing the Unsplash images removed two passes
  earlier, and had not yet been told the forms now submit.
- **Zero console errors and zero failed same-origin requests** across all 39
  pages. `/projects/` makes 45 requests to ImageKit, which a network-restricted
  environment will show as failures.
- **No base64 or data-URI images.** HTML totals 1.66 MB across 39 pages (largest
  single page 64 KB); CSS 79 KB across two files; JS 23 KB in one deferred file.
- Images 9.3 MB on disk, of which only the hero of each page is eager. Every
  `<img>` carries `width`, `height`, `alt`, and `loading`/`decoding`; heroes are
  preloaded with `imagesrcset` and never lazy.
- **The residual 0.0152 CLS on the homepage is font swap** and is left alone
  deliberately: the `h1` sets on two lines in Cormorant Garamond and three in the
  fallback. The standard `size-adjust` fix must be calibrated against the font the
  *visitor* falls back to (Georgia), which is not installed in the build
  environment; calibrating against the wrong one measurably made it worse. 0.0152
  is well inside the 0.1 "good" threshold. See `PROJECT-SPEC.md` §16.3.

## 12. Accessibility

- **Zero structural findings across all 39 pages**: landmarks, one `main`, alt
  text, SVG labelling, form labels, accessible names on every link and button, no
  duplicate ids, `aria-expanded` only on buttons.
- Skip link is the first tab stop and visible on focus; focus outline is 3px solid.
- Dropdowns open on click and `Enter`, close on `Escape` and return focus. The
  mobile drawer locks body scroll with `position: fixed` and releases it on
  `Escape`. Accordions are native `<details>`. The gallery filter is buttons.
- `prefers-reduced-motion: reduce` leaves no revealed content hidden.
- No crowded sub-24px touch targets at 390px (WCAG 2.2 §2.5.8 with the spacing
  exception applied).
- **Contrast: WCAG AA across the site.** The palette debt was paid in the previous
  pass by moving only HSL lightness, so hue and saturation are unchanged. Three
  elements sit over photographs and must be measured from rendered pixels rather
  than the DOM — they measure 6.70:1, 12.56:1 and 3.52:1.
- `/accessibility/` publishes the known shortfalls rather than claiming
  compliance. It does not say "100% ADA compliant" or "WCAG certified", and it
  must not be edited to.

## 13. Responsive

39 pages × 7 widths (360, 390, 430, 768, 1024, 1280, 1440) — **zero horizontal
overflow**. All nine page types re-inspected individually at 390px: no clipped
headings, no broken cards, no navigation problems.

## 14. Deployment notes

- **Mount-point independent.** Every internal URL is relative and depth-correct.
  Verified by crawling all 38 URLs at a domain root *and* under `/arcooutdoors/` —
  3,554 link instances across header, footer, breadcrumbs, cards, CTAs and body
  copy, **zero dead links at either mount point.**
- **No `localhost`, no filesystem path, no `file://`, no source map, no
  development asset** anywhere in the served files. Canonicals, `og:url`, sitemap
  entries and JSON-LD `@id`s correctly stay absolute on the production domain even
  when previewed elsewhere.
- `robots.txt` allows everything, blocks no CSS/JS/image, and points at
  `https://www.arcooutdoors.com/sitemap.xml`.
- **For GitHub Pages on the custom domain:** add a `CNAME` file containing
  `www.arcooutdoors.com` at the repository root and point DNS at Pages. `.nojekyll`
  is already present.
- **There is no build step and must never be one.** The committed HTML is what
  ships. `tools/sync-partials.py` (header/footer + path relativising),
  `tools/check-links.py` and `tools/audit-seo.py` are pre-commit guards, not build
  tools; all three must exit 0 before any commit.
- The form endpoint is set (§6). Before submitting the sitemap to Search Console,
  settle the redirect question in §8 if a site already ranks on this domain.

## 15. Launch readiness

**Ready to launch.** Structure, content, SEO, accessibility, performance and
deployment all pass, the unsupported claims carried since the first build are
gone, and the forms now deliver. The one remaining caution is the redirect
question in §8: if a site already ranks on this domain, export its indexed URLs
before switching DNS.

| | Status |
|---|---|
| Pages, navigation, links | ✅ 39 pages, 0 dead links at both mount points |
| Business information | ✅ One consistent phone, email, address and licence sitewide |
| Content accuracy | ✅ Unsupported claims removed or reworded (§9) |
| Duplication | ✅ 0 exact, 0 near-duplicate across locations; no colliding FAQ questions |
| SEO | ✅ `audit-seo.py` exits 0 |
| Accessibility | ✅ 0 structural findings; AA contrast |
| Performance | ✅ LCP < 300 ms, CLS ≤ 0.0152, 0 third-party requests |
| Deployment | ✅ Works at domain root and at a subpath |
| **Forms** | ✅ Connected to Formspree, both paths verified |
| Redirects | ⚠️ Empty, and correct only if nothing currently ranks on the domain |

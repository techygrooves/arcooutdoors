# REDIRECTS.md — 301 map for the arcooutdoors.com rebuild

**Status: no redirect is required by anything this repository has built so far.**
This file exists so that stays true deliberately rather than by accident, and so
the owner has somewhere to record the redirects only they can supply.

---

## 1. What this rebuild has changed

Nothing. Every URL this project has ever published is still live at the same
address. The route map (`PROJECT-SPEC.md` §8.2) has only ever grown:

| Pass | URLs added | URLs changed | URLs removed |
|---|---|---|---|
| 1–13 | 38 | 0 | 0 |
| 14 (technical SEO) | 0 | 0 | 0 |

`sitemap.xml` lists 38 URLs and was diffed against the file system during pass
14 — the two match exactly, with no entry pointing at a missing page and no page
missing from the sitemap.

Pass 14 retargeted twenty in-page calls to action from `/projects/` to
`/gallery/`, because the anchor promised browsing by build type and `/gallery/`
is the page that carries that filter. **That is a link change, not a URL
change.** `/projects/` is unchanged, still indexable, and still linked from the
navigation, the footer and the body of other pages. No redirect is involved.

## 2. What is *not* known, and must not be guessed

**This repository contains no inventory of the previous arcooutdoors.com site.**
There is no crawl, no exported sitemap, no server log and no redirect map in the
git history — the pass-1 source bundle carries no legacy internal URLs at all.

So no row in the table below can be filled in from anything in this repository.
Inventing plausible-looking legacy paths (`/pavers.html`, `/services/patio`,
`/index.php?page=contact`) would produce redirects that 301 nothing, hide real
404s behind guesses, and give a false sense that the migration was checked.
**Do not populate this file from memory or assumption.** Populate it from the
sources in §3, or leave it empty and honest.

## 3. How to produce the real list before launch

1. **Google Search Console** on the existing property → Indexing → Pages →
   export every URL currently indexed. This is the list that actually matters,
   because these are the URLs with links and history pointing at them.
2. **The old site's `sitemap.xml`**, if the current host still serves one.
3. **Server access logs**, for URLs that receive traffic but were never indexed.
4. **Backlink export** (Search Console → Links → Top linked pages), so an
   externally linked URL is not dropped.

Then diff that list against the 38 live routes in `PROJECT-SPEC.md` §8.2 and
record every old URL in the table below.

## 4. The map

| OLD URL | NEW URL | 301 REQUIRED |
|---|---|---|
| _(none identified — see §2)_ | — | — |

Rules for filling this in:

- One row per old URL. Use absolute URLs including `https://www.`.
- **301, never 302.** A temporary redirect does not pass signals or update the
  index.
- Redirect to the closest genuine equivalent, **never to the homepage by
  default.** A mass redirect to `/` is treated as a soft 404 and loses the page's
  history. If no equivalent exists, mark the row `410 Gone` and say so.
- Never chain: old → final, not old → interim → final.
- An old URL that maps to a route this site does not have is not a redirect
  problem — it is a missing page. Decide whether to build it before launch.

## 5. Where the redirects have to live

This is a static site with no build step and no server layer of its own, so it
cannot serve a 301 by itself. The redirects belong wherever the domain is
terminated:

- **GitHub Pages** cannot issue 301s from repository content. A custom domain
  needs the redirects at the DNS/CDN layer, or a host that supports them.
- **Cloudflare** — Bulk Redirects, or a Redirect Rule per row.
- **Netlify / Vercel** — a `_redirects` file or `vercel.json`, generated from
  the table above.
- **Apache / nginx** — `Redirect 301` or `return 301` directives.

Whichever is used, verify each row after cutover with
`curl -sSI <OLD URL>` and confirm `HTTP/… 301` plus the expected `Location:`.

## 6. Before removing any URL, ever

Per the standing rule for this project: **do not silently remove an indexed
URL.** If a route in §8.2 is ever retired, it must, in the same change,
(a) gain a row in §4 pointing at its replacement, (b) be removed from
`sitemap.xml`, and (c) be recorded in the `PROJECT-SPEC.md` pass log. A page
that simply disappears takes its rankings and its inbound links with it.

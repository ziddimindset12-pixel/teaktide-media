# Teak & Tide website: handover for a new Claude chat

The owner (Ashu Dhakre) speaks Hinglish only. Business decisions, goals and rules are in Claude memory: `/areas/sourcing-agency-business.md` (read it first).

## Where things are
- Live site: https://teakandtidesourcing.com (Cloudflare Pages).
- Site source: GitHub `ziddimindset12-pixel/teaktide-media`, branch **`website`** (static HTML; Cloudflare auto-deploys on push, ~2 min).
- Builder scripts: this branch (**`site-tools`**), folder `seo/`.
- Media for social posts: branch `main` of the same repo.

## Set up in a new session
```
git clone -b website https://github.com/ziddimindset12-pixel/teaktide-media /home/claude/site3
git clone -b site-tools https://github.com/ziddimindset12-pixel/teaktide-media /home/claude/tools && cp -r /home/claude/tools/seo /home/claude/seo
```
The scripts expect the site at `/home/claude/site3` and themselves at `/home/claude/seo`.

## How the site is built
- Every page is a static `index.html` with one `<div data-view="...">` block. `assets/app.js` registers views in `PATHS`, `VIEWS`, `NAV`, `TITLES` (and `POSTS` for blog cards). Product category pages are rendered by `renderProduct()` in app.js (the `GUIDES` map adds "Buyer guides" links).
- Blog posts: content in `seo/posts_v*.py`, built with `build_posts_v2.build()` (template = makhana blog). Latest batch script: `seo/build_v9.py` (posts in `seo/posts_v9.py`; earlier `build_v7.py`) (adds FAQ schema from `<details>`, author, cards, sitemap, app.js entries, cache-bust).
- Top-level pages (services, tools): `seo/pages_v6.py` / `pages_v8.py` with `build_v6.py` (template = quality-inspection-india).
- Cache-bust string in all HTML: `?v=YYYYMMDDx`. Bump it when CSS/JS changes.
- Forms POST to `/` and are handled by `functions/index.js` (Cloudflare Function) → Make webhook → Google Sheet "Website Leads". Allowed form names are listed in that file.
- Free checklist PDF: `seo/checklist/checklist.html` → rendered with Playwright to `/India-Supplier-Verification-Checklist.pdf`.

## Deploy
```
cd <clone of website branch> && git add -A && git commit -m "..." && git push origin HEAD:website
gh api repos/ziddimindset12-pixel/teaktide-media/commits/<sha>/check-runs   # wait for "Cloudflare Pages success"
```
Check on a phone width (390px) and desktop before pushing. Verify live pages with the OpenRush `audit_site` tool (WebFetch can't reach the domain).

## Rules that matter for the site
- Titles ≤ 60 chars, descriptions ≤ 155. No fake reviews, clients or claims. Data must be correct (check official sources).
- White theme for site and images; green theme only for videos. India maps show the full official boundary.
- No LinkedIn links. Rate card PDF is never public.
- Pace: 5–7 new pages a week, each with unique, real content (no copy-paste country pages).

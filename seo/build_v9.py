import re, json, html, sys, pathlib
sys.path.insert(0, '/home/claude/seo')
import posts_v9 as P
import build_posts_v2 as BP
SITE = pathlib.Path('/home/claude/site3')
strip = lambda s: html.unescape(re.sub('<[^>]+>', '', s)).strip()
AUTH = {"@type":"Person","name":"Ashu Dhakre","jobTitle":"Founder, Teak & Tide Sourcing","url":"https://about.me/ashudhakre","sameAs":["https://about.me/ashudhakre","https://www.quora.com/profile/Ashu-Dhakre","https://www.youtube.com/@teaktidesourcingagency"]}
OLD = '"author": {"@type": "Person", "name": "Ashu Dhakre", "jobTitle": "Founder, Teak & Tide Sourcing"}'

for b in P.POSTS:
    assert len(b['seo_title']) <= 60, (b['slug'], len(b['seo_title']))
    assert len(b['desc']) <= 155, (b['slug'], len(b['desc']))
    assert not (SITE/'blog'/b['slug']).exists(), 'exists: ' + b['slug']

for b in P.POSTS:
    BP.build(b)
    f = SITE/'blog'/b['slug']/'index.html'; s = f.read_text()
    s = s.replace(OLD, '"author": ' + json.dumps(AUTH, ensure_ascii=False))
    qs = re.findall(r'<details><summary>(.*?)</summary><div class="ans"><p>(.*?)</p></div></details>', b['body'], re.S)
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in qs]}
    s = re.sub(r'<script type="application/ld\+json">\{"@context": ?"https://schema.org", ?"@type": ?"FAQPage".*?</script>', '', s, flags=re.S)
    s = s.replace('</head>', '<script type="application/ld+json">' + json.dumps(faq, ensure_ascii=False, separators=(',',':')) + '</script></head>', 1)
    assert s.count('"FAQPage"') == 1 and s.count('<h1') == 1, b['slug']
    f.write_text(s)
BP.add_cards(P.POSTS)
BP.add_sitemap([f'/blog/{b["slug"]}/' for b in P.POSTS])

a = SITE/'assets/app.js'; s = a.read_text()
for b in P.POSTS:
    v = b["view"]
    if f'"{v}"' in s: continue
    s = s.replace('var PATHS = {', f'var PATHS = {{"{v}": "/blog/{b["slug"]}/", ', 1).replace('var VIEWS = [', f'var VIEWS = ["{v}", ', 1)
    s = s.replace('var NAV = {', f'var NAV = {{ "{v}": "blog", ', 1).replace('var TITLES = {', f'var TITLES = {{ "{v}": {json.dumps(b["seo_title"])}, ', 1)
    s = s.replace('var POSTS = [\n', f'var POSTS = [\n  {{ id: "{v}", tag: "{b["tag"]}", title: {json.dumps(b["title"])}, text: {json.dumps(b["card"])}, mins: {b["mins"]} }},\n', 1)

# category "Buyer guides" links (JS map + pre-rendered pages)
NEWG = {
 'spices': [("cumin-seed-suppliers-india","Cumin seed suppliers"),("cardamom-suppliers-india","Cardamom suppliers"),("black-pepper-suppliers-india","Black pepper suppliers")],
 'agriculture': [("basmati-rice-exporters-india","Basmati rice exporters")],
 'leather': [("leather-shoe-manufacturers-india","Leather shoe manufacturers")],
}
for cat, items in NEWG.items():
    add = ''.join(',' + json.dumps([sl, t]) for sl, t in items if f'"{sl}"' not in s)
    s = re.sub(r'(\n  %s: \[\[.*?\]\])' % cat, lambda m: m.group(1)[:-1] + add + ']', s, 1)
a.write_text(s)
for page, cat in [('spices', 'spices'), ('agricultural-products', 'agriculture'), ('leather-goods', 'leather')]:
    f = SITE/page/'index.html'; t = f.read_text()
    if 'id="guides-links"' not in t: continue
    links = ''.join(f' · <a href="/blog/{sl}/">{tt}</a>' for sl, tt in NEWG[cat] if f'/blog/{sl}/' not in t)
    t = re.sub(r'(<section class="block" id="guides-links"><div class="wrap"><h2>Buyer guides</h2><p>.*?)(</p>)', lambda m: m.group(1) + links + m.group(2), t, 1)
    f.write_text(t)

# homepage: product tiles + country links
f = SITE/'index.html'; t = f.read_text()
tiles = [("cumin-seed-suppliers-india","SPICES","Cumin"),("cardamom-suppliers-india","SPICES","Cardamom"),("black-pepper-suppliers-india","SPICES","Black pepper"),("basmati-rice-exporters-india","AGRICULTURE","Basmati rice"),("leather-shoe-manufacturers-india","LEATHER","Leather shoes")]
tt = ''.join(f'<a class="guide-tile" href="/blog/{sl}/"><span>{c}</span><strong>{n}</strong><em>Supplier guide →</em></a>' for sl, c, n in tiles if f'/blog/{sl}/' not in t)
t = t.replace('<div class="guide-grid">', '<div class="guide-grid">' + tt, 1)
t = t.replace('<a href="/blog/import-from-india-to-netherlands/">Netherlands</a>', '<a href="/blog/import-from-india-to-netherlands/">Netherlands</a> <a href="/blog/import-from-india-to-spain/">Spain</a> <a href="/blog/import-from-india-to-france/">France</a> <a href="/blog/import-from-india-to-italy/">Italy</a>', 1)
t = t.replace('<a href="/sourcing-from-india-for-uae-buyers/">UAE</a></p>', '<a href="/sourcing-from-india-for-uae-buyers/">UAE</a> <a href="/blog/import-from-india-to-qatar/">Qatar</a></p>', 1)
t = t.replace('<a href="/blog/import-from-india-to-singapore/">Singapore</a>', '<a href="/blog/import-from-india-to-singapore/">Singapore</a> <a href="/blog/import-from-india-to-malaysia/">Malaysia</a>', 1)
for sl in ['spain','france','italy','qatar','malaysia']: assert f'import-from-india-to-{sl}/' in t, sl
f.write_text(t)

# sourcing / buying agent pages: country guide list
ctry = ''.join(f' · <a href="/blog/import-from-india-to-{sl}/">Importing to {n}</a>' for sl, n in [('spain','Spain'),('france','France'),('italy','Italy'),('qatar','Qatar'),('malaysia','Malaysia')])
for page in ['sourcing-agent-in-india', 'buying-agent-in-india']:
    f = SITE/page/'index.html'; t = f.read_text()
    if 'import-from-india-to-spain' in t: continue
    k = '<a href="/blog/import-from-india-to-new-zealand/">Importing to New Zealand</a>'
    assert k in t, page
    f.write_text(t.replace(k, k + ctry, 1))

n = 0
for f in SITE.rglob('*.html'):
    t = f.read_text(); o = t
    t = t.replace('?v=20261128b', '?v=20261128c')
    if t != o: f.write_text(t); n += 1
print('built', [b['slug'] for b in P.POSTS], 'cache-bust', n)

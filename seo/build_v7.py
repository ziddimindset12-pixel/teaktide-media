import re, json, html, sys, pathlib
sys.path.insert(0, '/home/claude/seo')
import posts_v7 as P
import build_posts_v2 as BP
SITE = pathlib.Path('/home/claude/site3')
strip = lambda s: html.unescape(re.sub('<[^>]+>', '', s)).strip()
AUTH = {"@type":"Person","name":"Ashu Dhakre","jobTitle":"Founder, Teak & Tide Sourcing","url":"https://about.me/ashudhakre","sameAs":["https://about.me/ashudhakre","https://www.quora.com/profile/Ashu-Dhakre","https://www.youtube.com/@teaktidesourcingagency"]}
OLD = '"author": {"@type": "Person", "name": "Ashu Dhakre", "jobTitle": "Founder, Teak & Tide Sourcing"}'

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
a.write_text(s)

n = 0
for f in SITE.rglob('*.html'):
    t = f.read_text(); o = t
    t = t.replace('?v=20261127a', '?v=20261128a')
    if t != o: f.write_text(t); n += 1
print('built', [b['slug'] for b in P.POSTS], 'cache-bust', n)

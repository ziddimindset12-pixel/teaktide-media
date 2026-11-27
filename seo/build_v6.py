import re, json, html, sys, pathlib, datetime, urllib.parse
sys.path.insert(0, '/home/claude/seo')
import pages_v6 as P
import build_posts_v2 as BP
SITE = pathlib.Path('/home/claude/site3'); BASE = 'https://teakandtidesourcing.com'
TPL = (SITE/'quality-inspection-india/index.html').read_text()
TODAY = datetime.date.today().isoformat()
e = lambda s: html.escape(s, quote=True)
def wa(t): return 'https://wa.me/917042367845?text=' + urllib.parse.quote('Hello Teak & Tide, ' + t)
strip = lambda s: html.unescape(re.sub('<[^>]+>', '', s)).strip()
AUTH={"@type":"Person","name":"Ashu Dhakre","jobTitle":"Founder, Teak & Tide Sourcing","url":"https://about.me/ashudhakre","sameAs":["https://about.me/ashudhakre","https://www.quora.com/profile/Ashu-Dhakre","https://www.youtube.com/@teaktidesourcingagency"]}

def build_page(p):
    url = f'{BASE}/{p["slug"]}/'
    h = TPL
    h = re.sub(r'<title>.*?</title>', f'<title>{e(p["seo_title"])}</title>', h, count=1)
    for k in ('name="description"', 'property="og:description"'):
        h = re.sub(r'<meta ' + k + r' content="[^"]*">', f'<meta {k} content="{e(p["desc"])}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{e(p["seo_title"])}">', h, count=1)
    h = h.replace(f'{BASE}/quality-inspection-india/', url).replace('window.PAGE_VIEW="lp-inspection"', f'window.PAGE_VIEW="{p["view"]}"')
    h = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "VideoObject".*?</script>', '', h, flags=re.S)
    qs = re.findall(r'<details><summary>(.*?)</summary><div class="ans"><p>(.*?)</p></div></details>', p["body"], re.S)
    faq = ''
    if qs:
        faq = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in qs]}, ensure_ascii=False, separators=(',',':')) + '</script>'
    h = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"FAQPage".*?</script>', lambda m: faq, h, count=1, flags=re.S)
    extra = []
    if p.get("terms"):
        extra.append({"@context":"https://schema.org","@type":"DefinedTermSet","name":p["h1"],"url":url,"hasDefinedTerm":[{"@type":"DefinedTerm","name":t,"description":d,"url":url+"#"+re.sub(r'[^a-z0-9]+','-',t.split(' (')[0].lower()).strip('-')} for t,d in p["terms"]]})
    if p["slug"]=="free-tools":
        extra.append({"@context":"https://schema.org","@type":"WebApplication","name":"Import calculators: CBM, landed cost, GSM","url":url,"applicationCategory":"BusinessApplication","operatingSystem":"Any","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"publisher":{"@type":"Organization","name":"Teak & Tide Sourcing"}})
    if p["slug"] not in ("free-tools","glossary"):
        extra.append({"@context":"https://schema.org","@type":"Article","headline":p["h1"],"description":p["desc"],"datePublished":TODAY,"dateModified":TODAY,"mainEntityOfPage":url,"author":AUTH,"publisher":{"@type":"Organization","name":"Teak & Tide Sourcing","logo":{"@type":"ImageObject","url":f"{BASE}/logo.webp"}}})
    if extra:
        h = h.replace('</head>', ''.join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False)+'</script>' for x in extra)+'</head>', 1)
    related = '<p style="margin-top:28px;font-size:15px"><strong>Related:</strong> <a href="/free-tools/">Free import calculators</a> · <a href="/glossary/">Sourcing glossary</a> · <a href="/how-it-works/">How it works</a> · <a href="/quality-inspection-india/">Quality inspection</a> · <a href="/supplier-verification-india/">Supplier verification</a> · <a href="/blog/">Buyer guides</a></p>'
    block = f'''<div data-view="{p["view"]}" class="on">
  <section class="page-head"><div class="wrap"><div class="crumb"><a href="/">Home</a> / {e(p["crumb"])}</div><span class="eyebrow">{e(p["eyebrow"])}</span><h1>{e(p["h1"])}</h1><p>{e(p["sub"])}</p></div></section>
  <section class="block"><div class="wrap article">
{p["body"]}
    <div class="cta-inline"><strong>Need help with an order from India?</strong><p>Tell us the product, quantity and destination. We reply within one business day.</p><div class="actions" style="margin-top:0"><a class="btn btn-green" href="/contact/">Get a quote</a><a class="btn btn-ghost" href="{wa(p["wa_text"])}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
    {related}
  </div></section>
</div>'''
    h = re.sub(r'<div data-view="lp-inspection" class="on">.*?\n</div>\n', lambda m: block + '\n', h, count=1, flags=re.S)
    if p.get("extra_foot"): h = h.replace('</body>', p["extra_foot"] + '</body>', 1)
    assert 'lp-inspection' not in h and 'VideoObject' not in h and h.count('<h1')==1, p["slug"]
    d = SITE/p["slug"]; d.mkdir(exist_ok=True); (d/'index.html').write_text(h)

for p in P.PAGES: build_page(p)
for b in P.BLOGS: BP.build(b)
BP.add_cards(P.BLOGS)
BP.add_sitemap([f'/{p["slug"]}/' for p in P.PAGES] + [f'/blog/{b["slug"]}/' for b in P.BLOGS])
old='"author": {"@type": "Person", "name": "Ashu Dhakre", "jobTitle": "Founder, Teak & Tide Sourcing"}'
for b in P.BLOGS:
    f=SITE/'blog'/b['slug']/'index.html'; s=f.read_text(); f.write_text(s.replace(old,'"author": '+json.dumps(AUTH,ensure_ascii=False)))

a = SITE/'assets/app.js'; s = a.read_text()
for p in P.PAGES:
    v=p["view"]
    if f'"{v}"' in s: continue
    s=s.replace('var PATHS = {',f'var PATHS = {{"{v}": "/{p["slug"]}/", ',1).replace('var VIEWS = [',f'var VIEWS = ["{v}", ',1)
    s=s.replace('var NAV = {',f'var NAV = {{ "{v}": "", ',1).replace('var TITLES = {',f'var TITLES = {{ "{v}": {json.dumps(p["seo_title"])}, ',1)
for b in P.BLOGS:
    v=b["view"]
    if f'"{v}"' in s: continue
    s=s.replace('var PATHS = {',f'var PATHS = {{"{v}": "/blog/{b["slug"]}/", ',1).replace('var VIEWS = [',f'var VIEWS = ["{v}", ',1)
    s=s.replace('var NAV = {',f'var NAV = {{ "{v}": "blog", ',1).replace('var TITLES = {',f'var TITLES = {{ "{v}": {json.dumps(b["seo_title"])}, ',1)
    s=s.replace('var POSTS = [\n',f'var POSTS = [\n  {{ id: "{v}", tag: "{b["tag"]}", title: {json.dumps(b["title"])}, text: {json.dumps(b["card"])}, mins: {b["mins"]} }},\n',1)
a.write_text(s)

# footer links on every page
A1='<li><a href="/blog/">Blog</a></li>'; N1=A1+'<li><a href="/free-tools/">Free import calculators</a></li><li><a href="/glossary/">Sourcing glossary</a></li>'
A2='<li><a href="/private-label-manufacturing-india/">Private label manufacturing</a></li></ul>'
N2='<li><a href="/private-label-manufacturing-india/">Private label manufacturing</a></li><li><a href="/amazon-fba-prep-india/">Amazon FBA prep</a></li><li><a href="/ddp-shipping-from-india/">DDP shipping from India</a></li><li><a href="/ethical-sourcing-india/">Ethical sourcing</a></li></ul>'
n=0
for f in SITE.rglob('*.html'):
    t=f.read_text(); o=t
    if '/free-tools/">Free import' not in t: t=t.replace(A1,N1,1)
    if '/amazon-fba-prep-india/">Amazon' not in t: t=t.replace(A2,N2,1)
    t=re.sub(r'\?v=20261123b', '?v=20261127a', t)
    if t!=o: f.write_text(t); n+=1
print('pages',[p['slug'] for p in P.PAGES],'blogs',[b['slug'] for b in P.BLOGS],'footer updated',n, 'terms',len(P.G))

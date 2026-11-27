import re, json, html, sys, urllib.parse, pathlib, datetime
sys.path.insert(0, '/home/claude/seo')
from landing_v2 import PAGES
SITE = pathlib.Path('/home/claude/site3')
BASE = 'https://teakandtidesourcing.com'
TPL_PATH = 'quality-inspection-india'
TPL = (SITE / TPL_PATH / 'index.html').read_text()
TODAY = datetime.date.today().isoformat()
e = lambda s: html.escape(s, quote=True)

def wa(t):
    return 'https://wa.me/917042367845?text=' + urllib.parse.quote('Hello Teak & Tide, ' + t)

def faq_schema(body):
    qs = re.findall(r'<details><summary>(.*?)</summary><div class="ans"><p>(.*?)</p></div></details>', body, re.S)
    strip = lambda s: html.unescape(re.sub('<[^>]+>', '', s)).strip()
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qs]}

def set_head(h, p, old_url, old_view):
    url = f'{BASE}/{p["slug"]}/'
    h = re.sub(r'<title>.*?</title>', f'<title>{e(p["seo_title"])}</title>', h, count=1)
    for k in ('name="description"', 'property="og:description"'):
        h = re.sub(r'<meta ' + k + r' content="[^"]*">', f'<meta {k} content="{e(p["desc"])}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{e(p["seo_title"])}">', h, count=1)
    h = h.replace(old_url, url).replace(f'window.PAGE_VIEW="{old_view}"', f'window.PAGE_VIEW="{p["view"]}"')
    return h

def replace_faq_schema(h, body):
    return re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema.org","@type":"FAQPage".*?</script>',
                  '<script type="application/ld+json">' + json.dumps(faq_schema(body), ensure_ascii=False, separators=(',', ':')) + '</script>', h, count=1, flags=re.S)

related = re.search(r'<p style="margin-top:28px;font-size:15px"><strong>Related:</strong>.*?</p>', TPL).group(0)

def build_new(p):
    h = set_head(TPL, p, f'{BASE}/{TPL_PATH}/', 'lp-inspection')
    block = f'''<div data-view="{p["view"]}" class="on">
  <section class="page-head"><div class="wrap"><div class="crumb"><a href="/">Home</a> / {e(p["crumb"])}</div><span class="eyebrow">{e(p["eyebrow"])}</span><h1>{e(p["h1"])}</h1><p>{e(p["sub"])}</p></div></section>
  <section class="block"><div class="wrap article">
{p["body"]}
    <div class="cta-inline"><strong>Send us your requirement</strong><p>Tell us the product, quantity and destination. We reply within one business day.</p><div class="actions" style="margin-top:0"><a class="btn btn-green" href="/contact/">Get a quote</a><a class="btn btn-ghost" href="{wa(p["wa_text"])}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
    {related}
  </div></section>
</div>'''
    h = re.sub(r'<div data-view="lp-inspection" class="on">.*?\n</div>\n', block + '\n', h, count=1, flags=re.S)
    h = replace_faq_schema(h, p["body"])
    assert 'lp-inspection' not in h and 'VideoObject' not in h, p["slug"]
    d = SITE / p["slug"]; d.mkdir(exist_ok=True); (d / 'index.html').write_text(h)

def upgrade_verification(p):
    path = SITE / 'supplier-verification-india/index.html'
    h = path.read_text()
    h = re.sub(r'<title>.*?</title>', f'<title>{e(p["seo_title"])}</title>', h, count=1)
    for k in ('name="description"', 'property="og:description"'):
        h = re.sub(r'<meta ' + k + r' content="[^"]*">', f'<meta {k} content="{e(p["desc"])}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{e(p["seo_title"])}">', h, count=1)
    h = h.replace('<h1>Supplier verification in India</h1>', '<h1>Supplier verification &amp; background check in India</h1>', 1)
    new = p["body"][p["body"].index('<h2>What we check</h2>'):]
    a = h.index('<h2>What we check</h2>'); b = h.index('<div class="cta-inline">', a)
    h = h[:a] + new.strip() + '\n\n    ' + h[b:]
    h = replace_faq_schema(h, new)
    path.write_text(h)

def add_footer_links():
    old = '<li><a href="/quality-inspection-india/">Quality inspection India</a></li></ul>'
    new = '<li><a href="/quality-inspection-india/">Quality inspection India</a></li><li><a href="/low-moq-sourcing-india/">Low MOQ sourcing</a></li><li><a href="/private-label-manufacturing-india/">Private label manufacturing</a></li></ul>'
    n = 0
    for f in SITE.rglob('*.html'):
        s = f.read_text()
        if old in s and '/low-moq-sourcing-india/">Low MOQ' not in s:
            f.write_text(s.replace(old, new)); n += 1
    rel_old = '<a href="/supplier-verification-india/">Supplier verification India</a> · '
    rel_new = rel_old + '<a href="/low-moq-sourcing-india/">Low MOQ sourcing</a> · <a href="/private-label-manufacturing-india/">Private label &amp; OEM</a> · '
    m = 0
    for f in SITE.rglob('*.html'):
        s = f.read_text()
        if rel_old in s and '/low-moq-sourcing-india/">Low MOQ sourcing</a> · ' not in s:
            f.write_text(s.replace(rel_old, rel_new, 1)); m += 1
    return n, m

for p in PAGES:
    if p["slug"] == 'supplier-background-check-india':
        upgrade_verification(p)
    else:
        build_new(p)
print('footer/related updated:', add_footer_links())
sp = SITE / 'sitemap.xml'; s = sp.read_text()
for slug in ('low-moq-sourcing-india', 'private-label-manufacturing-india'):
    loc = f'{BASE}/{slug}/'
    if loc not in s:
        s = s.replace('</urlset>', f'<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>')
s = re.sub(r'(<loc>https://teakandtidesourcing.com/supplier-verification-india/</loc><lastmod>)[^<]*', r'\g<1>' + TODAY, s)
sp.write_text(s)
print('ok')

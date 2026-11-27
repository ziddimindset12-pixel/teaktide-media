import re, json, html, sys, urllib.parse, pathlib, datetime
sys.path.insert(0, '/home/claude/seo')
import importlib
SITE = pathlib.Path('/home/claude/site3')
BASE = 'https://teakandtidesourcing.com'
TPL = (SITE / 'blog/how-to-import-makhana-from-india/index.html').read_text()
TODAY = datetime.date.today().isoformat()

def wa(t):
    return 'https://wa.me/917042367845?text=' + urllib.parse.quote('Hello Teak & Tide, ' + t)

def build(p):
    e = lambda s: html.escape(s, quote=True)
    url = f'{BASE}/blog/{p["slug"]}/'
    h = TPL
    h = re.sub(r'<title>.*?</title>', f'<title>{e(p["seo_title"])}</title>', h, 1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{e(p["desc"])}">', h, 1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{e(p["seo_title"])}">', h, 1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{e(p["desc"])}">', h, 1)
    h = re.sub(r'<meta property="og:type" content="[^"]*">', '<meta property="og:type" content="article">', h, 1)
    h = h.replace(f'{BASE}/blog/how-to-import-makhana-from-india/', url)
    h = h.replace('window.PAGE_VIEW="blog-import-makhana"', f'window.PAGE_VIEW="{p["view"]}"')
    art = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["desc"],
           "datePublished": TODAY, "dateModified": TODAY, "mainEntityOfPage": url, "image": f"{BASE}/og-image.png",
           "author": {"@type": "Person", "name": "Ashu Dhakre", "jobTitle": "Founder, Teak & Tide Sourcing"},
           "publisher": {"@type": "Organization", "name": "Teak & Tide Sourcing", "logo": {"@type": "ImageObject", "url": f"{BASE}/logo.webp"}}}
    h = h.replace('</head>', '<script type="application/ld+json">' + json.dumps(art, ensure_ascii=False) + '</script></head>', 1)
    block = f'''<div data-view="{p["view"]}" class="on">
  <section class="page-head"><div class="wrap"><div class="crumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / {e(p["crumb"])}</div><span class="eyebrow">{e(p["eyebrow"])}</span><h1>{e(p["title"])}</h1><p>{e(p["sub"])}</p></div></section>
  <section class="block"><div class="wrap article">
    <p class="post-meta">{p["mins"]} MIN READ · {p["tag"]} · By Ashu Dhakre</p>
{p["body"]}
    <div class="cta-inline"><strong>{e(p["cta_t"])}</strong><p>{e(p["cta_p"])}</p><div class="actions" style="margin-top:0"><a class="btn btn-green" href="{p["cat_href"]}">{e(p["cat_label"])}</a><a class="btn btn-ghost" href="{wa(p["wa_text"])}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
  </div></section>
</div>'''
    h = re.sub(r'<div data-view="blog-import-makhana" class="on">.*?\n</div>\n', block + '\n', h, 1, flags=re.S)
    assert f"data-view=\"{p['view']}\"" in h and "blog-import-makhana" not in h, p["slug"]
    d = SITE / 'blog' / p["slug"]; d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(h)

def add_cards(posts):
    ip = SITE / 'blog/index.html'; s = ip.read_text()
    cards = ''
    for p in posts:
        href = f'/blog/{p["slug"]}/'
        if href in s: continue
        cards += f'<a class="card" href="{href}"><span class="tag">{p["tag"]} · {p["mins"]} MIN READ</span><h3>{html.escape(p["title"])}</h3><p>{html.escape(p["card"])}</p></a>'
    s = s.replace('<div class="posts" id="post-list">', '<div class="posts" id="post-list">' + cards, 1)
    ip.write_text(s)

def add_sitemap(paths):
    sp = SITE / 'sitemap.xml'; s = sp.read_text()
    for path in paths:
        loc = f'{BASE}{path}'
        if f'<loc>{loc}</loc>' in s: continue
        s = s.replace('</urlset>', f'<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>')
    sp.write_text(s)

if __name__ == '__main__':
    mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'posts_v2')
    for p in mod.POSTS: build(p)
    add_cards(mod.POSTS)
    add_sitemap([f'/blog/{p["slug"]}/' for p in mod.POSTS])
    print('built', [p['slug'] for p in mod.POSTS])

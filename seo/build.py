import base64, re, json, os, shutil
SITE='https://teakandtidesourcing.netlify.app'
s=open('/home/claude/tt-src.html').read()
L='data:image/webp;base64,'+base64.b64encode(open('/home/claude/logo-l.webp','rb').read()).decode()
S='data:image/webp;base64,'+base64.b64encode(open('/home/claude/logo-s.webp','rb').read()).decode()
s=s.replace('{{LOGO_L}}',L).replace('{{LOGO_S}}',S).replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
PATHS={"home":"/","services":"/services/","products":"/products/","process":"/how-it-works/","about":"/about/","case-study":"/case-study/","faq":"/faq/","contact":"/contact/","privacy":"/privacy-policy/","terms":"/terms/","blog":"/blog/",
"blog-import-spices":"/blog/how-to-import-spices-from-india/","blog-choose-sourcing-agent":"/blog/how-to-choose-a-sourcing-agent-in-india/","blog-private-label-leather":"/blog/private-label-leather-goods-india/","blog-import-makhana":"/blog/how-to-import-makhana-from-india/","blog-cashew-grades":"/blog/cashew-grades-w180-w240-w320/","blog-ashwagandha-supplier":"/blog/ashwagandha-supplier-india/","blog-brass-handicrafts-moradabad":"/blog/brass-handicrafts-moradabad/","blog-india-vs-china-sourcing":"/blog/sourcing-from-india-vs-china/","lp-sourcing-agent":"/sourcing-agent-in-india/","lp-buying-agent":"/buying-agent-in-india/","lp-purchasing-agent":"/purchasing-agent-in-india/","lp-procurement":"/procurement-services-india/","lp-delhi":"/sourcing-agency-delhi/","lp-trusted":"/trusted-sourcing-agent-india/","lp-export-sourcing":"/export-sourcing-agent-india/","lp-product-sourcing":"/product-sourcing-india/","lp-supplier-verification":"/supplier-verification-india/","lp-inspection":"/quality-inspection-india/","lp-usa":"/sourcing-from-india-for-usa-buyers/","lp-uk":"/sourcing-from-india-for-uk-buyers/","lp-europe":"/sourcing-from-india-for-european-buyers/","lp-australia":"/sourcing-from-india-for-australian-buyers/","lp-uae":"/sourcing-from-india-for-uae-buyers/",
"agriculture":"/agricultural-products/","spices":"/spices/","dryfruits":"/dry-fruits/","herbs":"/herbs/","leather":"/leather-goods/","handicrafts":"/handicrafts/","textiles":"/textiles/"}
# ---- JS patches (null-safe + path aware) ----
def R(a,b):
    global s
    assert a in s, a[:60]; s=s.replace(a,b,1)
R('document.getElementById("home-cats").innerHTML = CATS.map(catCard).join("") + OTHER;','function setHTML(id, h) { var e = document.getElementById(id); if (e) e.innerHTML = h; }\nvar PATHS = '+json.dumps(PATHS)+';\nfunction pathFix(root) { (root || document).querySelectorAll(\'a[href^="#"]\').forEach(function (a) { var k = a.getAttribute("href").slice(1); if (PATHS[k]) a.setAttribute("href", PATHS[k]); }); }\nsetHTML("home-cats", CATS.map(catCard).join("") + OTHER);')
R('document.getElementById("all-cats").innerHTML = CATS.map(catCard).join("") + OTHER;','setHTML("all-cats", CATS.map(catCard).join("") + OTHER);')
R('document.getElementById("foot-cats").innerHTML = CATS.map(function (c) { return \'<li><a href="#\' + c.id + \'">\' + esc(c.name) + \'</a></li>\'; }).join("");','setHTML("foot-cats", CATS.map(function (c) { return \'<li><a href="#\' + c.id + \'">\' + esc(c.name) + \'</a></li>\'; }).join(""));')
R('document.getElementById("post-list").innerHTML = POSTS.map(','var _pl = document.getElementById("post-list"); if (_pl) _pl.innerHTML = POSTS.map(')
R('  var h = (location.hash || "#home").slice(1);','  var h = location.hash ? location.hash.slice(1) : (window.PAGE_VIEW || "home");')
R('    if (a.getAttribute("href") === "#" + cur)','    if (a.getAttribute("href") === "#" + cur || a.getAttribute("href") === PATHS[cur])')
R('document.getElementById("reg-grid").innerHTML = filled.map(','setHTML("reg-grid", "") ; document.getElementById("reg-grid") && (document.getElementById("reg-grid").innerHTML = filled.map(')
# close the paren for reg-grid statement: find the join after it
i=s.index('document.getElementById("reg-grid").innerHTML = filled.map(')
j=s.index('}).join("");',i)
s=s[:j]+'}).join(""));'+s[j+len('}).join("");'):]
R('document.getElementById("testi-grid").innerHTML = TESTIMONIALS.map(','setHTML("testi-grid", TESTIMONIALS.map(')
i=s.index('setHTML("testi-grid", TESTIMONIALS.map(')
j=s.index('}).join("");',i)
s=s[:j]+'}).join(""));'+s[j+len('}).join("");'):]
R('document.getElementById("quote").addEventListener("submit"','(document.getElementById("quote") || document.createElement("form")).addEventListener("submit"')
R("closest('a[href=\"' + PDF_NAME + '\"]')","closest('a[href$=\"' + PDF_NAME + '\"]')")
# path fix after each route render
R('  window.scrollTo(0, 0);\n}','  pathFix();\n  window.scrollTo(0, 0);\n}')
# absolute asset refs
s=s.replace('href="Teak-and-Tide-Company-Profile.pdf"','href="/Teak-and-Tide-Company-Profile.pdf"')
s=s.replace('"sameAs":','"url":"'+SITE+'/","logo":"'+SITE+'/logo.webp","sameAs":')
i=s.index('</style>')+len('</style>')
head,body=s[:i],s[i:]
doc='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="google-site-verification" content="qdfq5eYwdat5sHlNmLMkIqszqVobfrAHOZxo_WeX-tw">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<link rel="icon" type="image/webp" href="/favicon.webp">\n'+head+'\n<style>html{padding:env(safe-area-inset-top,0) 0 env(safe-area-inset-bottom,0)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
os.makedirs('/home/claude/seo',exist_ok=True)
open('/home/claude/seo/master.html','w').write(doc)
json.dump(PATHS,open('/home/claude/seo/paths.json','w'))
print('ok')

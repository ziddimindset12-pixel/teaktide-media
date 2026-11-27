import json, os, shutil, datetime
from playwright.sync_api import sync_playwright
SITE='https://teakandtidesourcing.netlify.app'
PATHS=json.load(open('/home/claude/seo/paths.json'))
META={
"home":("Sourcing Agent in India for Overseas Buyers | Teak & Tide Sourcing","Delhi NCR sourcing agent for overseas buyers. We find the right Indian suppliers for spices, dry fruits, herbs, agri products, leather and handicrafts."),
"services":("Sourcing Services in India: Search, Negotiation, QC | Teak & Tide","Supplier search, price negotiation, samples, production follow-up, AQL quality inspection and export support for buyers sourcing from India."),
"products":("Products We Source from India | Teak & Tide Sourcing","India's top export categories sourced to your requirement: spices, agri products, dry fruits, herbs, leather goods, handicrafts and textiles."),
"process":("How Sourcing from India Works: 6 Steps | Teak & Tide Sourcing","From requirement and supplier search to samples, production, quality inspection and shipping. Trade terms EXW, FOB, CIF and DDP explained."),
"about":("About Teak & Tide Sourcing | Buying Agent in Delhi NCR, India","Teak & Tide Sourcing is a buying agency in Delhi NCR helping overseas brands and importers buy from Indian suppliers safely. Founder: Ashu Dhakre."),
"case-study":("Example Case Study: Sourcing Brass Lamps from India | Teak & Tide","An illustrative example of how a first order runs with a sourcing agent in India, from supplier shortlist to inspection and shipment."),
"faq":("Sourcing Agent India FAQ: Fees, MOQ, Samples | Teak & Tide","Answers to common questions about working with a sourcing agent in India: fees, commitment fee, MOQ, samples, payment, quality inspection and shipping."),
"contact":("Get a Quote: Sourcing from India | Teak & Tide Sourcing","Send your sourcing requirement and get a reply within one business day. WhatsApp +91 70423 67845. Based in Delhi NCR, India."),
"privacy":("Privacy Policy | Teak & Tide Sourcing","How Teak & Tide Sourcing collects, uses and protects your information."),
"terms":("Terms & Conditions | Teak & Tide Sourcing","The terms on which Teak & Tide Sourcing provides sourcing agent services, including the commitment fee and service fee."),
"blog":("Buyer Guides: Importing from India | Teak & Tide Sourcing","Practical guides for importers, brands and traders sourcing spices, leather goods and more from Indian suppliers."),
"blog-import-spices":("How to Import Spices from India Safely (Buyer Guide) | Teak & Tide","Specifications, food-safety limits, Spices Board and FSSAI checks, samples, lab reports and inspection before your first spice order from India."),
"blog-choose-sourcing-agent":("How to Choose a Sourcing Agent in India: 7 Questions | Teak & Tide","Seven questions to ask before hiring a sourcing agent in India: who pays the agent, fixed suppliers, quality checks, fees and registrations."),
"blog-private-label-leather":("Private Label Leather Goods Manufacturing in India | Teak & Tide","How to make bags, wallets, belts and footwear under your own brand in India: design pack, manufacturers, samples, branding and compliance."),
"lp-sourcing-agent":("Sourcing Agent in India for Overseas Buyers | Teak & Tide","Independent sourcing agent in India. We search fresh suppliers for your product, negotiate, check samples, inspect quality and manage shipping."),
"lp-buying-agent":("Buying Agent in India for Importers and Brands | Teak & Tide","Buying agent in India who represents the buyer, not the seller. Supplier search, negotiation, samples, AQL inspection and export support from Delhi NCR."),
"lp-purchasing-agent":("Purchasing Agent in India for Overseas Buyers | Teak & Tide","Need a purchasing agent in India? We handle supplier search, purchase negotiation, order follow-up, quality checks and shipping for overseas buyers."),
"lp-procurement":("Procurement Services in India for Overseas Buyers | Teak & Tide","Outsourced procurement services in India: supplier discovery, RFQs, negotiation, quality control and logistics coordination for importers and brands."),
"lp-delhi":("Sourcing Agency in Delhi NCR, India | Teak & Tide Sourcing","Sourcing agency based in Delhi NCR. Close to the manufacturing hubs of North India: Moradabad, Agra, Kanpur, Panipat, Jaipur and Khari Baoli markets."),
"lp-trusted":("How to Find a Trusted Sourcing Agent in India | Teak & Tide","Signs of a trustworthy sourcing agent in India, red flags to avoid, and the safeguards we use so your money and quality are protected."),
"lp-export-sourcing":("Export Sourcing Agent in India: From Factory to Port | Teak & Tide","Export sourcing agent in India who manages suppliers, quality, export packing, documents and freight so your goods arrive as ordered."),
"lp-product-sourcing":("Product Sourcing Services in India for Brands | Teak & Tide","Product sourcing services in India for brands and e-commerce sellers: private label, custom packaging, samples, MOQ negotiation and quality checks."),
"lp-supplier-verification":("Supplier Verification and Factory Checks in India | Teak & Tide","Check an Indian supplier before you pay: registration checks, factory visits or video audits, capacity, export history and sample review."),
"lp-inspection":("Pre-Shipment Quality Inspection in India (AQL) | Teak & Tide","Pre-shipment and during-production quality inspection in India using AQL sampling, with photo reports before you pay the balance."),
"lp-usa":("Sourcing from India for US Buyers | Teak & Tide Sourcing","A sourcing agent in India for US importers, brands and Amazon sellers: suppliers, quality checks, FDA-related food requirements and shipping to the USA."),
"lp-uk":("Sourcing from India for UK Buyers | Teak & Tide Sourcing","Sourcing agent in India for UK importers and brands: supplier search, quality inspection, UK food and product rules, and shipping from India to the UK."),
"lp-europe":("Sourcing from India for EU Buyers | Teak & Tide Sourcing","Sourcing agent in India for buyers in Germany, France, the Netherlands and across the EU: suppliers, EU compliance checks and shipping from India."),
"lp-australia":("Sourcing from India for Australian Buyers | Teak & Tide","Sourcing agent in India for Australian importers: suppliers, quality checks, biosecurity requirements for food and wood products, and shipping to Australia."),
"lp-uae":("Sourcing from India for UAE and Gulf Buyers | Teak & Tide","Sourcing agent in India for buyers in the UAE, Saudi Arabia and the Gulf: rice, spices, dry fruits, textiles, decor and fast shipping from India."),
"blog-import-makhana":("How to Import Makhana (Fox Nuts) from India | Teak & Tide","Makhana grades, moisture and quality checks, FSSAI and APEDA suppliers, packing and shipping. A buyer guide to importing fox nuts from India."),
"blog-cashew-grades":("Cashew Grades Explained: W180, W240, W320 | Teak & Tide","What cashew kernel grades W180, W210, W240, W320, W450, SW, splits and pieces mean, and how to compare cashew quotes from Indian processors."),
"blog-ashwagandha-supplier":("Ashwagandha Supplier India: Root, Powder, Extract | Teak & Tide","How to buy ashwagandha from India: root, powder or extract, withanolide content, heavy metal and microbial tests, COA and supplier checks."),
"blog-brass-handicrafts-moradabad":("Brass Handicrafts from Moradabad, India: Buyer Guide | Teak & Tide","How to source brass decor, lamps and tableware from Moradabad: solid vs plated brass, finishes, food-contact safety, quality checks and packing."),
"blog-india-vs-china-sourcing":("Sourcing from India vs China: A Buyer Guide | Teak & Tide","An honest comparison of sourcing from India and China: product strengths, MOQs, finding factories, quality control and import duties."),
"agriculture":("Agricultural Products from India: Rice, Pulses | Teak & Tide","Source basmati rice, wheat, pulses, groundnuts and more from India to your grade and packing. APEDA-registered exporters, inspection and fumigation."),
"spices":("Spice Sourcing Agent in India: Turmeric, Chilli | Teak & Tide","Source every type of spice from India: turmeric, red chilli, cumin, black pepper, cardamom and blends. Spices Board and FSSAI suppliers, lab-tested."),
"dryfruits":("Dry Fruits Supplier India: Cashew, Makhana | Teak & Tide","Source Indian cashew kernels (W180–W320), makhana, raisins, walnuts, almonds and dates. APEDA and FSSAI processors, graded and inspected."),
"herbs":("Ayurvedic Herbs Supplier India: Ashwagandha | Teak & Tide","Source ashwagandha, moringa, tulsi, neem and other herbs from India as leaves, roots, powders or extracts, with lab tests for your market."),
"leather":("Private Label Leather Goods Manufacturer India | Teak & Tide","Leather bags, wallets, belts and footwear made to your design and brand by manufacturers in Kanpur, Agra and Chennai."),
"handicrafts":("Indian Handicrafts Sourcing: Brass, Wood, Marble | Teak & Tide","Source handmade brass, wood, marble and pottery from India's craft cities to your design, with quality checks and export packing."),
"textiles":("Textiles and Apparel Sourcing from India | Teak & Tide Sourcing","Source garments, knitwear, home textiles and rugs from Tiruppur, Delhi NCR, Panipat and Bhadohi, to your design and certifications."),
}
out='/home/claude/site2'
shutil.rmtree(out,ignore_errors=True); os.makedirs(out)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1280,'height':900}); errs=[]
    pg.on('pageerror',lambda e: errs.append(str(e)))
    pg.route('**/*', lambda r: r.abort() if r.request.url.startswith('http') else r.continue_())
    for view,path in PATHS.items():
        pg.goto('about:blank'); pg.goto('file:///home/claude/seo/master.html#'+view); pg.wait_for_timeout(250)
        t,d=META[view]; url=SITE+path
        html=pg.evaluate("""([view,t,d,url])=>{
          document.querySelectorAll('[data-view]').forEach(el=>{ if(!el.classList.contains('on')) el.remove(); });
          document.querySelectorAll('script[src*="translate.google"], #goog-gt-tt, .skiptranslate, iframe').forEach(e=>e.remove());
          document.title=t;
          const set=(sel,attr,val,make)=>{let e=document.head.querySelector(sel); if(!e){e=document.createElement(make[0]); for(const [k,v] of Object.entries(make[1])) e.setAttribute(k,v); document.head.appendChild(e);} e.setAttribute(attr,val);};
          set('meta[name="description"]','content',d,['meta',{name:'description'}]);
          set('meta[property="og:title"]','content',t,['meta',{property:'og:title'}]);
          set('meta[property="og:description"]','content',d,['meta',{property:'og:description'}]);
          set('meta[property="og:url"]','content',url,['meta',{property:'og:url'}]);
          set('meta[property="og:image"]','content','https://teakandtidesourcing.netlify.app/og-image.png',['meta',{property:'og:image'}]);
          set('link[rel="canonical"]','href',url,['link',{rel:'canonical'}]);
          const pv=document.createElement('script'); pv.textContent='window.PAGE_VIEW='+JSON.stringify(view)+';';
          document.head.appendChild(pv);
          document.documentElement.removeAttribute('dir');
          const qs=[...document.querySelectorAll('[data-view].on details')].map(d=>({"@type":"Question","name":d.querySelector('summary').textContent.trim(),"acceptedAnswer":{"@type":"Answer","text":(d.querySelector('.ans')||d).textContent.trim()}})).filter(x=>x.name&&x.acceptedAnswer.text);
          if(qs.length){const sc=document.createElement('script');sc.type='application/ld+json';sc.textContent=JSON.stringify({"@context":"https://schema.org","@type":"FAQPage","mainEntity":qs});document.head.appendChild(sc);}
          return '<!doctype html>\\n'+document.documentElement.outerHTML;
        }""",[view,t,d,url])
        dest=os.path.join(out,path.strip('/'),'index.html') if path!='/' else os.path.join(out,'index.html')
        os.makedirs(os.path.dirname(dest),exist_ok=True); open(dest,'w').write(html)
    print('errors',errs); b.close()
today=datetime.date(2026,11,16).isoformat()
prio={"home":"1.0","services":"0.9","products":"0.9","spices":"0.8","dryfruits":"0.8","agriculture":"0.8","herbs":"0.8","leather":"0.8","handicrafts":"0.8","textiles":"0.8","contact":"0.8","blog":"0.7"}
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{p}</loc><lastmod>{today}</lastmod><priority>{prio.get(v,"0.6")}</priority></url>\n' for v,p in PATHS.items())+'</urlset>\n'
open(out+'/sitemap.xml','w').write(sm)
open(out+'/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(out+'/404.html','w').write(open(out+'/index.html').read())

import json, urllib.parse
P='/home/claude/tt-src.html'
s=open(P).read()

def wa(t): return 'https://wa.me/917042367845?text='+urllib.parse.quote('Hello Teak & Tide, '+t)

PAGES=[]  # (id, path, nav_label, seo_title, seo_desc, eyebrow, h1, sub, body_html, wa_text)

def faq(items):
    return '\n    <h2>Frequently asked questions</h2>\n'+''.join(f'    <details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>\n' for q,a in items)

def ul(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'

PAGES.append(("lp-sourcing-agent","/sourcing-agent-in-india/","Sourcing agent in India",
"Sourcing Agent in India for Overseas Buyers | Teak & Tide",
"Independent sourcing agent in India. We search fresh suppliers for your product, negotiate, check samples, inspect quality and manage shipping.",
"Sourcing agent · India","Sourcing agent in India, working for you","An independent sourcing agent in Delhi NCR for importers, brands and retailers who want to buy from India safely.",f'''
    <p>A sourcing agent is your team on the ground. Instead of searching directories, chasing replies and travelling to India, you tell us what you need and we do the work: find the right manufacturers, compare quotes, negotiate, check samples, follow production and inspect the goods before they ship.</p>
    <h2>What makes us different</h2>
    {ul(["<strong>Not tied to any supplier.</strong> We search fresh suppliers for every requirement instead of pushing the same few factories.",
         "<strong>Paid by you, not by suppliers.</strong> Our only job is to get you the right quality at the right price.",
         "<strong>You know every supplier.</strong> Names and details are shared with you, and you pay the supplier directly.",
         "<strong>Local language, local knowledge.</strong> We negotiate in Hindi and know India's manufacturing clusters."])}
    <h2>What we source</h2>
    <p>Spices, dry fruits and nuts, Ayurvedic herbs, rice, pulses and grains, leather goods made to your brand, handicrafts in brass, wood, marble and pottery, and textiles. Need something else? Ask us.</p>
    <h2>How it works</h2>
    {ul(["Share your requirement: product, quantity, specification, destination and target price.",
         "We search and verify suppliers and send you a comparison of quotes, usually within 7–10 days.",
         "Samples are checked by us and sent to you for approval.",
         "We follow production with regular photo updates and inspect before shipment.",
         "We coordinate export documents and freight on EXW, FOB, CIF or DDP terms."])}
''' + faq([("How much does a sourcing agent in India cost?","Our service fee starts from 3% of order value and is agreed in writing before you order. A small commitment fee of USD 100–200 starts the project and is fully adjusted against the service fee."),
           ("Do I pay the supplier or the agent?","You pay the supplier directly. Your order money never comes to us."),
           ("How long does it take to get quotes?","Usually 7–10 days after we receive your full requirement, depending on the product.")]),
"I am looking for a sourcing agent in India."))

PAGES.append(("lp-buying-agent","/buying-agent-in-india/","Buying agent in India",
"Buying Agent in India for Importers and Brands | Teak & Tide",
"Buying agent in India who represents the buyer, not the seller. Supplier search, negotiation, samples, AQL inspection and export support from Delhi NCR.",
"Buying agent · India","A buying agent in India who sits on your side of the table","Buying agents represent the buyer. Here is what that means and how we work for you.",f'''
    <p>A buying agent (or buying house) acts for the buyer in dealings with manufacturers. The key word is <em>for</em>: a buying agent should negotiate in your interest, protect your quality standards and tell you the truth about suppliers, even when that is not what a factory wants to hear.</p>
    <h2>Buying agent vs trader vs manufacturer</h2>
    {ul(["<strong>Manufacturer:</strong> makes the product and sells its own capacity.",
         "<strong>Trader:</strong> buys from manufacturers and resells at a margin. You often don't know who made your goods.",
         "<strong>Buying agent:</strong> finds and manages manufacturers for you, for a service fee. You know the supplier and pay them directly."])}
    <h2>What our buying agent service covers</h2>
    {ul(["Supplier search and verification for your exact product",
         "Price negotiation and comparison of at least two or three quotes where possible",
         "Sample development and approval",
         "Production follow-up with photo updates",
         "AQL quality inspection before you pay the balance",
         "Export documents and freight coordination"])}
    <h2>Who we work with</h2>
    <p>Importers, wholesalers, retailers, Amazon and e-commerce sellers, and brands making private-label products in spices, dry fruits, herbs, agri products, leather goods, handicrafts and textiles.</p>
''' + faq([("Does a buying agent take commission from suppliers?","We do not. We are paid only by the buyer, so our interest is the same as yours."),
           ("Can you work with small trial orders?","Yes. Many Indian manufacturers accept smaller first orders, and we help you find them."),
           ("Where are you based?","Delhi NCR, India, with suppliers across India's manufacturing clusters.")]),
"I need a buying agent in India."))

PAGES.append(("lp-purchasing-agent","/purchasing-agent-in-india/","Purchasing agent in India",
"Purchasing Agent in India: Supplier Search to Shipment | Teak & Tide",
"Need a purchasing agent in India? We handle supplier search, purchase negotiation, order follow-up, quality checks and shipping for overseas buyers.",
"Purchasing agent · India","Purchasing agent in India for overseas companies","We manage your purchases from Indian suppliers, from the first quote to the final shipment.",f'''
    <p>A purchasing agent handles the buying process on your behalf. For overseas companies without staff in India, this removes the hardest parts of buying from a new country: finding reliable suppliers, communicating clearly, following orders and checking quality before goods leave the factory.</p>
    <h2>Your purchase, step by step</h2>
    {ul(["<strong>Requirement:</strong> we turn your needs into a clear written specification suppliers can quote on.",
         "<strong>Quotes:</strong> we collect and compare quotes on the same basis, including price, MOQ, lead time and payment terms.",
         "<strong>Purchase order:</strong> we help you agree a PO that includes specifications, packing, labelling, inspection and delivery terms.",
         "<strong>Follow-up:</strong> we track production and raise issues early.",
         "<strong>Inspection and shipping:</strong> we inspect before shipment and coordinate documents and freight."])}
    <h2>Why use a purchasing agent instead of buying direct?</h2>
    <p>Buying direct can work once you know a supplier well. For new products or new suppliers, an agent on the ground reduces the risk of wrong specifications, delays and quality problems, and usually saves more than the fee through better prices and fewer mistakes.</p>
''' + faq([("Can you handle repeat purchases?","Yes. Once a supplier is approved, we can manage repeat orders, follow-up and inspection for each shipment."),
           ("Which payment terms are common in India?","Many suppliers ask for an advance with the balance before shipment. We recommend paying the balance only after a satisfactory inspection."),
           ("Do you issue the purchase order?","You issue the PO to the supplier in your company's name. We help you prepare it.")]),
"I need a purchasing agent in India."))

PAGES.append(("lp-procurement","/procurement-services-india/","Procurement services India",
"Procurement Services in India for Overseas Buyers | Teak & Tide",
"Outsourced procurement services in India: supplier discovery, RFQs, negotiation, quality control and logistics coordination for importers and brands.",
"Procurement · India","Procurement services in India","Outsource your India procurement to a team that works only for the buyer.",f'''
    <p>If your company buys from India but has no procurement team there, we act as your local procurement office. We run the supplier search and RFQ process, negotiate terms, manage orders and make sure what ships matches what you approved.</p>
    <h2>What we do</h2>
    {ul(["Supplier discovery across India's manufacturing clusters",
         "RFQs and like-for-like quote comparison",
         "Supplier verification: registrations, facilities and export experience",
         "Negotiation of price, MOQ, lead time and payment terms",
         "Sample management and approval records",
         "During-production and pre-shipment inspection",
         "Coordination with freight forwarders and customs brokers"])}
    <h2>Categories</h2>
    <p>Food and agri commodities (spices, rice, pulses, dry fruits), herbal raw materials, leather goods, handicrafts and home decor, and textiles.</p>
''' + faq([("Can you work with our existing suppliers?","Yes. We can follow up and inspect orders with suppliers you already use, as well as find new ones."),
           ("Do you sign an agreement?","Yes. Scope and fees are agreed in writing before work starts."),
           ("Can you arrange third-party inspection?","Yes. We can arrange agencies such as SGS, Bureau Veritas, Intertek, QIMA or TÜV at the buyer's cost.")]),
"I am looking for procurement services in India."))

PAGES.append(("lp-delhi","/sourcing-agency-delhi/","Sourcing agency in Delhi",
"Sourcing Agency in Delhi NCR, India | Teak & Tide Sourcing",
"Sourcing agency based in Delhi NCR. Close to the manufacturing hubs of North India: Moradabad, Agra, Kanpur, Panipat, Jaipur and Khari Baoli markets.",
"Delhi NCR · Sourcing agency","Sourcing agency in Delhi NCR","Based in Delhi, close to many of North India's biggest manufacturing and trading hubs.",f'''
    <p>Delhi NCR is a natural base for sourcing from India. It is a major trading centre in its own right and sits within a day's travel of many important manufacturing clusters, which makes supplier visits, sample collection and inspections faster.</p>
    <h2>Clusters we can reach quickly from Delhi</h2>
    {ul(["<strong>Moradabad:</strong> brass and metal handicrafts",
         "<strong>Agra:</strong> leather footwear and goods, marble inlay",
         "<strong>Kanpur:</strong> leather goods",
         "<strong>Panipat:</strong> home textiles and rugs",
         "<strong>Jaipur:</strong> pottery, block-print textiles, handicrafts",
         "<strong>Saharanpur:</strong> wood carving",
         "<strong>Khari Baoli, Old Delhi:</strong> one of Asia's largest wholesale markets for spices and dry fruits",
         "<strong>Delhi NCR itself:</strong> garments, packaging and many small manufacturers"])}
    <h2>What we do</h2>
    <p>We search fresh suppliers for your requirement, compare quotes, check samples, follow production, inspect before shipment and coordinate export. For products made in South or West India, we work with suppliers there too.</p>
''' + faq([("Can I visit suppliers with you?","Yes. If you travel to India, we can plan and join supplier visits."),
           ("Do you only source from North India?","No. Delhi is our base, but we source from suppliers across India."),
           ("How do I contact you?","Send your requirement through the contact page or WhatsApp +91 70423 67845.")]),
"I am looking for a sourcing agency in Delhi."))

PAGES.append(("lp-trusted","/trusted-sourcing-agent-india/","How to find a trusted agent",
"How to Find a Trusted Sourcing Agent in India | Teak & Tide",
"Signs of a trustworthy sourcing agent in India, red flags to avoid, and the safeguards we use so your money and quality are protected.",
"Trust · Buyer guide","How to find a trusted sourcing agent in India","Red flags, good signs and the safeguards that protect your money.",f'''
    <p>Trust is the real question behind every sourcing decision. Here is how to judge any agent in India, including us.</p>
    <h2>Good signs</h2>
    {ul(["You pay the supplier directly, not through the agent.",
         "The agent tells you the name and location of every supplier.",
         "Fees are clear and agreed in writing before work starts.",
         "They explain how they check quality: samples, during-production checks and pre-shipment inspection with a written report.",
         "They are happy to speak on a video call and show who they are.",
         "Their business has a public presence: website, Google Business Profile and consistent contact details."])}
    <h2>Red flags</h2>
    {ul(["Asking you to send the full order payment to the agent's personal account.",
         "Refusing to tell you who the supplier is.",
         "Prices far below everyone else with no explanation.",
         "No written agreement or vague fees that change later.",
         "Pressure to pay quickly before samples or inspection."])}
    <h2>Our safeguards</h2>
    {ul(["Your order money goes directly to the supplier, never to us.",
         "Every supplier is disclosed to you.",
         "Service fee from 3%, agreed in writing; the small commitment fee is fully adjusted against it.",
         "Pre-shipment inspection before you pay the balance, and third-party inspection on request."])}
''' + faq([("Why do you ask for a commitment fee?","Supplier search takes real time and travel. A small fee confirms the buyer is serious. It is fully adjusted against the service fee."),
           ("Can I verify your business?","Yes. Video call us anytime and check our website and Google Business Profile."),
           ("What if the goods fail inspection?","The supplier must fix or replace them before shipment. This is why the balance is paid only after inspection.")]),
"I would like to know more about how you work."))

PAGES.append(("lp-export-sourcing","/export-sourcing-agent-india/","Export sourcing agent",
"Export Sourcing Agent in India: From Factory to Port | Teak & Tide",
"Export sourcing agent in India who manages suppliers, quality, export packing, documents and freight so your goods arrive as ordered.",
"Export · Sourcing","Export sourcing agent in India","We manage the whole path from Indian factory to your port.",f'''
    <p>Finding a supplier is only half of importing from India. The other half is getting the goods export-ready: correct packing and labelling, the right documents for your country and smooth handover to the freight forwarder. We manage both halves.</p>
    <h2>Export support we provide</h2>
    {ul(["Export packing and carton marking checks",
         "Labelling to your market's requirements, agreed before production",
         "Coordination of documents such as commercial invoice, packing list, certificate of origin and phytosanitary or health certificates where needed",
         "Coordination with your freight forwarder, or introductions to forwarders in India",
         "Trade terms explained: EXW, FOB, CIF and DDP"])}
    <h2>Choosing the right trade term</h2>
    <p>With <strong>FOB</strong>, the supplier delivers to the Indian port and you arrange the main freight. With <strong>CIF</strong>, the supplier pays freight and insurance to your port. With <strong>DDP</strong>, duties and delivery to your door are included. We help you compare landed costs before you decide.</p>
''' + faq([("Do I need an import licence?","That depends on your country and product. Check with your customs broker; we provide the export-side documents."),
           ("Can you ship small orders?","Yes. Small orders can go by courier, air or shared sea containers (LCL)."),
           ("Which Indian ports are common?","Nhava Sheva (Mumbai), Mundra, Chennai and Kolkata are among the busiest, and ICDs near Delhi handle many North Indian shipments.")]),
"I want help exporting goods from India."))

PAGES.append(("lp-product-sourcing","/product-sourcing-india/","Product sourcing services",
"Product Sourcing Services in India for Brands | Teak & Tide",
"Product sourcing services in India for brands and e-commerce sellers: private label, custom packaging, samples, MOQ negotiation and quality checks.",
"Product sourcing · India","Product sourcing services in India","For brands, retailers and e-commerce sellers launching products made in India.",f'''
    <p>Launching a product is different from buying a commodity. You need the right manufacturer, a sample that matches your idea, packaging with your brand, an MOQ you can afford and quality that stays the same from the first order to the tenth.</p>
    <h2>What we help with</h2>
    {ul(["Finding manufacturers who accept private label and custom work",
         "Sample development and revisions until you approve",
         "Custom packaging and labelling with your brand",
         "Negotiating MOQs suitable for a first launch",
         "Consistent quality checks on every order",
         "Packing that suits Amazon FBA, retail or wholesale"])}
    <h2>Popular private-label categories from India</h2>
    <p>Leather bags, wallets and belts; spice blends and single spices in retail packs; makhana and dry-fruit snacks; herbal powders; brass and wooden home decor; cotton textiles and home linen.</p>
''' + faq([("Can you help with Amazon FBA packaging?","Yes. Share Amazon's packing and labelling requirements for your product and we will check them before shipment."),
           ("What MOQ can I expect?","It depends on the product and supplier. Many Indian manufacturers accept smaller trial orders than large factories elsewhere."),
           ("Do you design products?","You provide the design or reference. We work with manufacturers to turn it into samples.")]),
"I want to source a private-label product from India."))

PAGES.append(("lp-supplier-verification","/supplier-verification-india/","Supplier verification India",
"Supplier Verification and Factory Checks in India | Teak & Tide",
"Check an Indian supplier before you pay: registration checks, factory visits or video audits, capacity, export history and sample review.",
"Verification · India","Supplier verification in India","Check a supplier before you send money.",f'''
    <p>Found a supplier online and not sure they are real, or that they really manufacture what they claim? A verification before your first order is one of the cheapest ways to avoid losing money.</p>
    <h2>What we check</h2>
    {ul(["Business registrations such as GST and Import Export Code (IEC), and product licences where relevant (for example FSSAI for food)",
         "Whether they are a manufacturer or a trader",
         "Factory or warehouse visit, or a live video walk-through",
         "Machinery, capacity and number of workers",
         "Export experience and markets served",
         "Sample quality against your specification"])}
    <h2>What you receive</h2>
    <p>A clear written summary with photos and our honest view: proceed, proceed with caution, or avoid.</p>
''' + faq([("Can you verify a supplier I found on a B2B website?","Yes. Send us the supplier's details and your product requirement."),
           ("Do you visit in person?","Where practical we visit; otherwise we run a live video check and verify documents."),
           ("Will the supplier know?","We contact the supplier openly as your representative. Transparency gives the most reliable result.")]),
"I want to verify a supplier in India."))

PAGES.append(("lp-inspection","/quality-inspection-india/","Quality inspection India",
"Pre-Shipment Quality Inspection in India (AQL) | Teak & Tide",
"Pre-shipment and during-production quality inspection in India using AQL sampling, with photo reports before you pay the balance.",
"Inspection · India","Quality inspection in India","Check your goods before they leave the factory.",f'''
    <p>Problems found after goods arrive are expensive. Problems found before shipment can be fixed by the supplier. That is why we recommend inspecting every order before you pay the balance.</p>
    <h2>Types of inspection</h2>
    {ul(["<strong>Pre-production check:</strong> materials and the approved sample before mass production starts.",
         "<strong>During-production inspection:</strong> early check when part of the order is made, to catch issues while they can still be corrected.",
         "<strong>Pre-shipment inspection:</strong> random sample of finished, packed goods checked against your order using AQL sampling.",
         "<strong>Container loading check:</strong> quantity and loading supervision where needed."])}
    <h2>What we check</h2>
    <p>Product against approved sample and specification, workmanship and defects, measurements and weight, packing and labelling, carton marking and quantity. You receive a written report with photos.</p>
    <h2>Third-party inspection</h2>
    <p>If your customer or market requires an independent certificate, we can arrange agencies such as SGS, Bureau Veritas, Intertek, QIMA or TÜV at the buyer's cost.</p>
''' + faq([("What is AQL?","Acceptance Quality Limit: an international sampling method that decides how many units to check and how many defects are acceptable for your order size."),
           ("Can you inspect orders I placed myself?","Yes, if the supplier is in India and agrees to the inspection."),
           ("What happens if the order fails?","The supplier reworks or replaces the defective goods and we re-inspect before shipment.")]),
"I need a quality inspection in India."))

COUNTRIES=[
("usa","/sourcing-from-india-for-usa-buyers/","For US buyers","Sourcing from India for US Buyers | Teak & Tide Sourcing",
 "A sourcing agent in India for US importers, brands and Amazon sellers: suppliers, quality checks, FDA-related food requirements and shipping to the USA.",
 "USA","US importers, brands and Amazon sellers",
 ["Food products such as spices, dry fruits and herbs must meet US FDA rules, including facility registration and Prior Notice, which your supplier and customs broker handle together.",
  "Many sellers ship to Amazon FBA warehouses; packing and labelling must follow Amazon's rules.",
  "Duty rates depend on the product's HTS code; check with your US customs broker before comparing landed costs.",
  "Common routes include sea freight from Nhava Sheva or Mundra to US East and West Coast ports, and air freight for samples and urgent orders."]),
("uk","/sourcing-from-india-for-uk-buyers/","For UK buyers","Sourcing from India for UK Buyers | Teak & Tide Sourcing",
 "Sourcing agent in India for UK importers and brands: supplier search, quality inspection, UK food and product rules, and shipping from India to the UK.",
 "UK","UK importers, retailers and brands",
 ["The UK and India have agreed a trade deal that is expected to reduce duties on many goods; check the current status and rate for your product's commodity code.",
  "Food imports must meet UK limits on pesticide residues, contaminants and labelling.",
  "Products for UK consumers must meet UK product-safety rules; agree test reports with the supplier before production.",
  "Sea freight to UK ports such as Felixstowe and Southampton is common, with air freight for samples."]),
("europe","/sourcing-from-india-for-european-buyers/","For European buyers","Sourcing from India for EU Buyers | Teak & Tide Sourcing",
 "Sourcing agent in India for buyers in Germany, France, the Netherlands and across the EU: suppliers, EU compliance checks and shipping from India.",
 "Europe","importers and brands across the EU",
 ["EU food rules set strict limits on pesticide residues, aflatoxins and ethylene oxide in spices and similar products; share your limits with suppliers before production.",
  "Leather and textile goods must meet EU chemical rules such as REACH restrictions; ask for relevant test reports.",
  "Products may need CE marking or other conformity marks depending on the category.",
  "Sea freight to Rotterdam, Hamburg and Antwerp is common for European buyers."]),
("australia","/sourcing-from-india-for-australian-buyers/","For Australian buyers","Sourcing from India for Australian Buyers | Teak & Tide",
 "Sourcing agent in India for Australian importers: suppliers, quality checks, biosecurity requirements for food and wood products, and shipping to Australia.",
 "Australia","Australian importers and brands",
 ["Australia has a trade agreement with India that reduces duties on many goods; check the rate for your product.",
  "Australia's biosecurity rules are strict for food, plant material, wood and some handicrafts; check import conditions for your product before ordering.",
  "Wooden items and packaging may need treatment and certificates.",
  "Sea freight to Sydney, Melbourne and Brisbane is common."]),
("uae","/sourcing-from-india-for-uae-buyers/","For UAE & Gulf buyers","Sourcing from India for UAE and Gulf Buyers | Teak & Tide",
 "Sourcing agent in India for buyers in the UAE, Saudi Arabia and the Gulf: rice, spices, dry fruits, textiles, decor and fast shipping from India.",
 "UAE & Gulf","traders and retailers in the UAE and Gulf",
 ["India and the UAE have a trade agreement that reduces duties on many goods; check the rate for your product.",
  "Food products need labelling that meets local rules, often including Arabic labelling.",
  "Short sea transit times from Indian west-coast ports make the Gulf one of the fastest markets to supply.",
  "Halal certification may be required for some food products; confirm with your market."]),
]
for code,path,label,t,d,name,who,points in COUNTRIES:
    PAGES.append((f"lp-{code}",path,label,t,d,f"{name} · Buyer guide",f"Sourcing from India for {name} buyers",f"Help for {who} who want to buy from India with less risk.",f'''
    <p>We work as your sourcing agent in India: we search fresh suppliers for your requirement, negotiate, check samples, follow production, inspect before shipment and coordinate export to {name}.</p>
    <h2>What {name} buyers should know</h2>
    {ul(points)}
    <p>Rules and duties change, so always confirm the current requirements for your product with your customs broker or the relevant authority. We make sure suppliers in India provide the documents and test reports you need.</p>
    <h2>What we source for {name} buyers</h2>
    <p>Spices, dry fruits and nuts, herbs, rice and pulses, private-label leather goods, handicrafts and home decor, and textiles.</p>
    <h2>Working across time zones</h2>
    <p>We communicate by WhatsApp and email with clear written updates, so you always know where your order stands.</p>
''' + faq([("How do I start?","Send your requirement: product, quantity, specification and destination. We reply within one business day."),
           ("Do you handle shipping?","We coordinate export documents and freight with your forwarder, or introduce forwarders in India."),
           ("How do I pay?","You pay the supplier directly for goods. Our service fee is agreed in writing.")]),
f"I am a buyer from {name} and want to source from India."))

# ---- build view HTML
views=''
for vid,path,label,t,d,eyebrow,h1,sub,body,wat in PAGES:
    views+=f'''
<div data-view="{vid}">
  <section class="page-head"><div class="wrap"><div class="crumb"><a href="#home">Home</a> / {label}</div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{sub}</p></div></section>
  <section class="block"><div class="wrap article">
{body}
    <div class="cta-inline"><strong>Send us your requirement</strong><p>Tell us the product, quantity and destination. We reply within one business day.</p><div class="actions" style="margin-top:0"><a class="btn btn-green" href="#contact">Get a quote</a><a class="btn btn-ghost" href="{wa(wat)}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
    <p style="margin-top:28px;font-size:15px"><strong>Related:</strong> {" · ".join(f'<a href="#{p[0]}">{p[2]}</a>' for p in PAGES if p[0]!=vid)}</p>
  </div></section>
</div>
'''
i=s.index('<div data-view="blog-india-vs-china-sourcing">'); j=s.index('</div></section>\n</div>',i)+len('</div></section>\n</div>')
s=s[:j]+views+s[j:]
# footer column
col='''    <div>
      <h4>SOURCING IN INDIA</h4>
      <ul>'''+''.join(f'<li><a href="#{p[0]}">{p[2]}</a></li>' for p in PAGES[:10])+'''</ul>
    </div>
    <div class="legal">'''
assert '    <div class="legal">' in s
s=s.replace('    <div class="legal">',col,1)
ids=[p[0] for p in PAGES]
s=s.replace('"blog-india-vs-china-sourcing"];','"blog-india-vs-china-sourcing", '+', '.join(json.dumps(x) for x in ids)+'];',1)
s=s.replace('"blog-india-vs-china-sourcing": "blog" };','"blog-india-vs-china-sourcing": "blog", '+', '.join(json.dumps(x)+': ""' for x in ids)+' };',1)
i=s.index('var TITLES = {'); j=s.index('};',i)
s=s[:j].rstrip()+', '+', '.join(json.dumps(p[0])+': '+json.dumps(p[3]) for p in PAGES)+' '+s[j:]
open(P,'w').write(s)
json.dump({p[0]:[p[1],p[3],p[4]] for p in PAGES},open('/home/claude/seo/landing.json','w'))
print(len(PAGES),'pages')

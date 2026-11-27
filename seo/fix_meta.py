import html,pathlib,re
root=pathlib.Path('/home/claude/site3')
T={
"What Does the US Import from India? 15 Products to Source (2026) | Teak & Tide":"15 Best Products to Import from India (2026) | Teak & Tide",
"Clothing Manufacturers in India: Hubs, MOQs & How to Vet (2026) | Teak & Tide":"Clothing Manufacturers in India: Hubs & MOQs | Teak & Tide",
"How to Find Suppliers in India and Verify Them (2026) | Teak & Tide":"How to Find & Verify Suppliers in India | Teak & Tide",
"How to Import from India on a Small Budget (First Order Guide) | Teak & Tide":"Import from India on a Small Budget (2026) | Teak & Tide",
"Import from India to UK: Zero Duty Under the India-UK Trade Deal (2026) | Teak & Tide":"India-UK Trade Deal: Zero Duty Imports | Teak & Tide",
"Indian Spices Wholesale: Buying Bulk Spices from India (2026) | Teak & Tide":"Indian Spices Wholesale: Bulk Buyer Guide | Teak & Tide",
"Leather Bag Manufacturers in India: Clusters, Leather Types, MOQs | Teak & Tide":"Leather Bag Manufacturers in India (2026) | Teak & Tide",
"Low MOQ Suppliers in India for Amazon FBA Sellers (2026) | Teak & Tide":"Low MOQ Suppliers in India for Amazon FBA | Teak & Tide",
"Towel & Bedsheet Manufacturers in India: Clusters, Specs, MOQs | Teak & Tide":"Towel & Bedsheet Manufacturers in India | Teak & Tide",
"US Tariffs on Indian Goods (2026): What Importers Pay Now | Teak & Tide":"US Tariffs on Indian Goods (2026) | Teak & Tide",
"Low MOQ Sourcing from India for Small Brands & Amazon Sellers | Teak & Tide":"Low MOQ Sourcing from India for Small Brands | Teak & Tide",
"Sourcing Agent in India for Overseas Buyers | Teak & Tide Sourcing":"Sourcing Agent in India for Overseas Buyers | Teak & Tide",
"Brass Handicrafts from Moradabad, India: Buyer Guide | Teak & Tide":"Brass Handicrafts from Moradabad: Buyer Guide | Teak & Tide",
"How to Choose a Sourcing Agent in India: 7 Questions | Teak & Tide":"How to Choose a Sourcing Agent in India | Teak & Tide",
"How to Import Spices from India Safely (Buyer Guide) | Teak & Tide":"How to Import Spices from India Safely | Teak & Tide",
"Supplier Background Check & Due Diligence in India | Teak & Tide":"Supplier Verification in India: Due Diligence | Teak & Tide",
"Export Sourcing Agent in India: From Factory to Port | Teak & Tide":"Export Sourcing Agent in India | Teak & Tide",
"Example Case Study: Sourcing Brass Lamps from India | Teak & Tide":"Case Study: Sourcing Brass Lamps from India | Teak & Tide",
}
D={
"The biggest US imports from India, plus 15 products small and mid-size buyers can realistically source: spices, basmati rice, home textiles, garments, rugs, brass decor, leather bags, cashews, makhana and more.":"15 products small buyers can source from India in 2026: spices, rice, home textiles, garments, rugs, brass decor, leather bags, cashews, makhana and more.",
"Where India's clothing manufacturers are (Tiruppur, Bengaluru, Delhi NCR, Jaipur, Ludhiana, Mumbai), typical MOQs, tech packs, sampling, compliance and how to vet a garment factory.":"India's clothing manufacturing hubs (Tiruppur, Delhi NCR, Jaipur, Ludhiana), typical MOQs, tech packs, sampling and how to vet a garment factory.",
"Where overseas buyers find suppliers in India: manufacturing clusters, export promotion councils, trade fairs, B2B portals and sourcing agents, plus how to verify a supplier before you pay.":"Where to find suppliers in India (clusters, export councils, trade fairs, B2B portals) and how to verify a supplier before you pay.",
"Step-by-step guide for US buyers importing from India: finding suppliers, HTS codes, duties and the 2026 tariff, customs bond, ISF, FDA rules, shipping times and payment terms.":"Step-by-step guide for US importers: finding Indian suppliers, HTS codes, 2026 tariffs, customs bond, ISF, FDA rules, shipping and payment terms.",
"A practical guide for small businesses importing from India for the first time: picking a product, keeping MOQs and samples affordable, shipping options, paying safely and working out landed cost.":"First import from India on a small budget: picking a product, low MOQs, affordable samples, shipping options, safe payment and landed cost.",
"The India-UK trade agreement has been in force since 15 July 2026. What it means for UK importers of Indian textiles, leather, food and home goods, how to claim zero duty, and what still needs checking.":"The India-UK trade deal is in force since 15 July 2026. How UK importers of Indian textiles, leather and food claim zero duty, and what to check.",
"How importers buy Indian spices wholesale: where each spice is traded (Unjha, Guntur, Erode, Kochi), grades that move the price, MOQs, packing, sterilization and the tests buyers in the USA, UK and EU ask for.":"Buying Indian spices wholesale: trading hubs (Unjha, Guntur, Erode, Kochi), grades, MOQs, packing, sterilization and the lab tests US, UK and EU buyers need.",
"How to source leather bags from India: Kolkata, Kanpur, Chennai and Agra, full-grain vs top-grain, veg vs chrome tanning, LWG, MOQs for private label, and what to inspect.":"Source leather bags from India: Kolkata, Kanpur, Chennai and Agra clusters, full-grain vs top-grain, tanning, LWG, private label MOQs and QC.",
"How Amazon FBA and private label sellers can source from India with low MOQs: product ideas, white label vs private label, FBA labelling and packing, compliance and inspection.":"How Amazon FBA sellers source from India with low MOQs: product ideas, white vs private label, FBA labelling and packing, compliance and inspection.",
"A buyer's guide to towel and bed linen manufacturers in India: Solapur, Karur, Panipat and Erode, the big integrated mills, GSM and thread count, certifications, MOQs and how to check quality.":"Towel and bed linen manufacturers in India: Solapur, Karur, Panipat and Erode, GSM and thread count, certifications, MOQs and quality checks.",
"What US importers pay on goods from India in late 2026: the normal duty, the 10% Section 301 tariff since July 2026, Section 232 products, exemptions, and how to keep landed cost down.":"What US importers pay on Indian goods in 2026: normal duty, the 10% Section 301 tariff, Section 232 products, exemptions and cutting landed cost.",
"Small order? We find Indian suppliers who accept low MOQs for private label, Amazon FBA, Shopify and Etsy brands, and help you combine products into one shipment.":"Small order? We find Indian suppliers with low MOQs for private label, Amazon FBA, Shopify and Etsy brands, and combine products into one shipment.",
"Make products under your own brand in India: we find OEM and private label manufacturers for textiles, leather goods, home decor, spices and herbal products, and manage samples, packaging and quality.":"Your brand, made in India: we find OEM and private label manufacturers for textiles, leather, home decor, spices and herbals, and manage samples and QC.",
"Already found a supplier in India? Before you pay, we verify the company: registrations, GST and IEC, ownership, factory visit, capacity, references and red flags, with a written report.":"Found a supplier in India? Before you pay, we check GST, IEC, ownership, factory, capacity and references, and send a written verification report.",
}
for k,v in list(T.items())+list(D.items()):
    assert len(v)<=160,(v,len(v))
for k,v in T.items(): assert len(v)<=60,(v,len(v))
cnt={}
files=list(root.rglob('*.html'))+[root/'assets/app.js']
for f in files:
    s=o=f.read_text()
    for old,new in list(T.items())+list(D.items()):
        for a,b in ((html.escape(old,quote=False),html.escape(new,quote=False)),(html.escape(old),html.escape(new)),(old.replace("'","&#x27;").replace('&','&amp;').replace('&amp;#x27;','&#x27;'),new.replace("'","&#x27;").replace('&','&amp;').replace('&amp;#x27;','&#x27;')),(old,new)):
            if a in s: cnt[old]=cnt.get(old,0)+s.count(a); s=s.replace(a,b)
    if s!=o: f.write_text(s)
for k in list(T)+list(D):
    print(cnt.get(k,0), k[:60])

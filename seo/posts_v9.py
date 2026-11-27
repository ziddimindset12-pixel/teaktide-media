from posts_v7 import faq, AGENT
POSTS = []

EU_FTA = '<p>The EU and India concluded negotiations on a free trade agreement in January 2026. Signing is targeted for December 2026, and the agreement still has to be ratified before any duty cuts apply, so for now use the TARIC rate that applies on your import date. Once it is in force, many Indian labour-intensive products such as textiles, leather and footwear are expected to enter duty-free.</p>'

# ---------------- COUNTRY GUIDES ----------------
POSTS.append(dict(
slug="import-from-india-to-spain", view="blog-spain-import",
title="How to Import from India to Spain: EORI, Duty, IVA and Ports",
seo_title="How to Import from India to Spain (2026) | Teak & Tide",
desc="Importing from India to Spain: EORI from the AEAT, EU duty and the EU-India deal, Spanish IVA rates, Canary Islands rules, Valencia port, supplier checks.",
crumb="Import from India to Spain", eyebrow="Spain buyers · Import guide",
sub="The registrations, taxes and product rules a Spanish business deals with when it buys from India.",
mins=7, tag="SPAIN IMPORT",
cta_t="Buying from India for Spain?",
cta_p="We find and verify Indian suppliers, approve samples with you, inspect goods before shipment and check the documents your Spanish customs agent will ask for.",
cat_href="/sourcing-from-india-for-european-buyers/", cat_label="Sourcing for European buyers",
wa_text="I want to import from India to Spain.",
card="EORI, EU duty, Spanish IVA, Canary Islands rules and shipping from India to Valencia.",
body='''
    <p>Spanish importers buy a wide mix from India: cotton clothing and home textiles, leather goods and footwear components, spices, rice, handicrafts, chemicals and auto parts. Spain is in the EU, so customs duty and most product rules are EU-wide. What is Spanish is the tax office, the VAT rates and a few territories with their own system.</p>

    <h2>1. Get an EORI number</h2>
    <p>Any business importing into the EU needs an <strong>EORI number</strong>. In Spain it is issued through the Agencia Tributaria (AEAT). Most Spanish companies use their NIF as the base of the EORI, and your customs agent (agente de aduanas) needs it before filing the import declaration.</p>

    <h2>2. Check the EU duty rate</h2>
    <p>Look up your product's code in the EU <strong>TARIC</strong> database. Rates are the same in every EU country. Many spices and raw materials are low or zero, while clothing is often 12% and some footwear is higher. India gets lower GSP rates on some products, but several Indian sectors, including many textiles, pay the full rate.</p>
    ''' + EU_FTA + '''

    <h2>3. Add Spanish import VAT (IVA)</h2>
    <p>Spain charges IVA on imports at <strong>21%</strong> for most goods, <strong>10%</strong> for most food, and <strong>4%</strong> for a short list of basic foods. It is calculated on the customs value plus duty and transport to the EU border. Registered businesses normally recover it on their VAT return.</p>
    <p>One thing that catches buyers out: the <strong>Canary Islands, Ceuta and Melilla</strong> are outside the EU VAT area. The Canaries apply their own tax (IGIC) instead of IVA, so goods shipped there are treated differently from goods going to mainland Spain.</p>

    <h2>4. Product rules that matter</h2>
    <ul>
      <li><strong>Food and spices:</strong> EU limits on pesticide residues, aflatoxins and ethylene oxide apply. Some Indian spices face extra border checks, so get a lab report on your lot before it ships.</li>
      <li><strong>Labels:</strong> food and consumer products sold in Spain need labelling in Spanish.</li>
      <li><strong>Textiles and leather:</strong> fibre content labels are mandatory and EU REACH limits restricted dyes and chromium VI in leather.</li>
      <li><strong>Toys, electricals, cosmetics:</strong> need CE marking or EU cosmetic notification before sale.</li>
    </ul>

    <h2>5. Shipping from India to Spain</h2>
    <p>Most sea freight arrives at <strong>Valencia</strong>, Spain's busiest container port, or at Algeciras and Barcelona. Cargo usually leaves from Nhava Sheva or Mundra on the west coast of India. Sea transit is typically a few weeks and depends on the route through the Red Sea or around Africa. Air freight to Madrid suits samples and urgent orders. Our <a href="/free-tools/">CBM and landed cost calculators</a> help you compare.</p>

    <h2>6. Check the supplier before you pay</h2>
    <p>Confirm the supplier's GST registration and Import Export Code, ask for a live video call from the factory, approve a production sample, and pay the balance only after a pre-shipment inspection. Our guide on <a href="/blog/how-to-find-suppliers-in-india/">finding and verifying suppliers in India</a> walks through each step.</p>
    ''' + AGENT + faq(
("Do I need an EORI number to import from India to Spain?", "Yes. Every business importing goods into the EU needs an EORI number. In Spain it is issued through the Agencia Tributaria (AEAT), usually based on your NIF."),
("What is the import VAT rate in Spain?", "The standard IVA rate is 21%. Most food is taxed at 10% and some basic foods at 4%. The Canary Islands use IGIC instead of IVA."),
("Is there a free trade agreement between Spain and India?", "Trade agreements are made at EU level. The EU-India agreement was concluded in January 2026 and is expected to be signed in December 2026, but its lower duties only apply once it enters into force."))))

POSTS.append(dict(
slug="import-from-india-to-france", view="blog-france-import",
title="How to Import from India to France: EORI, Duty, TVA and Labels",
seo_title="How to Import from India to France (2026) | Teak & Tide",
desc="Importing from India to France: EORI, EU duty, the EU-India deal, TVA and the import VAT reverse charge, French labels, Le Havre port and supplier checks.",
crumb="Import from India to France", eyebrow="France buyers · Import guide",
sub="What a French business needs to register, what it will pay, and how import VAT works in France.",
mins=7, tag="FRANCE IMPORT",
cta_t="Buying from India for France?",
cta_p="We shortlist and verify Indian suppliers, manage samples, inspect before shipment and make sure the paperwork matches what your French customs broker needs.",
cat_href="/sourcing-from-india-for-european-buyers/", cat_label="Sourcing for European buyers",
wa_text="I want to import from India to France.",
card="EORI, EU duty, TVA and the import VAT reverse charge, French labels and shipping to Le Havre.",
body='''
    <p>France buys Indian clothing and home linen, leather goods, jewellery, spices and tea, handicrafts, chemicals and engineering parts. Like every EU country, France uses EU customs duty and EU product rules. Two things are more French than European: how import VAT is paid, and the language rules for labels.</p>

    <h2>1. Get an EORI number</h2>
    <p>An <strong>EORI number</strong> is required for any EU import. French businesses request it from French customs (la douane), usually based on their SIRET number. Your customs representative cannot clear goods without it.</p>

    <h2>2. Find the EU duty rate</h2>
    <p>Duty is set by the EU and published in the <strong>TARIC</strong> database. Check your exact product code: spices and many raw materials are low or duty-free, while clothing is often 12%. Some Indian products get reduced GSP rates, but many textile lines do not.</p>
    ''' + EU_FTA + '''

    <h2>3. TVA, and the import VAT reverse charge</h2>
    <p>France charges TVA at <strong>20%</strong> on most goods and <strong>5.5%</strong> on most food. Since 2022, VAT-registered businesses in France account for import VAT on their regular VAT return instead of paying it to customs at the border (autoliquidation de la TVA à l'importation). In practice that means no VAT cash outlay when the container lands, which helps cash flow on bigger orders.</p>
    <p>The French overseas departments, such as Réunion or Martinique, are outside the EU VAT area and have their own local tax (octroi de mer), so treat them as separate destinations.</p>

    <h2>4. Product rules and labels</h2>
    <ul>
      <li><strong>French language:</strong> product information, labels and instructions for consumer goods sold in France must be in French.</li>
      <li><strong>Food and spices:</strong> EU limits for pesticides, aflatoxins and ethylene oxide apply. Ask for a lab report on your lot before shipment.</li>
      <li><strong>Textiles and leather:</strong> fibre composition labels, plus REACH limits on restricted dyes and chromium VI. France also has its own environmental labelling and recycling (Triman) rules for many consumer products, so check them with your importer.</li>
      <li><strong>Toys, electricals, cosmetics:</strong> CE marking or EU cosmetic notification before sale.</li>
    </ul>

    <h2>5. Shipping from India to France</h2>
    <p><strong>Le Havre</strong> is the main gateway for Paris and northern France, and <strong>Marseille-Fos</strong> serves the south. Some French importers also bring goods in through Antwerp or Rotterdam and truck them in. Sea freight usually loads at Nhava Sheva or Mundra. Air cargo to Paris-Charles de Gaulle works for samples and urgent shipments. Compare the options with our <a href="/free-tools/">CBM and landed cost calculators</a>.</p>

    <h2>6. Vet the supplier</h2>
    <p>Check GST and the Import Export Code, do a live factory video call, approve a pre-production sample and inspect before paying the balance. See our <a href="/blog/how-to-find-suppliers-in-india/">supplier verification guide</a> and our page on <a href="/quality-inspection-india/">quality inspection in India</a>.</p>
    ''' + AGENT + faq(
("How much is import VAT in France?", "The standard TVA rate is 20% and most food is taxed at 5.5%. VAT-registered businesses declare import VAT on their VAT return instead of paying it at customs."),
("Do product labels need to be in French?", "Yes. Labels, product information and instructions for consumer goods sold in France must be in French. Other languages can appear alongside."),
("Which French port is best for goods from India?", "Le Havre is the main port for Paris and northern France, and Marseille-Fos serves the south. The right one depends on where your warehouse is."))))

POSTS.append(dict(
slug="import-from-india-to-italy", view="blog-italy-import",
title="How to Import from India to Italy: EORI, Duty, IVA and Ports",
seo_title="How to Import from India to Italy (2026) | Teak & Tide",
desc="Importing from India to Italy: EORI, EU duty and the EU-India deal, Italian IVA rates, labels in Italian, Genoa and La Spezia ports, and supplier checks.",
crumb="Import from India to Italy", eyebrow="Italy buyers · Import guide",
sub="Registrations, taxes, ports and product rules for Italian companies buying from India.",
mins=7, tag="ITALY IMPORT",
cta_t="Buying from India for Italy?",
cta_p="We find and check Indian suppliers, approve samples with you, inspect before shipment and prepare the documents your Italian customs broker needs.",
cat_href="/sourcing-from-india-for-european-buyers/", cat_label="Sourcing for European buyers",
wa_text="I want to import from India to Italy.",
card="EORI, EU duty, Italian IVA, labels in Italian and shipping from India to Genoa or La Spezia.",
body='''
    <p>Italy has a long trade relationship with India. Italian companies buy textiles and yarn, leather and footwear components, chemicals, iron and steel products, spices, rice and handicrafts. Many Italian brands also produce part of their range in India and finish or sell it in Italy. Customs rules are EU-wide; the tax rates and some paperwork are Italian.</p>

    <h2>1. Get an EORI number</h2>
    <p>Every EU importer needs an <strong>EORI number</strong>. In Italy it is linked to your partita IVA (VAT number) and handled with the customs agency, the Agenzia delle Dogane e dei Monopoli (ADM). Your spedizioniere doganale (customs broker) will ask for it first.</p>

    <h2>2. Check the EU duty rate</h2>
    <p>Look up the product code in <strong>TARIC</strong>. The rate is the same across the EU. Spices and many raw materials are low or zero, clothing is often 12%, and leather footwear has its own rates by type. Several Indian sectors no longer get GSP preferences, so check rather than assume.</p>
    ''' + EU_FTA + '''

    <h2>3. Add Italian import VAT (IVA)</h2>
    <p>Italy's standard IVA rate is <strong>22%</strong>. Reduced rates of <strong>10%</strong> and <strong>4%</strong> apply to many foods, depending on the product. IVA is charged on the customs value plus duty and transport to the EU border, and registered businesses recover it on their VAT return.</p>

    <h2>4. Product rules</h2>
    <ul>
      <li><strong>Labels in Italian:</strong> food and consumer goods sold in Italy need Italian-language labelling.</li>
      <li><strong>Food and spices:</strong> EU residue and contaminant limits apply, and some Indian spices face extra border checks. Insist on an accredited lab report for your lot.</li>
      <li><strong>Leather and textiles:</strong> REACH limits on chromium VI in leather and restricted azo dyes. "Made in Italy" claims have strict rules, so goods made in India must not be labelled as Italian.</li>
      <li><strong>Toys, electricals, cosmetics:</strong> CE marking or EU cosmetic notification.</li>
    </ul>

    <h2>5. Shipping from India to Italy</h2>
    <p>Containers from Nhava Sheva, Mundra or Chennai usually arrive at <strong>Genoa</strong> or <strong>La Spezia</strong> for northern Italy, where most importers are based. <strong>Trieste</strong> and Venice serve the north-east, and Naples and Salerno the south. Transit time depends on the shipping route. Air freight to Milan Malpensa suits samples and urgent orders. Use our <a href="/free-tools/">landed cost calculator</a> to compare.</p>

    <h2>6. Check the supplier</h2>
    <p>Verify GST and the Import Export Code, see the factory on a live video call, approve samples and pay the balance only after a <a href="/quality-inspection-india/">pre-shipment inspection</a>. For leather and textile orders, ask for chemical test reports from an accredited lab.</p>
    ''' + AGENT + faq(
("What is the import VAT rate in Italy?", "The standard IVA rate is 22%. Many foods are taxed at reduced rates of 10% or 4%, depending on the product."),
("Can goods made in India be sold as Made in Italy?", "No. Origin is decided by where the goods were made or last substantially transformed. Labelling Indian-made goods as Made in Italy can lead to seizure and fines."),
("Which Italian ports handle cargo from India?", "Genoa and La Spezia handle most containers for northern Italy. Trieste and Venice serve the north-east, and Naples and Salerno the south."))))

POSTS.append(dict(
slug="import-from-india-to-qatar", view="blog-qatar-import",
title="How to Import from India to Qatar: GCC Duty, Licences and Legalisation",
seo_title="How to Import from India to Qatar (2026) | Teak & Tide",
desc="Importing from India to Qatar: importer registration, 5% GCC duty, duty-free foods, no VAT yet, document legalisation, food rules and Hamad Port.",
crumb="Import from India to Qatar", eyebrow="Qatar buyers · Import guide",
sub="Who can import, what duty applies, which documents need legalising and how goods reach Hamad Port.",
mins=6, tag="QATAR IMPORT",
cta_t="Buying from India for Qatar?",
cta_p="We source and verify Indian suppliers, check samples, inspect goods before shipment and make sure invoices and certificates are ready for legalisation.",
cat_href="/sourcing-from-india-for-uae-buyers/", cat_label="Sourcing for Gulf buyers",
wa_text="I want to import from India to Qatar.",
card="Importer registration, 5% GCC duty, duty-free foods, document legalisation and shipping to Hamad Port.",
body='''
    <p>India is one of Qatar's main suppliers of food. Qatari importers buy rice, spices, fresh produce, tea, meat and dairy alongside textiles, building materials, furniture and handicrafts. The rules are simpler than in Europe, but the paperwork has to be exact.</p>

    <h2>1. Who can import</h2>
    <p>Commercial imports into Qatar are made by a business with a Qatari commercial registration that is entered in the <strong>Importers' Register</strong>. Foreign suppliers usually work through a local importer, distributor or agent who holds these registrations. Customs declarations are filed electronically through Qatar's customs clearance system, usually by a licensed clearing agent.</p>

    <h2>2. Customs duty</h2>
    <p>Qatar is part of the GCC Customs Union and applies a <strong>5% duty</strong> on the CIF value of most goods. Many basic foods, including grains, spices, tea, sugar and fresh fruit and vegetables, are duty-free. Some goods pay much more: pork products, tobacco and alcohol face 100%, and certain steel products 20%.</p>
    <p>Rates can change for specific products. For example, Qatar announced higher duty on selected chicken and agricultural products from 15 November 2026 to support local production, so check the current rate for your product code before you quote a price to your customer.</p>

    <h2>3. No VAT, for now</h2>
    <p>Qatar has not introduced VAT, so imports currently pay customs duty but no import VAT. The GCC countries agreed a common VAT framework years ago and Qatar may still introduce it, so keep an eye on announcements if you are planning long-term pricing.</p>

    <h2>4. Documents and legalisation</h2>
    <ul>
      <li>Commercial invoice and packing list</li>
      <li>Certificate of origin, usually issued by an Indian chamber of commerce or export council</li>
      <li>Bill of lading or air waybill</li>
      <li>Health or phytosanitary certificates for food and plant products</li>
    </ul>
    <p>The commercial invoice and certificate of origin for commercial shipments usually need <strong>legalisation</strong>, and fees apply. Confirm the current process with your clearing agent before the goods ship. A missing stamp is the most common reason for delays at Hamad Port.</p>

    <h2>5. Food rules</h2>
    <p>Imported food is checked by Qatar's Ministry of Public Health. Labels need Arabic (English can appear alongside), with production and expiry dates and enough remaining shelf life. Meat and poultry must come from approved plants with halal certification. Plan these details with the supplier before production, not after.</p>

    <h2>6. Shipping from India to Qatar</h2>
    <p>Most sea freight goes from Mundra or Nhava Sheva to <strong>Hamad Port</strong>, south of Doha, on a short route across the Arabian Sea. Air freight from Delhi, Mumbai or Kochi to Hamad International Airport is common for fresh produce and urgent orders.</p>

    <h2>7. Check the supplier</h2>
    <p>Verify the supplier's GST registration and Import Export Code, ask for a factory video call, approve a sample and inspect before paying the balance. Our guide on <a href="/blog/how-to-find-suppliers-in-india/">verifying suppliers in India</a> has the full checklist. For other Gulf markets, see our <a href="/blog/import-from-india-to-saudi-arabia/">Saudi Arabia guide</a> and <a href="/sourcing-from-india-for-uae-buyers/">UAE page</a>.</p>
    ''' + AGENT + faq(
("What is the customs duty on goods from India to Qatar?", "Most goods pay 5% of the CIF value under the GCC common tariff. Many basic foods such as grains, spices, tea and fresh produce are duty-free, while pork, tobacco and alcohol pay 100%."),
("Does Qatar charge VAT on imports?", "No. Qatar has not introduced VAT yet, so imports pay customs duty but no import VAT. This could change if Qatar implements the GCC VAT framework."),
("Do documents for Qatar need to be legalised?", "For commercial shipments, the invoice and certificate of origin usually need legalisation, and fees apply. Check the current process with your clearing agent before shipping."))))

POSTS.append(dict(
slug="import-from-india-to-malaysia", view="blog-malaysia-import",
title="How to Import from India to Malaysia: Duty, Sales Tax and FTAs",
seo_title="How to Import from India to Malaysia (2026) | Teak & Tide",
desc="Importing from India to Malaysia: duty under the ASEAN-India and MICECA deals, 5% and 10% sales tax, rice rules, halal, food labels and Port Klang.",
crumb="Import from India to Malaysia", eyebrow="Malaysia buyers · Import guide",
sub="How duty, sales tax and India's two trade agreements with Malaysia affect your landed cost.",
mins=7, tag="MALAYSIA IMPORT",
cta_t="Buying from India for Malaysia?",
cta_p="We find and verify Indian suppliers, approve samples, inspect before shipment and make sure the certificate of origin is right so you can claim the lower FTA duty.",
cat_href="/sourcing-agent-in-india/", cat_label="Our sourcing service",
wa_text="I want to import from India to Malaysia.",
card="Customs duty, ASEAN-India and MICECA trade deals, Malaysian sales tax, halal and shipping to Port Klang.",
body='''
    <p>Malaysia buys spices, textiles and yarn, meat, chemicals, machinery parts, aluminium and a growing range of consumer goods from India. The country has a large Indian-origin community, which keeps demand strong for Indian food, sarees, jewellery and festival goods.</p>

    <h2>1. Registration</h2>
    <p>You need a business registered in Malaysia with the Companies Commission (SSM). Import declarations go to the Royal Malaysian Customs Department, normally filed by a licensed forwarding or customs agent. Some products also need an import permit from the relevant ministry before they arrive.</p>

    <h2>2. Customs duty and the two trade deals</h2>
    <p>Duty depends on the product code in Malaysia's customs tariff. Many raw materials are duty-free, while some consumer goods pay more. India has two trade agreements with Malaysia that can lower the rate:</p>
    <ul>
      <li><strong>ASEAN-India Free Trade Area (AIFTA)</strong>, covering India and all ASEAN countries</li>
      <li><strong>Malaysia-India Comprehensive Economic Cooperation Agreement (MICECA)</strong>, in force since 2011</li>
    </ul>
    <p>To claim the lower rate, the shipment needs the right <strong>certificate of origin</strong> from the Indian side, issued for that agreement and filled in correctly. Compare both rates for your product, as one agreement can be better than the other for a given item.</p>

    <h2>3. Sales tax</h2>
    <p>Malaysia does not have VAT or GST. Instead, imported goods pay <strong>sales tax at 5% or 10%</strong>, depending on the product code, unless they are exempt. Essential foods are generally exempt. Since the July 2025 expansion, more items are taxable, and leather goods, for example, are taxed at 10%. Check your exact product code before you work out the landed cost.</p>

    <h2>4. Product rules</h2>
    <ul>
      <li><strong>Rice:</strong> only BERNAS, the national rice company, is authorised to import rice into Malaysia. If you want to sell Indian basmati in Malaysia, you will buy through or with BERNAS, not import directly.</li>
      <li><strong>Plant products and spices:</strong> may need an import permit and inspection by MAQIS, the Malaysian quarantine and inspection service.</li>
      <li><strong>Food labels:</strong> food must meet Malaysian food regulations, with labelling in Bahasa Malaysia (English can be added).</li>
      <li><strong>Halal:</strong> meat must come from approved plants, and any halal claim on a product should be backed by a certification JAKIM recognises.</li>
    </ul>

    <h2>5. Shipping from India to Malaysia</h2>
    <p><strong>Port Klang</strong>, near Kuala Lumpur, handles most cargo from India, with Tanjung Pelepas in the south and Penang in the north as alternatives. Chennai, Kolkata and Visakhapatnam on India's east coast have the shortest routes, though west-coast ports also have regular services. Air freight to Kuala Lumpur International Airport suits samples and urgent orders.</p>

    <h2>6. Check the supplier</h2>
    <p>Verify GST and the Import Export Code, ask for a live factory video call, approve a sample and inspect before paying the balance. Ask the supplier early whether they have issued certificates of origin under AIFTA or MICECA before; an exporter who has done it before saves you a lot of back and forth. See also our <a href="/blog/import-from-india-to-singapore/">Singapore import guide</a>.</p>
    ''' + AGENT + faq(
("Is there a free trade agreement between India and Malaysia?", "Yes, two. Goods can qualify for lower duty under the ASEAN-India Free Trade Area or the Malaysia-India CECA, with the right certificate of origin."),
("What is the sales tax on imports into Malaysia?", "Taxable imported goods pay sales tax at 5% or 10% depending on the product code. Essential foods are generally exempt, and Malaysia has no VAT or GST."),
("Can I import basmati rice from India into Malaysia myself?", "Not directly. BERNAS is Malaysia's sole authorised rice importer, so rice imports go through it."))))

# ---------------- PRODUCT GUIDES ----------------
POSTS.append(dict(
slug="cumin-seed-suppliers-india", view="blog-cumin",
title="Cumin Seed Suppliers in India: Unjha, Grades and Lab Tests",
seo_title="Cumin Seed Suppliers in India: Buyer's Guide | Teak & Tide",
desc="Buying cumin seeds from India: Gujarat and Rajasthan crops, the Unjha market, Singapore vs Europe quality, purity and pesticide tests, and supplier checks.",
crumb="Cumin seed suppliers in India", eyebrow="Spices · Buyer guide",
sub="Where Indian cumin comes from, what the trade grades mean and which tests to ask for before you import.",
mins=6, tag="CUMIN",
cta_t="Looking for a cumin supplier in India?",
cta_p="Tell us the grade, purity, packing and quantity. We shortlist processors, get lab-tested samples and inspect before shipment.",
cat_href="/spices/", cat_label="Spices we source",
wa_text="I want to source cumin seeds from India.",
card="Gujarat and Rajasthan cumin, the Unjha market, Singapore vs Europe quality and lab tests.",
body='''
    <p>India is the world's largest producer and exporter of cumin (jeera). Spice packers, seasoning makers, food manufacturers and wholesalers across Asia, the Middle East, Europe and the Americas buy Indian cumin, whole or ground. Price moves a lot with the crop, so timing and specification matter as much as the supplier.</p>

    <h2>Where Indian cumin is grown</h2>
    <p>Almost all of it comes from <strong>Gujarat</strong> and <strong>Rajasthan</strong>. It is a winter crop: sown around November and harvested from about February to April. The main trading hub is <strong>Unjha</strong> in Mehsana district, Gujarat, where most of the crop is bought, cleaned and graded. Many exporters have cleaning and sorting plants in or near Unjha.</p>

    <h2>Common export grades</h2>
    <ul>
      <li><strong>Singapore quality:</strong> machine-cleaned, typically around 98–99% purity. The standard bulk grade for many Asian and Middle East buyers.</li>
      <li><strong>Europe quality:</strong> higher purity, often 99–99.5%, with less dust and fewer foreign seeds.</li>
      <li><strong>Sortex-cleaned:</strong> passed through colour sorters for the cleanest lots, used by premium packers.</li>
      <li><strong>Ground cumin and cumin oil:</strong> for food factories and flavour houses.</li>
    </ul>
    <p>Grade names are trade terms, not legal standards, so two suppliers' "Europe quality" can differ. Write the numbers into your order.</p>

    <h2>What to put in your specification</h2>
    <p>Purity %, maximum admixture and broken seeds, moisture, volatile oil content, mesh size for powder, packing (25 kg or 50 kg bags, paper or PP) and whether you need steam sterilisation. Ask each supplier to quote on the same spec so prices are comparable.</p>

    <h2>Tests to ask for</h2>
    <ul>
      <li><strong>Pesticide residues</strong> against your market's limits. EU and UK limits are strict and some lots fail.</li>
      <li><strong>Ethylene oxide</strong>, required by many EU and UK buyers</li>
      <li><strong>Salmonella and microbiology</strong>, especially for ground cumin</li>
      <li><strong>Aflatoxins</strong> and, for powder, adulteration checks</li>
    </ul>
    <p>Use an accredited lab report on a sample drawn from <em>your</em> lot, not a general certificate.</p>

    <h2>Checking the supplier</h2>
    <p>Spice exporters must be registered with the <strong>Spices Board of India</strong> and hold GST, an Import Export Code and an FSSAI food licence. Visit or video-call the cleaning plant, and inspect before the balance payment. See our guides to <a href="/blog/how-to-import-spices-from-india/">importing spices from India</a> and <a href="/blog/indian-spices-wholesale-bulk/">buying Indian spices wholesale</a>.</p>
    ''' + AGENT + faq(
("Where does Indian cumin come from?", "Almost all Indian cumin is grown in Gujarat and Rajasthan. Unjha in Gujarat is the main market where it is traded, cleaned and graded."),
("What is the difference between Singapore and Europe quality cumin?", "Both are trade grades. Singapore quality is machine-cleaned at roughly 98–99% purity; Europe quality is cleaner, usually 99–99.5%. Always write the exact purity into your contract."),
("When is the best time to buy Indian cumin?", "The new crop arrives from about February to April, when supply is highest. Prices can swing sharply with crop size, so many buyers book part of their needs early in the season."))))

POSTS.append(dict(
slug="cardamom-suppliers-india", view="blog-cardamom",
title="Green Cardamom Suppliers in India: Grades, Sizes and Auctions",
seo_title="Cardamom Suppliers in India: Buyer's Guide | Teak & Tide",
desc="Buying green cardamom from India: Idukki growing areas, Spices Board e-auctions, AGEB and size grades, colour and pesticide tests, and supplier checks.",
crumb="Cardamom suppliers in India", eyebrow="Spices · Buyer guide",
sub="How Indian green cardamom is sold, how it is graded by size and what to test before you import.",
mins=6, tag="CARDAMOM",
cta_t="Looking for a cardamom supplier in India?",
cta_p="Tell us the size grade, colour, packing and quantity. We get samples from exporters, check them against your spec and inspect before shipment.",
cat_href="/spices/", cat_label="Spices we source",
wa_text="I want to source green cardamom from India.",
card="Idukki cardamom, Spices Board e-auctions, AGEB and mm size grades, colour and pesticide tests.",
body='''
    <p>Indian green cardamom (small cardamom, elaichi) is known for its strong aroma and deep green colour. Buyers in the Gulf, Europe, the US and Asia use it for coffee, tea, sweets, spice blends and food manufacturing. Guatemala is the other major supplier, so Indian cardamom usually competes on quality and flavour rather than price.</p>

    <h2>Where it grows and how it is sold</h2>
    <p>Most Indian small cardamom comes from the <strong>Idukki district of Kerala</strong>, with smaller areas in the Bodi hills of Tamil Nadu and in Karnataka. Growers sell their crop through Spices Board <strong>e-auctions</strong> at <strong>Puttady</strong> in Kerala and <strong>Bodinayakanur</strong> in Tamil Nadu. Exporters buy at these auctions, then clean, grade and pack for export. Auction prices are public, which gives you a useful reference when you compare quotes.</p>
    <p>Large or black cardamom is a different spice, grown mainly in Sikkim and the North-East. Make sure your supplier knows which one you want.</p>

    <h2>How cardamom is graded</h2>
    <ul>
      <li><strong>By size:</strong> the trade usually quotes by pod diameter, such as 6–7 mm, 7–8 mm and 8 mm+. Bigger, bolder pods cost more.</li>
      <li><strong>AGEB (Alleppey Green Extra Bold):</strong> 7 mm and above, with a minimum litre weight. <strong>AGB (Alleppey Green Bold)</strong> is 6 mm and above.</li>
      <li><strong>Litre weight:</strong> the weight of one litre of pods. Higher litre weight means fuller, better-filled pods.</li>
      <li><strong>Colour:</strong> uniform deep green is preferred. Splits, pale pods and yellow pods go into lower grades or seed.</li>
    </ul>

    <h2>What to specify</h2>
    <p>Size range, minimum litre weight, colour, maximum percentage of splits and empty pods, moisture, and packing (often in lined cartons or bags to protect colour and aroma). Say whether you need whole pods, seeds or powder.</p>

    <h2>Tests to insist on</h2>
    <ul>
      <li><strong>Pesticide residues:</strong> the most important test for cardamom, especially for the EU, UK and Saudi markets</li>
      <li><strong>Artificial colour:</strong> check that the green is natural</li>
      <li><strong>Moisture and microbiology</strong>, plus ethylene oxide for EU and UK buyers</li>
    </ul>
    <p>Get results from an accredited lab on a sample from your own lot.</p>

    <h2>Checking the supplier</h2>
    <p>Exporters need Spices Board registration plus GST, an Import Export Code and an FSSAI licence. Ask where they buy (auction lot numbers help) and how they store the cardamom, since colour fades with heat and light. Then approve a sample and <a href="/quality-inspection-india/">inspect before shipment</a>. See also our guide to <a href="/blog/how-to-import-spices-from-india/">importing spices from India</a>.</p>
    ''' + AGENT + faq(
("Where is Indian green cardamom grown?", "Mostly in the Idukki district of Kerala, with smaller areas in Tamil Nadu and Karnataka. It is sold through Spices Board e-auctions at Puttady and Bodinayakanur."),
("What does AGEB mean in cardamom?", "AGEB stands for Alleppey Green Extra Bold, a grade for pods 7 mm and above with a minimum litre weight. AGB is the bold grade, 6 mm and above."),
("What is the most important test for Indian cardamom?", "Pesticide residues. Test every lot against your market's limits at an accredited lab, and check for artificial colour too."))))

POSTS.append(dict(
slug="basmati-rice-exporters-india", view="blog-basmati",
title="Basmati Rice Exporters in India: Varieties, Sella and EU Rules",
seo_title="Basmati Rice Exporters in India: Buyer's Guide | Teak & Tide",
desc="Buying basmati rice from India: GI growing states, 1121, 1509 and 1401 varieties, raw, steam and sella, APEDA registration, EU pesticide limits and checks.",
crumb="Basmati rice exporters in India", eyebrow="Agricultural products · Buyer guide",
sub="Varieties, processing types and the pesticide rules that decide whether your basmati clears customs.",
mins=7, tag="BASMATI RICE",
cta_t="Looking for a basmati rice exporter in India?",
cta_p="Tell us the variety, type, grain length, packing and destination. We compare mills, get tested samples and inspect before shipment.",
cat_href="/agricultural-products/", cat_label="Agricultural products we source",
wa_text="I want to source basmati rice from India.",
card="Basmati varieties, raw vs steam vs sella, APEDA rules and the EU pesticide limits buyers must know.",
body='''
    <p>India produces most of the world's basmati rice and exports it to the Gulf, Europe, the UK, North America and beyond. Saudi Arabia, Iran, Iraq and the UAE are among the biggest buyers. For a buyer, the hard part is not finding a mill, it is getting the right variety, the right processing and a lot that passes your country's pesticide limits.</p>

    <h2>Where basmati is grown</h2>
    <p>Basmati has a protected geographical indication in India. It is grown in the Indo-Gangetic plain: <strong>Punjab, Haryana, Himachal Pradesh, Uttarakhand, Delhi, western Uttar Pradesh and parts of Jammu &amp; Kashmir</strong>. Most export mills are in Punjab and Haryana, around Amritsar, Karnal, Kaithal and Sonipat. The paddy is harvested from about October to December.</p>

    <h2>Main varieties</h2>
    <ul>
      <li><strong>1121:</strong> extra-long grain that elongates a lot on cooking. Very popular in the Gulf.</li>
      <li><strong>1509:</strong> long grain, shorter growing season, usually priced below 1121.</li>
      <li><strong>1401 and Pusa Basmati 1:</strong> widely sold in Europe and the UK.</li>
      <li><strong>Traditional basmati:</strong> older varieties with strong aroma but lower yields, sold at a premium.</li>
    </ul>

    <h2>Raw, steam or sella</h2>
    <ul>
      <li><strong>Raw (white):</strong> milled without parboiling. Strongest aroma.</li>
      <li><strong>Steam:</strong> paddy is steamed lightly before milling, so grains stay firmer and separate.</li>
      <li><strong>Golden sella and white sella:</strong> parboiled rice, very firm and non-sticky, popular in the Middle East and with restaurants.</li>
    </ul>
    <p>Also specify whether you want aged rice (often 6–12 months), since ageing improves cooking quality.</p>

    <h2>What to specify</h2>
    <p>Variety, type, average grain length (for example, raw length in mm), maximum broken grains, moisture, purity (share of non-basmati grains, which UK and EU buyers check by DNA test), sortex cleaning, packing size and brand or private label.</p>

    <h2>EU and UK pesticide limits</h2>
    <p>The EU sets very low maximum residue limits on rice, including <strong>0.01 mg/kg for tricyclazole</strong>, a fungicide used on paddy. India's APEDA requires pre-shipment pesticide testing for basmati going to the EU and neighbouring countries. Buyers should still ask for their own accredited lab report on the actual lot, covering pesticides and aflatoxin. Shipments that fail are rejected at the border, and the cost falls on whoever owns the goods.</p>

    <h2>Checking the exporter</h2>
    <p>Basmati exporters must be registered with <strong>APEDA</strong>, and export contracts are registered with APEDA before shipment. Also check GST, the Import Export Code and FSSAI licence, see the mill on video, and inspect before you pay the balance. Note that some markets control rice imports: in Malaysia, for example, only BERNAS can import rice. See our <a href="/blog/best-products-to-import-from-india/">best products to import from India</a> guide for more agricultural options.</p>
    ''' + AGENT + faq(
("Which basmati variety is best for the Middle East?", "1121 is the most popular in the Gulf because of its extra-long grain, often bought as golden or white sella. 1509 is a lower-priced alternative."),
("What is the EU limit for tricyclazole in basmati rice?", "The EU limit for tricyclazole in rice is 0.01 mg/kg. Ask for an accredited lab test on your lot before it ships."),
("Do basmati exporters in India need registration?", "Yes. They must be registered with APEDA, and export contracts are registered with APEDA. They also need GST, an Import Export Code and an FSSAI licence."))))

POSTS.append(dict(
slug="black-pepper-suppliers-india", view="blog-black-pepper",
title="Black Pepper Suppliers in India: Malabar, Tellicherry and Grades",
seo_title="Black Pepper Suppliers in India: Buyer's Guide | Teak & Tide",
desc="Buying black pepper from India: Kerala and Karnataka crops, Malabar MG1 and Tellicherry TGSEB grades, bulk density, steam sterilising and lab tests.",
crumb="Black pepper suppliers in India", eyebrow="Spices · Buyer guide",
sub="What Malabar and Tellicherry grades mean, why Indian pepper costs more, and which tests to ask for.",
mins=6, tag="BLACK PEPPER",
cta_t="Looking for a black pepper supplier in India?",
cta_p="Tell us the grade, density, cleaning and quantity. We compare exporters, get lab-tested samples and inspect before shipment.",
cat_href="/spices/", cat_label="Spices we source",
wa_text="I want to source black pepper from India.",
card="Malabar MG1 and Tellicherry TGSEB grades, bulk density, sterilising and lab tests for buyers.",
body='''
    <p>Black pepper first went from India to the rest of the world, and Indian Malabar and Tellicherry pepper still carry that name in spice catalogues. Today Vietnam is the biggest exporter and Brazil and Indonesia are large suppliers too, so Indian pepper usually costs more. Buyers who choose it want its flavour, pungency and well-known grades, often for premium retail packs and gourmet brands.</p>

    <h2>Where Indian pepper grows</h2>
    <p>Pepper is grown in the Western Ghats: <strong>Karnataka</strong> (Kodagu, Chikkamagaluru, Hassan) and <strong>Kerala</strong> (Wayanad, Idukki), with some in Tamil Nadu. <strong>Kochi</strong> in Kerala is the traditional trading and export hub. The main harvest runs from about December to March.</p>

    <h2>Grades you will see</h2>
    <ul>
      <li><strong>MG1 (Malabar Garbled Grade 1):</strong> the classic bulk grade, cleaned and graded, sold with a minimum bulk density (often quoted around 550 g/litre).</li>
      <li><strong>TGEB (Tellicherry Garbled Extra Bold):</strong> large berries, 4.25 mm and above.</li>
      <li><strong>TGSEB (Tellicherry Garbled Special Extra Bold):</strong> the boldest grade, 4.8 mm and above, used in premium and gourmet packs.</li>
      <li><strong>Other forms:</strong> white pepper, cracked and ground pepper, pepper oil and oleoresin.</li>
    </ul>

    <h2>What to specify</h2>
    <p>Grade or berry size, bulk density (g/litre), moisture, maximum light berries and extraneous matter, and whether you want it steam sterilised, machine-cleaned or sortex-cleaned. For ground pepper, give the mesh size. Packing is usually 25 kg or 50 kg bags, or retail packs for private label.</p>

    <h2>Tests to ask for</h2>
    <ul>
      <li><strong>Microbiology and salmonella:</strong> pepper is a raw farm product, so many buyers need steam-sterilised pepper with a certificate</li>
      <li><strong>Pesticide residues</strong> against your market's limits</li>
      <li><strong>Aflatoxins and ochratoxin</strong></li>
      <li><strong>Mineral oil:</strong> to rule out berries coated to improve shine</li>
      <li><strong>Ethylene oxide</strong> for EU and UK buyers</li>
    </ul>
    <p>Always ask for an accredited lab report on a sample from your own lot.</p>

    <h2>Checking the supplier</h2>
    <p>Check Spices Board registration, GST, the Import Export Code and FSSAI licence. Ask whether the exporter sells only Indian pepper or also blends in imported pepper, and ask for proof of origin if Indian origin matters to you. Then approve a sample and inspect before you pay the balance. See our guides to <a href="/blog/how-to-import-spices-from-india/">importing spices from India</a> and <a href="/blog/indian-spices-wholesale-bulk/">buying spices wholesale</a>.</p>
    ''' + AGENT + faq(
("What is the difference between Malabar and Tellicherry pepper?", "Both are Indian grades. Malabar (MG1) is the standard cleaned grade sold by bulk density. Tellicherry grades (TGEB, TGSEB) are sorted for larger berries and sold at a premium."),
("What does TGSEB mean?", "Tellicherry Garbled Special Extra Bold: the largest Indian black pepper grade, with berries 4.8 mm and above."),
("Why is Indian black pepper more expensive than Vietnamese?", "India's production costs are higher, and Indian pepper is mostly sold on flavour, pungency and well-known grades, while Vietnam competes on large volumes at lower prices."))))

POSTS.append(dict(
slug="leather-shoe-manufacturers-india", view="blog-leather-shoes",
title="Leather Shoe Manufacturers in India: Agra, Kanpur and Tamil Nadu",
seo_title="Leather Shoe Manufacturers in India: Guide | Teak & Tide",
desc="Sourcing leather shoes from India: Agra, Kanpur, Chennai and Ambur clusters, Goodyear welted vs cemented construction, MOQs, sizing and chemical tests.",
crumb="Leather shoe manufacturers in India", eyebrow="Leather goods · Buyer guide",
sub="Where Indian leather footwear is made, how construction affects price, and what to check before bulk production.",
mins=7, tag="LEATHER FOOTWEAR",
cta_t="Looking for a leather shoe manufacturer in India?",
cta_p="Send us your designs or samples, target price and sizes. We find factories that make your construction type, manage sampling and inspect before shipment.",
cat_href="/leather-goods/", cat_label="Leather goods we source",
wa_text="I want to source leather shoes from India.",
card="Agra, Kanpur and Tamil Nadu clusters, shoe construction types, MOQs, sizing and chemical tests.",
body='''
    <p>India is one of the world's largest producers of footwear and has a deep leather industry, from tanneries to finished shoes. European, UK and US brands buy Indian men's formal shoes, boots, sandals, safety shoes and women's footwear, often under their own label. Indian factories are a good fit for leather shoes in particular, because the leather supply is local.</p>

    <h2>Main footwear clusters</h2>
    <ul>
      <li><strong>Agra (Uttar Pradesh):</strong> one of India's biggest shoe-making centres, strong in men's leather shoes and formal styles.</li>
      <li><strong>Kanpur (Uttar Pradesh):</strong> a major tannery hub, also making safety shoes and heavy-duty footwear.</li>
      <li><strong>Chennai, Ambur, Vaniyambadi and Ranipet (Tamil Nadu):</strong> a large export cluster with tanneries and shoe factories supplying many European brands.</li>
      <li><strong>Kolkata (West Bengal):</strong> tanneries and footwear units, including leather sandals and casual shoes.</li>
    </ul>

    <h2>Construction decides price</h2>
    <ul>
      <li><strong>Cemented:</strong> the sole is glued on. Lighter and cheaper, common for casual and fashion shoes.</li>
      <li><strong>Goodyear welted:</strong> the sole is stitched to a welt, so the shoe can be resoled. More labour, higher price, used for premium formal shoes and boots.</li>
      <li><strong>Blake stitched:</strong> sleeker profile than Goodyear, also resoleable.</li>
      <li><strong>Moccasin and hand-stitched:</strong> for loafers and driving shoes.</li>
    </ul>
    <p>Not every factory does every construction, so ask what they make day to day, not what they can try.</p>

    <h2>MOQ and sizing</h2>
    <p>Factories usually set a minimum per style and colour, commonly a few hundred pairs, and spread across a size run. Agree the size system (UK, EU or US) and the last early, because a wrong last means every pair fits badly. Ask for a full size set of samples, not just one size, before you approve bulk production.</p>

    <h2>Tests and compliance</h2>
    <ul>
      <li><strong>Chromium VI:</strong> restricted in leather in the EU and UK. Ask for a test from an accredited lab.</li>
      <li><strong>Azo dyes and other restricted chemicals</strong> under REACH and your brand's restricted substances list</li>
      <li><strong>Physical tests:</strong> sole bond strength, flexing, colour fastness and slip resistance for safety shoes</li>
      <li><strong>Safety shoes:</strong> must be certified to your market's safety footwear standard</li>
    </ul>

    <h2>Trade deals</h2>
    <p>Leather and footwear are among the sectors expected to get duty-free access to the EU once the EU-India free trade agreement enters into force, which could make Indian shoes more competitive for European buyers. The UK-India trade agreement also covers footwear. Check the current rate for your product code when you order.</p>

    <h2>Checking the factory</h2>
    <p>Verify GST and the Import Export Code, see the production line on a live video call, check membership of the Council for Leather Exports, and inspect finished pairs before the balance payment. Our guides to <a href="/blog/private-label-leather-goods-india/">private label leather goods</a> and <a href="/blog/leather-bag-manufacturers-india/">leather bag manufacturers</a> cover the rest of the leather range.</p>
    ''' + AGENT + faq(
("Where are leather shoes made in India?", "The main clusters are Agra and Kanpur in Uttar Pradesh, Chennai, Ambur, Vaniyambadi and Ranipet in Tamil Nadu, and Kolkata in West Bengal."),
("What is the MOQ for leather shoes from India?", "It varies by factory, but minimums are usually set per style and colour, commonly a few hundred pairs spread across a size run."),
("Which tests do leather shoes need for Europe?", "At minimum chromium VI and restricted azo dyes under REACH, plus physical tests such as sole bond strength and colour fastness. Safety shoes need certification to the EU safety footwear standard."))))

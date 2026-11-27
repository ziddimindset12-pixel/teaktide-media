POSTS = []

def faq(*qa):
    return '\n    <h2>Frequently asked questions</h2>\n    <div class="faq">' + ''.join(
        f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in qa) + '</div>'

AGENT = '<p>Not sure where to start? A <a href="/sourcing-agent-in-india/">sourcing agent in India</a> or <a href="/buying-agent-in-india/">buying agent</a> can shortlist suppliers, check samples and inspect goods before you pay the balance.</p>'

# ---------------- COUNTRY GUIDES ----------------
POSTS.append(dict(
slug="import-from-india-to-germany", view="blog-germany-import",
title="How to Import from India to Germany: EORI, Duty, VAT and Product Rules",
seo_title="How to Import from India to Germany (2026) | Teak & Tide",
desc="Importing from India to Germany: EORI, EU duty and the EU-India trade deal, 19% import VAT, food and textile rules, shipping to Hamburg and supplier checks.",
crumb="Import from India to Germany", eyebrow="Germany buyers · Import guide",
sub="What a German business needs to set up, what it will pay, and which EU rules matter for Indian products.",
mins=7, tag="GERMANY IMPORT",
cta_t="Buying from India for Germany?",
cta_p="We find and verify Indian suppliers, approve samples with you, inspect goods before shipment and make sure the documents your German customs broker needs are complete.",
cat_href="/sourcing-from-india-for-european-buyers/", cat_label="Sourcing for European buyers",
wa_text="I want to import from India to Germany.",
card="EORI, EU duty, German import VAT, food and textile rules, and shipping from India to Hamburg.",
body='''
    <p>Germany is one of India's largest trading partners in Europe. German companies buy Indian textiles and home furnishings, leather goods, spices and tea, auto components, machinery parts, chemicals and handicrafts. Because Germany is in the EU, most of the rules below are EU rules, with a few German additions.</p>

    <h2>1. Get an EORI number</h2>
    <p>Every business that imports into the EU needs an <strong>EORI number</strong>. In Germany you apply to the German customs administration (Zoll). It is free, and your customs broker cannot file the import declaration without it.</p>

    <h2>2. Find the EU duty rate</h2>
    <p>Duty is set at EU level and the same in every member state. Look up your product's code in the EU's <strong>TARIC</strong> database. Many raw materials and some spices are duty-free or low; clothing is often 12% and footwear can be higher.</p>
    <p>India gets lower rates on some products under the EU's GSP scheme, but several Indian sectors, including many textiles, are "graduated" and pay the normal rate. The EU and India concluded negotiations on a free trade agreement in early 2026, but the agreement has to be signed and ratified before its duty cuts apply. Until then, price your products on today's TARIC rate.</p>

    <h2>3. Add German import VAT</h2>
    <p>Germany charges import VAT (Einfuhrumsatzsteuer) of <strong>19%</strong>, or <strong>7%</strong> on most food. It is charged on the customs value plus duty and freight to the EU border. VAT-registered businesses can normally reclaim it.</p>

    <h2>4. Check the product rules</h2>
    <ul>
      <li><strong>Food and spices:</strong> must meet EU limits for pesticide residues, aflatoxins and contaminants. Some Indian spices and herbs are on the EU list for increased border checks, so ask for lab reports from an accredited lab before shipment.</li>
      <li><strong>Textiles and leather:</strong> the EU REACH rules restrict certain azo dyes, chromium VI in leather and other chemicals. Fibre content labels are required for textiles.</li>
      <li><strong>Toys, electrical goods and cosmetics:</strong> need CE marking or EU cosmetic registration before they can be sold.</li>
      <li><strong>Supply chain due diligence:</strong> larger German buyers have legal duties to check human rights and environmental risks in their supply chain. Even smaller buyers are often asked about it by their retail customers. See our <a href="/ethical-sourcing-india/">ethical sourcing</a> guide.</li>
    </ul>

    <h2>5. Shipping from India to Germany</h2>
    <p>Sea freight usually leaves from Nhava Sheva (Mumbai) or Mundra and arrives in Hamburg or Bremerhaven. Transit times depend on the route and are often around four to six weeks. Air freight from Delhi or Mumbai to Frankfurt is much faster and suits samples and urgent, high-value orders. Use our <a href="/free-tools/">CBM and landed cost calculators</a> to compare options.</p>

    <h2>6. Vet the supplier</h2>
    <p>Check the supplier's GST registration and Import Export Code (IEC), ask for a live video call from the factory, approve production samples, and pay the balance only after a pre-shipment inspection. Our guide on <a href="/blog/how-to-find-suppliers-in-india/">how to find and verify suppliers in India</a> has the full checklist.</p>
    ''' + AGENT + faq(
("Do I need a licence to import from India to Germany?", "Most goods need only an EORI number and a correct customs declaration. Food, cosmetics, medicines, plants, and some chemicals and electrical goods have extra registration or certification rules."),
("Is there a free trade agreement between India and Germany?", "Trade deals are made at EU level. The EU and India concluded negotiations on a free trade agreement in early 2026, but it must be signed and ratified before lower duties apply. Check TARIC for the rate that applies on your import date."),
("How much is import VAT in Germany?", "The standard rate is 19% and the reduced rate, used for most food, is 7%. It is charged on the customs value plus duty and transport costs to the EU border."))))

POSTS.append(dict(
slug="import-from-india-to-netherlands", view="blog-netherlands-import",
title="How to Import from India to the Netherlands: Rotterdam, Duty and VAT Deferment",
seo_title="Import from India to the Netherlands | Teak & Tide",
desc="Importing from India to the Netherlands: EORI, EU duty, 21% VAT and the Article 23 deferment licence, shipping via Rotterdam and supplier checks.",
crumb="Import from India to the Netherlands", eyebrow="Netherlands buyers · Import guide",
sub="Why many EU importers clear Indian goods through Rotterdam, and how the Dutch VAT system helps cash flow.",
mins=6, tag="NETHERLANDS",
cta_t="Buying from India for the Netherlands or EU?",
cta_p="We shortlist and verify Indian suppliers, approve samples, inspect goods before shipment and coordinate export documents with your Dutch forwarder.",
cat_href="/sourcing-from-india-for-european-buyers/", cat_label="Sourcing for European buyers",
wa_text="I want to import from India to the Netherlands.",
card="EORI, EU duty, Article 23 VAT deferment, Rotterdam shipping and supplier checks for Dutch importers.",
body='''
    <p>The Netherlands imports far more from India than its size suggests, because <strong>Rotterdam</strong> is Europe's biggest port and a main entry point for goods heading to Germany, Belgium and the rest of the EU. Dutch companies buy Indian spices, nuts, rice, textiles, home décor, leather goods and chemicals, often for distribution across Europe.</p>

    <h2>1. EORI number</h2>
    <p>Apply for an <strong>EORI number</strong> with Dutch Customs (Douane). It is free and required for any EU import declaration. Non-EU companies importing into the Netherlands often appoint a fiscal representative.</p>

    <h2>2. Duty: the EU tariff</h2>
    <p>Duty rates are the same across the EU. Look up your product in the EU's <strong>TARIC</strong> database. Some Indian products get GSP preferences, but many sectors are excluded. The EU-India free trade agreement concluded in early 2026 is not yet in force, so price on current rates.</p>

    <h2>3. Import VAT and the Article 23 licence</h2>
    <p>Dutch import VAT is <strong>21%</strong>, or <strong>9%</strong> for most food. The big advantage of importing through the Netherlands is the <strong>Article 23 licence</strong> (VAT deferment). With it, you don't pay import VAT at the border. You declare and reclaim it in the same VAT return, so it never ties up your cash. Ask your Dutch customs broker or fiscal representative about it.</p>

    <h2>4. Food and product rules</h2>
    <ul>
      <li><strong>Food:</strong> the Dutch food authority (NVWA) carries out EU border checks. Indian spices, herbs and some nuts may face increased checks for pesticide residues, aflatoxins and ethylene oxide, so test before shipment.</li>
      <li><strong>Organic:</strong> organic food must come with an EU electronic certificate of inspection (COI) issued through the TRACES system.</li>
      <li><strong>Non-food:</strong> REACH chemical limits, CE marking for regulated goods, and textile fibre labelling all apply as in the rest of the EU.</li>
    </ul>

    <h2>5. Shipping</h2>
    <p>Most sea freight goes from Nhava Sheva or Mundra to Rotterdam, usually in about four to six weeks depending on routing. From Rotterdam, goods can move under customs transit to warehouses across Europe, or into a bonded warehouse until you sell them. Air freight goes to Amsterdam Schiphol.</p>

    <h2>6. Vet the supplier</h2>
    <p>Check GST and IEC, get a factory video call, approve samples and inspect before the final payment. See <a href="/supplier-verification-india/">supplier verification in India</a>.</p>
    ''' + AGENT + faq(
("Why do importers use Rotterdam for Indian goods?", "Rotterdam is Europe's largest port, with frequent sailings from India and good rail, road and barge links across the EU. Goods can be cleared there or moved under transit to another EU country."),
("What is the Article 23 licence?", "It is a Dutch VAT deferment licence. Instead of paying import VAT at the border, the importer reports it in the periodic VAT return and deducts it at the same time, which helps cash flow."),
("What is the import VAT rate in the Netherlands?", "21% is the standard rate and 9% is the reduced rate that applies to most food."))))

POSTS.append(dict(
slug="import-from-india-to-saudi-arabia", view="blog-saudi-import",
title="How to Import from India to Saudi Arabia: SABER, SFDA, Duty and VAT",
seo_title="How to Import from India to Saudi Arabia | Teak & Tide",
desc="Importing from India to Saudi Arabia: registration, SABER certificates, SFDA food rules, duty, 15% VAT, Arabic labels and shipping to Jeddah.",
crumb="Import from India to Saudi Arabia", eyebrow="Saudi buyers · Import guide",
sub="The registrations, certificates and labels Saudi customs will ask for, so your Indian goods are cleared without delays.",
mins=7, tag="SAUDI ARABIA",
cta_t="Buying from India for Saudi Arabia?",
cta_p="We find and verify Indian suppliers, check samples and Arabic labelling, inspect goods before shipment and coordinate the documents needed for SABER and customs.",
cat_href="/sourcing-from-india-for-uae-buyers/", cat_label="Sourcing for Gulf buyers",
wa_text="I want to import from India to Saudi Arabia.",
card="Commercial registration, SABER certificates, SFDA rules, duty, VAT and shipping from India to Saudi Arabia.",
body='''
    <p>Saudi Arabia is one of India's biggest trading partners. Saudi importers buy Indian basmati rice, spices, tea, meat, textiles and clothing, home furnishings, building materials, auto parts and machinery. Shipping is short, and demand keeps growing with Vision 2030 projects and a large Indian community.</p>

    <h2>1. Registration</h2>
    <p>To import commercially you need a <strong>commercial registration (CR)</strong> from the Ministry of Commerce and an importer account with ZATCA (the Zakat, Tax and Customs Authority). Most importers work with a licensed customs broker in Jeddah, Dammam or Riyadh.</p>

    <h2>2. SABER: product and shipment certificates</h2>
    <p>Most consumer and industrial goods regulated by SASO need conformity certificates issued through the <strong>SABER</strong> platform:</p>
    <ul>
      <li>a <strong>Product Certificate of Conformity</strong> for each regulated product, and</li>
      <li>a <strong>Shipment Certificate</strong> for each consignment.</li>
    </ul>
    <p>Certificates are issued by approved conformity bodies, and some products need testing first. Without them, goods can be held at the port, so sort this out before the supplier ships.</p>

    <h2>3. Food: SFDA rules</h2>
    <p>Food, cosmetics and health products are regulated by the <strong>SFDA</strong>. Expect registration of the importer and products, shelf-life and labelling checks, and Arabic labels. Meat and some other foods also need halal certificates from approved bodies.</p>

    <h2>4. Duty and VAT</h2>
    <p>Saudi Arabia applies the GCC common external tariff, but it has raised duties on many products above the common 5% base rate. Check your product code in the Saudi customs tariff. On top of duty, imports pay <strong>15% VAT</strong>. India and the GCC have been negotiating a free trade agreement, but it is not in force, so Indian goods pay the normal rate.</p>

    <h2>5. Shipping</h2>
    <p>Sea freight from Nhava Sheva or Mundra reaches Jeddah (Red Sea) or Dammam (Gulf) quickly compared with most routes, often in one to two weeks. Air freight from Delhi or Mumbai to Riyadh and Jeddah is quick and suits samples.</p>

    <h2>6. Arabic labels and documents</h2>
    <p>Retail goods need Arabic (or Arabic and English) labels with the product name, origin, importer details and, for food, production and expiry dates. Ask your supplier to apply labels in India, which is usually cheaper than relabelling in Saudi Arabia. Invoices must match the packing list and the certificate of origin.</p>

    <h2>7. Vet the supplier</h2>
    <p>Check GST and IEC, ask for a factory video call, approve samples and inspect before final payment. See <a href="/quality-inspection-india/">quality inspection in India</a>.</p>
    ''' + AGENT + faq(
("What is SABER?", "SABER is Saudi Arabia's online product conformity platform. Regulated products need a Product Certificate of Conformity, and each shipment needs a Shipment Certificate before customs clearance."),
("What is the VAT rate on imports into Saudi Arabia?", "Imports pay 15% VAT, calculated on the customs value plus duty."),
("Do Indian food products need Arabic labels in Saudi Arabia?", "Yes. Retail food must carry Arabic labelling that meets SFDA rules, including product name, ingredients, origin, importer and production and expiry dates."))))

POSTS.append(dict(
slug="import-from-india-to-singapore", view="blog-singapore-import",
title="How to Import from India to Singapore: GST, Permits and the CECA",
seo_title="Import from India to Singapore (2026) | Teak & Tide",
desc="Importing from India to Singapore: customs account, TradeNet permits, 9% GST, the India-Singapore CECA, SFA food licences and shipping times.",
crumb="Import from India to Singapore", eyebrow="Singapore buyers · Import guide",
sub="Singapore charges almost no duty, but permits, GST and food rules still need to be right.",
mins=6, tag="SINGAPORE",
cta_t="Buying from India for Singapore or Southeast Asia?",
cta_p="We shortlist and verify Indian suppliers, approve samples, inspect goods before shipment and coordinate documents with your Singapore declaring agent.",
cat_href="/sourcing-agent-in-india/", cat_label="Our sourcing service",
wa_text="I want to import from India to Singapore.",
card="Customs account, TradeNet permits, 9% GST, CECA, SFA food rules and shipping from India to Singapore.",
body='''
    <p>Singapore is a major buyer of Indian goods and a re-export hub for Southeast Asia. Companies there import Indian rice, spices, vegetables, textiles, jewellery, machinery parts and household goods, either for the local market or to ship on to Malaysia, Indonesia and beyond.</p>

    <h2>1. UEN and customs account</h2>
    <p>Your business needs a <strong>Unique Entity Number (UEN)</strong> from ACRA, and you must activate a <strong>customs account</strong> with Singapore Customs. Import permits are filed through the TradeNet system, usually by a declaring agent such as your freight forwarder.</p>

    <h2>2. Duty: almost none</h2>
    <p>Singapore is a free port. Customs duty applies only to a short list of goods: alcohol, tobacco, motor vehicles and petroleum products. Almost everything else from India enters duty-free. India and Singapore also have a trade agreement, the <strong>CECA</strong>, in force since 2005.</p>

    <h2>3. GST</h2>
    <p>Imports pay <strong>9% GST</strong> on the CIF value plus any duty. GST-registered businesses can claim it back. Businesses that import often may use schemes that suspend GST at import, so ask your accountant.</p>

    <h2>4. Food and controlled goods</h2>
    <ul>
      <li><strong>Food:</strong> commercial food importers need a licence or registration with the Singapore Food Agency (SFA), and each consignment must be declared. Some food, such as meat, needs extra approval.</li>
      <li><strong>Health products and cosmetics:</strong> regulated by the Health Sciences Authority (HSA).</li>
      <li><strong>Controlled and strategic goods:</strong> need extra permits, so check before ordering.</li>
    </ul>

    <h2>5. Shipping</h2>
    <p>Singapore is close to India's east and west coasts, with frequent sailings from Chennai, Nhava Sheva and Mundra. Sea transit is often around one to two weeks. Air freight from Delhi, Mumbai or Chennai takes a few hours of flying and suits samples and fresh produce.</p>

    <h2>6. Vet the supplier</h2>
    <p>Low duty doesn't remove supplier risk. Check GST and IEC, get a factory video call, approve samples, and pay the balance after a pre-shipment inspection. Read <a href="/blog/how-to-choose-a-sourcing-agent-in-india/">how to choose a sourcing agent in India</a>.</p>
    ''' + AGENT + faq(
("Is there import duty on goods from India to Singapore?", "For most goods, no. Singapore charges duty only on alcohol, tobacco, motor vehicles and petroleum products. Imports still pay 9% GST."),
("Do I need a permit to import into Singapore?", "Yes. Every import needs a customs permit filed through TradeNet, usually by a declaring agent, and your business must have an activated customs account."),
("Does Singapore have a trade agreement with India?", "Yes. The India-Singapore Comprehensive Economic Cooperation Agreement (CECA) has been in force since 2005."))))

POSTS.append(dict(
slug="import-from-india-to-new-zealand", view="blog-nz-import",
title="How to Import from India to New Zealand: Customs, GST and Biosecurity",
seo_title="How to Import from India to New Zealand | Teak & Tide",
desc="Importing from India to New Zealand: customs client code, duty, 15% GST, strict MPI biosecurity rules for wood and food, and shipping to Auckland.",
crumb="Import from India to New Zealand", eyebrow="New Zealand buyers · Import guide",
sub="New Zealand's biosecurity rules are some of the strictest in the world. Here is how to get Indian goods through.",
mins=6, tag="NEW ZEALAND",
cta_t="Buying from India for New Zealand?",
cta_p="We find and verify Indian suppliers, check samples, confirm treatment and packing for biosecurity, and inspect goods before shipment.",
cat_href="/sourcing-from-india-for-australian-buyers/", cat_label="Sourcing for Australia & NZ",
wa_text="I want to import from India to New Zealand.",
card="Customs client code, duty, 15% GST, MPI biosecurity rules and shipping from India to New Zealand.",
body='''
    <p>New Zealand businesses import Indian clothing, textiles, rugs, spices, rice, tea, jewellery, furniture and handicrafts. A growing Indian community has also increased demand for Indian food and household products.</p>

    <h2>1. Customs client code</h2>
    <p>Regular importers should get a <strong>customs client code</strong> from the New Zealand Customs Service. Most use a licensed customs broker, who lodges the import entry for them.</p>

    <h2>2. Duty and GST</h2>
    <p>Many goods enter New Zealand duty-free, and others usually pay modest rates. Check your product's code in the New Zealand Working Tariff. India and New Zealand have been negotiating a free trade agreement, so check whether it is in force for your product before you price. Imports also pay <strong>15% GST</strong>, plus small customs and biosecurity fees on each entry.</p>

    <h2>3. Biosecurity (MPI): the big one</h2>
    <p>The Ministry for Primary Industries (MPI) protects New Zealand from pests and diseases, and it is strict. Rules are set in <strong>Import Health Standards</strong> for each type of product.</p>
    <ul>
      <li><strong>Wooden goods and handicrafts:</strong> must be free of bark, insects and soil. Some need fumigation or heat treatment with certificates.</li>
      <li><strong>Wooden pallets and crates:</strong> must be ISPM 15 treated and stamped.</li>
      <li><strong>Food, spices, seeds and plant products:</strong> many need permits, treatment or inspection. Some are not allowed at all.</li>
      <li><strong>Containers:</strong> must arrive clean, with no soil or plant material inside or out.</li>
    </ul>
    <p>Goods that don't comply can be treated, re-shipped or destroyed at your cost, so check the Import Health Standard before you order.</p>

    <h2>4. Shipping</h2>
    <p>There are few direct sailings from India, so sea freight usually transships in Singapore or another Asian hub before reaching Auckland, Tauranga or Lyttelton. Allow several weeks. For small orders, compare LCL with air freight to Auckland.</p>

    <h2>5. Vet the supplier</h2>
    <p>Check GST and IEC, get a factory video call, approve samples and inspect before the final payment. Make sure the supplier understands fumigation and packing requirements for New Zealand.</p>
    ''' + AGENT + faq(
("Why is New Zealand strict about wooden products from India?", "Wood and plant material can carry insects and diseases. MPI's Import Health Standards require clean, treated goods and certified packaging, and non-compliant goods are treated, re-shipped or destroyed at the importer's cost."),
("What is the GST on imports into New Zealand?", "Imports pay 15% GST, calculated on the customs value plus duty and freight and insurance."),
("How long does shipping from India to New Zealand take?", "Sea freight usually transships in an Asian hub and takes several weeks. Air freight to Auckland is much faster and suits samples and small orders."))))

# ---------------- PRODUCT GUIDES ----------------
POSTS.append(dict(
slug="turmeric-suppliers-india", view="blog-turmeric",
title="Turmeric Suppliers in India: Erode, Nizamabad and Lakadong Explained",
seo_title="Turmeric Suppliers in India: Buyer's Guide | Teak & Tide",
desc="Buying turmeric from India: Erode, Nizamabad and Lakadong varieties, curcumin, fingers vs powder, lead and ethylene oxide tests, and supplier checks.",
crumb="Turmeric suppliers in India", eyebrow="Spices · Buyer guide",
sub="Fingers, powder or high-curcumin: what to specify and which tests to insist on before you import turmeric.",
mins=6, tag="TURMERIC",
cta_t="Looking for a turmeric supplier in India?",
cta_p="Tell us the variety, form, curcumin level and quantity. We shortlist exporters, get lab-tested samples and inspect before shipment.",
cat_href="/spices/", cat_label="Spices we source",
wa_text="I want to source turmeric from India.",
card="Turmeric varieties, curcumin, fingers vs powder, lab tests and supplier checks for buyers.",
body='''
    <p>India grows most of the world's turmeric and is also its biggest exporter. Buyers range from spice packers and food manufacturers to supplement brands looking for high-curcumin roots. The right supplier depends on which turmeric you need.</p>

    <h2>Main growing regions</h2>
    <ul>
      <li><strong>Erode (Tamil Nadu):</strong> India's best-known turmeric market, with bright yellow fingers popular with spice packers.</li>
      <li><strong>Nizamabad (Telangana):</strong> a large trading hub with high volumes at competitive prices.</li>
      <li><strong>Sangli (Maharashtra):</strong> another major market, known for good colour.</li>
      <li><strong>Lakadong (Meghalaya):</strong> a small-volume variety known for high curcumin, popular with health and supplement brands.</li>
      <li><strong>Alleppey (Kerala):</strong> deep colour and higher oil, often used for oleoresin and extracts.</li>
    </ul>

    <h2>Forms you can buy</h2>
    <ul>
      <li><strong>Whole fingers and bulbs:</strong> polished or unpolished, for grinding at destination</li>
      <li><strong>Powder:</strong> in bulk bags or retail packs, with a set mesh size</li>
      <li><strong>Cut or sliced:</strong> for teas and blends</li>
      <li><strong>Organic:</strong> certified under India's NPOP and, for the EU or US, the buyer market's organic rules</li>
    </ul>

    <h2>What to specify</h2>
    <p>Write down curcumin content (tested by HPLC, not just "high"), moisture, mesh size for powder, colour value, packing and whether you need steam sterilisation. Ask every supplier to quote on the same specification so prices can be compared.</p>

    <h2>Tests to insist on</h2>
    <ul>
      <li><strong>Lead and lead chromate:</strong> turmeric has a history of colour adulteration, so test for lead every time</li>
      <li><strong>Pesticide residues:</strong> against your market's limits (EU limits are strict)</li>
      <li><strong>Ethylene oxide:</strong> required by many EU and UK buyers</li>
      <li><strong>Aflatoxins and microbiology:</strong> especially for powder</li>
    </ul>
    <p>Use a lab report from an accredited lab on a sample from <em>your</em> lot, not a general certificate.</p>

    <h2>Checking the supplier</h2>
    <p>Spice exporters in India must register with the <strong>Spices Board</strong>. Also check GST, IEC and FSSAI licences, ask for a factory video call and inspect before shipment. See our guide to <a href="/blog/how-to-import-spices-from-india/">importing spices from India</a> and <a href="/blog/indian-spices-wholesale-bulk/">buying Indian spices wholesale</a>.</p>
    ''' + AGENT + faq(
("Which Indian turmeric has the most curcumin?", "Lakadong turmeric from Meghalaya is known for high curcumin, often well above common commercial varieties. Always confirm the level with an HPLC lab test on your lot."),
("What tests should I ask for when importing turmeric?", "At minimum: lead, pesticide residues, aflatoxins, microbiology and, for EU and UK buyers, ethylene oxide. Ask for results from an accredited lab on a sample from your shipment."),
("Do Indian turmeric exporters need registration?", "Yes. Spice exporters must register with the Spices Board of India and also hold GST, an Import Export Code and an FSSAI food licence."))))

POSTS.append(dict(
slug="rug-dhurrie-manufacturers-india", view="blog-rugs",
title="Rug and Dhurrie Manufacturers in India: Panipat, Bhadohi and Jaipur",
seo_title="Rug Manufacturers in India: Buyer's Guide | Teak & Tide",
desc="Sourcing rugs from India: Panipat dhurries, Bhadohi hand-knotted and tufted rugs, Jaipur designs, materials, MOQs and quality checks.",
crumb="Rug manufacturers in India", eyebrow="Home textiles · Buyer guide",
sub="Hand-knotted, tufted or flat-weave: where each type is made and what to check before you order.",
mins=7, tag="RUGS",
cta_t="Looking for a rug manufacturer in India?",
cta_p="Send your designs, sizes and quantities. We shortlist manufacturers in Panipat, Bhadohi or Jaipur, approve strike-offs and samples and inspect before shipment.",
cat_href="/textiles/", cat_label="Textiles we source",
wa_text="I want to source rugs from India.",
card="Rug types, the Panipat, Bhadohi and Jaipur clusters, materials, MOQs and quality checks.",
body='''
    <p>India is one of the world's largest exporters of handmade rugs and carpets. Furniture retailers, interior designers and online home brands buy Indian rugs because of the range of handmade techniques and the ability to make custom designs in modest quantities.</p>

    <h2>Main rug clusters</h2>
    <ul>
      <li><strong>Bhadohi and Mirzapur (Uttar Pradesh):</strong> India's "carpet belt", known for hand-knotted and hand-tufted wool rugs.</li>
      <li><strong>Panipat (Haryana):</strong> flat-weave dhurries, kilims, cotton and recycled-yarn rugs, bath mats and throws.</li>
      <li><strong>Jaipur (Rajasthan):</strong> design-led hand-knotted and flat-weave rugs, popular with boutique brands.</li>
      <li><strong>Agra, Kashmir and others:</strong> smaller hubs, including fine silk and wool carpets.</li>
    </ul>

    <h2>Types of rugs</h2>
    <ul>
      <li><strong>Hand-knotted:</strong> the most durable and expensive; priced by knot density</li>
      <li><strong>Hand-tufted:</strong> made with a tufting gun on a backing cloth; faster and cheaper than knotted</li>
      <li><strong>Flat-weave (dhurrie, kilim):</strong> no pile, reversible, light and easy to ship</li>
      <li><strong>Braided and jute rugs:</strong> natural, casual styles</li>
      <li><strong>Recycled PET and indoor-outdoor rugs:</strong> a growing Panipat speciality</li>
    </ul>

    <h2>What to specify</h2>
    <p>Size and tolerance, material (wool, cotton, jute, viscose, recycled PET), construction, pile height, weight per square metre, colours (with Pantone or yarn poms), backing for tufted rugs, and packing. For new designs, approve a small <strong>strike-off</strong> or sample before production.</p>

    <h2>MOQs and lead times</h2>
    <p>Many manufacturers accept a small number of pieces per design for handmade rugs, especially flat-weaves. Hand-knotted rugs take longest, often a couple of months or more, because each piece is woven by hand.</p>

    <h2>Quality checks before shipment</h2>
    <ul>
      <li>Size, shape and squareness</li>
      <li>Colour match to the approved sample</li>
      <li>Weight and pile height</li>
      <li>Backing glue and smell on tufted rugs</li>
      <li>Shedding, loose ends and edge finishing</li>
    </ul>

    <h2>Child-labour-free sourcing</h2>
    <p>Handmade carpets have a history of child labour risk. Ask about certifications such as <strong>GoodWeave</strong>, visit or video-call the weaving units, and make audits part of the order. Read our <a href="/ethical-sourcing-india/">ethical sourcing</a> guide. Exporters are usually members of the Carpet Export Promotion Council (CEPC).</p>
    ''' + AGENT + faq(
("Where are most rugs made in India?", "Bhadohi and Mirzapur in Uttar Pradesh for hand-knotted and tufted rugs, Panipat in Haryana for flat-weaves, dhurries and recycled rugs, and Jaipur for design-led handmade rugs."),
("What is the difference between hand-knotted and hand-tufted rugs?", "Hand-knotted rugs are woven knot by knot and last longest. Hand-tufted rugs are made by punching yarn into a backing cloth with a tufting gun, which is faster and cheaper."),
("Can I order custom rug designs in small quantities?", "Often yes. Many Indian manufacturers make custom designs from a few pieces per design, especially for flat-weaves, after a strike-off or sample is approved."))))

POSTS.append(dict(
slug="leather-wallet-belt-manufacturers-india", view="blog-wallets",
title="Leather Wallet and Belt Manufacturers in India: Kolkata, Kanpur and Delhi NCR",
seo_title="Leather Wallet and Belt Makers in India | Teak & Tide",
desc="Sourcing leather wallets and belts from India: Kolkata, Kanpur and Delhi NCR makers, leather types, tanning, private label MOQs and quality checks.",
crumb="Leather wallet & belt manufacturers in India", eyebrow="Leather · Buyer guide",
sub="Small leather goods for private label brands: what to specify, where to buy and what to check.",
mins=6, tag="LEATHER",
cta_t="Looking for a wallet or belt manufacturer?",
cta_p="Send your design, leather type and quantity. We shortlist manufacturers, approve samples and logo work, and inspect before shipment.",
cat_href="/leather-goods/", cat_label="Leather goods we source",
wa_text="I want to source leather wallets or belts from India.",
card="Wallet and belt clusters, leather types, tanning, RFID, MOQs and quality checks for private label buyers.",
body='''
    <p>India is one of the world's biggest producers of leather and leather goods. Small leather goods such as wallets, card holders, belts, passport covers and key cases are a good fit for private label brands, because they need less material and tooling than bags and can be made in modest quantities.</p>

    <h2>Main clusters</h2>
    <ul>
      <li><strong>Kolkata (West Bengal):</strong> a major hub for wallets, card holders and other small leather goods, with many export units around the Bantala leather complex.</li>
      <li><strong>Kanpur (Uttar Pradesh):</strong> known for heavy leathers, belts, saddlery and harness goods.</li>
      <li><strong>Delhi NCR (Noida and surroundings):</strong> fashion accessories and private label work for export brands.</li>
      <li><strong>Chennai, Ambur and Vaniyambadi (Tamil Nadu):</strong> large tanneries, mostly serving footwear and garments.</li>
    </ul>

    <h2>Leather and finish</h2>
    <ul>
      <li><strong>Full-grain, top-grain or split:</strong> full-grain is the most durable and ages best</li>
      <li><strong>Cow, buffalo or goat:</strong> goat is soft and thin; buffalo is strong and textured</li>
      <li><strong>Vegetable-tanned or chrome-tanned:</strong> veg-tan suits a natural, heritage look; chrome-tan is softer and more colour-stable</li>
      <li><strong>Hunter, crazy-horse, saffiano and other finishes</strong></li>
    </ul>

    <h2>What to specify</h2>
    <p>Design drawing with dimensions, card slot count, leather type and thickness, lining, stitching (machine or hand), edge finish, hardware for belts (buckle material and plating), RFID blocking lining if needed, logo method (emboss, deboss or foil) and packaging.</p>

    <h2>MOQs</h2>
    <p>Private label wallet and belt orders often start from a few hundred pieces per design, with lower MOQs possible if you use the manufacturer's stock leathers and colours.</p>

    <h2>Quality checks</h2>
    <ul>
      <li>Leather grade and thickness match the approved sample</li>
      <li>Even stitching with no loose threads</li>
      <li>Smooth, sealed edges</li>
      <li>Card slots fit standard cards</li>
      <li>Buckle plating and attachment strength on belts</li>
      <li>Smell and mould: leather must be packed dry, with silica gel</li>
    </ul>

    <h2>Compliance</h2>
    <p>EU and UK buyers will ask for chromium VI and azo dye test reports under REACH. Some brands prefer leather from <strong>Leather Working Group (LWG)</strong> certified tanneries. Exporters are usually registered with the Council for Leather Exports (CLE). Read more in our guides to <a href="/blog/private-label-leather-goods-india/">private label leather goods</a> and <a href="/blog/leather-bag-manufacturers-india/">leather bag manufacturers in India</a>.</p>
    ''' + AGENT + faq(
("Where are leather wallets made in India?", "Kolkata is the biggest hub for wallets and small leather goods. Kanpur is known for belts and heavy leather, and Delhi NCR has many private label accessory makers."),
("What is the MOQ for private label leather wallets from India?", "Often a few hundred pieces per design. Using the manufacturer's stock leathers and colours can lower the minimum."),
("What tests do EU buyers need for leather goods?", "Usually chromium VI and restricted azo dye tests under REACH, from an accredited lab. Some brands also ask for leather from LWG-certified tanneries."))))

POSTS.append(dict(
slug="moringa-powder-suppliers-india", view="blog-moringa",
title="Moringa Powder Suppliers in India: A Buyer's Guide to Quality and Testing",
seo_title="Moringa Powder Suppliers in India | Teak & Tide",
desc="Buying moringa powder from India: Tamil Nadu sources, leaf powder vs tea cut, colour, microbial and heavy metal tests, organic and supplier checks.",
crumb="Moringa powder suppliers in India", eyebrow="Herbs · Buyer guide",
sub="Moringa looks simple, but colour, drying and microbiology decide whether a lot passes in your market.",
mins=5, tag="MORINGA",
cta_t="Looking for a moringa supplier in India?",
cta_p="Tell us the form, grade, certification and quantity. We shortlist processors, get lab-tested samples and inspect before shipment.",
cat_href="/herbs/", cat_label="Herbs we source",
wa_text="I want to source moringa powder from India.",
card="Growing regions, product forms, quality specs, lab tests and supplier checks for moringa buyers.",
body='''
    <p>India is the world's largest producer of moringa (drumstick tree). Moringa leaf powder is bought by supplement brands, health food stores, tea blenders and food manufacturers in the US, Europe, the UK and the Middle East.</p>

    <h2>Where it is grown</h2>
    <p>Most export moringa comes from <strong>Tamil Nadu</strong> (around Theni, Dindigul, Karur and Tiruppur), with more from Andhra Pradesh, Karnataka and Gujarat. Processors dry the leaves, mill them and pack them for export.</p>

    <h2>Forms you can buy</h2>
    <ul>
      <li><strong>Leaf powder:</strong> the main export product, in bulk bags or private label packs</li>
      <li><strong>Tea cut (TBC):</strong> cut dried leaves for tea bags and blends</li>
      <li><strong>Capsules and tablets:</strong> made by contract manufacturers</li>
      <li><strong>Seeds and seed oil:</strong> for cosmetics and food</li>
    </ul>

    <h2>What decides quality</h2>
    <ul>
      <li><strong>Colour:</strong> bright green means careful, low-temperature drying; brown or dull powder suggests poor drying or old stock</li>
      <li><strong>Mesh size:</strong> how fine the powder is</li>
      <li><strong>Moisture:</strong> low moisture keeps the powder stable</li>
      <li><strong>Stem content:</strong> leaf-only powder is better than powder with ground stems</li>
    </ul>

    <h2>Tests to ask for</h2>
    <ul>
      <li><strong>Microbiology:</strong> leaf powder can have high bacterial counts, so many buyers need steam-sterilised lots and tests for total plate count, yeast and mould, E. coli and Salmonella</li>
      <li><strong>Heavy metals:</strong> lead, cadmium, arsenic and mercury</li>
      <li><strong>Pesticide residues:</strong> against your market's limits</li>
    </ul>
    <p>Ask for a lab report on your lot from an accredited lab. If you sell moringa as a supplement, check your market's supplement or novel food rules before you launch.</p>

    <h2>Organic</h2>
    <p>Organic moringa is common. Ask for the NPOP certificate and, for the EU or US, certification for that market. A transaction certificate should cover your shipment.</p>

    <h2>Checking the supplier</h2>
    <p>Check GST, IEC and FSSAI licences, ask for a video call of the drying and milling unit, and inspect before shipment. See our <a href="/blog/ashwagandha-supplier-india/">ashwagandha supplier guide</a> for more on buying Indian herbs.</p>
    ''' + AGENT + faq(
("Where does India's export moringa come from?", "Mostly Tamil Nadu, around Theni, Dindigul, Karur and Tiruppur, with additional supply from Andhra Pradesh, Karnataka and Gujarat."),
("Why is the colour of moringa powder important?", "A bright green colour usually means the leaves were dried carefully at low temperature. Dull or brown powder can mean poor drying, stems mixed in or old stock."),
("Does moringa powder need steam sterilisation?", "Many buyers require it, because dried leaf powder can carry a high microbial load. Ask for test results for total plate count, yeast and mould, E. coli and Salmonella."))))

POSTS.append(dict(
slug="wooden-handicraft-manufacturers-india", view="blog-wooden",
title="Wooden Handicraft Manufacturers in India: Saharanpur, Jodhpur and Channapatna",
seo_title="Wooden Handicraft Manufacturers in India | Teak & Tide",
desc="Sourcing wooden handicrafts from India: Saharanpur carving, Jodhpur mango and sheesham, kiln drying, fumigation, the Lacey Act and EUDR.",
crumb="Wooden handicraft manufacturers in India", eyebrow="Handicrafts · Buyer guide",
sub="Carved décor, serveware, boxes and small furniture: where they are made and how to avoid cracked or rejected shipments.",
mins=6, tag="WOODEN CRAFTS",
cta_t="Looking for wooden handicraft suppliers?",
cta_p="Send photos, sizes and quantities. We shortlist workshops in Saharanpur, Jodhpur and other clusters, approve samples and inspect before shipment.",
cat_href="/handicrafts/", cat_label="Handicrafts we source",
wa_text="I want to source wooden handicrafts from India.",
card="Wood craft clusters, wood types, drying, fumigation, US Lacey Act and EU deforestation rules.",
body='''
    <p>Indian wooden handicrafts, from carved boxes and wall décor to serving boards, bowls and small furniture, sell well with gift shops, home décor brands and hospitality buyers. Each region has its own style and wood.</p>

    <h2>Main clusters</h2>
    <ul>
      <li><strong>Saharanpur (Uttar Pradesh):</strong> India's best-known wood-carving centre, making carved boxes, screens, décor and small furniture, mostly in sheesham and mango wood.</li>
      <li><strong>Jodhpur (Rajasthan):</strong> a large export hub for wooden furniture, décor and serveware in mango, acacia and sheesham.</li>
      <li><strong>Channapatna (Karnataka):</strong> traditional lacquered wooden toys, with a protected geographical indication (GI).</li>
      <li><strong>Hoshiarpur (Punjab):</strong> wood inlay work.</li>
      <li><strong>Moradabad (Uttar Pradesh):</strong> wood combined with metal, alongside its <a href="/blog/brass-handicrafts-moradabad/">brass handicrafts</a>.</li>
    </ul>

    <h2>Common woods</h2>
    <ul>
      <li><strong>Mango wood:</strong> affordable, widely available and popular for serveware and décor</li>
      <li><strong>Sheesham (Indian rosewood):</strong> dense, rich grain, good for carving and furniture</li>
      <li><strong>Acacia:</strong> hard and durable, common in kitchenware</li>
    </ul>

    <h2>Avoiding cracks and mould</h2>
    <p>The most common problem with wooden goods is cracking or mould after arrival in a colder or drier climate. Ask for <strong>kiln-dried</strong> wood with a stated moisture content, check moisture with a meter during inspection, and pack with silica gel and breathable wrapping. For serveware, confirm the finish is food-safe.</p>

    <h2>Export rules to check</h2>
    <ul>
      <li><strong>Fumigation and phytosanitary certificate:</strong> often required for wooden goods; packaging must meet ISPM 15</li>
      <li><strong>US Lacey Act:</strong> US importers must declare the wood species and country of harvest for many wooden products</li>
      <li><strong>EU Deforestation Regulation (EUDR):</strong> covers wood products and requires proof that the wood didn't come from deforested land; check the current application dates</li>
      <li><strong>Australia and New Zealand:</strong> strict biosecurity checks for bark, insects and soil</li>
    </ul>

    <h2>Checking the supplier</h2>
    <p>Check GST and IEC, ask for workshop videos, approve samples and inspect before shipment. Many exporters are members of the Export Promotion Council for Handicrafts (EPCH).</p>
    ''' + AGENT + faq(
("Which Indian city is famous for wood carving?", "Saharanpur in Uttar Pradesh is India's best-known wood-carving centre. Jodhpur in Rajasthan is a major hub for wooden furniture and décor."),
("How do I stop wooden products from cracking after import?", "Buy kiln-dried wood with a stated moisture content, check moisture during inspection, and pack with silica gel and breathable wrapping."),
("Do wooden handicrafts from India need fumigation?", "Often yes, depending on the product and destination. Wooden packaging must meet ISPM 15, and some countries require a phytosanitary certificate or treatment for wooden goods."))))

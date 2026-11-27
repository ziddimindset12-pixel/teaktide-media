PAGES = []

TOOLS_BODY = '''
    <style>
      .tool{border:1px solid rgba(12,51,38,.14);border-radius:16px;padding:22px;margin:26px 0;background:#fff;box-shadow:0 10px 26px rgba(12,51,38,.06)}
      .tool h2{margin-top:0}
      .tool form{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:14px 0}
      .tool label{display:flex;flex-direction:column;font-size:14px;font-weight:600;color:#0c3326;gap:6px}
      .tool input,.tool select{font:inherit;font-weight:400;padding:10px 12px;border:1px solid rgba(12,51,38,.25);border-radius:10px;background:#fbfaf6;min-width:0}
      .tool-out{background:#f4f1e8;border-radius:12px;padding:14px 16px;font-size:15px}
      .tool-out p{margin:4px 0}
      .tool-note{color:#5b6b64;font-size:13px}
      .tool-tip{color:#0c3326;font-weight:600;margin-top:8px!important}
      .tool-table{width:100%;border-collapse:collapse}
      .tool-table td{padding:6px 4px;border-bottom:1px solid rgba(12,51,38,.1)}
      .tool-table td:last-child{text-align:right;white-space:nowrap}
      .tool-total td{font-weight:700;color:#0c3326}
      .tool-jump{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 0}
      .tool-jump a{padding:8px 14px;border-radius:999px;background:#0c3326;color:#fff;text-decoration:none;font-size:14px}
    </style>
    <p>Three quick calculators we use every day when we plan orders for buyers. They run in your browser, nothing is saved or sent anywhere, and you don't need to sign up.</p>
    <div class="tool-jump"><a href="#cbm">CBM &amp; container calculator</a><a href="#landed">Landed cost calculator</a><a href="#gsm">GSM calculator</a></div>

    <div class="tool" id="cbm">
      <h2>CBM and container calculator</h2>
      <p>Enter the outer size of one carton and how many cartons you have. You get the total volume, the volumetric weight for air and courier, and roughly how many cartons fit in each container.</p>
      <form id="tool-cbm">
        <label>Length<input id="cbm-l" type="number" min="0" step="any" inputmode="decimal" value="60"></label>
        <label>Width<input id="cbm-w" type="number" min="0" step="any" inputmode="decimal" value="40"></label>
        <label>Height<input id="cbm-h" type="number" min="0" step="any" inputmode="decimal" value="40"></label>
        <label>Unit<select id="cbm-unit"><option value="cm">cm</option><option value="in">inches</option></select></label>
        <label>Number of cartons<input id="cbm-q" type="number" min="0" step="1" inputmode="numeric" value="100"></label>
        <label>Gross weight per carton (kg)<input id="cbm-kg" type="number" min="0" step="any" inputmode="decimal" value="12"></label>
      </form>
      <div class="tool-out" id="cbm-out" aria-live="polite"></div>
      <p class="tool-note">Container figures use practical loading volumes of about 28 CBM for a 20ft, 58 CBM for a 40ft and 68 CBM for a 40ft high cube. The real number depends on carton shape, pallets and how the container is stuffed.</p>
    </div>

    <div class="tool" id="landed">
      <h2>Landed cost calculator</h2>
      <p>Landed cost is what one unit really costs you once it reaches your warehouse: the supplier price plus freight, insurance, duty, import tax and local charges. Use the same currency in every box.</p>
      <form id="tool-lc">
        <label>Unit price (FOB)<input id="lc-price" type="number" min="0" step="any" inputmode="decimal" value="4.50"></label>
        <label>Quantity<input id="lc-qty" type="number" min="0" step="1" inputmode="numeric" value="2000"></label>
        <label>Freight to your port<input id="lc-freight" type="number" min="0" step="any" inputmode="decimal" value="1200"></label>
        <label>Insurance<input id="lc-ins" type="number" min="0" step="any" inputmode="decimal" value="45"></label>
        <label>Duty rate %<input id="lc-duty" type="number" min="0" step="any" inputmode="decimal" value="12"></label>
        <label>Extra tariff % (if any)<input id="lc-extra" type="number" min="0" step="any" inputmode="decimal" value="0"></label>
        <label>Duty charged on<select id="lc-basis"><option value="cif">CIF value (UK, EU, most countries)</option><option value="fob">FOB value (USA, Canada, Australia)</option></select></label>
        <label>Import VAT / GST %<input id="lc-vat" type="number" min="0" step="any" inputmode="decimal" value="20"></label>
        <label>Other costs (broker, port, delivery)<input id="lc-other" type="number" min="0" step="any" inputmode="decimal" value="350"></label>
      </form>
      <div class="tool-out" id="lc-out" aria-live="polite"></div>
      <p class="tool-note">This is an estimate. Duty rates depend on the exact HS code, the origin rules and any trade agreement, and some countries add the duty to the VAT base in slightly different ways. Ask your customs broker to confirm before you price a product. For India-specific rates see our guides on <a href="/blog/us-tariffs-on-indian-goods/">US tariffs on Indian goods</a> and <a href="/blog/import-from-india-to-uk-zero-duty/">zero duty under the India-UK trade deal</a>.</p>
    </div>

    <div class="tool" id="gsm">
      <h2>GSM calculator (fabric and towel weight)</h2>
      <p>GSM means grams per square metre. It is the number buyers and mills use to agree how heavy a fabric or towel should be. Weigh a sample, measure it, and enter both.</p>
      <form id="tool-gsm">
        <label>Weight of the piece (grams)<input id="gsm-g" type="number" min="0" step="any" inputmode="decimal" value="500"></label>
        <label>Length<input id="gsm-l" type="number" min="0" step="any" inputmode="decimal" value="140"></label>
        <label>Width<input id="gsm-w" type="number" min="0" step="any" inputmode="decimal" value="70"></label>
        <label>Unit<select id="gsm-unit"><option value="cm">cm</option><option value="in">inches</option></select></label>
      </form>
      <div class="tool-out" id="gsm-out" aria-live="polite"></div>
      <p class="tool-note">For towels, weigh the whole towel and use its full size including borders. For fabric, mills usually cut a 100 cm² round sample and multiply its weight by 100. More on towels in our <a href="/blog/towel-bedsheet-manufacturers-india/">towel and bedsheet manufacturers guide</a>.</p>
    </div>

    <h2>Frequently asked questions</h2>
    <details><summary>How do I calculate CBM?</summary><div class="ans"><p>Multiply length × width × height of one carton in centimetres and divide by 1,000,000. Then multiply by the number of cartons. A 60 × 40 × 40 cm carton is 0.096 CBM, so 100 cartons are 9.6 CBM.</p></div></details>
    <details><summary>What is volumetric weight for air freight?</summary><div class="ans"><p>Airlines charge the higher of the actual weight and the volumetric weight. For air cargo the usual formula is length × width × height in cm divided by 6,000. Most express couriers use 5,000, which makes light, bulky parcels more expensive.</p></div></details>
    <details><summary>Is duty charged on FOB or CIF value?</summary><div class="ans"><p>It depends on the country. The USA, Canada and Australia generally use the FOB (transaction) value, so freight and insurance are not part of the duty base. The UK, the EU and many other countries use the CIF value, which includes freight and insurance to the border.</p></div></details>
    <details><summary>What GSM should a good bath towel be?</summary><div class="ans"><p>Most everyday bath towels sit between about 400 and 600 GSM. Hotel and premium towels are often 600 GSM or more. Lighter towels dry faster, heavier ones feel thicker and softer. Agree a GSM range and a tolerance with the mill in writing.</p></div></details>
'''

PAGES.append(dict(
    slug="free-tools", view="lp-free-tools",
    seo_title="Free Import Calculators: CBM, Landed Cost, GSM | Teak & Tide",
    desc="Free calculators for importers buying from India: CBM and container loading, air volumetric weight, landed cost with duty and VAT, and fabric or towel GSM.",
    crumb="Free tools", eyebrow="Free tools · No sign-up",
    h1="Free import calculators: CBM, landed cost and GSM",
    sub="Work out volume, container fit, landed cost and fabric weight before you place an order.",
    body=TOOLS_BODY, wa_text="I used your free tools and need help with an order from India.",
    extra_head='', extra_foot='<script src="/assets/tools.js?v=20261127a" defer></script>',
    nav_label="Free tools"))

G = [
 ("AQL (Acceptable Quality Limit)", "A sampling standard (ISO 2859-1) used in inspections. It sets how many defective pieces are acceptable in a random sample before the lot fails. Common levels are 0 for critical, 2.5 for major and 4.0 for minor defects."),
 ("Air waybill (AWB)", "The transport document for air freight. Unlike a bill of lading it is not a document of title, so the goods are released to the named consignee."),
 ("APEDA", "Agricultural and Processed Food Products Export Development Authority. Indian exporters of many food and agri products must register with it."),
 ("Bill of lading (B/L)", "The document a shipping line issues when goods are loaded on a ship. An original B/L is a document of title: whoever holds it can claim the cargo."),
 ("BSCI / amfori BSCI", "A social compliance audit programme run by amfori, widely used by European retailers to check labour conditions in factories."),
 ("CBM", "Cubic metre. Sea freight is priced by volume, so you will see CBM on every LCL quote. 1 CBM = 100 × 100 × 100 cm."),
 ("Certificate of origin (COO)", "A document confirming the country where goods were made. It is needed to claim lower duty under a trade agreement and is often asked for by customs or banks."),
 ("CIF (Cost, Insurance and Freight)", "Incoterm where the seller pays freight and insurance to your port, but the risk passes to you once the goods are loaded in India."),
 ("COA (Certificate of Analysis)", "A lab report for a specific batch, showing test results such as moisture, purity, pesticide residues or microbes. Always ask for a COA from the actual lot."),
 ("Commercial invoice", "The seller's invoice for the shipment. Customs uses it to value the goods, so the description, quantity, value and HS code must be correct."),
 ("Consolidation", "Combining goods from several suppliers into one shipment or container to save freight."),
 ("Customs broker", "A licensed agent who files your import declaration and pays duties on your behalf in your country."),
 ("DAP (Delivered at Place)", "Incoterm where the seller delivers to an agreed place in your country, but you pay import duty and taxes."),
 ("DDP (Delivered Duty Paid)", "Incoterm where the seller delivers to your door and pays import duty and taxes. Easy for the buyer, but the seller must be able to act as importer in your country."),
 ("Demurrage and detention", "Charges for keeping a container at the port (demurrage) or outside the port (detention) beyond the free days."),
 ("DGFT", "Directorate General of Foreign Trade, the Indian government body that issues Import Export Codes and runs export schemes."),
 ("Drawback (duty drawback)", "A refund of some duties or taxes paid on inputs used to make exported goods. In India it helps exporters keep prices competitive."),
 ("EXW (Ex Works)", "Incoterm where you collect the goods at the factory and handle everything after that, including Indian export clearance. Rarely the best choice for overseas buyers."),
 ("FCL (Full Container Load)", "You book a whole container for your goods only. Usually cheaper per CBM than LCL once you are above about 15 CBM."),
 ("FOB (Free on Board)", "Incoterm where the supplier clears the goods for export and loads them on the ship in India. You pay ocean freight and take the risk from then on."),
 ("Freight forwarder", "A company that books space with shipping lines or airlines and organises the transport and paperwork for your shipment."),
 ("FSSAI", "Food Safety and Standards Authority of India. Indian food businesses, including exporters, need an FSSAI licence."),
 ("GI tag (Geographical Indication)", "A legal label for products linked to a place, such as Darjeeling tea, Mithila makhana or Mysore agarbathi."),
 ("GOTS", "Global Organic Textile Standard. Certifies organic fibre content and responsible processing for textiles."),
 ("GSM", "Grams per square metre, the weight of a fabric or towel. Higher GSM usually means a thicker, heavier product."),
 ("GST / GSTIN", "India's Goods and Services Tax. Every registered Indian business has a 15-character GSTIN you can verify on the government GST portal."),
 ("HS code", "The Harmonized System code that classifies a product for customs. The first 6 digits are international; countries add more digits for their own tariff."),
 ("IEC (Import Export Code)", "A 10-character code issued by DGFT. An Indian company needs it to export, so it is one of the first things to check."),
 ("Incoterms", "Standard trade terms published by the International Chamber of Commerce (current version: Incoterms 2020) that define who pays for and who is responsible for each step of a shipment."),
 ("Inspection certificate", "A report from an inspection company confirming the goods were checked before shipment. Some buyers make it a condition of paying the balance."),
 ("ISF (Importer Security Filing)", "Also called 10+2. US importers must file it before goods are loaded on a ship bound for the USA."),
 ("Landed cost", "The full cost of a product delivered to your warehouse: price, freight, insurance, duty, taxes and local charges."),
 ("LC (Letter of Credit)", "A bank guarantee that the supplier will be paid once they present the agreed documents. Safer for both sides, but slower and more expensive than a bank transfer."),
 ("LCL (Less than Container Load)", "Your goods share a container with other shippers. Priced per CBM and good for small orders."),
 ("Lead time", "The time from confirming an order to the goods being ready to ship. Agree it in writing, including sample approval time."),
 ("MOQ (Minimum Order Quantity)", "The smallest order a supplier will accept, per product, colour or size. Often negotiable for a first order."),
 ("OEKO-TEX Standard 100", "A label showing textiles have been tested for harmful substances."),
 ("OEM", "Original Equipment Manufacturer. The factory makes the product to your design and specifications."),
 ("Packing list", "A list of what is in each carton: quantities, weights and dimensions. It must match the commercial invoice."),
 ("Pre-shipment inspection (PSI)", "A check of finished goods at the factory before they ship, usually when at least 80% of the order is packed."),
 ("Private label", "Selling a manufacturer's product under your own brand, usually with your packaging and small changes to the product."),
 ("Proforma invoice (PI)", "A quotation in invoice form. It confirms price, quantity, terms and bank details before you pay a deposit."),
 ("RFQ (Request for Quotation)", "Your written request to suppliers, with the specification, quantity and terms, so their quotes can be compared fairly."),
 ("Sample (pre-production / PP sample)", "A sample made from the actual materials before bulk production starts. Approve it in writing and keep one as the reference."),
 ("SEDEX / SMETA", "Sedex is a platform for sharing ethical audit data. SMETA is its audit method, popular with UK retailers."),
 ("Shipping marks", "The text and symbols printed on cartons, such as your order number, carton number and handling marks."),
 ("Spices Board", "The Indian government board that registers spice exporters and runs quality labs."),
 ("Statement on origin", "A declaration by the exporter that goods meet a trade agreement's rules of origin. Used under the India-UK agreement to claim preferential duty."),
 ("T/T (Telegraphic Transfer)", "A bank wire. The most common way to pay Indian suppliers, usually as a deposit and a balance."),
 ("Third-party inspection", "An inspection by an independent company such as SGS, Bureau Veritas, Intertek, QIMA or TÜV, booked by the buyer."),
 ("Transit time", "How long goods take from the port of loading to the port of discharge. India to the US East Coast by sea is often around a month or more."),
 ("UFLPA / forced labour rules", "Laws such as the US ban on goods made with forced labour. Buyers increasingly ask suppliers to show where raw materials come from."),
 ("Volumetric weight", "A weight calculated from size, used by airlines and couriers. They charge whichever is higher: actual or volumetric weight."),
 ("WRAP", "Worldwide Responsible Accredited Production, a social compliance certification common in apparel factories."),
]
import re as _re
def _slug(t): return _re.sub(r'[^a-z0-9]+', '-', t.split(' (')[0].lower()).strip('-')
gl = "\n".join(f'      <div class="gl-row" id="{_slug(t)}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in G)
GLOSS_BODY = f'''
    <style>.gl dl{{margin:0}}.gl-row{{padding:14px 0;border-bottom:1px solid rgba(12,51,38,.1)}}.gl-row dt{{font-weight:700;color:#0c3326;font-family:var(--font-mark,inherit)}}.gl-row dd{{margin:6px 0 0}}</style>
    <p>Sourcing from India comes with a lot of short forms: FOB, AQL, IEC, COA, LCL. Here are {len(G)} terms you will see in quotes, contracts and shipping documents, explained in plain English.</p>
    <div class="gl"><dl>
{gl}
    </dl></div>
    <p style="margin-top:22px">Want the numbers behind some of these terms? Try our <a href="/free-tools/">free CBM, landed cost and GSM calculators</a>, or read <a href="/how-it-works/">how sourcing from India works, step by step</a>.</p>
'''
PAGES.append(dict(
    slug="glossary", view="lp-glossary",
    seo_title="Import & Sourcing Glossary: 55 Trade Terms | Teak & Tide",
    desc=f"Plain-English glossary of {len(G)} import and sourcing terms for buying from India: Incoterms, AQL, MOQ, IEC, GST, COA, LCL, FCL, HS codes and more.",
    crumb="Glossary", eyebrow="Buyer resources",
    h1="Import and sourcing glossary",
    sub="The trade terms you will meet when buying from India, explained simply.",
    body=GLOSS_BODY, wa_text="I have a question about importing from India.",
    terms=G, nav_label="Glossary"))

PAGES.append(dict(
    slug="ddp-shipping-from-india", view="lp-ddp",
    seo_title="DDP Shipping from India: What It Means and Costs | Teak & Tide",
    desc="DDP (Delivered Duty Paid) from India explained: what the seller pays, why it needs an importer of record, DDP vs DAP vs FOB, risks for buyers and when it makes sense.",
    crumb="DDP shipping from India", eyebrow="Shipping guide",
    h1="DDP shipping from India: what it means and when to use it",
    sub="Door-to-door with duties paid sounds simple. Here is what actually happens behind it.",
    wa_text="I want a DDP quote from India.",
    body='''
    <p>Many first-time importers ask Indian suppliers for a "DDP price". It is an understandable request: one price, goods arrive at your door, no customs to deal with. But DDP is the Incoterm that asks the most of the seller, and if it isn't set up properly the shipment can get stuck at your border.</p>

    <h2>What DDP means</h2>
    <p>Under Incoterms 2020, <strong>Delivered Duty Paid</strong> means the seller delivers the goods to the named place in your country, cleared for import, with import duty and taxes paid. The seller carries the cost and risk all the way to your door. You only unload.</p>

    <h2>The catch: someone has to be the importer</h2>
    <p>To pay duty and clear customs in your country, the seller (or its agent) has to act as the <strong>importer of record</strong>. In the USA a non-resident importer can do this through a customs broker. In the UK and EU the seller usually needs a VAT or EORI registration, or an agent who takes on that role. Many small Indian suppliers have never done this. When they quote DDP, they often rely on a freight forwarder's DDP service and add a margin.</p>
    <p>If the paperwork isn't right, customs may hold the goods or bill <em>you</em> as the receiver. Before you accept a DDP price, ask who the importer of record is, and get it in writing.</p>

    <h2>DDP vs DAP vs FOB</h2>
    <ul>
      <li><strong>FOB:</strong> the supplier loads the goods on the ship in India. You book freight and clear customs at home. Usually the cheapest and the most transparent option.</li>
      <li><strong>DAP:</strong> the supplier delivers to your door, but you pay import duty and tax. A good middle ground if you want door delivery but control over customs.</li>
      <li><strong>DDP:</strong> door delivery with duties and taxes paid by the seller. Simplest for you, most complex for the seller.</li>
    </ul>
    <p>Our page on <a href="/how-it-works/">how sourcing works</a> explains EXW, FOB, CIF and DDP side by side.</p>

    <h2>What is inside a DDP price</h2>
    <ul>
      <li>Product price and export packing</li>
      <li>Indian export clearance and port charges</li>
      <li>Ocean or air freight and insurance</li>
      <li>Import duty, plus any extra tariff (for example the US Section 301 tariff on many Indian goods since July 2026)</li>
      <li>Import VAT or GST, where it applies</li>
      <li>Customs broker fees, destination port charges and delivery to your address</li>
    </ul>
    <p>Because duty and tax are inside the price, a DDP quote can look expensive next to an FOB quote. Compare them properly with our <a href="/free-tools/#landed">landed cost calculator</a>.</p>

    <h2>When DDP makes sense</h2>
    <ul>
      <li>Small or sample shipments, where setting up your own customs broker isn't worth it</li>
      <li>Shipments straight to Amazon FBA or a 3PL warehouse</li>
      <li>Buyers who don't want to register as an importer yet</li>
    </ul>
    <p>For regular, larger orders, FOB or DAP with your own broker usually costs less and gives you more control over the duty you pay.</p>

    <h2>How we handle DDP for buyers</h2>
    <p>We compare FOB, DAP and DDP for your shipment, check that the forwarder offering DDP can actually act as importer in your country, and make sure the HS code and invoice value are correct, so the duty paid is the duty owed. We don't tie you to any forwarder.</p>

    <h2>Frequently asked questions</h2>
    <details><summary>Does DDP include import VAT?</summary><div class="ans"><p>Under Incoterms 2020, DDP includes import duties and taxes, including VAT, unless the contract says otherwise. Many contracts write "DDP, VAT unpaid" to exclude it, so always check.</p></div></details>
    <details><summary>Can an Indian supplier ship DDP to the USA?</summary><div class="ans"><p>Yes, usually through a freight forwarder or customs broker who acts as importer of record. Ask for the forwarder's name and who will pay any duty adjustments later.</p></div></details>
    <details><summary>Is DDP cheaper than FOB?</summary><div class="ans"><p>Rarely. DDP includes freight, duty and the seller's margin on handling them. It saves you work, not money. FOB or DAP is usually cheaper for regular orders.</p></div></details>
''', nav_label="DDP shipping"))

PAGES.append(dict(
    slug="ethical-sourcing-india", view="lp-ethical",
    seo_title="Ethical Sourcing in India: Audits & Certifications | Teak & Tide",
    desc="Ethical sourcing from India for UK, EU and US buyers: social audits (amfori BSCI, SMETA, SA8000, WRAP), product certifications, forced labour rules and how to check factories.",
    crumb="Ethical sourcing in India", eyebrow="Compliance guide",
    h1="Ethical sourcing in India: audits, certifications and what to check",
    sub="Retailers and customers want to know who made your products and how. Here is how to answer that.",
    wa_text="I need ethically audited suppliers in India.",
    body='''
    <p>For UK, European and US brands, the question is no longer only "is the price right?" but also "can we show this was made responsibly?". Big retailers ask for social audit reports before they list a product, and laws on forced labour and supply chain transparency keep getting stricter.</p>
    <p>India has thousands of factories that meet international audit standards, especially in textiles, home textiles, leather and handicrafts. The work is finding the right ones and checking the paperwork is real.</p>

    <h2>Social audits buyers ask for</h2>
    <ul>
      <li><strong>amfori BSCI:</strong> common with European retailers. Rated A to E.</li>
      <li><strong>SMETA (Sedex):</strong> widely used by UK retailers. Reports are shared on the Sedex platform.</li>
      <li><strong>SA8000:</strong> a certification for social accountability, stricter than a one-off audit.</li>
      <li><strong>WRAP:</strong> common in apparel and footwear factories supplying the US.</li>
    </ul>
    <p>Ask which standard your customer accepts before choosing suppliers. An audit report is only valid for a set period, so check the date.</p>

    <h2>Product and material certifications</h2>
    <ul>
      <li><strong>GOTS</strong> and <strong>OCS</strong> for organic cotton</li>
      <li><strong>OEKO-TEX Standard 100</strong> for textiles tested for harmful substances</li>
      <li><strong>LWG</strong> (Leather Working Group) for tanneries</li>
      <li><strong>Fairtrade</strong> for some agricultural products and cotton</li>
      <li><strong>FSC</strong> for wood and paper products</li>
    </ul>
    <p>Many certificates can be checked online in the issuing body's public database. Always do that: copied or expired certificates are a real problem.</p>

    <h2>Laws behind the questions</h2>
    <ul>
      <li><strong>UK Modern Slavery Act 2015:</strong> larger companies must publish a yearly statement on what they do to prevent slavery in their supply chains.</li>
      <li><strong>US forced labour ban:</strong> US customs can stop goods it believes were made with forced labour.</li>
      <li><strong>EU due diligence rules:</strong> new EU rules are pushing larger companies to check human rights and environmental risks in their supply chains.</li>
    </ul>
    <p>This is general information, not legal advice. Your compliance team or lawyer should confirm what applies to your business.</p>

    <h2>What we check before recommending a factory</h2>
    <ul>
      <li>Valid audit reports and certificates, verified with the issuing body</li>
      <li>That the audited factory is the one that will actually make your goods, not a sister unit</li>
      <li>Subcontracting: whether any process (embroidery, dyeing, finishing) goes to outside units</li>
      <li>Basic signs on a factory visit: fire exits, working conditions, age checks, wage records</li>
      <li>Registrations: GST, IEC and, where relevant, factory licence</li>
    </ul>
    <p>See also our <a href="/supplier-verification-india/">supplier verification</a> and <a href="/quality-inspection-india/">quality inspection</a> services.</p>

    <h2>Frequently asked questions</h2>
    <details><summary>Who pays for a social audit?</summary><div class="ans"><p>It depends. Many factories already hold a recent BSCI, SMETA or WRAP audit they can share. If your customer needs a new audit, the buyer or the factory books it with an approved audit firm, and the cost is agreed between them.</p></div></details>
    <details><summary>Are Indian factories audited for child labour?</summary><div class="ans"><p>Yes. All major social audits check age records and hiring practices. The risk is higher further down the chain, such as home-based work in some handicrafts, which is why tracing subcontracting matters.</p></div></details>
''', nav_label="Ethical sourcing"))

PAGES.append(dict(
    slug="amazon-fba-prep-india", view="lp-fba",
    seo_title="Amazon FBA Prep from India: Labels & Packing | Teak & Tide",
    desc="Shipping from Indian suppliers to Amazon FBA: since Jan 2026 Amazon US no longer preps or labels items, so FNSKU labels, poly bags and carton rules must be done before shipping.",
    crumb="Amazon FBA prep from India", eyebrow="Amazon sellers",
    h1="Amazon FBA prep from India: labels, packing and carton rules",
    sub="Since January 2026, Amazon US expects every unit to arrive prepped and labelled. Here is how to get it done at the factory.",
    wa_text="I sell on Amazon and want to source from India with FBA prep.",
    body='''
    <p>Amazon ended its own prep and item labelling services for US FBA shipments on <strong>1 January 2026</strong>. Shipments created after that date have to arrive already prepped and labelled, and Amazon says inventory that isn't prepped properly won't be eligible for reimbursement if it is damaged or can't be traced.</p>
    <p>For sellers buying from India, the cheapest place to do this is usually the factory, before the cartons are sealed. It costs a little more per unit at source, but far less than fixing it in a US prep centre.</p>

    <h2>What "prep" covers</h2>
    <ul>
      <li><strong>FNSKU labels:</strong> the Amazon barcode on each unit, unless the product is enrolled to use the manufacturer barcode</li>
      <li><strong>Poly bags:</strong> for textiles and loose items, with a suffocation warning on larger bags</li>
      <li><strong>Bubble wrap or boxing:</strong> for fragile items such as glass, ceramics or brass decor</li>
      <li><strong>Sets:</strong> items sold together must be bagged or boxed and marked as a set</li>
      <li><strong>Carton labels:</strong> FBA box labels on each shipping carton, from your shipment in Seller Central</li>
    </ul>
    <p>Check Amazon's current prep guidance in Seller Central for your category, because rules differ by product type.</p>

    <h2>Carton rules to give your supplier</h2>
    <p>Amazon US has limits on standard carton size and weight. Commonly quoted limits are no side longer than 25 inches and no more than 50 lb per carton, unless a single item is larger. Give the factory your limits in centimetres and kilograms, and check them against Amazon's latest requirements before you book the shipment. Use our <a href="/free-tools/#cbm">CBM calculator</a> to plan cartons.</p>

    <h2>How to brief an Indian factory</h2>
    <ol>
      <li>Send the FNSKU label file and the exact label size</li>
      <li>Send poly bag size, thickness and the warning text</li>
      <li>Say which cartons go to which FBA warehouse if your shipment is split</li>
      <li>Ask for photos of a fully prepped sample unit before bulk packing</li>
      <li>Check labels and cartons in the pre-shipment inspection</li>
    </ol>

    <h2>Products that work well from India for Amazon</h2>
    <p>Home textiles, cotton bags, leather wallets and belts, brass and wooden decor, spices, herbal powders and snacks like makhana are common. Low MOQs are possible with the right suppliers: see our guide to <a href="/blog/low-moq-suppliers-india-amazon-sellers/">low MOQ suppliers in India for Amazon sellers</a>.</p>

    <h2>How we help</h2>
    <p>We find suppliers who can label and pack to FBA requirements, approve a prepped sample with you, and check labels, barcodes and carton weights during the pre-shipment inspection. If you prefer, we can also arrange shipping to a prep centre or 3PL in your country instead.</p>

    <h2>Frequently asked questions</h2>
    <details><summary>Can an Indian factory print FNSKU labels?</summary><div class="ans"><p>Yes. You download the labels from Seller Central and send the file. Most factories can print and apply them. Ask for a photo and test-scan a sample before bulk packing.</p></div></details>
    <details><summary>Does this change apply outside the USA?</summary><div class="ans"><p>The end of Amazon's prep service announced for 2026 applies to the US marketplace. Check the rules for Amazon UK, EU, Canada or Australia separately in Seller Central.</p></div></details>
''', nav_label="Amazon FBA prep"))

BLOGS = []
BLOGS.append(dict(
slug="jute-bag-manufacturers-india",
view="blog-jute-bags",
title="Jute Bag Manufacturers in India: Where They Are and How to Choose One",
seo_title="Jute Bag Manufacturers in India: Buyer's Guide | Teak & Tide",
desc="How to source jute bags from India: Kolkata and West Bengal clusters, jute vs juco, laminated vs non-laminated, printing, MOQs, quality checks and the jute export council.",
crumb="Jute bag manufacturers in India", eyebrow="Bags · Buyer guide",
sub="Shopping bags, wine bags, beach totes and promo bags: what to specify and what to check.",
mins=6, tag="JUTE BAGS",
cta_t="Looking for a jute bag manufacturer?",
cta_p="Send your bag size, print and quantity. We shortlist manufacturers in West Bengal, compare quotes, approve samples and inspect before shipment.",
cat_href="/handicrafts/", cat_label="Handicrafts & home",
wa_text="I want to source jute bags from India.",
card="Jute vs juco, lamination, printing, MOQs and quality checks for buyers of jute bags from India.",
body='''
    <p>India is one of the world's biggest producers of jute, and most of it is grown and processed in West Bengal. That is why the bulk of India's jute bag manufacturers sit in and around <strong>Kolkata</strong> and the surrounding districts, close to the jute mills that make the fabric.</p>
    <p>Jute bags are popular with supermarkets, wine shops, event organisers and brands looking for a reusable, plastic-free option. Here is what to know before you ask for quotes.</p>

    <h2>Types of jute bags</h2>
    <ul>
      <li><strong>Shopping and grocery totes:</strong> the most common, often with gussets and a laminated inside</li>
      <li><strong>Wine and bottle bags:</strong> single, two- or four-bottle, with dividers</li>
      <li><strong>Beach and fashion totes:</strong> with cotton or leather handles, zips and linings</li>
      <li><strong>Promotional and conference bags:</strong> simple flat bags with a printed logo</li>
      <li><strong>Sacks and hessian bags:</strong> for coffee, rice, potatoes and other produce</li>
    </ul>

    <h2>What to specify</h2>
    <ul>
      <li><strong>Fabric:</strong> pure jute, or <em>juco</em> (a jute and cotton blend that is softer and prints better)</li>
      <li><strong>Fabric weight:</strong> usually given in GSM or ounces; heavier fabric holds shape better</li>
      <li><strong>Lamination:</strong> a thin inner coating that makes the bag stiffer and water-resistant; non-laminated bags are fully natural</li>
      <li><strong>Size and gusset:</strong> width × height × base in cm</li>
      <li><strong>Handles:</strong> padded jute rope, cotton webbing, cane or leather</li>
      <li><strong>Printing:</strong> screen print is standard; number of colours affects price</li>
    </ul>

    <h2>MOQs and pricing</h2>
    <p>Simple printed promo bags can often start from a few hundred to a couple of thousand pieces per design. Fashion totes with linings and accessories usually need higher quantities. Price depends mostly on fabric weight, size, lamination, handles and print colours, so ask every supplier to quote on the same specification.</p>

    <h2>Quality checks before shipment</h2>
    <ul>
      <li>Stitching strength at handles (the most common failure point)</li>
      <li>Print alignment, colour and rub-fastness</li>
      <li>Size within the agreed tolerance</li>
      <li>Smell and moisture: jute can develop odour or mould if packed damp</li>
      <li>Packing: flat-packed in bundles, with cartons kept dry</li>
    </ul>

    <h2>Checking the supplier</h2>
    <p>Apart from GST and IEC, many jute exporters are registered with the <strong>Jute Products Development &amp; Export Promotion Council (JPDEPC)</strong> in Kolkata. Registration isn't a quality guarantee, but it is one more sign of a real exporter. Our guide on <a href="/blog/how-to-find-suppliers-in-india/">how to find and verify suppliers in India</a> covers the full checklist.</p>'''))

BLOGS.append(dict(
slug="incense-stick-manufacturers-india",
view="blog-incense",
title="Incense Stick Manufacturers in India: A Buyer's Guide to Agarbatti",
seo_title="Incense Stick Manufacturers in India (Agarbatti) | Teak & Tide",
desc="Buying incense sticks from India: Mysore and Bengaluru hubs, masala vs charcoal agarbatti, dhoop cones, private label packing, fragrance oils, MOQs and safety labelling.",
crumb="Incense stick manufacturers in India", eyebrow="Home fragrance · Buyer guide",
sub="Masala, charcoal, cones and dhoop: how to source and private label Indian incense.",
mins=6, tag="INCENSE",
cta_t="Looking for an incense manufacturer?",
cta_p="Tell us the type, fragrances, packing and quantity. We shortlist manufacturers, arrange samples and inspect before shipment.",
cat_href="/herbs/", cat_label="Herbs & natural products",
wa_text="I want to source incense sticks from India.",
card="Masala vs charcoal incense, Mysore agarbathi, private label packing, MOQs and labelling.",
body='''
    <p>India is the home of agarbatti, and Indian incense sells in gift shops, yoga studios, spiritual stores and online marketplaces around the world. The traditional centre of the industry is Karnataka: <strong>Mysore Agarbathi</strong> holds a Geographical Indication (GI) tag, and the organised incense industry grew up in Bengaluru. Today there are also large manufacturers in Gujarat, Maharashtra, Tamil Nadu and elsewhere.</p>

    <h2>Main types</h2>
    <ul>
      <li><strong>Masala incense:</strong> a paste of herbs, resins, wood powders and essential oils rolled onto a bamboo stick. The classic Indian style.</li>
      <li><strong>Charcoal (dipped) incense:</strong> plain sticks dipped in fragrance oil. Cheaper and easy to customise, but quality depends heavily on the oils used.</li>
      <li><strong>Dhoop sticks and cones:</strong> no bamboo core; denser and slower burning</li>
      <li><strong>Resin and backflow cones:</strong> popular for decorative burners</li>
    </ul>

    <h2>What to specify</h2>
    <ul>
      <li>Type, stick length and burn time</li>
      <li>Fragrance list, and whether you want natural ingredients or fragrance oils</li>
      <li>Smoke level (low-smoke versions are popular in Europe and the US)</li>
      <li>Packing: hexagonal boxes, flat packs, tubes, bulk for repacking</li>
      <li>Private label artwork, barcodes and carton marks</li>
    </ul>

    <h2>MOQs</h2>
    <p>Many manufacturers can start private label orders at a modest quantity per fragrance, especially if you use their standard box sizes. Custom boxes, special fragrances and gift sets raise the MOQ. Mixed containers of several fragrances are normal.</p>

    <h2>Quality and compliance checks</h2>
    <ul>
      <li>Burn test: even burn, stays lit, ash falls cleanly</li>
      <li>Fragrance strength and consistency between batches</li>
      <li>Moisture and mould, especially for sea shipments</li>
      <li>Labelling: many markets expect safety warnings on incense packs, and the EU has rules on fragrance allergens and chemical safety for some home fragrance products. Check what your market requires.</li>
      <li>For natural claims, ask for ingredient lists and supplier declarations</li>
    </ul>

    <h2>How we help</h2>
    <p>We find manufacturers that match your style and price, compare samples side by side, check packing and labelling against your market, and inspect before shipment. For related products see our <a href="/herbs/">herbs</a> and <a href="/handicrafts/">handicrafts</a> pages.</p>'''))

import json, re
P='/home/claude/tt-src.html'
s=open(P).read()

def wa(t):
    import urllib.parse
    return 'https://wa.me/917042367845?text='+urllib.parse.quote('Hello Teak & Tide, '+t)

def art(vid, crumb, eyebrow, h1, sub, mins, tag, body, cta_t, cta_p, cat_href, cat_label, wa_text):
    return f'''
<div data-view="{vid}">
  <section class="page-head"><div class="wrap"><div class="crumb"><a href="#home">Home</a> / <a href="#blog">Blog</a> / {crumb}</div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{sub}</p></div></section>
  <section class="block"><div class="wrap article">
    <p class="post-meta">{mins} MIN READ · {tag}</p>
{body}
    <div class="cta-inline"><strong>{cta_t}</strong><p>{cta_p}</p><div class="actions" style="margin-top:0"><a class="btn btn-green" href="#{cat_href}">{cat_label}</a><a class="btn btn-ghost" href="{wa(wa_text)}" target="_blank" rel="noopener">WhatsApp us</a></div></div>
  </div></section>
</div>
'''

POSTS=[]
A=[]

# 1 Makhana
A.append(art("blog-import-makhana","Importing makhana","Dry fruits · Buyer guide",
"How to import makhana (fox nuts) from India","Grades, quality checks, packing and shipping for buyers of raw and roasted makhana.",6,"DRY FRUITS",'''
    <p>Makhana, also called fox nuts or lotus seeds, is the popped seed of the Euryale ferox plant. Most of the world's commercial supply comes from India, mainly from the Mithila region of Bihar, where "Mithila Makhana" holds a Geographical Indication (GI) tag. Demand is growing as a healthy snack in the USA, UK, Europe and the Middle East.</p>
    <h2>1. Know the grades</h2>
    <p>Makhana is sold by size and quality, usually described by the size of the popped seed (for example in "suta" sizes like 4 suta, 5 suta, 6 suta and above, or by millimetres). Larger, whiter and evenly popped seeds are premium grades and cost more. Smaller or broken seeds are cheaper and often used for flour or processing. Agree the grade in writing and ask for photos against a ruler.</p>
    <h2>2. Raw or flavoured?</h2>
    <p>You can import plain (raw popped) makhana in bulk and roast or flavour it in your country, or buy ready roasted and flavoured makhana in retail packs under your own brand. Flavoured products need ingredient lists, nutrition labels and shelf-life testing that match your country's food rules.</p>
    <h2>3. Quality checks that matter</h2>
    <ul><li>Moisture: makhana absorbs moisture easily and loses crunch. Ask for the moisture level and check it on arrival.</li><li>Colour and uniformity: avoid lots with many dark or half-popped seeds.</li><li>Foreign matter: husk pieces, stones and insects should be within your agreed limit.</li><li>Food safety: ask for a recent lab report covering pesticide residues and microbiology for your market.</li></ul>
    <h2>4. Check the supplier</h2>
    <p>Look for a valid FSSAI licence, APEDA registration for export, an Import Export Code (IEC) and GST registration. Ask whether they process and grade themselves or buy from traders. A processor in Bihar usually gives more consistent grading.</p>
    <h2>5. Packing and shipping</h2>
    <p>Makhana is very light and bulky, so freight is charged mostly by volume. Moisture-proof inner bags (often multilayer or with nitrogen flushing for retail packs) and strong cartons protect the product. Ask the supplier how many kilograms fit in a 20-foot or 40-foot container for your packing.</p>
    <h2>6. Order samples first</h2>
    <p>Always approve samples from the actual lot before you pay the balance. A pre-shipment inspection checks grade, moisture, packing and quantity against your order.</p>''',
"Want to import makhana from India?","Tell us the grade, packing and quantity. We search processors, compare quotes, check samples and inspect before shipment.","dryfruits","Dry fruits we source","I want to import makhana from India."))
POSTS.append(dict(id="blog-import-makhana",tag="DRY FRUITS",title="How to import makhana (fox nuts) from India",text="Grades, quality checks, packing and shipping for raw and roasted makhana.",mins=6))

# 2 Cashew grades
A.append(art("blog-cashew-grades","Cashew grades","Dry fruits · Buyer guide",
"Cashew kernel grades explained: W180, W240, W320 and more","What the grade codes mean, how to compare quotes, and what to check before you buy cashews from India.",6,"DRY FRUITS",'''
    <p>India is one of the world's largest cashew processors, with major processing centres in Kerala (especially Kollam), Karnataka, Goa, Andhra Pradesh, Odisha and Tamil Nadu. To buy cashews well, you first need to understand the grade codes on every quote.</p>
    <h2>1. What "W" and the number mean</h2>
    <p>"W" stands for whole white kernels. The number is the approximate count of kernels per pound (about 454 g). So W180 means around 180 kernels per pound, which makes it the largest and most expensive grade. Common whole grades are W180, W210, W240, W320 and W450. W320 is the most traded grade worldwide and a good balance of size and price.</p>
    <h2>2. Other common codes</h2>
    <ul><li><strong>SW</strong> (scorched wholes): slightly darker kernels from longer roasting, cheaper than W grades.</li><li><strong>DW</strong> (dessert wholes): darker or spotted wholes, used in processing.</li><li><strong>B</strong> (butts): kernels broken across, still in large pieces.</li><li><strong>S</strong> (splits): kernels split along their natural line.</li><li><strong>LWP / SWP</strong>: large and small white pieces, used in sweets, bakery and cooking.</li></ul>
    <h2>3. Compare quotes fairly</h2>
    <p>Two quotes for "W320" can still differ in moisture, broken percentage, colour and packing. Ask every supplier for the same details: grade, moisture limit, maximum broken kernels, packing (usually vacuum-packed tins or bags with CO2 or nitrogen flushing), and the trade term (FOB or CIF).</p>
    <h2>4. Quality checks</h2>
    <ul><li>Count a sample: weigh out one pound and count the kernels to confirm the grade.</li><li>Check moisture, colour, broken kernels and insect damage.</li><li>Ask for lab reports on aflatoxins and microbiology for your market.</li></ul>
    <h2>5. Check the processor</h2>
    <p>Look for FSSAI and export registrations, an IEC and GST number, and food-safety certifications if your buyers need them. A processor with its own factory gives more consistent grading than a trader.</p>''',
"Need cashew kernels from India?","Send us your grade, quantity and destination. We compare processors and inspect the lot before it ships.","dryfruits","Dry fruits we source","I want to buy cashew kernels from India."))
POSTS.append(dict(id="blog-cashew-grades",tag="DRY FRUITS",title="Cashew kernel grades explained: W180, W240, W320",text="What the grade codes mean and how to compare cashew quotes from India.",mins=6))

# 3 Ashwagandha
A.append(art("blog-ashwagandha-supplier","Buying ashwagandha","Herbs · Buyer guide",
"Buying ashwagandha from India: root, powder or extract","What to specify, which tests to ask for, and how to choose an Indian ashwagandha supplier.",6,"HERBS",'''
    <p>Ashwagandha (Withania somnifera) is one of the best-known Ayurvedic herbs, and India is its main source. Buyers use it in supplements, teas, powders and cosmetics. Because rules and quality vary a lot, a clear specification is the first step.</p>
    <h2>1. Choose the form</h2>
    <ul><li><strong>Dried root:</strong> whole or cut, for further processing.</li><li><strong>Root powder:</strong> ground root, usually sold by mesh size.</li><li><strong>Extract:</strong> concentrated and standardised to a withanolide content (for example 1.5%, 2.5% or 5%), sold as powder.</li></ul>
    <p>Many markets and brands prefer root-only material. Some countries restrict ashwagandha or certain parts of the plant, so check your own country's rules before you order.</p>
    <h2>2. Write the specification</h2>
    <p>Include the plant part, form, mesh size or extract ratio, withanolide content and test method, moisture, colour, and packing. If you need organic, say which certification your market accepts.</p>
    <h2>3. Tests to ask for</h2>
    <ul><li>Identity and active content (withanolides).</li><li>Heavy metals (lead, arsenic, cadmium, mercury).</li><li>Pesticide residues.</li><li>Microbiology (total plate count, yeast and mould, pathogens).</li></ul>
    <p>Ask for a Certificate of Analysis (COA) for the actual batch, and consider independent testing of a pre-shipment sample.</p>
    <h2>4. Check the supplier</h2>
    <p>Look for an export registration, IEC and GST, a manufacturing licence where required, and quality certifications that your buyers expect. Ask where the root is grown and whether they process it themselves.</p>
    <h2>5. Labels and claims</h2>
    <p>Health claims on herbal products are tightly controlled in most countries. Keep your labels to what your market allows and keep the supplier's COAs on file.</p>''',
"Looking for an ashwagandha supplier in India?","Share your form, specification and market. We find suppliers, arrange samples and lab tests, and inspect before shipment.","herbs","Herbs we source","I want to source ashwagandha from India."))
POSTS.append(dict(id="blog-ashwagandha-supplier",tag="HERBS",title="Buying ashwagandha from India: root, powder or extract",text="What to specify, which tests to ask for and how to choose a supplier.",mins=6))

# 4 Brass Moradabad
A.append(art("blog-brass-handicrafts-moradabad","Brass from Moradabad","Handicrafts · Buyer guide",
"Sourcing brass handicrafts from Moradabad, India","How to buy brass decor, lamps and tableware from India's best-known metal-craft city.",5,"HANDICRAFTS",'''
    <p>Moradabad in Uttar Pradesh is known as "Peetal Nagri", the brass city. Its workshops make decor, planters, lamps, candle holders, trays, tableware and hardware for importers and brands around the world. Moradabad metal craft also carries a Geographical Indication (GI) tag.</p>
    <h2>1. Decide what you need</h2>
    <p>Moradabad makes solid brass, brass-plated iron or aluminium, and mixed-metal products. Solid brass is heavier and more expensive; plated items are lighter and cheaper. Be clear which one you want, because photos can look the same.</p>
    <h2>2. Finishes and coatings</h2>
    <p>Common finishes include polished, antique, hammered, matte and coloured lacquer. Ask for a protective lacquer if you don't want the brass to tarnish quickly. Agree the finish on an approved sample, not only a photo.</p>
    <h2>3. Food-contact items need extra care</h2>
    <p>Bowls, cups, plates and serving ware that touch food must meet your country's food-contact rules, including limits on lead. Ask the factory for food-safe lining or coating and a test report from an accredited lab before you order.</p>
    <h2>4. Quality checks</h2>
    <ul><li>Weight and thickness against the approved sample.</li><li>Finish, colour and polish consistency across the lot.</li><li>No sharp edges, loose joints or soldering marks.</li><li>Export packing that survives sea freight: individual wrapping, inner boxes and strong master cartons.</li></ul>
    <h2>5. Plan time for handmade work</h2>
    <p>Many pieces are made by hand in small workshops, so lead times depend on the season and order size. Weekly photo updates during production help you stay on schedule.</p>''',
"Sourcing brass or metal decor from India?","Send us your designs or references. We find the right Moradabad workshops, approve samples and inspect before shipment.","handicrafts","Handicrafts we source","I want to source brass handicrafts from Moradabad."))
POSTS.append(dict(id="blog-brass-handicrafts-moradabad",tag="HANDICRAFTS",title="Sourcing brass handicrafts from Moradabad, India",text="How to buy brass decor, lamps and tableware from India's brass city.",mins=5))

# 5 India vs China
A.append(art("blog-india-vs-china-sourcing","India vs China","Sourcing · Buyer guide",
"Sourcing from India vs China: what buyers should know","An honest comparison to help you decide which products to source from India.",6,"SOURCING",'''
    <p>Many brands and importers are adding India to their supplier base alongside China. Both countries have strengths. Knowing where India fits best helps you avoid frustration and get good results.</p>
    <h2>1. Where India is strong</h2>
    <ul><li>Natural and agricultural products: spices, rice, pulses, dry fruits, herbs and tea.</li><li>Handmade and craft products: brass, wood, marble, pottery, rugs and hand-block textiles.</li><li>Cotton textiles and garments, leather goods and footwear.</li></ul>
    <h2>2. Where China is often easier</h2>
    <p>For highly automated, electronics-heavy or very complex products, China's supply chains are usually deeper and faster. India is growing quickly in many of these areas, but you may need more time to find the right factory.</p>
    <h2>3. Minimum orders and flexibility</h2>
    <p>Many Indian manufacturers, especially in handicrafts, leather and garments, accept smaller trial orders than large factories elsewhere. This makes India attractive for new brands testing a product.</p>
    <h2>4. Finding suppliers is different</h2>
    <p>Many good Indian factories have simple websites or none at all, and online directories often list traders instead of manufacturers. Local knowledge, phone calls in Hindi or regional languages, and factory visits make a big difference.</p>
    <h2>5. Quality and follow-up</h2>
    <p>Write detailed specifications, approve a pre-production sample, ask for photo updates during production and inspect before you pay the balance. These steps matter in every country, but they are what separate good and bad experiences in India.</p>
    <h2>6. Trade agreements and duties</h2>
    <p>Import duties on Indian goods depend on your country and the product. Some countries have trade agreements with India that reduce duties. Check your tariff code with your customs broker before you compare landed costs.</p>''',
"Thinking of adding India to your supply chain?","Tell us your product and target price. We search fresh suppliers for every requirement and handle quality checks for you.","services","Our services","I would like to compare sourcing my product from India."))
POSTS.append(dict(id="blog-india-vs-china-sourcing",tag="SOURCING",title="Sourcing from India vs China: what buyers should know",text="An honest comparison of where India is strong and how to source well.",mins=6))

# insert articles after leather article
anchor='<div data-view="blog-private-label-leather">'
i=s.index(anchor); j=s.index('</div></section>\n</div>',i)+len('</div></section>\n</div>')
s=s[:j]+''.join(A)+s[j:]

# POSTS list
old='  { id: "blog-private-label-leather", tag: "LEATHER GOODS", title: "Making leather goods under your own brand in India", text: "From your design to finished products with your logo.", mins: 5 }'
assert old in s
new=',\n'.join('  { id: %s, tag: %s, title: %s, text: %s, mins: %d }'%(json.dumps(p['id']),json.dumps(p['tag']),json.dumps(p['title']),json.dumps(p['text']),p['mins']) for p in POSTS)
s=s.replace(old, new+',\n'+old)
ids=[p['id'] for p in POSTS]
s=s.replace('"blog-private-label-leather"];', '"blog-private-label-leather", '+', '.join(json.dumps(x) for x in ids)+'];',1)
s=s.replace('"blog-private-label-leather": "blog" };', '"blog-private-label-leather": "blog", '+', '.join(json.dumps(x)+': "blog"' for x in ids)+' };',1)
s=s.replace('"blog-private-label-leather": "Private-label leather goods from India | Teak & Tide" };','"blog-private-label-leather": "Private-label leather goods from India | Teak & Tide", '+', '.join(json.dumps(p['id'])+': '+json.dumps(p['title']+' | Teak & Tide') for p in POSTS)+' };',1)
open(P,'w').write(s)
print('ok')

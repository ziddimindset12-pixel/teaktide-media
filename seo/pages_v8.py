PAGES = []
BLOGS = []
FORM = '''
    <div class="card" id="ck-box" style="margin:22px 0;padding:22px">
      <h2 style="margin-top:0">Get the free checklist (PDF)</h2>
      <p>Enter your email and the download starts straight away. We may send you one or two useful sourcing tips later. No spam, and you can ask us to stop at any time.</p>
      <form id="ck-form" novalidate style="display:grid;gap:12px;max-width:520px">
        <input type="text" name="bot-field" id="ck-bot" style="display:none" tabindex="-1" autocomplete="off">
        <label>Your name<input id="ck-name" required autocomplete="name" style="display:block;width:100%;margin-top:4px;padding:11px;border:1px solid var(--gold-line);border-radius:8px;font:inherit"></label>
        <label>Work email<input id="ck-email" type="email" required autocomplete="email" style="display:block;width:100%;margin-top:4px;padding:11px;border:1px solid var(--gold-line);border-radius:8px;font:inherit"></label>
        <label>Country<input id="ck-country" autocomplete="country-name" style="display:block;width:100%;margin-top:4px;padding:11px;border:1px solid var(--gold-line);border-radius:8px;font:inherit"></label>
        <label>Company (optional)<input id="ck-company" autocomplete="organization" style="display:block;width:100%;margin-top:4px;padding:11px;border:1px solid var(--gold-line);border-radius:8px;font:inherit"></label>
        <button class="btn btn-green" type="submit">Download the checklist</button>
        <p id="ck-status" role="status" style="margin:0"></p>
      </form>
    </div>'''
SCRIPT = '''<script>
(function(){var f=document.getElementById("ck-form");if(!f)return;
f.addEventListener("submit",function(e){e.preventDefault();
var g=function(i){return document.getElementById(i).value.trim()},st=document.getElementById("ck-status"),em=document.getElementById("ck-email");
if(!g("ck-name")||!g("ck-email")||!em.checkValidity()){st.textContent="Please add your name and a valid email address.";return;}
var d={"form-name":"checklist","bot-field":g("ck-bot"),name:g("ck-name"),email:g("ck-email"),country:g("ck-country"),company:g("ck-company"),msg:"Downloaded: India Supplier Verification Checklist",page:location.pathname};
try{fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:Object.keys(d).map(function(k){return encodeURIComponent(k)+"="+encodeURIComponent(d[k])}).join("&")}).catch(function(){});}catch(x){}
st.innerHTML='Thank you! <a class="btn btn-green" style="margin-top:8px" href="/India-Supplier-Verification-Checklist.pdf" download>Open the checklist (PDF)</a>';
var a=document.createElement("a");a.href="/India-Supplier-Verification-Checklist.pdf";a.download="";document.body.appendChild(a);a.click();a.remove();});})();
</script>'''
PAGES.append(dict(
    slug="supplier-verification-checklist", view="lp-checklist",
    seo_title="Free Supplier Verification Checklist (PDF) | Teak & Tide",
    desc="Free PDF checklist for checking an Indian supplier before you pay: GST and IEC checks, factory video calls, samples, safe payment terms, inspection and red flags.",
    crumb="Supplier verification checklist", eyebrow="Free download · PDF",
    h1="India Supplier Verification Checklist",
    sub="A two-page checklist to use before you pay a deposit to any supplier in India.",
    wa_text="I'd like help verifying a supplier in India.",
    extra_foot=SCRIPT,
    body='''
    <p>Most problems buying from India start before the first shipment: a supplier who isn't who they say they are, a sample that doesn't match production, or a deposit paid with no protection. This free checklist is the same set of checks we run for our clients, written so you can use it yourself.</p>
    <h2>What's inside</h2>
    <ul>
      <li><strong>Company documents:</strong> how to check GST, the Import Export Code, company registration, export council membership and product licences</li>
      <li><strong>Is the factory real?</strong> Live video calls, address checks, manufacturer vs trader, capacity and export history</li>
      <li><strong>Samples and specification:</strong> what to put in writing and when you need lab tests</li>
      <li><strong>Quote and payment:</strong> comparing quotes, the proforma invoice, staged payments and bank-detail fraud</li>
      <li><strong>Before shipment:</strong> AQL inspection, packing, labels and documents</li>
      <li><strong>Red flags</strong> that usually come before a lost deposit</li>
    </ul>''' + FORM + '''
    <p>Want the checks done for you? See our <a href="/supplier-verification-india/">supplier verification service</a> or read <a href="/blog/how-to-find-suppliers-in-india/">how to find and verify suppliers in India</a>.</p>
    <h2>Frequently asked questions</h2>
    <div class="faq"><details><summary>Is the checklist really free?</summary><div class="ans"><p>Yes. Enter your name and email and the PDF downloads straight away. There is nothing to pay.</p></div></details><details><summary>Who is this checklist for?</summary><div class="ans"><p>Importers, retailers, Amazon sellers and brands buying from India for the first time, or anyone about to pay a deposit to a new Indian supplier.</p></div></details><details><summary>Can you verify a supplier for me?</summary><div class="ans"><p>Yes. We are a buying agent in Delhi NCR. We check documents, visit or video-call the factory, approve samples and inspect goods before you pay the balance.</p></div></details></div>''',
))

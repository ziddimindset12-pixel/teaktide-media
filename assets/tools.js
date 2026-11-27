(function () {
  function num(id) { var v = parseFloat((document.getElementById(id) || {}).value); return isFinite(v) ? v : 0; }
  function fmt(n, d) { return n.toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function out(id, html) { var el = document.getElementById(id); if (el) el.innerHTML = html; }

  // CBM
  function cbm() {
    var l = num("cbm-l"), w = num("cbm-w"), h = num("cbm-h"), q = num("cbm-q"), kg = num("cbm-kg");
    var unit = document.getElementById("cbm-unit").value;
    var f = unit === "in" ? 2.54 : 1;
    var one = (l * f) * (w * f) * (h * f) / 1e6;
    var total = one * q;
    if (!one || !q) { out("cbm-out", "Enter carton size and number of cartons."); return; }
    var gross = kg * q;
    var air = (l * f) * (w * f) * (h * f) / 6000 * q;
    var courier = (l * f) * (w * f) * (h * f) / 5000 * q;
    var c20 = Math.floor(28 / one), c40 = Math.floor(58 / one), c40h = Math.floor(68 / one);
    var load = total <= 15 ? "LCL (shared container) is usually cheaper at this volume."
      : total <= 28 ? "Close to a 20ft container. Compare an LCL quote with a 20ft FCL quote."
      : total <= 58 ? "Too big for a 20ft. Look at a 40ft container."
      : total <= 68 ? "Fits a 40ft high cube (40HC)." : "More than one 40ft container.";
    out("cbm-out",
      "<p><strong>Per carton:</strong> " + fmt(one, 4) + " CBM</p>" +
      "<p><strong>Total volume:</strong> " + fmt(total, 3) + " CBM (" + fmt(total * 35.3147, 1) + " cu ft)</p>" +
      (kg ? "<p><strong>Total gross weight:</strong> " + fmt(gross, 1) + " kg</p>" : "") +
      (kg ? "<p><strong>Air freight chargeable weight:</strong> " + fmt(Math.max(gross, air), 1) + " kg <span class='tool-note'>(higher of actual and volumetric, ÷6000)</span></p>" : "<p><strong>Air volumetric weight:</strong> " + fmt(air, 1) + " kg <span class='tool-note'>(÷6000)</span></p>") +
      "<p><strong>Courier volumetric weight:</strong> " + fmt(courier, 1) + " kg <span class='tool-note'>(÷5000, used by most express couriers)</span></p>" +
      "<p><strong>Cartons per container (approx.):</strong> 20ft ≈ " + c20 + " · 40ft ≈ " + c40 + " · 40HC ≈ " + c40h + "</p>" +
      "<p class='tool-tip'>" + load + "</p>");
  }

  // Landed cost
  function landed() {
    var price = num("lc-price"), qty = num("lc-qty"), freight = num("lc-freight"), ins = num("lc-ins");
    var duty = num("lc-duty"), extra = num("lc-extra"), vat = num("lc-vat"), other = num("lc-other");
    var basis = document.getElementById("lc-basis").value;
    if (!price || !qty) { out("lc-out", "Enter the unit price and quantity."); return; }
    var goods = price * qty;
    var insurance = ins > 0 ? ins : 0;
    var cif = goods + freight + insurance;
    var dutyBase = basis === "fob" ? goods : cif;
    var dutyAmt = dutyBase * (duty + extra) / 100;
    var vatAmt = (cif + dutyAmt) * vat / 100;
    var total = cif + dutyAmt + vatAmt + other;
    out("lc-out",
      "<table class='tool-table'>" +
      "<tr><td>Goods (FOB value)</td><td>" + fmt(goods, 2) + "</td></tr>" +
      "<tr><td>Freight + insurance</td><td>" + fmt(freight + insurance, 2) + "</td></tr>" +
      "<tr><td>Import duty (" + fmt(duty + extra, 2) + "% on " + (basis === "fob" ? "FOB" : "CIF") + " value)</td><td>" + fmt(dutyAmt, 2) + "</td></tr>" +
      (vat ? "<tr><td>Import VAT / GST (" + fmt(vat, 2) + "%)</td><td>" + fmt(vatAmt, 2) + "</td></tr>" : "") +
      (other ? "<tr><td>Other costs (broker, port, delivery)</td><td>" + fmt(other, 2) + "</td></tr>" : "") +
      "<tr class='tool-total'><td>Total landed cost</td><td>" + fmt(total, 2) + "</td></tr>" +
      "<tr class='tool-total'><td>Landed cost per unit</td><td>" + fmt(total / qty, 3) + "</td></tr>" +
      "</table>" +
      (vat ? "<p class='tool-note'>If you are VAT/GST registered you can usually reclaim import VAT, so your real cost per unit is " + fmt((total - vatAmt) / qty, 3) + ".</p>" : ""));
  }

  // GSM
  function gsm() {
    var g = num("gsm-g"), l = num("gsm-l"), w = num("gsm-w");
    var unit = document.getElementById("gsm-unit").value;
    var f = unit === "in" ? 0.0254 : 0.01;
    if (!g || !l || !w) { out("gsm-out", "Enter weight and size."); return; }
    var area = (l * f) * (w * f);
    var v = g / area;
    var band = v < 150 ? "Very light (lining, voile, tissue-weight fabric)"
      : v < 250 ? "Light to medium (shirting, T-shirt jersey, sheeting)"
      : v < 400 ? "Medium to heavy (sweatshirts, denim, light towels)"
      : v < 600 ? "Heavy (everyday bath towels)" : "Very heavy (premium, plush towels and bath mats)";
    out("gsm-out", "<p><strong>GSM:</strong> " + fmt(v, 0) + " g/m²</p><p><strong>Weight in oz/yd²:</strong> " + fmt(v / 33.906, 2) + "</p><p class='tool-tip'>" + band + "</p>");
  }

  function bind(form, fn) {
    var f = document.getElementById(form);
    if (!f) return;
    f.addEventListener("input", fn);
    f.addEventListener("change", fn);
    f.addEventListener("submit", function (e) { e.preventDefault(); fn(); });
    fn();
  }
  function init() { bind("tool-cbm", cbm); bind("tool-lc", landed); bind("tool-gsm", gsm); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();

/* Product finder: where in India a product comes from. No supplier data. */
(function () {
  var roots = document.querySelectorAll("[data-finder]");
  if (!roots.length) return;
  var DATA = null, loading = null, WA = "https://wa.me/917042367845?text=";
  var POPULAR = ["Basmati rice", "Turmeric", "Cashew", "Makhana", "Brass", "Bed linen", "Psyllium husk", "Guar gum"];

  function load() {
    if (DATA) return Promise.resolve(DATA);
    if (!loading) loading = fetch("/assets/finder.json").then(function (r) { return r.json(); }).then(function (d) {
      d.forEach(function (x) {
        x._n = norm(x.n + " " + (x.p || ""));
        x._k = norm(x.k || "");
        x._c = norm(x.c);
        x._o = norm((x.f || "") + " " + (x.s || ""));
        x._w = (x._n + " " + x._k).split(" ").filter(Boolean);
      });
      DATA = d; return d;
    });
    return loading;
  }
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, " ").trim(); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function near(a, b) { // edit distance <= 1
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0, j = 0, e = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++e > 1) return false;
      if (a.length > b.length) i++; else if (b.length > a.length) j++; else { i++; j++; }
    }
    return e + (a.length - i) + (b.length - j) <= 1;
  }
  function score(x, q, toks) {
    var s = 0;
    if (x._n === q) s += 120; else if (x._n.indexOf(q) === 0) s += 70; else if ((" " + x._n).indexOf(" " + q) > -1) s += 45;
    for (var t = 0; t < toks.length; t++) {
      var w = toks[t], hit = 0;
      if ((" " + x._n).indexOf(" " + w) > -1) hit = 22;
      else if ((" " + x._k).indexOf(" " + w) > -1) hit = 18;
      else if ((" " + x._c).indexOf(" " + w) > -1) hit = 8;
      else if (w.length > 3 && (" " + x._o).indexOf(" " + w) > -1) hit = 5;
      else if (w.length > 4) { for (var k = 0; k < x._w.length; k++) { var ww = x._w[k]; if (ww.length > 4 && near(w, ww)) { hit = 12; break; } } }
      if (!hit) return 0;
      s += hit;
    }
    if (!x.p) s += 3; // prefer main products over sub-items
    return s;
  }
  function search(q) {
    var nq = norm(q); if (!nq) return [];
    var toks = nq.split(" ");
    return DATA.map(function (x) { return [score(x, nq, toks), x]; }).filter(function (r) { return r[0] > 0; })
      .sort(function (a, b) { return b[0] - a[0]; }).map(function (r) { return r[1]; });
  }
  function row(label, val) { return val ? '<div class="fd-row"><dt>' + label + '</dt><dd>' + esc(val) + '</dd></div>' : ""; }
  function card(x) {
    var img = x.i ? '<img class="fd-thumb" src="' + esc(x.i.replace("w=1200", "w=240")) + '" alt="" loading="lazy" onerror="this.remove()">' : '<span class="fd-thumb fd-none" aria-hidden="true"></span>';
    var where = x.s || "Ask us – we will find the right region for your specification";
    var msg = "Hello Teak & Tide, I found " + x.n + " in your product finder. My requirement: ";
    return '<li class="fd-card"><div class="fd-head">' + img + '<div><p class="fd-name">' + esc(x.n) + '</p><p class="fd-cat">' + esc(x.p ? x.p + " · " + x.c : x.c) + '</p></div></div>' +
      '<dl>' + row("Where in India", where) + row("Available as", x.f) + row("Main buyers", x.b) + row("India's exports", x.e) + '</dl>' +
      '<div class="fd-actions"><a class="btn btn-green" target="_blank" rel="noopener" href="' + WA + encodeURIComponent(msg) + '">Get a quote</a><a class="btn btn-ghost" href="' + x.u + '#catalogue">See category</a></div></li>';
  }
  function logMiss(q) {
    try {
      var body = "form-name=product-search-miss&query=" + encodeURIComponent(q.slice(0, 80)) + "&page=" + encodeURIComponent(location.pathname);
      fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: body }).catch(function () {});
    } catch (e) {}
  }
  roots.forEach(function (root) {
    var input = root.querySelector("input"), out = root.querySelector(".fd-results"), status = root.querySelector(".fd-status"), chips = root.querySelector(".fd-chips");
    var timer = null, lastMiss = "";
    chips.innerHTML = POPULAR.map(function (p) { return '<button type="button" class="fd-chip">' + esc(p.replace(/ \(.*\)/, "")) + '</button>'; }).join("");
    chips.addEventListener("click", function (e) { var b = e.target.closest(".fd-chip"); if (!b) return; input.value = b.textContent; run(true, true); });
    input.addEventListener("focus", load, { once: true });
    input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(function () { run(false); }, 160); });
    root.querySelector("form").addEventListener("submit", function (e) { e.preventDefault(); input.blur(); run(true, true); });
    function run(commit, jump) {
      var q = input.value.trim();
      if (q.length < 2) { out.innerHTML = ""; status.textContent = ""; return; }
      load().then(function () {
        var res = search(q), shown = res.slice(0, 6);
        if (!res.length) {
          status.textContent = "";
          out.innerHTML = '<li class="fd-empty"><p><strong>We could not find “' + esc(q) + '” in our list yet.</strong></p><p>We source many products that are not listed here. Tell us what you need and we will find where it is made in India.</p>' +
            '<a class="btn btn-green" target="_blank" rel="noopener" href="' + WA + encodeURIComponent("Hello Teak & Tide, I am looking for " + q + " from India. My requirement: ") + '">Ask us about ' + esc(q) + '</a></li>';
          if (commit && q !== lastMiss) { lastMiss = q; logMiss(q); }
          return;
        }
        status.textContent = res.length + (res.length === 1 ? " product found" : " products found");
        out.innerHTML = shown.map(card).join("") + (res.length > 6 ? '<li class="fd-more"><button type="button" class="btn btn-ghost">Show all ' + res.length + ' results</button></li>' : "");
        var more = out.querySelector(".fd-more button");
        if (more) more.addEventListener("click", function () { out.innerHTML = res.map(card).join(""); });
        if (jump && status.scrollIntoView) status.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
  });
})();

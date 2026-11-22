// Cloudflare Pages Function: receives the site's form POSTs (quote, feedback,
// product-search-miss) that used to go to Netlify Forms, and forwards them to
// the Make webhook. GET requests to "/" are not handled here and fall through
// to the static homepage.
const HOOK = "https://hook.eu1.make.com/t8a2ppbsqv4qedatlk2f3qw8qy2xan86";
const FORMS = new Set(["quote", "feedback", "product-search-miss"]);

export async function onRequestPost({ request }) {
  try {
    const raw = await request.text();
    if (raw.length > 20000) return new Response("Too large", { status: 413 });
    const params = new URLSearchParams(raw);
    const data = {};
    for (const [k, v] of params) data[k] = String(v).slice(0, 4000);
    const form = data["form-name"];
    if (!FORMS.has(form)) return new Response("Unknown form", { status: 400 });
    if (data["bot-field"]) return new Response("OK", { status: 200 });
    const payload = {
      form,
      fields: data,
      received_at: new Date().toISOString(),
      visitor_country: request.headers.get("cf-ipcountry") || "",
      referer: request.headers.get("referer") || "",
      user_agent: (request.headers.get("user-agent") || "").slice(0, 300),
    };
    const r = await fetch(HOOK, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    return new Response(r.ok ? "OK" : "Queued", { status: 200 });
  } catch (e) {
    return new Response("Error", { status: 500 });
  }
}

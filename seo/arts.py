# Rich SVG illustrations for the 7 product categories (viewBox 0 0 320 200)
def defs(p):
    return f'''<defs>
<radialGradient id="{p}bg" cx="50%" cy="30%" r="80%"><stop offset="0" stop-color="#1f5d45"/><stop offset=".55" stop-color="#0f3a2b"/><stop offset="1" stop-color="#08251a"/></radialGradient>
<radialGradient id="{p}spot" cx="50%" cy="100%" r="60%"><stop offset="0" stop-color="#f0cf8c" stop-opacity=".22"/><stop offset="1" stop-color="#f0cf8c" stop-opacity="0"/></radialGradient>
<linearGradient id="{p}gold" x1="0" x2="1"><stop offset="0" stop-color="#9a6522"/><stop offset=".45" stop-color="#f0cf8c"/><stop offset="1" stop-color="#a8742c"/></linearGradient>
<linearGradient id="{p}brass" x1="0" x2="1"><stop offset="0" stop-color="#7a4f17"/><stop offset=".35" stop-color="#e8c071"/><stop offset=".55" stop-color="#fbe3a6"/><stop offset="1" stop-color="#8a5a1c"/></linearGradient>
<filter id="{p}sh" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity=".35"/></filter>
</defs>'''
def base(p):
    return (f'<rect width="320" height="200" fill="url(#{p}bg)"/>'
            f'<g fill="none" stroke="#c9a868" stroke-opacity=".10"><circle cx="160" cy="70" r="120"/><ellipse cx="160" cy="70" rx="45" ry="120"/><ellipse cx="160" cy="70" rx="90" ry="120"/><path d="M40 70h240M52 20h216M52 120h216"/></g>'
            f'<ellipse cx="160" cy="182" rx="170" ry="40" fill="url(#{p}spot)"/>'
            f'<ellipse cx="160" cy="178" rx="128" ry="10" fill="#000" opacity=".28"/>')
def grains(cx,cy,n,rx,ry,col,seed=1):
    import random
    r=random.Random(seed); out=''
    for i in range(n):
        x=cx+r.uniform(-rx,rx); y=cy+r.uniform(-ry,ry)*abs(1-((x-cx)/rx)**2)**.5
        a=r.uniform(0,180)
        out+=f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="2.4" ry="1.1" transform="rotate({a:.0f} {x:.1f} {y:.1f})" fill="{col}"/>'
    return out

ART={}

# 1 Agricultural: jute sack of rice + wheat sheaf + lentil bowl
p='ag'
wheat=''
for i,(x,a) in enumerate([(78,-14),(88,-6),(98,0),(108,7),(118,15)]):
    ear=''.join(f'<ellipse cx="0" cy="{-60-j*7}" rx="3.2" ry="6" transform="rotate({(-1)**j*28} 0 {-60-j*7}) translate({(-1)**j*3} 0)" fill="url(#{p}gold)"/>' for j in range(7))
    wheat+=f'<g transform="translate({x} 168) rotate({a})"><path d="M0 0 V-60" stroke="#c9a157" stroke-width="2"/>{ear}<path d="M0 -108 l0 -14" stroke="#e8c88a" stroke-width="1"/></g>'
ART['agriculture']=defs(p)+base(p)+wheat+f'''
<g filter="url(#{p}sh)">
<path d="M150 176 C140 150 146 110 160 92 L238 92 C252 110 258 150 248 176Z" fill="#b99764"/>
<path d="M150 176 C140 150 146 110 160 92 L238 92 C252 110 258 150 248 176Z" fill="none" stroke="#7d6136" stroke-width="1.5"/>
<clipPath id="{p}sk"><path d="M150 176 C140 150 146 110 160 92 L238 92 C252 110 258 150 248 176Z"/></clipPath>
<g clip-path="url(#{p}sk)"><g stroke="#a3824f" stroke-width=".7" opacity=".45">{''.join(f'<path d="M{146+i*10} 178 V90"/>' for i in range(12))}</g>
<g stroke="#d4bb88" stroke-width=".7" opacity=".45">{''.join(f'<path d="M140 {98+i*9} H260"/>' for i in range(10))}</g>
<path d="M156 110 C152 140 154 160 160 176" stroke="#fff" stroke-opacity=".18" stroke-width="8" fill="none"/></g>
<ellipse cx="199" cy="94" rx="40" ry="10" fill="#f6efe0"/>
{grains(199,92,70,36,8,"#fffaf0",3)}
<path d="M160 92 C170 84 228 84 238 92" fill="none" stroke="#7d6136" stroke-width="2"/>
<rect x="176" y="128" width="46" height="22" rx="2" fill="#0c3326" opacity=".85"/><text x="199" y="143" text-anchor="middle" font-family="Georgia,serif" font-size="9" fill="#f0cf8c" letter-spacing="1">BASMATI</text>
</g>
<g filter="url(#{p}sh)"><path d="M246 168 a26 12 0 0 0 52 0 Z" fill="url(#{p}brass)"/><ellipse cx="272" cy="166" rx="26" ry="7" fill="#c46a2c"/>{grains(272,164,40,22,5,"#e0873f",5)}</g>
'''

# 2 Spices: three heaps on brass plates + chillies, cinnamon, star anise
p='sp'
def heap(cx,cy,w,h,c1,c2,seed):
    import random
    r=random.Random(seed)
    dots=''.join(f'<circle cx="{cx+r.uniform(-w*.8,w*.8):.1f}" cy="{cy-r.uniform(2,h*.8):.1f}" r=".9" fill="{c2}" opacity=".7"/>' for _ in range(40))
    return (f'<ellipse cx="{cx}" cy="{cy+4}" rx="{w+12}" ry="8" fill="url(#{p}brass)"/><ellipse cx="{cx}" cy="{cy+2}" rx="{w+8}" ry="5.5" fill="#6b4614"/>'
            f'<path d="M{cx-w} {cy+2} Q{cx-w*.5} {cy-h*.9} {cx} {cy-h} Q{cx+w*.5} {cy-h*.9} {cx+w} {cy+2}Z" fill="{c1}"/>'
            f'<path d="M{cx-w*.35} {cy-h*.55} Q{cx-w*.1} {cy-h*.95} {cx+w*.1} {cy-h*.9}" stroke="#fff" stroke-opacity=".35" stroke-width="3" fill="none" stroke-linecap="round"/>{dots}')
chilli=lambda x,y,a,s=1: f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><path d="M0 0 C18 -4 40 2 52 14 C38 8 18 8 2 6Z" fill="#c62f1f"/><path d="M4 2 C18 0 34 4 44 10" stroke="#ff8a6a" stroke-width="1.4" fill="none" opacity=".7"/><path d="M0 0 C-4 -2 -8 -8 -6 -12" stroke="#3f6b2a" stroke-width="2.4" fill="none" stroke-linecap="round"/></g>'
star=lambda x,y,s: f'<g transform="translate({x} {y}) scale({s})">'+''.join(f'<path d="M0 0 L-3 -11 Q0 -14 3 -11Z" transform="rotate({k*45})" fill="#6a3b1d" stroke="#3d200e" stroke-width=".6"/>' for k in range(8))+'<circle r="2" fill="#3d200e"/></g>'
ART['spices']=defs(p)+base(p)+f'''
<g filter="url(#{p}sh)">{heap(104,160,40,40,"#e2a920","#a86c08",1)}{heap(212,160,40,44,"#b8321f","#6e170c",2)}{heap(158,170,34,30,"#8a6236","#4e3418",3)}</g>
<g filter="url(#{p}sh)">{chilli(210,92,-18)}{chilli(232,104,8,.8)}
<g transform="translate(66 104) rotate(-14)"><rect width="56" height="9" rx="4.5" fill="#8b4a22"/><rect y="3" width="56" height="3" fill="#a75d2f"/><rect y="12" width="50" height="8" rx="4" fill="#7a3f1b"/></g>
{star(270,150,1)}{star(40,160,.8)}</g>
<g fill="#7d9a3c">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.6" transform="rotate({a} {x} {y})"/>' for x,y,a in [(262,176,10),(276,180,-20),(50,182,30),(130,186,-10)])}</g>'''

# 3 Dry fruits: wooden bowl of cashews, almonds, raisins, makhana, walnut
p='df'
cashew=lambda x,y,a,s=1: f'<path transform="translate({x} {y}) rotate({a}) scale({s})" d="M-12 4 C-16 -8 -4 -16 8 -12 C3 -8 1 -2 6 4 C1 10 -9 10 -12 4Z" fill="#f2d4a0" stroke="#b98a4e" stroke-width="1"/>'
almond=lambda x,y,a: f'<g transform="translate({x} {y}) rotate({a})"><ellipse rx="9" ry="5" fill="#9b5a2e"/><path d="M-6 0 Q0 -3 6 0" stroke="#6d3c1b" stroke-width=".8" fill="none"/></g>'
makhana=lambda x,y,r: f'<g><circle cx="{x}" cy="{y}" r="{r}" fill="#f7f1e4"/><circle cx="{x-r*.3}" cy="{y-r*.3}" r="{r*.35}" fill="#fff"/><path d="M{x-r*.6} {y+r*.2} q{r*.6} {r*.5} {r*1.2} 0" stroke="#8b5a32" stroke-width="1.2" fill="none" opacity=".6"/></g>'
cs=''.join(cashew(x,y,a) for x,y,a in [(140,104,-20),(158,98,10),(176,102,-5),(194,98,20),(150,114,30),(170,112,-25),(188,112,5),(208,106,-12),(130,114,15)])
ART['dryfruits']=defs(p)+base(p)+f'''
<g filter="url(#{p}sh)">
<path d="M112 108 C112 150 132 172 170 172 C208 172 228 150 228 108Z" fill="#6b3d1e"/>
<path d="M112 108 C112 150 132 172 170 172 C208 172 228 150 228 108Z" fill="none" stroke="#3e220f" stroke-width="1.5"/>
<g stroke="#8a5530" stroke-width="1" opacity=".55" fill="none"><path d="M118 124 Q170 140 222 124"/><path d="M124 142 Q170 156 216 142"/><path d="M136 158 Q170 168 204 158"/></g>
<ellipse cx="170" cy="108" rx="58" ry="12" fill="#4a2912"/>{cs}</g>
<g filter="url(#{p}sh)">{''.join(makhana(x,y,r) for x,y,r in [(62,160,11),(84,170,10),(56,180,9),(80,150,8),(250,166,11),(272,158,9)])}
{''.join(almond(x,y,a) for x,y,a in [(266,182,20),(240,184,-15),(100,184,30)])}
<g fill="#5a1f2e">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="3"/>' for x,y in [(110,174),(120,180),(232,174),(288,176),(42,168)])}</g>
<g transform="translate(286 138)"><circle r="13" fill="#b98a5a"/><path d="M0 -13 V13 M-9 -6 q5 3 0 6 q-5 3 0 6 M9 -6 q-5 3 0 6 q5 3 0 6" stroke="#7a5534" stroke-width="1.4" fill="none"/></g></g>'''

# 4 Herbs: mortar & pestle with green powder, roots, leaves, jar
p='hb'
leaf=lambda x,y,a,s,c="#4f9a4a": f'<g transform="translate({x} {y}) rotate({a}) scale({s})"><path d="M0 0 C10 -10 30 -10 40 0 C30 10 10 10 0 0Z" fill="{c}"/><path d="M0 0 H38" stroke="#2c5e2a" stroke-width="1"/>'+''.join(f'<path d="M{8+k*8} 0 l4 -4 M{8+k*8} 0 l4 4" stroke="#2c5e2a" stroke-width=".7"/>' for k in range(4))+'</g>'
ART['herbs']=defs(p)+base(p)+f'''
<g filter="url(#{p}sh)">
<path d="M54 60 C70 40 120 60 112 100" stroke="#3f7a3a" stroke-width="2" fill="none"/>
{leaf(60,64,-30,.8)}{leaf(76,56,-10,.7,"#5aa852")}{leaf(92,64,20,.75)}{leaf(104,80,50,.7,"#5aa852")}{leaf(70,80,-60,.6,"#468f42")}
</g>
<g filter="url(#{p}sh)">
<path d="M124 120 h88 l-10 44 q-34 14 -68 0Z" fill="#cfc7b6"/><path d="M124 120 h88 l-10 44 q-34 14 -68 0Z" fill="none" stroke="#8d8576" stroke-width="1.4"/>
<ellipse cx="168" cy="120" rx="44" ry="9" fill="#a39b8a"/><ellipse cx="168" cy="119" rx="38" ry="6.5" fill="#7fa84a"/>
<path d="M150 116 q18 -8 34 0" fill="#97bd5e"/>
<path d="M190 70 L172 116" stroke="#b5ad9b" stroke-width="12" stroke-linecap="round"/><path d="M190 70 L180 94" stroke="#e8e1d1" stroke-width="3" stroke-linecap="round" opacity=".6"/>
<path d="M140 150 q28 8 56 0" stroke="#e8e1d1" stroke-width="2" fill="none" opacity=".5"/>
</g>
<g filter="url(#{p}sh)">
<g transform="translate(232 128)"><rect x="0" y="0" width="44" height="46" rx="8" fill="#f3ead6" opacity=".95"/><rect x="0" y="22" width="44" height="24" rx="6" fill="#c9a24a"/><rect x="-2" y="-8" width="48" height="12" rx="3" fill="url(#{p}gold)"/><rect x="6" y="28" width="32" height="10" rx="1" fill="#0c3326"/><text x="22" y="35.5" text-anchor="middle" font-family="Georgia,serif" font-size="6" fill="#f0cf8c">HERBAL</text></g>
</g>
<g filter="url(#{p}sh)" stroke-linecap="round" fill="none">
<path d="M60 168 C80 150 104 162 120 150" stroke="#c9a16a" stroke-width="6"/><path d="M80 160 C82 170 76 178 70 182" stroke="#b58a52" stroke-width="3"/><path d="M100 156 C108 166 106 176 112 182" stroke="#b58a52" stroke-width="2.5"/>
<path d="M66 172 C88 160 100 172 118 162" stroke="#e2c08a" stroke-width="1.5" opacity=".6"/>
</g>
{leaf(246,182,-170,.55,"#5aa852")}{leaf(210,186,-150,.5)}'''

# 5 Leather: tote bag + wallet + belt
p='lt'
ART['leather']=defs(p)+base(p)+f'''
<defs><linearGradient id="{p}lea" x1="0" x2="1"><stop offset="0" stop-color="#5c2f16"/><stop offset=".5" stop-color="#9a5a2c"/><stop offset="1" stop-color="#5a2d14"/></linearGradient></defs>
<g filter="url(#{p}sh)">
<path d="M128 74 C128 40 196 40 196 74" stroke="#4a2410" stroke-width="7" fill="none"/>
<path d="M128 74 C128 40 196 40 196 74" stroke="#7a4421" stroke-width="3" fill="none"/>
<path d="M98 76 H226 L240 172 H84Z" fill="url(#{p}lea)"/>
<path d="M102 82 H222 L234 166 H90Z" fill="none" stroke="#e8c48a" stroke-width="1.3" stroke-dasharray="4 3" opacity=".9"/>
<path d="M98 76 H226 L230 100 H94Z" fill="#7d4320"/>
<rect x="150" y="96" width="24" height="16" rx="3" fill="url(#{p}brass)"/><rect x="157" y="101" width="10" height="6" rx="1" fill="#6b4614"/>
<path d="M120 76 v-2 M204 76 v-2" stroke="url(#{p}gold)" stroke-width="6"/>
<path d="M110 120 C140 128 186 128 214 120" stroke="#b87a45" stroke-width="2" fill="none" opacity=".4"/>
</g>
<g filter="url(#{p}sh)" transform="translate(246 136) rotate(-8)">
<rect width="52" height="36" rx="5" fill="#3b1e10"/><rect x="3" y="3" width="46" height="30" rx="4" fill="none" stroke="#d9a95e" stroke-width="1" stroke-dasharray="3 2"/><path d="M0 12 H52" stroke="#5c321a" stroke-width="2"/><circle cx="44" cy="20" r="2.5" fill="url(#{p}brass)"/></g>
<g filter="url(#{p}sh)">
<path d="M30 176 C30 150 80 150 80 168 C80 180 50 182 44 172 C40 164 58 160 66 166" stroke="#6e3a1a" stroke-width="9" fill="none" stroke-linecap="round"/>
<path d="M30 176 C30 150 80 150 80 168" stroke="#9a5a2c" stroke-width="2" fill="none" opacity=".6"/>
<rect x="22" y="168" width="18" height="16" rx="2" fill="none" stroke="url(#{p}brass)" stroke-width="3.5"/></g>'''

# 6 Handicrafts: brass lota/vase, diya with flame, marble inlay plate, terracotta pot
p='hc'
ART['handicrafts']=defs(p)+base(p)+f'''
<defs><radialGradient id="{p}fl" cx="50%" cy="70%" r="60%"><stop offset="0" stop-color="#fff6c8"/><stop offset=".5" stop-color="#ffc24a"/><stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/></radialGradient>
<linearGradient id="{p}tc" x1="0" x2="1"><stop offset="0" stop-color="#8a3f1e"/><stop offset=".5" stop-color="#c66a3a"/><stop offset="1" stop-color="#7a361a"/></linearGradient></defs>
<g filter="url(#{p}sh)">
<ellipse cx="160" cy="150" rx="62" ry="22" fill="#f1ece2"/><ellipse cx="160" cy="150" rx="54" ry="18" fill="none" stroke="#c9c1b0" stroke-width="1"/>
<g fill="#1f6b55">{''.join(f'<ellipse cx="{160+40*__import__("math").cos(k*3.1416/4):.1f}" cy="{150+13*__import__("math").sin(k*3.1416/4):.1f}" rx="5" ry="2.4"/>' for k in range(8))}</g>
<g fill="#b8321f">{''.join(f'<circle cx="{160+30*__import__("math").cos(k*3.1416/4+.4):.1f}" cy="{150+10*__import__("math").sin(k*3.1416/4+.4):.1f}" r="1.8"/>' for k in range(8))}</g>
<circle cx="160" cy="150" r="0"/><ellipse cx="160" cy="150" rx="12" ry="4.5" fill="#d9a24a"/>
</g>
<g filter="url(#{p}sh)">
<path d="M96 168 C66 150 66 108 86 92 C80 82 82 72 88 68 H104 C110 72 112 82 106 92 C126 108 126 150 96 168Z" fill="url(#{p}brass)"/>
<path d="M70 124 H122 M72 136 H120" stroke="#7a4f17" stroke-width="1.2" opacity=".7"/>
<g stroke="#7a4f17" stroke-width=".9" fill="none" opacity=".7">{''.join(f'<path d="M{74+i*8} 130 q4 -5 8 0"/>' for i in range(6))}</g>
<ellipse cx="96" cy="68" rx="14" ry="4" fill="#7a4f17"/><path d="M82 100 q4 -6 10 -6" stroke="#fff4cf" stroke-width="3" fill="none" opacity=".6" stroke-linecap="round"/>
</g>
<g filter="url(#{p}sh)">
<path d="M222 120 C214 138 222 170 246 170 C270 170 278 138 270 120 C262 112 230 112 222 120Z" fill="url(#{p}tc)"/>
<ellipse cx="246" cy="118" rx="22" ry="6" fill="#5e2810"/><path d="M226 140 Q246 148 266 140" stroke="#f0cf8c" stroke-width="2" fill="none"/><path d="M228 150 Q246 157 264 150" stroke="#f0cf8c" stroke-width="1.2" fill="none" stroke-dasharray="2 3"/>
</g>
<g filter="url(#{p}sh)">
<path d="M190 176 q22 16 44 0 q-6 12 -22 12 q-16 0 -22 -12Z" fill="url(#{p}brass)"/><path d="M212 176 q0 -4 0 -8" stroke="#3d200e" stroke-width="1.5"/>
</g>
<ellipse cx="212" cy="156" rx="16" ry="22" fill="url(#{p}fl)"/><path d="M212 168 C205 161 207 150 212 141 C217 150 219 161 212 168Z" fill="#ffd25a"/><path d="M212 166 C209 161 210 155 212 150 C214 155 215 161 212 166Z" fill="#fff6d8"/>'''

# 7 Textiles: folded block-print stack, spool, rolled rug
p='tx'
def fold(x,y,w,h,c,pat):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{c}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="url(#{pat})"/><path d="M{x+4} {y+2} H{x+w-4}" stroke="#fff" stroke-opacity=".25" stroke-width="1.5"/>'
ART['textiles']=defs(p)+base(p)+f'''
<defs>
<pattern id="{p}p1" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="2.4" fill="#f0cf8c" opacity=".85"/><circle cx="0" cy="0" r="1.2" fill="#f0cf8c" opacity=".6"/><circle cx="12" cy="12" r="1.2" fill="#f0cf8c" opacity=".6"/></pattern>
<pattern id="{p}p2" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M7 1 L13 7 L7 13 L1 7Z" fill="none" stroke="#fff3d6" stroke-width="1.1" opacity=".75"/></pattern>
<pattern id="{p}p3" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 5 H10" stroke="#0c3326" stroke-width="2" opacity=".35"/></pattern>
<pattern id="{p}p4" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M8 2 C11 6 11 10 8 14 C5 10 5 6 8 2Z" fill="#1d4f3b" opacity=".55"/></pattern>
</defs>
<g filter="url(#{p}sh)">
{fold(62,148,132,24,"#7a2f2a",p+"p2")}{fold(68,124,124,24,"#1f6b55",p+"p1")}{fold(58,100,134,24,"#e4b65a",p+"p4")}{fold(70,78,116,22,"#2b4f7e",p+"p2")}
</g>
<g filter="url(#{p}sh)">
<rect x="228" y="70" width="40" height="8" rx="2" fill="#8b5a2b"/><rect x="228" y="150" width="40" height="8" rx="2" fill="#8b5a2b"/>
<rect x="232" y="78" width="32" height="72" fill="#c9302c"/>
<g stroke="#ff8a7a" stroke-width="1" opacity=".55">{''.join(f'<path d="M232 {82+i*5} H264"/>' for i in range(14))}</g>
<path d="M264 120 C280 132 284 160 296 172" stroke="#c9302c" stroke-width="1.6" fill="none"/>
</g>
<g filter="url(#{p}sh)" transform="translate(210 172)">
<rect x="-6" y="-10" width="96" height="20" rx="10" fill="#d9c49b"/><rect x="-6" y="-10" width="96" height="20" rx="10" fill="url(#{p}p3)"/>
<ellipse cx="-6" cy="0" rx="6" ry="10" fill="#b89c6a"/><path d="M-10 0 a4 7 0 1 0 8 0 a3 5 0 1 0 -6 0" stroke="#8a6a3a" fill="none" stroke-width="1"/>
</g>'''

def svg(cat):
    return f'<svg class="art" viewBox="0 0 320 200" role="img" aria-label="{cat} illustration">{ART[cat]}</svg>'
MAP={'agriculture':'agriculture','spices':'spices','dryfruits':'dryfruits','herbs':'herbs','leather':'leather','handicrafts':'handicrafts','textiles':'textiles'}
if __name__=='__main__':
    html='<html><body style="margin:0;background:#fff;display:grid;grid-template-columns:repeat(2,640px);gap:8px">'+''.join(f'<div style="width:640px">{svg(k).replace("class=\"art\"","width=\"640\" height=\"400\"")}</div>' for k in ART)+'</body></html>'
    open('/home/claude/seo/arts_test.html','w').write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1300,'height':1650})
        pg.goto('file:///home/claude/seo/arts_test.html'); pg.wait_for_timeout(300)
        pg.screenshot(path='/tmp/claude-0/-home-claude/3e5b28d0-d3ed-5aac-bf05-a4c728260f60/scratchpad/arts.png',full_page=True); b.close()

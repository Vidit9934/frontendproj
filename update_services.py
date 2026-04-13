import re, subprocess

# ── All 12 services from tunefry.com ──
SERVICES = [
    {
        "name": "Digital Music Distribution",
        "desc": "Publish your songs across 100+ platforms including Spotify, Apple Music, JioSaavn, Amazon Music, and more with reliable digital music distribution.",
        "color": "#3B82F6",
        "bg": "linear-gradient(145deg,rgba(59,130,246,0.28),rgba(4,10,32,0.96))",
        "icon": '<path d="M12 2a10 10 0 100 20A10 10 0 0012 2z"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>',
        "svg_bg": '<circle cx="50" cy="50" r="42"/><ellipse cx="50" cy="50" rx="22" ry="42"/><line x1="8" y1="50" x2="92" y2="50"/><line x1="50" y1="8" x2="50" y2="92"/>'
    },
    {
        "name": "Music Marketing & Playlist Pitching",
        "desc": "Promote your songs through editorial playlists on Spotify, curated marketing strategies, and targeted audience discovery.",
        "color": "#2DCA72",
        "bg": "linear-gradient(145deg,rgba(45,202,114,0.28),rgba(0,26,12,0.96))",
        "icon": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
        "svg_bg": '<rect x="15" y="15" width="70" height="70" rx="10"/><line x1="28" y1="36" x2="72" y2="36"/><line x1="28" y1="50" x2="72" y2="50"/><line x1="28" y1="64" x2="58" y2="64"/>'
    },
    {
        "name": "Callertune (CRBT)",
        "desc": "Turn your songs into caller tunes and reach millions of mobile users across India through all major telecom operators.",
        "color": "#FF6B00",
        "bg": "linear-gradient(145deg,rgba(255,107,0,0.28),rgba(32,12,0,0.96))",
        "icon": '<path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/>',
        "svg_bg": '<rect x="28" y="10" width="44" height="80" rx="8"/><rect x="33" y="16" width="34" height="56" rx="4" opacity="0.15" fill="currentColor"/><line x1="42" y1="78" x2="58" y2="78" stroke-width="3"/>'
    },
    {
        "name": "Artist Services",
        "desc": "Access professional one-on-one support designed for creators. Our dedicated team helps you grow your career and navigate the music industry.",
        "color": "#A855F7",
        "bg": "linear-gradient(145deg,rgba(168,85,247,0.28),rgba(20,0,38,0.96))",
        "icon": '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/>',
        "svg_bg": '<circle cx="35" cy="30" r="14"/><path d="M10 80 Q10 56 35 56 Q60 56 60 80"/><circle cx="70" cy="32" r="12"/><path d="M52 80 Q52 58 70 58 Q88 58 88 80"/>'
    },
    {
        "name": "Song Transfer & Portability",
        "desc": "Easily transfer your entire music catalog from DistroKid, TuneCore, CD Baby, or any other distributor to Tunefry without losing stream counts.",
        "color": "#06B6D4",
        "bg": "linear-gradient(145deg,rgba(6,182,212,0.28),rgba(0,20,30,0.96))",
        "icon": '<polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 014-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 01-4 4H3"/>',
        "svg_bg": '<circle cx="50" cy="50" r="38"/><polyline points="35,35 20,50 35,65"/><polyline points="65,35 80,50 65,65"/><line x1="20" y1="50" x2="80" y2="50"/>'
    },
    {
        "name": "Content ID (YouTube)",
        "desc": "Protect your music on YouTube with Content ID and automatically monetize every video that uses your tracks across the platform.",
        "color": "#EF4444",
        "bg": "linear-gradient(145deg,rgba(239,68,68,0.28),rgba(38,0,0,0.96))",
        "icon": '<path d="M22.54 6.42a2.78 2.78 0 00-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46A2.78 2.78 0 001.46 6.42 29 29 0 001 12a29 29 0 00.46 5.58A2.78 2.78 0 003.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 001.95-1.95A29 29 0 0023 12a29 29 0 00-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02"/>',
        "svg_bg": '<rect x="8" y="22" width="84" height="56" rx="12"/><polygon points="40,45 65,58 40,71" fill="currentColor" opacity="0.25" stroke-width="2"/>'
    },
    {
        "name": "Lyrics Distribution",
        "desc": "Distribute your song lyrics to Spotify, Apple Music, and other major streaming platforms for enhanced listener engagement.",
        "color": "#EC4899",
        "bg": "linear-gradient(145deg,rgba(236,72,153,0.28),rgba(38,0,18,0.96))",
        "icon": '<line x1="17" y1="10" x2="3" y2="10"/><line x1="21" y1="6" x2="3" y2="6"/><line x1="21" y1="14" x2="3" y2="14"/><line x1="17" y1="18" x2="3" y2="18"/>',
        "svg_bg": '<rect x="12" y="12" width="76" height="76" rx="8"/><line x1="24" y1="30" x2="76" y2="30"/><line x1="24" y1="44" x2="76" y2="44"/><line x1="24" y1="58" x2="60" y2="58"/><line x1="24" y1="72" x2="50" y2="72"/>'
    },
    {
        "name": "Reports & Analytics",
        "desc": "Track your music performance with detailed real-time analytics across all platforms — streams, revenue, audience location, and growth trends.",
        "color": "#8B5CF6",
        "bg": "linear-gradient(145deg,rgba(139,92,246,0.28),rgba(18,0,40,0.96))",
        "icon": '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><path d="M3 3v18h18"/>',
        "svg_bg": '<rect x="10" y="10" width="80" height="80" rx="8" fill="currentColor" opacity="0.04"/><line x1="10" y1="75" x2="90" y2="75"/><line x1="20" y1="75" x2="20" y2="55" stroke-width="8" stroke-linecap="round" opacity="0.5"/><line x1="36" y1="75" x2="36" y2="35" stroke-width="8" stroke-linecap="round" opacity="0.7"/><line x1="52" y1="75" x2="52" y2="45" stroke-width="8" stroke-linecap="round" opacity="0.6"/><line x1="68" y1="75" x2="68" y2="25" stroke-width="8" stroke-linecap="round" opacity="0.8"/>'
    },
    {
        "name": "Affordable Plans",
        "desc": "Start free and scale as you grow. Tunefry offers the most affordable distribution plans for independent artists — starting at ₹0.",
        "color": "#EAB308",
        "bg": "linear-gradient(145deg,rgba(234,179,8,0.28),rgba(30,22,0,0.96))",
        "icon": '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
        "svg_bg": '<circle cx="50" cy="50" r="38"/><circle cx="50" cy="50" r="28" stroke-dasharray="5 4"/><line x1="50" y1="22" x2="50" y2="78"/><path d="M62 32 Q74 32 74 44 Q74 56 50 56 Q26 56 26 68 Q26 80 50 80"/>'
    },
    {
        "name": "Copyright Protection",
        "desc": "Secure your music rights with robust copyright protection. We register your releases and defend your ownership across all digital platforms.",
        "color": "#6366F1",
        "bg": "linear-gradient(145deg,rgba(99,102,241,0.28),rgba(10,10,40,0.96))",
        "icon": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        "svg_bg": '<path d="M50 10 L86 24 L86 52 Q86 78 50 90 Q14 78 14 52 L14 24 Z" opacity="0.15" fill="currentColor"/><path d="M50 10 L86 24 L86 52 Q86 78 50 90 Q14 78 14 52 L14 24 Z"/>'
    },
    {
        "name": "Illegal Takedown",
        "desc": "Remove unauthorized copies of your music from online platforms. We file DMCA takedowns and protect your content from piracy.",
        "color": "#F97316",
        "bg": "linear-gradient(145deg,rgba(249,115,22,0.28),rgba(40,8,0,0.96))",
        "icon": '<circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/>',
        "svg_bg": '<circle cx="50" cy="50" r="40"/><line x1="18" y1="18" x2="82" y2="82" stroke-width="8" stroke-linecap="round"/>'
    },
    {
        "name": "Lifetime Availability",
        "desc": "Your music stays live on all streaming platforms forever — no annual renewals needed. One upload, permanent presence.",
        "color": "#14B8A6",
        "bg": "linear-gradient(145deg,rgba(20,184,166,0.28),rgba(0,22,20,0.96))",
        "icon": '<path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3"/>',
        "svg_bg": '<circle cx="50" cy="50" r="38"/><path d="M26 50 Q26 26 50 26 Q74 26 74 50 Q74 74 50 74 Q26 74 26 50" fill="none"/><path d="M35 50 Q35 38 50 38 Q65 38 65 50 Q65 62 50 62 Q35 62 35 50" fill="none"/>'
    },
]

# ═══════════════════════════════════════════════════
# 1. BUILD services.html — 12 cards, 4-col, smaller
# ═══════════════════════════════════════════════════
result = subprocess.run(
    ['git', 'show', '869231f:services.html'],
    capture_output=True,
    cwd=r'C:/Users/ViditVaibhav/Desktop/frontend 11'
)
c = result.stdout.decode('utf-8', errors='replace')
print(f"Base services.html: {len(c)} chars")

# Branding
c = c.replace("onclick=\"alert('Kindly login'); return false;\" class=\"nav-refer\"", "class=\"nav-refer\"")
c = c.replace("onclick=\"alert('Kindly login'); return false;\" style=\"color:var(--or)\"", "style=\"color:var(--or)\"")
c = c.replace('href="#" class="nav-refer"', 'href="refer-earn.html" class="nav-refer"')
c = c.replace('href="#" style="color:var(--or)"', 'href="refer-earn.html" style="color:var(--or)"')
c = c.replace('<a href="index.html" class="btn-ghost">Log in</a>', '<a href="login.html" class="btn-ghost">Log in</a>')
c = c.replace('<a href="index.html" class="btn-or"', '<a href="signup.html" class="btn-or"')
c = c.replace('150+', '100+')
c = c.replace(
    '    <div class="logo-sq">T</div>\n    <div class="logo-txt"><b>Tune</b>fry</div>',
    '    <img src="tunefry-logo.png" alt="Tunefry" style="height:38px;width:auto;display:block;object-fit:contain;">'
)
c = c.replace(
    '        <div class="footer-logo-sq">T</div>\n        <div class="footer-logo-txt"><b>Tune</b>fry</div>',
    '        <img src="tunefry-logo.png" alt="Tunefry" style="height:30px;width:auto;display:block;object-fit:contain;">'
)

# 4-col grid
c = c.replace(
    '.services-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; }',
    '.services-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; }'
)

# Flip CSS (smaller cards — 220px)
flip_css = """
/* FLIP CARDS */
.flip-wrap { perspective:900px; height:220px; }
.flip-wrap:hover .flip-inner,
.flip-wrap.tapped .flip-inner { transform:rotateY(180deg); }
.flip-inner {
  position:relative; width:100%; height:100%;
  transform-style:preserve-3d;
  transition:transform 0.6s ease;
  border-radius:16px;
}
.flip-face {
  position:absolute; inset:0;
  border-radius:16px;
  backface-visibility:hidden;
  -webkit-backface-visibility:hidden;
  overflow:hidden;
}
.flip-front {
  background:linear-gradient(165deg,rgba(26,21,17,0.97) 0%,rgba(16,13,10,0.98) 100%);
  border:0.5px solid rgba(255,255,255,0.11);
  box-shadow:0 6px 24px rgba(0,0,0,0.45),inset 0 1px 0 rgba(255,255,255,0.06);
  padding:20px 18px 16px;
  display:flex; flex-direction:column; gap:8px; position:relative;
}
.flip-front::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2.5px;
  border-radius:16px 16px 0 0;
  background:var(--faccent,rgba(255,107,0,0.9));
}
.flip-back {
  transform:rotateY(180deg);
  padding:18px 18px;
  display:flex; flex-direction:column; justify-content:center; gap:10px;
  border:0.5px solid rgba(255,255,255,0.13);
  box-shadow:0 6px 24px rgba(0,0,0,0.55),inset 0 1px 0 rgba(255,255,255,0.07);
}
.fb-title { font-family:var(--font-d); font-size:14px; font-weight:700; color:#fff; line-height:1.3; }
.fb-desc  { font-size:11.5px; line-height:1.75; color:rgba(255,255,255,0.8); flex:1; }
.fb-btn   {
  display:inline-flex; align-items:center; gap:5px; padding:6px 14px;
  background:rgba(255,255,255,0.12); border:0.5px solid rgba(255,255,255,0.2);
  border-radius:100px; font-size:11px; font-weight:600; color:#fff;
  text-decoration:none; width:fit-content; transition:background .2s;
}
.fb-btn:hover { background:rgba(255,255,255,0.22); }
.flip-hint { font-size:9.5px; color:rgba(255,255,255,0.2); margin-top:auto; }
.svc-name { font-family:var(--font-d); font-size:13.5px; font-weight:700; color:var(--t1); line-height:1.3; }
"""
c = c.replace('.svc-card:hover .svc-link { color:var(--or); gap:8px; }',
              '.svc-card:hover .svc-link { color:var(--or); gap:8px; }' + flip_css)

# Build 12 card HTML
def make_card(svc, au_cls, idx):
    return (
        f'      <div class="flip-wrap {au_cls}" style="--faccent:{svc["color"]};">\n'
        f'        <div class="flip-inner">\n'
        f'          <div class="flip-face flip-front">\n'
        f'            <div class="svc-bg"><svg viewBox="0 0 100 100" fill="none" stroke="{svc["color"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{svc["svg_bg"]}</svg></div>\n'
        f'            <div class="svc-icon-wrap" style="stroke:{svc["color"]};">'
        f'<svg viewBox="0 0 24 24" fill="none" stroke="{svc["color"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{svc["icon"]}</svg></div>\n'
        f'            <div class="svc-name">{svc["name"]}</div>\n'
        f'            <div class="flip-hint">&#8635; hover for details</div>\n'
        f'          </div>\n'
        f'          <div class="flip-face flip-back" style="background:{svc["bg"]};">\n'
        f'            <div class="fb-title">{svc["name"]}</div>\n'
        f'            <div class="fb-desc">{svc["desc"]}</div>\n'
        f'            <a href="services.html" class="fb-btn">Learn more &rarr;</a>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>\n'
    )

au_classes = ['au','au au-d1','au au-d2','au au-d3','au','au au-d1','au au-d2','au au-d3','au','au au-d1','au au-d2','au au-d3']

cards_html = '\n'.join(make_card(svc, au_classes[i], i) for i, svc in enumerate(SERVICES))

# Replace entire services-grid content
grid_start = c.find('<div class="services-grid">')
grid_end   = c.find('</div>', c.rfind('</div>', 0, c.find('<!-- ── HOW IT WORKS ──'))) + 6
# More reliable: find the closing of services-grid
# Find the last svc-card closing
idx = c.find('<div class="services-grid">')
# find its closing </div>
depth = 0
pos = idx
while pos < len(c):
    if c[pos:pos+4] == '<div':
        depth += 1
    elif c[pos:pos+6] == '</div>':
        depth -= 1
        if depth == 0:
            grid_end = pos + 6
            break
    pos += 1

old_grid = c[grid_start:grid_end]
new_grid = '<div class="services-grid">\n\n' + cards_html + '\n    </div>'
c = c.replace(old_grid, new_grid)

# Mobile tap JS
tap = """
document.querySelectorAll('.flip-wrap').forEach(function(w){
  w.addEventListener('click',function(){ this.classList.toggle('tapped'); });
});
"""
c = c.replace('});\n\nwindow.addEventListener', tap + '\n});\n\nwindow.addEventListener')

with open(r'C:/Users/ViditVaibhav/Desktop/frontend 11/services.html', 'w', encoding='utf-8') as f:
    f.write(c)
print(f"services.html done — {c.count('flip-wrap')} flip cards")


# ═══════════════════════════════════════════════════
# 2. UPDATE home.html services section
# ═══════════════════════════════════════════════════
with open(r'C:/Users/ViditVaibhav/Desktop/frontend 11/home.html', 'r', encoding='utf-8') as f:
    h = f.read()

# Add flip CSS for home page (inside the <style> block)
home_flip_css = """
/* ── Home page service flip cards ── */
.home-svc-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-bottom:32px; }
.h-flip-wrap { perspective:900px; height:200px; cursor:pointer; }
.h-flip-wrap:hover .h-flip-inner,
.h-flip-wrap.tapped .h-flip-inner { transform:rotateY(180deg); }
.h-flip-inner {
  position:relative; width:100%; height:100%;
  transform-style:preserve-3d;
  transition:transform 0.6s ease;
  border-radius:14px;
}
.h-flip-face {
  position:absolute; inset:0;
  border-radius:14px;
  backface-visibility:hidden;
  -webkit-backface-visibility:hidden;
  overflow:hidden;
}
.h-flip-front {
  background:linear-gradient(165deg,rgba(26,21,17,0.97) 0%,rgba(16,13,10,0.98) 100%);
  border:0.5px solid rgba(255,255,255,0.10);
  box-shadow:0 4px 16px rgba(0,0,0,0.4),inset 0 1px 0 rgba(255,255,255,0.05);
  padding:18px 14px 14px;
  display:flex; flex-direction:column; align-items:center; text-align:center; gap:8px; position:relative;
}
.h-flip-front::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  border-radius:14px 14px 0 0;
  background:var(--hfa,rgba(255,107,0,0.9));
}
.h-flip-back {
  transform:rotateY(180deg);
  padding:14px 14px;
  display:flex; flex-direction:column; justify-content:center; gap:8px;
  border:0.5px solid rgba(255,255,255,0.12);
  box-shadow:0 4px 16px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.06);
}
.h-fb-title { font-family:var(--font-d); font-size:12.5px; font-weight:700; color:#fff; line-height:1.3; }
.h-fb-desc  { font-size:11px; line-height:1.7; color:rgba(255,255,255,0.78); flex:1; }
.h-flip-icon { width:36px; height:36px; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.h-flip-icon svg { width:18px; height:18px; fill:none; stroke-width:1.8; stroke-linecap:round; stroke-linejoin:round; }
.h-flip-name { font-family:var(--font-d); font-size:11.5px; font-weight:700; color:var(--t1); line-height:1.3; }
.h-flip-hint { font-size:9px; color:rgba(255,255,255,0.18); margin-top:auto; }
@media(max-width:900px){ .home-svc-grid{ grid-template-columns:repeat(3,1fr); } }
@media(max-width:600px){ .home-svc-grid{ grid-template-columns:repeat(2,1fr); } }
"""

# Insert the CSS right before the closing </style> of the inline style block in home.html
# Find the first </style> after the opening <style> tag
style_close = h.find('</style>')
h = h[:style_close] + home_flip_css + '\n' + h[style_close:]

# Build home service cards (all 12)
def make_home_card(svc, i):
    return (
        f'      <div class="h-flip-wrap au" style="--hfa:{svc["color"]};">\n'
        f'        <div class="h-flip-inner">\n'
        f'          <div class="h-flip-face h-flip-front">\n'
        f'            <div class="h-flip-icon" style="background:rgba({hex_to_rgb(svc["color"])},0.15);border:0.5px solid rgba({hex_to_rgb(svc["color"])},0.3);">'
        f'<svg viewBox="0 0 24 24" stroke="{svc["color"]}">{svc["icon"]}</svg></div>\n'
        f'            <div class="h-flip-name">{svc["name"]}</div>\n'
        f'            <div class="h-flip-hint">&#8635;</div>\n'
        f'          </div>\n'
        f'          <div class="h-flip-face h-flip-back" style="background:{svc["bg"]};">\n'
        f'            <div class="h-fb-title">{svc["name"]}</div>\n'
        f'            <div class="h-fb-desc">{svc["desc"]}</div>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>\n'
    )

def hex_to_rgb(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f'{r},{g},{b}'

home_cards_html = '\n'.join(make_home_card(svc, i) for i, svc in enumerate(SERVICES))

# Find and replace the Our Services section in home.html
svc_section_start = h.find('<!-- ── OUR SERVICES ──')
svc_section_end   = h.find('\n<!-- ──', svc_section_start + 10)

new_home_svc_section = (
    '<!-- \u2500\u2500 OUR SERVICES \u2500\u2500 -->\n'
    '<section style="padding:80px 40px; background:var(--s1); border-top:0.5px solid var(--bd);">\n'
    '  <div class="sec-inner">\n'
    '    <div class="sec-head au" style="text-align:center; margin-bottom:36px;">\n'
    '      <div class="sec-eyebrow">What We Offer</div>\n'
    '      <h2 class="sec-title">Our Services</h2>\n'
    '      <p class="sec-sub" style="max-width:520px; margin:0 auto;">Hover or tap any card to learn more.</p>\n'
    '    </div>\n'
    '    <div class="home-svc-grid">\n'
    + home_cards_html +
    '    </div>\n'
    '    <div style="text-align:center;">\n'
    '      <a href="services.html" style="display:inline-flex;align-items:center;gap:8px;padding:12px 28px;background:linear-gradient(135deg,var(--or),#ff8a40);border-radius:100px;font-family:var(--font-d);font-size:13px;font-weight:700;color:#fff;text-decoration:none;box-shadow:0 6px 20px rgba(255,107,0,0.35);">View All Services &rarr;</a>\n'
    '    </div>\n'
    '  </div>\n'
    '</section>\n'
)

h = h[:svc_section_start] + new_home_svc_section + h[svc_section_end:]

# Add mobile tap JS for home page
home_tap = """
document.querySelectorAll('.h-flip-wrap').forEach(function(w){
  w.addEventListener('click',function(){ this.classList.toggle('tapped'); });
});
"""
h = h.replace('\nfunction homeFaqToggle', home_tap + '\nfunction homeFaqToggle')

with open(r'C:/Users/ViditVaibhav/Desktop/frontend 11/home.html', 'w', encoding='utf-8') as f:
    f.write(h)
print(f"home.html done — {h.count('h-flip-wrap')} home service flip cards")
print("All done!")

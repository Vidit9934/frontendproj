import re, subprocess

# Get good working version from git
result = subprocess.run(
    ['git', 'show', '869231f:services.html'],
    capture_output=True,
    cwd=r'C:/Users/ViditVaibhav/Desktop/frontend 11'
)
c = result.stdout.decode('utf-8', errors='replace')
print(f"Got {len(c)} chars from git")

# ── Branding updates ──
c = c.replace("onclick=\"alert('Kindly login'); return false;\" class=\"nav-refer\"", "class=\"nav-refer\"")
c = c.replace("onclick=\"alert('Kindly login'); return false;\" style=\"color:var(--or)\"", "style=\"color:var(--or)\"")
c = c.replace('href="#" class="nav-refer"', 'href="refer-earn.html" class="nav-refer"')
c = c.replace('href="#" style="color:var(--or)"', 'href="refer-earn.html" style="color:var(--or)"')
c = c.replace('<a href="index.html" class="btn-ghost">Log in</a>', '<a href="login.html" class="btn-ghost">Log in</a>')
c = c.replace('<a href="index.html" class="btn-or"', '<a href="signup.html" class="btn-or"')
c = c.replace('150+', '100+')

# Logo swap
c = c.replace(
    '    <div class="logo-sq">T</div>\n    <div class="logo-txt"><b>Tune</b>fry</div>',
    '    <img src="tunefry-logo.png" alt="Tunefry" style="height:38px;width:auto;display:block;object-fit:contain;">'
)
c = c.replace(
    '        <div class="footer-logo-sq">T</div>\n        <div class="footer-logo-txt"><b>Tune</b>fry</div>',
    '        <img src="tunefry-logo.png" alt="Tunefry" style="height:30px;width:auto;display:block;object-fit:contain;">'
)

# ── Inject FLIP CSS after .svc-link hover rule ──
flip_css = """
/* ═══════════════════════════════════════════════════
   FLIP CARD — injected cleanly, no backdrop-filter
   ═══════════════════════════════════════════════════ */
.flip-wrap {
  perspective: 900px;
  height: 280px;
}
.flip-wrap:hover .flip-inner { transform: rotateY(180deg); }
.flip-inner {
  position: relative;
  width: 100%; height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.6s ease;
  border-radius: 18px;
}
.flip-face {
  position: absolute; inset: 0;
  border-radius: 18px;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}
.flip-front {
  background: linear-gradient(165deg,rgba(28,23,18,0.97) 0%,rgba(18,15,12,0.98) 100%);
  border: 0.5px solid rgba(255,255,255,0.12);
  box-shadow: 0 8px 32px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.07);
  padding: 28px 24px 20px;
  display: flex; flex-direction: column; gap: 10px;
  position: relative;
}
.flip-front::before {
  content:''; position:absolute; top:0; left:0; right:0; height:3px;
  border-radius:18px 18px 0 0; background:var(--faccent,rgba(255,107,0,0.9));
}
.flip-back {
  transform: rotateY(180deg);
  padding: 26px 24px;
  display: flex; flex-direction: column; justify-content: center; gap: 14px;
  border: 0.5px solid rgba(255,255,255,0.14);
  box-shadow: 0 8px 32px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.08);
}
.fb-title { font-family:var(--font-d); font-size:17px; font-weight:700; color:#fff; }
.fb-desc  { font-size:13px; line-height:1.8; color:rgba(255,255,255,0.82); flex:1; }
.fb-btn   {
  display:inline-flex; align-items:center; gap:6px; padding:8px 18px;
  background:rgba(255,255,255,0.12); border:0.5px solid rgba(255,255,255,0.22);
  border-radius:100px; font-size:12.5px; font-weight:600; color:#fff;
  text-decoration:none; width:fit-content; transition:background .2s;
}
.fb-btn:hover { background:rgba(255,255,255,0.22); }
.flip-hint { font-size:10px; color:rgba(255,255,255,0.2); margin-top:auto; }
"""
c = c.replace('.svc-card:hover .svc-link { color:var(--or); gap:8px; }',
              '.svc-card:hover .svc-link { color:var(--or); gap:8px; }' + flip_css)

# ── Wrap each card ──
back_bgs = [
    'linear-gradient(145deg,rgba(59,130,246,0.28),rgba(4,10,32,0.96))',
    'linear-gradient(145deg,rgba(255,107,0,0.28),rgba(32,12,0,0.96))',
    'linear-gradient(145deg,rgba(45,202,114,0.28),rgba(0,26,12,0.96))',
    'linear-gradient(145deg,rgba(6,182,212,0.28),rgba(0,20,30,0.96))',
    'linear-gradient(145deg,rgba(234,179,8,0.28),rgba(30,22,0,0.96))',
    'linear-gradient(145deg,rgba(168,85,247,0.28),rgba(20,0,38,0.96))',
    'linear-gradient(145deg,rgba(239,68,68,0.28),rgba(38,0,0,0.96))',
    'linear-gradient(145deg,rgba(236,72,153,0.28),rgba(38,0,18,0.96))',
    'linear-gradient(145deg,rgba(45,202,114,0.28),rgba(0,26,12,0.96))',
    'linear-gradient(145deg,rgba(255,107,0,0.28),rgba(32,12,0,0.96))',
]
icon_colors = ['#3B82F6','#FF6B00','#2DCA72','#06B6D4','#EAB308','#A855F7','#EF4444','#EC4899','#2DCA72','#FF6B00']
face_accents= ['rgba(59,130,246,0.9)','rgba(255,107,0,0.9)','rgba(45,202,114,0.9)','rgba(6,182,212,0.9)','rgba(234,179,8,0.9)','rgba(168,85,247,0.9)','rgba(239,68,68,0.9)','rgba(236,72,153,0.9)','rgba(45,202,114,0.9)','rgba(255,107,0,0.9)']

pat = re.compile(
    r'<div class="svc-card (au[^"]*)">\s*'
    r'<div class="svc-bg">.*?</div>\s*'
    r'<div class="svc-icon-wrap">(.*?)</div>\s*'
    r'<div class="svc-name">(.*?)</div>\s*'
    r'<div class="svc-desc">(.*?)</div>\s*'
    r'<div class="svc-link">.*?</div>\s*'
    r'</div>',
    re.DOTALL
)

matches = list(pat.finditer(c))
print(f"Matched {len(matches)} cards")

offset = 0
for i, m in enumerate(matches):
    au    = m.group(1)
    icon  = m.group(2).strip()
    name  = m.group(3).strip()
    desc  = m.group(4).strip()
    bg    = back_bgs[min(i,9)]
    ic    = icon_colors[min(i,9)]
    fa    = face_accents[min(i,9)]

    repl = (
        f'<div class="flip-wrap {au}" style="--faccent:{fa};">\n'
        f'  <div class="flip-inner">\n'
        f'    <div class="flip-face flip-front">\n'
        f'      <div class="svc-icon-wrap" style="stroke:{ic};">{icon}</div>\n'
        f'      <div class="svc-name">{name}</div>\n'
        f'      <div class="flip-hint">&#8635; Hover to learn more</div>\n'
        f'    </div>\n'
        f'    <div class="flip-face flip-back" style="background:{bg};">\n'
        f'      <div class="fb-title">{name}</div>\n'
        f'      <div class="fb-desc">{desc}</div>\n'
        f'      <a href="services.html" class="fb-btn">Learn more &rarr;</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</div>'
    )
    s = m.start() + offset
    e = m.end()   + offset
    c = c[:s] + repl + c[e:]
    offset += len(repl) - (m.end() - m.start())

# Mobile tap JS
tap = """
document.querySelectorAll('.flip-wrap').forEach(function(w){
  w.addEventListener('click',function(){ this.classList.toggle('tapped'); });
});
(function(){
  var s=document.createElement('style');
  s.textContent='.flip-wrap.tapped .flip-inner{transform:rotateY(180deg);}';
  document.head.appendChild(s);
})();
"""
c = c.replace('});\n\nwindow.addEventListener', tap + '\n});\n\nwindow.addEventListener')

out = r'C:/Users/ViditVaibhav/Desktop/frontend 11/services.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(c)
print("Done — services.html rebuilt")

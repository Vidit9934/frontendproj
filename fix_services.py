import re

path = r"C:/Users/ViditVaibhav/Desktop/frontend 11/services.html"
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# ── 1. Add flip-card CSS after .svc-card block ──
flip_css = """
/* ── Flip Card System ─────────────────────────────────────── */
.svc-wrap {
  perspective: 1000px;
  height: 240px;
}
.svc-wrap:hover .svc-card-inner { transform: rotateY(180deg); }
.svc-wrap.flipped .svc-card-inner { transform: rotateY(180deg); }
.svc-card-inner {
  position: relative;
  width: 100%; height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.65s cubic-bezier(0.4, 0.2, 0.2, 1);
  border-radius: 18px;
}
.svc-face {
  position: absolute; inset: 0;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 18px;
  overflow: hidden;
}
.svc-front {
  background: linear-gradient(165deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.03) 50%, rgba(255,255,255,0.01) 100%);
  backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 0.5px solid rgba(255,255,255,0.12);
  box-shadow: 0 20px 60px rgba(0,0,0,0.55), 0 4px 16px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
  padding: 24px 22px 18px;
  display: flex; flex-direction: column; align-items: flex-start; gap: 10px;
}
.svc-front::before {
  content:''; position:absolute; top:0; left:0; right:0; height:3px;
  border-radius:18px 18px 0 0;
  background: var(--accent);
}
.svc-back {
  transform: rotateY(180deg);
  padding: 24px 22px;
  display: flex; flex-direction: column; justify-content: center; gap: 12px;
  border: 0.5px solid rgba(255,255,255,0.14);
  box-shadow: 0 20px 60px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.1);
}
.svc-flip-hint {
  font-size: 10px; color: rgba(255,255,255,0.25); margin-top: auto;
  display: flex; align-items: center; gap: 5px;
}
.svc-back-name {
  font-family: var(--font-d); font-size: 16px; font-weight: 700; color: #fff;
}
.svc-back-desc {
  font-size: 12.5px; line-height: 1.75; color: rgba(255,255,255,0.78); flex: 1;
}
.svc-back-link {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 600; color: #fff;
  background: rgba(255,255,255,0.12); border: 0.5px solid rgba(255,255,255,0.2);
  padding: 7px 16px; border-radius: 100px; width: fit-content;
  transition: background .2s; text-decoration: none;
}
.svc-back-link:hover { background: rgba(255,255,255,0.22); }
"""

# Insert after the existing svc-icon-wrap hover rule
marker = ".svc-card:hover .svc-icon-wrap { background:rgba(255,255,255,.08); transform:scale(1.08); box-shadow: 0 6px 20px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.12); }"
c = c.replace(marker, marker + flip_css)

# ── 2. Back-face background per service ──
back_bgs = [
    'linear-gradient(145deg,rgba(59,130,246,0.22),rgba(10,20,50,0.9))',
    'linear-gradient(145deg,rgba(255,107,0,0.22),rgba(50,20,0,0.9))',
    'linear-gradient(145deg,rgba(45,202,114,0.22),rgba(0,40,20,0.9))',
    'linear-gradient(145deg,rgba(6,182,212,0.22),rgba(0,30,40,0.9))',
    'linear-gradient(145deg,rgba(234,179,8,0.22),rgba(40,30,0,0.9))',
    'linear-gradient(145deg,rgba(168,85,247,0.22),rgba(30,0,50,0.9))',
    'linear-gradient(145deg,rgba(239,68,68,0.22),rgba(50,0,0,0.9))',
    'linear-gradient(145deg,rgba(236,72,153,0.22),rgba(50,0,30,0.9))',
    'linear-gradient(145deg,rgba(45,202,114,0.22),rgba(0,40,20,0.9))',
    'linear-gradient(145deg,rgba(255,107,0,0.22),rgba(50,20,0,0.9))',
]

# ── 3. Find and rebuild each svc-card ──
# Pattern: <div class="svc-card ..."> ... </div>\n      </div>
# We'll do it block by block
grid_start = c.find('<div class="services-grid">')
grid_end   = c.find('</div>', c.find('<!-- 10 -->')) + 6  # after last card closes

grid_html = c[grid_start:grid_end]

# Extract cards using regex
card_pat = re.compile(
    r'(      <!-- \d+ -->\n)'
    r'      (<div class="svc-card[^"]*">)(.*?)(</div>\n\n)',
    re.DOTALL
)

def rebuild(m, idx):
    comment   = m.group(1)
    open_tag  = m.group(2)
    inner     = m.group(3)
    close_end = m.group(4)

    au_cls = re.search(r'class="(svc-card[^"]*)"', open_tag)
    au_str = au_cls.group(1).replace('svc-card','').strip() if au_cls else ''

    bg_m    = re.search(r'<div class="svc-bg">(.*?)</div>', inner, re.DOTALL)
    icon_m  = re.search(r'<div class="svc-icon-wrap">(.*?)</div>', inner, re.DOTALL)
    name_m  = re.search(r'<div class="svc-name">(.*?)</div>', inner)
    desc_m  = re.search(r'<div class="svc-desc">(.*?)</div>', inner, re.DOTALL)

    svc_bg   = bg_m.group(0)   if bg_m   else ''
    svc_icon = icon_m.group(0) if icon_m else ''
    svc_name = name_m.group(1).strip() if name_m else ''
    svc_desc = desc_m.group(1).strip() if desc_m else ''
    bg       = back_bgs[min(idx, len(back_bgs)-1)]

    return (
        comment
        + f'      <div class="svc-wrap {au_str}">\n'
        + f'        <div class="svc-card-inner">\n'
        + f'          <div class="svc-face svc-front">\n'
        + f'            {svc_bg}\n'
        + f'            {svc_icon}\n'
        + f'            <div class="svc-name">{svc_name}</div>\n'
        + f'            <div class="svc-flip-hint">'
          f'<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 4v6h6"/><path d="M23 20v-6h-6"/><path d="M20.49 9A9 9 0 005.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 013.51 15"/></svg>'
          f' Hover / tap for details</div>\n'
        + f'          </div>\n'
        + f'          <div class="svc-face svc-back" style="background:{bg};">\n'
        + f'            <div class="svc-back-name">{svc_name}</div>\n'
        + f'            <div class="svc-back-desc">{svc_desc}</div>\n'
        + f'            <a href="services.html" class="svc-back-link">Learn more &rarr;</a>\n'
        + f'          </div>\n'
        + f'        </div>\n'
        + f'      </div>\n\n'
    )

new_grid_html = grid_html
matches = list(card_pat.finditer(grid_html))
print(f"Cards found: {len(matches)}")

offset = 0
for i, m in enumerate(matches):
    repl = rebuild(m, i)
    s = m.start() + offset
    e = m.end()   + offset
    new_grid_html = new_grid_html[:s] + repl + new_grid_html[e:]
    offset += len(repl) - (m.end() - m.start())

c = c[:grid_start] + new_grid_html + c[grid_end:]

# ── 4. Add mobile tap JS before </script> ──
tap_js = """
// Flip cards: mobile tap support
document.querySelectorAll('.svc-wrap').forEach(function(w){
  w.addEventListener('click', function(){ this.classList.toggle('flipped'); });
});
"""
last_script = c.rfind('</script>')
c = c[:last_script] + tap_js + '\n</script>'

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Done — services.html flip cards applied")

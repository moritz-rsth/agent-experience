"""Three diagrams, one per AX layer, each showing what state B adds.
Run: python3 diagrams/layers.py  (from presentation/) -> assets/layer-find.svg, layer-read.svg, layer-act.svg
Facts: research/2026-11-08-configurator-demo-report.md §1, personal-terminal/scripts/build-agent-layer.mjs."""
import sys
sys.path.insert(0, "/workspace/home/moritz/.claude/plugins/cache/moritz-skills/slides/0.4.1/skills/slides/scripts")
import diagram as D

# Layer colours: keep in sync with --find / --read / --act in deck_src.html
FIND, READ, ACT = "#2563eb", "#b45309", "#e0218a"

def soft(hex_, a=0.10):
    h = hex_.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f"rgba({r},{g},{b},{a})"

def use(color):
    D.ACCENT, D.ACCENT_SOFT = color, soft(color)

OUT = "assets/"

# ---- L1 Find: one build step emits the discovery files from the shop's own source ----
use(FIND)
d = D.Diagram(1400, 560, "Find: one build step generates llms.txt, agents.md, robots.txt pointers, the agent-skills index and openapi.json from the same source as the shop")
src = d.block(40, 220, 300, 120, "Shop source")
d.note(190, 375, "options · prices · links")
build = d.block(450, 220, 300, 120, "Build step", accent=True)
d.note(600, 375, "every deploy", accent=True)
d.arrow_between(src, build)
# the files sit in one frame that carries the slide's headline and what the files are for
frame = d.group(880, 30, 480, 505)
d.text(frame.cx, 86, "Files, generated", size=D.TITLE, weight=600)
outs = ["llms.txt", "agents.md", "robots.txt", "agent-skills/index.json", "openapi.json"]
ys = [150, 222, 294, 366, 438]
for y, name in zip(ys, outs):
    t = d.token(1120, y, name, size=26)
    d.arrow(build.right + 8, build.cy, t.left - 8, y, accent=True)
d.note(frame.cx, 505, "Giving the agent context", accent=True)
d.save(OUT + "layer-find.svg")

# ---- L2 Read: one source, two renderings in the same HTML ----
use(READ)
d = D.Diagram(1400, 560, "Read: the same page source renders the React configurator for humans and, in the same HTML, a static text section with every option and price for agents, plus Markdown twins and a JSON API")
src = d.block(40, 220, 300, 120, "Shop source")
human = d.block(560, 70, 380, 120, "React page")
d.note(750, 225, "humans: run JavaScript")
agent = d.block(560, 330, 380, 120, "Static text", accent=True)
d.note(750, 485, "generated at build · no JavaScript", accent=True)
d.arrow(src.right + 8, src.cy - 20, human.left - 8, human.cy)
d.arrow(src.right + 8, src.cy + 20, agent.left - 8, agent.cy, accent=True)
d.group(520, 30, 460, 480, "one HTML page")
for y, name in [(330, "index.md twins"), (420, "/api/configure")]:
    t = d.token(1190, y, name, size=26, accent=True)
d.note(1190, 480, "generated files", accent=True)
d.arrow(agent.right + 8, agent.cy - 10, 1190 - 120, 330, accent=True)
d.arrow(agent.right + 8, agent.cy + 10, 1190 - 120, 420, accent=True)
d.save(OUT + "layer-read.svg")

# ---- L3 Act: a chain of GET links, ending in the human click ----
use(ACT)
d = D.Diagram(1400, 560, "Act: the agent follows GET links: /api/configure step 1, each option links to the next step, after step 9 a design code and checkout link, /api/configure/order validates many designs, the checkout page, and finally the human clicks zahlungspflichtig bestellen")
w, h, y1, y2 = 380, 120, 70, 330
a = d.block(40, y1, w, h, "Step 1")
d.note(40 + w / 2, y1 + h + 32, "GET /api/configure")
b = d.block(510, y1, w, h, "Steps 2–9")
d.note(510 + w / 2, y1 + h + 32, "each option: next URL")
c = d.block(980, y1, w, h, "Design code")
d.note(980 + w / 2, y1 + h + 32, "+ checkout link")
e = d.block(40, y2, w, h, "Order check")
d.note(40 + w / 2, y2 + h + 32, "/api/configure/order")
f = d.block(510, y2, w, h, "Checkout page")
d.note(510 + w / 2, y2 + h + 32, "all designs + total")
g = d.block(980, y2, w, h, "Human clicks", accent=True)
d.note(980 + w / 2, y2 + h + 32, "„zahlungspflichtig bestellen“", accent=True)
d.arrow_between(a, b); d.arrow_between(b, c)
# wrap from the end of row 1 to the start of row 2
d.line(c.cx, c.bottom + 50, c.cx, 270); d.line(c.cx, 270, e.cx, 270); d.arrow(e.cx, 270, e.cx, e.top - 8)
d.arrow_between(e, f); d.arrow_between(f, g, accent=True)
d.save(OUT + "layer-act.svg")
print("ok")

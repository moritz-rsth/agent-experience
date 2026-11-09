"""Closing diagram: an agent, the tool it should use, and the adapter in between ("improve agent experience").
Run: python3 diagrams/adapter.py  (from presentation/) -> assets/adapter.svg"""
import sys
sys.path.insert(0, "/workspace/home/moritz/.claude/plugins/cache/moritz-skills/slides/0.4.1/skills/slides/scripts")
import diagram as D

ACT = "#e0218a"  # same pink as --act / --accent in deck_src.html
h = ACT.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
D.ACCENT, D.ACCENT_SOFT = ACT, f"rgba({r},{g},{b},0.10)"

d = D.Diagram(1400, 560, "An agent on the left, the tool it should use on the right, and between them an adapter labelled improve agent experience; below the adapter three examples: host an endpoint, document the endpoint on the web, host a local MCP server")
agent = d.block(40, 150, 320, 140, "Agent")
d.note(200, 325, "Claude Code · Muse · your own")
adapter = d.block(500, 150, 400, 140, "improve agent experience", accent=True)
d.note(700, 325, "the adapter", accent=True)
tool = d.block(1040, 150, 320, 140, "Tool")
d.note(1200, 325, "calendar · mail · GPU server")
d.arrow_between(agent, adapter, accent=True)
d.arrow_between(adapter, tool)
for y, text in [(385, "host an endpoint"), (450, "document the endpoint on the web"), (515, "host a local MCP server")]:
    d.token(700, y, text, size=26, accent=True)
d.save("assets/adapter.svg")
print("ok")

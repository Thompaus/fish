"""Wrap src/page.html (the page body, also published as a Claude artifact) into a full index.html for GitHub Pages."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
page = (root / "src" / "page.html").read_text()
split = page.index('<div class="wrap">')
head, body = page[:split], page[split:]
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Per-species fishing forecast from solunar periods, moon phase, live pressure, water temperature and swell.">
<style>:root{{color-scheme:light}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""
(root / "index.html").write_text(html)
print("wrote index.html")

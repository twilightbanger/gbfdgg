#!/usr/bin/env python3
"""Bundle src/game.html + src/data.json into a single self-contained index.html.

`python3 build.py --artifact OUT` also writes OUT without the outer <!doctype>/<head>/<body>
skeleton, which the Artifact host adds itself when the page is published.
"""
import pathlib, sys
root = pathlib.Path(__file__).parent
tpl = (root / 'src/game.html').read_text()
data = (root / 'src/data.json').read_text().strip()
assert tpl.count('__DATA__') == 1
page = tpl.replace('__DATA__', data)
(root / 'index.html').write_text(page)
print('index.html', len(page), 'bytes')
if '--artifact' in sys.argv:
    out = pathlib.Path(sys.argv[sys.argv.index('--artifact') + 1])
    body = page[page.index('<body>') + len('<body>'):]
    body = body[:body.rindex('</body>')]
    out.write_text(body.lstrip('\n'))
    print(out, len(body), 'bytes')

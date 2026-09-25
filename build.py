#!/usr/bin/env python3
"""Bundle src/game.html + src/data.json into a single self-contained index.html."""
import pathlib
root = pathlib.Path(__file__).parent
tpl = (root / 'src/game.html').read_text()
data = (root / 'src/data.json').read_text().strip()
assert tpl.count('__DATA__') == 1
(root / 'index.html').write_text(tpl.replace('__DATA__', data))
print('index.html', len(tpl) + len(data), 'bytes')

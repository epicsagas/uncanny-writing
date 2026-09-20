import re, json, sys

ws = '/tmp/uncanny-writing/_workspace/2026-09-21-001'
html = open('/tmp/uncanny-writing/index.html').read()
final = open(f'{ws}/final.md').read()

# parse final.md blocks: ## KO-NNN -> text
blocks = {}
cur = None
buf = []
for line in final.split('\n'):
    m = re.match(r'^##\s+KO-(\d+)', line.strip())
    if m:
        if cur: blocks[cur] = ''.join(b.strip() for b in buf)
        cur = int(m.group(1)); buf = []
    elif cur:
        buf.append(line)
if cur: blocks[cur] = ''.join(b.strip() for b in buf)

orig = json.load(open(f'{ws}/spans_original.json'))
missing = [i for i in range(1, len(orig)+1) if i not in blocks or not blocks[i]]
if missing:
    print('MISSING BLOCKS:', missing); sys.exit(1)

it = iter(range(1, len(orig)+1))
def sub(m):
    i = next(it)
    t = blocks[i]
    for pfx in ('교정.', '방법.'):
        if t.startswith(pfx):
            t = f'<b>{pfx}</b>' + t[len(pfx):]
            break
    return f'<span class="ko">{t}</span>'

out = re.sub(r'<span class="ko">(.*?)</span>', sub, html, flags=re.S)
assert out.count('<span class="ko">') == len(orig)
open('/tmp/uncanny-writing/index.html','w').write(out)
print(f'reinserted {len(orig)} spans')

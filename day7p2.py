from collections import defaultdict
from itertools import accumulate
dirs = defaultdict(int)
cur = ['']
for line in open("input.txt"):
    match line.split():
        case '$', 'cd', 'l': cur = ['']
        case '$', 'cd', '..': cur.pop()
        case '$', 'cd', x: cur.append(x)
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for p in accumulate(cur):
                print(p)
                dirs[p] += int(size)


a = dirs[''] - 40_000_000
print(sum(s for s in dirs.values() if s <= 100000), min(s for s in dirs.values() if s >= a))


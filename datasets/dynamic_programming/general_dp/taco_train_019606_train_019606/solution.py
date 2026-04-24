from collections import namedtuple
import sys
XY = namedtuple('XY', 'x y')
n = int(input())
pg = [XY(*[int(w) for w in input().split()]) for _ in range(n)]
minx = min((p.x for p in pg))
miny = min((p.y for p in pg))
maxx = max((p.x for p in pg))
maxy = max((p.y for p in pg))
p4 = 2 * (maxx - minx + (maxy - miny))
p3 = p4 - 2 * min([min(p.x - minx, maxx - p.x) + min(p.y - miny, maxy - p.y) for p in pg])
print(p3, *[p4] * (n - 3))

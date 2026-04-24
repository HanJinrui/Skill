from heapq import *
import sys
F = 9 ** 99
p = lambda : map(int, sys.stdin.readline().split())
a = abs
(N, M) = p()
(A, B, C, D) = p()
e = []
g = [set() for _ in range(M + 2)]
for i in range(M):
	(x, y) = p()
	g[0].add((i + 2, min(a(x - A), a(y - B))))
	g[i + 2].add((1, a(x - C) + a(y - D)))
	e.append((i + 2, x, y))
for k in [1, 2]:
	e.sort(key=lambda x: x[k])
	for ((b, G, H), (i, x, y)) in zip(e, e[1:]):
		c = x - G if k < 2 else y - H
		g[i].add((b, c))
		g[b].add((i, c))
d = [F] * (M + 2)
q = [(0, 0)]
d[0] = 0
while q:
	(c, v) = heappop(q)
	if d[v] < c:
		continue
	for (t, e) in g[v]:
		if d[v] + e < d[t]:
			d[t] = d[v] + e
			heappush(q, (d[t], t))
print(min(d[1], a(D - B) + a(C - A)))

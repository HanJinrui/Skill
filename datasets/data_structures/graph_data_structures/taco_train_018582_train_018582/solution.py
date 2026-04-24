import sys
import numpy as np

def solve(n, ee):
	g = np.ones((n, n), dtype=np.int64)
	for i in range(n):
		g[i, i] = 0
	for (a, b) in ee:
		g[a, b] = 0
		g[b, a] = 0
	ret = np.zeros(n, dtype=np.int64)
	v = set(range(n))
	q = []
	while v:
		x = next(iter(v))
		v.remove(x)
		q = [x]
		ret[x] = 1
		while q:
			x = q[0]
			q = q[1:]
			cc = ret[x]
			for y in np.where(g[x, :] == 1)[0]:
				if ret[y] == cc:
					return 'NO'
				elif ret[y] == 0:
					ret[y] = 3 - cc
					q += [y]
					v.remove(y)
	return 'YES'
f = sys.stdin
t = int(f.readline())
for j in range(t):
	(n, m) = map(int, f.readline().split())
	ee = []
	for i in range(m):
		(x, y) = map(int, f.readline().split())
		ee += [(x - 1, y - 1)]
	print(solve(n, ee))

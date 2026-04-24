R = lambda : map(int, input().split())
(t,) = R()
for _ in range(t):
	(n,) = R()
	(k,) = R()
	g = [[] for _ in range(n)]
	for _ in range(k):
		(u, v) = R()
		u -= 1
		v -= 1
		g[u].append(v)
		g[v].append(u)
	r = [None] * n
	h = []
	for (l, u) in sorted(((len(x), i) for (i, x) in enumerate(g))):
		if r[u] is None:
			h.append(u + 1)
			r[u] = len(h)
			for v in g[u]:
				r[v] = r[u]
				if len(g[v]) > l:
					h[-1] = v + 1
	print(len(h))
	print(*r)
	print(*h)

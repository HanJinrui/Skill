def solve():
	(n, m) = map(int, input().split())
	g = [[] for i in range(n + 1)]
	for i in range(m):
		(u, v, c) = input().split()
		(u, v) = map(int, (u, v))
		if c == 'crewmate':
			g[u].append((v, 0))
			g[v].append((u, 0))
		else:
			g[u].append((v, 1))
			g[v].append((u, 1))
	val = [None] * (n + 1)
	r = 0
	for i in range(1, n + 1):
		if val[i] is None:
			q = [i]
			val[i] = 0
			i = 0
			c = [1, 0]
			while i < len(q):
				u = q[i]
				i += 1
				for (v, w) in g[u]:
					if val[v] is None:
						val[v] = val[u] ^ w
						c[val[v]] += 1
						q.append(v)
					elif val[v] != val[u] ^ w:
						print(-1)
						return
			r += max(c)
	print(r)
for _ in range(int(input())):
	solve()

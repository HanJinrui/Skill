t = int(input())
for i in range(t):
	(n, m, k) = map(int, input().split())
	a = list(map(int, input().split()))
	b = []
	for j in range(n):
		e = list(map(int, input().split()))
		b.append(e)
	c = []
	for z in range(n):
		e = list(map(int, input().split()))
		c.append(e)
	p = [0] * n
	g = [0] * n
	s = 0
	for v in range(n):
		p[v] = b[v][a[v] - 1]
		s += p[v]
		x = 0
		for u in range(m):
			e = b[v][u] - c[v][u] - p[v]
			x = max(x, e)
		g[v] = x
	g.sort()
	g.reverse()
	print(s + sum(g[:k]))

(n, m) = map(int, input().split())
g = set()
v = set()
for k in range(m):
	(a, b) = map(int, input().split())
	g.add(a)
	v.add(b)
	print((n - len(g)) * (n - len(v)), end=' ')

f = lambda : list(map(int, input().split()))

def g(t):
	n = t[0]
	for i in range(1, n):
		t[i + 1] += t[i]
	p = [t[n]] * (n + 1)
	p[n] = t[0] = 0
	for d in range(1, n):
		p[d] -= min((t[j + d] - t[j] for j in range(n - d + 1)))
	return p[::-1]
(n, m) = f()
u = g(f())
for i in range(n - 1):
	v = g(f())
	p = [0] * (min(m, len(u) + len(v)) + 1)
	for (i, x) in enumerate(u):
		for (j, y) in enumerate(v, i):
			if j > m:
				break
			p[j] = max(p[j], x + y)
	u = p
print(u[m])

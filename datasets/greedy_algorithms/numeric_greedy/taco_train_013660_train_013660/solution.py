R = lambda : map(int, input().split())
G = range
(t,) = R()

def f(n, m):
	b = [v // n for v in a if v >= 2 * n]
	return not (m & 1 and all((v == 2 for v in b))) and sum(b) >= m
for _ in G(t):
	(n, m, k) = R()
	a = [*R()]
	print(['No', 'Yes'][f(n, m) or f(m, n)])

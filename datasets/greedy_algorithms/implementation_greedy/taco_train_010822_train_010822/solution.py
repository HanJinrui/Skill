f = lambda : map(int, input().split())
(n, m) = f()
(a, b) = (1, n)
for i in range(m):
	(u, v) = sorted(f())
	a = max(a, u)
	b = min(b, v)
print(max(0, b - a))

(n, m) = map(int, input().split())
(p, r) = (sum((abs(i + 1 - (n + 1) // 2) for i in range(n))), 0)
for i in range(m):
	(x, d) = map(int, input().split())
	r += n * x + max(d * (n * (n - 1) // 2), d * p)
print(r / n)

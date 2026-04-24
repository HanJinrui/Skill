(n, m, k) = map(int, input().split())
if m > n:
	(n, m) = (m, n)
res = -1
if k < n:
	res = m * (n // (k + 1))
	if k < m:
		res = max(res, n * (m // (k + 1)))
elif k <= n - 1 + m - 1:
	res = m // (k + 1 - n + 1)
print(res)

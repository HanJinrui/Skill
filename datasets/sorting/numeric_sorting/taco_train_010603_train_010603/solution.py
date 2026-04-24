def f():
	if x <= m:
		return x * (x + 1) // 2
	t = x + m
	return t // 2 * (t - t // 2) - m * (m - 1) // 2
(n, m) = map(int, input().split())
(lo, hi) = (0, n)
while lo + 1 < hi:
	x = (lo + hi) // 2
	if f() < n:
		lo = x
	else:
		hi = x
print(hi)

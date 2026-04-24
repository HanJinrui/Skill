p = lambda : map(int, input().split())
(n, q, k) = p()
a = (0, *p())
for _ in [0] * q:
	(l, r) = p()
	print(a[r] - a[l] + (l - r) * 2 + k - 1)

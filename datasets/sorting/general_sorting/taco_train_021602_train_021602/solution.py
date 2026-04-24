R = lambda : map(int, input().split())
(n, S) = R()
a = list(R())
(l, r, s) = (0, n, 0)
while l < r:
	m = (l + r + 1) // 2
	t = sum(sorted((x + (i + 1) * m for (i, x) in enumerate(a)))[:m])
	if t <= S:
		l = m
		s = t
	else:
		r = m - 1
print(l, s)

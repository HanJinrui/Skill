R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n, c, q) = R()
	s = input()
	a = []
	while c:
		c -= 1
		(l, r) = R()
		a = [(n, n - l + 1)] + a
		n += r - l + 1
	while q:
		q -= 1
		(k,) = R()
		for (x, y) in a:
			k -= y * (k > x)
		print(s[k - 1])

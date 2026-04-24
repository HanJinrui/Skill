R = lambda : map(int, input().split())
(t,) = R()
while t:
	(n, x, m) = R()
	y = x
	t -= 1
	while m:
		(l, r) = R()
		m -= 1
		if y >= l and r >= x:
			x = min(x, l)
			y = max(y, r)
	print(y - x + 1)

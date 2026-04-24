R = lambda : [*map(int, input().split())]
for _ in [0] * R()[0]:
	(n, m) = R()
	a = (0, *R())
	b = [R() for _ in [0] * m]
	c = [0] + [0] * n
	for (x, y) in b:
		c[x] += 1
		c[y] += 1
	print(m % 2 and min([x for (x, y) in zip(a, c) if y % 2] + [a[x] + a[y] for (x, y) in b if c[x] | c[y] & 1 ^ 1]))

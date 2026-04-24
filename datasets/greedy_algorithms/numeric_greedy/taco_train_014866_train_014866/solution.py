for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(sum((1 & ~(x ^ y) for (x, y) in zip(a, a[1:]))))

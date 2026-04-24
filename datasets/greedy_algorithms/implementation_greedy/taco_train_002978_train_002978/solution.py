for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(sum(a) - 2 * min(map(sum, zip(a, a[1:]))))

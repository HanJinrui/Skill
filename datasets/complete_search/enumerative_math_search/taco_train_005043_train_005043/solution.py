for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(sum((i + j + 2 == x * a[j] for (i, x) in enumerate(a) for j in range(-(i + 2) % x, i, x))))

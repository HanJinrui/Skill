for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(sum((len(bin(-1 - y // -x)) - 3 for (x, y) in map(sorted, zip(a, a[1:])))))

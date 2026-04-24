for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	b = sorted(a)
	print('YNEOS'[any((y % b[0] for (x, y) in zip(a, b) if x ^ y))::2])

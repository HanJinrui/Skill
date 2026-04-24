for r in [*open(0)][2::2]:
	a = (*map(int, r.split()),)
	r = '0' + ''.join((str((x > y) - (x < y) + 1) for (x, y) in zip(a, a[1:])))
	print(max(0, r.rfind('2', 0, r.rfind('0'))))

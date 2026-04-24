for s in [*open(0)][1:]:
	a = (*map(int, s.split()),)
	print('YNEOS'[max(a[:2]) + max(a[2:]) != sum(sorted(a)[2:])::2])

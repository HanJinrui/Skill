for s in [*open(0)][1:]:
	a = (*map(int, s.split()),)
	s = sum(a)
	print('YNEOS'[0 < s % 9 or s > 9 * min(a)::2])

for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(len(a) - a.count(min(a)))

for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(sum(a) % 2 * min((len(x) - len(x.rstrip(x[-1])) for x in map(bin, a))))

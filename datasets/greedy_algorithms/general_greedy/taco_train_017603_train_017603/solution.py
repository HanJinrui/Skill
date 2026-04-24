for e in [*open(0)][2::2]:
	f = (*map(int, e.split()),)
	print('NYOE S'[sum(f) / len(f) in f::2])

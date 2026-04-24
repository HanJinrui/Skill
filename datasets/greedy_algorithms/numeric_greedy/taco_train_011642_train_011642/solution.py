for S in [*open(0)][2::2]:
	r = (*map(int, S.split()),)
	print(max(max(r) - r[0], r[-1] - min(r), *(b - a for (a, b) in zip(r, r[-1:] + r))))

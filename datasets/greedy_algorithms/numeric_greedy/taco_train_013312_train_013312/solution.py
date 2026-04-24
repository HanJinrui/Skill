for S in [*open(0)][2::2]:
	N = (*map(int, S.split()),)
	m = 2 * min(N) - 1
	print(-sum((-x // m + 1 for x in N)))

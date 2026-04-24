lst = []
for s in [*open(0)][2::2]:
	a = (*map(int, s.split()),)
	print(any(a) + max(0, 2 * max(a) - sum(a) - 1))

for s in [*open(0)][1:]:
	(l, r) = map(int, s.split())
	print(*([l, 2 * l], [-1] * 2)[r < 2 * l])

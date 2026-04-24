for s in [*open(0)][1:]:
	(x, y, *_, m) = map(int, s.split())
	print(x, y, m - x - y)

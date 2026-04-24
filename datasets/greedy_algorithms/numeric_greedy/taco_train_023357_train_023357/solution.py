for s in [*open(0)][1:]:
	(n, m) = map(int, s.split())
	print(m * min(n - 1, 2))

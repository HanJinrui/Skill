for s in [*open(0)][1:]:
	(a, b) = map(int, s.split())
	print((2 * b + a) * (a > 0) + 1)

for s in [*open(0)][1::1]:
	(a, b, c, d) = map(int, s.split())
	print([max(a, c), a + c][a > d or c > b])

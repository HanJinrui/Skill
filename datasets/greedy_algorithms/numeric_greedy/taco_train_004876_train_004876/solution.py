for s in [*open(0)][1:]:
	(a, b, c, d) = map(int, s.split())
	print(+(a < 1) or a + 2 * min(b, c) + min(a + 1, abs(b - c) + d))

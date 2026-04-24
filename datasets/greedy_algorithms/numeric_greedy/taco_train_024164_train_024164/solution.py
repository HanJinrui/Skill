for s in [*open(0)][1:]:
	(a, b, c, d) = map(int, s.split())
	print(max(a + b, c + d))

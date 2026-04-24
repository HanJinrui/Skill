for s in [*open(0)][1:]:
	(a, b) = map(int, s.split())
	print(min(a, b, (a + b) // 4))

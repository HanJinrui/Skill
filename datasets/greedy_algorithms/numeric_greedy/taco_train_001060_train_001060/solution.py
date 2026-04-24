for s in [*open(0)][1:]:
	(a, b) = map(int, s.split())
	print(b % max(a, b // 2 + 1))

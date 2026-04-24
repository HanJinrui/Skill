for s in [*open(0)][1:]:
	(a, b) = map(int, s.split())
	print((d := abs(a - b)), d and min(a % d, -a % d))

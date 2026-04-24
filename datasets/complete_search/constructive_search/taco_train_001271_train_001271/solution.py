for s in [*open(0)][1:]:
	(n, a, b) = map(int, s.split())
	print('YNeos'[a & b < n < a + b + 2::2])

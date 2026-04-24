for s in [*open(0)][1:]:
	(a, b, n, m) = map(int, s.split())
	print('YNeos'[a + b < n + m or min(a, b) < m::2])

for s in [*open(0)][1:]:
	(n, m) = sorted(map(int, s.split()))
	print(2 * n + m - 3 + (m > 1))

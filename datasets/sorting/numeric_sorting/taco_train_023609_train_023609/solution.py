for s in [*open(0)][1:]:
	(n, k) = map(int, s.split())
	print((k - 1) // (n - 1) + k)

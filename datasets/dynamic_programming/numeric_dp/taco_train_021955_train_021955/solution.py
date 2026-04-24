for g in [*open(0)][1:]:
	(m, n, k) = map(int, g.split())
	print('YNEOS'[k != m * n - 1::2])

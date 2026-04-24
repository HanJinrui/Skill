for s in [*open(0)][1:]:
	(x, n, m) = map(int, s.split())
	print('YNEOS'[x - 20 >> n * (x > 20) > 10 * m - 20::2])

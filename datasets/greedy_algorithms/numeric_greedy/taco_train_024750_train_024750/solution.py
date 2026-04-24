for f in [*open(0)][1:]:
	(p, q, r, x, y) = map(int, f.split())
	print('YNEOS'[r < max(0, x - p) + max(0, y - q)::2])

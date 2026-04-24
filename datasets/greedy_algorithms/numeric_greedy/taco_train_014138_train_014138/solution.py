for s in [*open(0)][1:]:
	(w, h, n) = map(int, s.split())
	print('YNEOS'[w * h & -w * h < n::2])

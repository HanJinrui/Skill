for s in [*open(0)][1:]:
	(l, r, k) = map(int, s.split())
	print('YNEOS'[r < 2 or (r > l and (r + 1) // 2 - l // 2 > k)::2])

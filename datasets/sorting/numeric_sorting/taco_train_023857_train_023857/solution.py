for s in [*open(0)][2::2]:
	a = sorted(map(int, s.split()))
	s = sum(a)
	print(*(s and ['YES'] + a[::1 - 2 * (s > 0)] or ['NO']))

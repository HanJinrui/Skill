for s in [*open(0)][2::2]:
	(b, *a) = map(int, s.split())
	print('YNEOS'[max((x % b for x in a)) > 0::2])

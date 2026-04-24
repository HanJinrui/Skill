for s in [*open(0)][2::2]:
	a = s.split()
	n = len(a)
	s = {*range(n)}
	print('YNEOS'[s > {(k + int(a[k])) % n for k in s}::2])

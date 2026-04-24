for s in [*open(0)][2::2]:
	i = t = q = f = 0
	for x in s.split():
		t += int(x)
		q += i
		f |= t < q
		i += 1
	print('YNEOS'[f::2])

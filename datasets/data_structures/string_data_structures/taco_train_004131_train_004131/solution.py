for s in [*open(0)][2::2]:
	d = {}
	i = a = 0
	for n in map(int, s.split()):
		g = d.get(n - i, 0)
		a += g
		d[n - i] = g + 1
		i += 1
	print(a)

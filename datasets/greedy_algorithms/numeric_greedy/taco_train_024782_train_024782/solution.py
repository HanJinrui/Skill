for s in [*open(0)][2::2]:
	a = [0] * 101
	for x in s.split():
		a[int(x)] += 1
	i = a.index(0)
	a[i] = 1
	print(i + a.index(1))

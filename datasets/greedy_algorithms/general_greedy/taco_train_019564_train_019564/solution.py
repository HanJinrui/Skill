for s in [*open(0)][2::2]:
	l = [*map(int, s.split())]
	print(max((x * y for (x, y) in zip(l, l[1:]))))

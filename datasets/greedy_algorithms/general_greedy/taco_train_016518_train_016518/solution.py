for s in [*open(0)][2::2]:
	a = s.split()
	m = len({*a})
	print(*(max(m, i + 1) for i in range(len(a))))

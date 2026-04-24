for a in [*open(0)][2::2]:
	(s, c) = (0, [0] * 50)
	for x in map(int, a.split()):
		l = len(bin(x)[2:])
		s += c[l]
		c[l] += 1
	print(s)

for s in [*open(0)][2::2]:
	a = []
	c = h = 0
	for x in map(int, s.split()):
		h |= 0 < x <= c
		c += x
		a += (c,)
	print(*(a, [-1])[h])

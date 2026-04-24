for s in [*open(0)][2::2]:
	r = p = 0
	for x in map(int, s.split()):
		r += max(0, p - x)
		p = x
	print(r)

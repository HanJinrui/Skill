for s in [*open(0)][2::2]:
	r = ''
	p = 0
	for x in map(int, s[:-1]):
		p = x + (x + 1 != p)
		r += str(p - x)
	print(r)

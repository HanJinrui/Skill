for s in [*open(0)][2::2]:
	r = -1
	m = 0
	for x in map(int, s.split()[::-1]):
		if x > m:
			r += 1
			m = x
	print(r)

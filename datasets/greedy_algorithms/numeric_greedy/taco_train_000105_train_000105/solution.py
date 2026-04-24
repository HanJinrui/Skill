for n in [*open(0)][1:]:
	r = ''
	f = 0
	for x in map(int, n[:-1]):
		y = x + f >> 1
		r += f'{y}{x - y}'
		f ^= x & 1
	print(int(r[::2]), int(r[1::2]))

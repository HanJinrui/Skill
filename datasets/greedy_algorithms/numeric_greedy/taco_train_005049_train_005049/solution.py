for s in [*open(0)][2::2]:
	r = d = x = 0
	for y in map(int, s.split() + [0]):
		r -= min(max(0, x - y), max(0, d)) - abs((d := (y - x)))
		x = y
	print(r)

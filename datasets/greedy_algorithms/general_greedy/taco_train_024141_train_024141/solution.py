for t in [*open(0)][2::2]:
	c = 0
	for x in t[:-1]:
		c = max(0, c + 2 * (x > 'A') - 1)
	print('YNeos'[c > 0::2])

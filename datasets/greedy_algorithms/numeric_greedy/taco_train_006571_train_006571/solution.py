for k in [*open(0)][2::2]:
	c = k.count('*')
	a = r = 0
	for x in k:
		if '*' < x:
			a += min(r, c - r)
		else:
			r += 1
	print(a)

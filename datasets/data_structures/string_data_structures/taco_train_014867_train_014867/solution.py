def find(a, b, q):
	c = []
	for i in q:
		d = 0
		A = a[i]
		for j in b:
			if j <= A:
				d += 1
		c.append(d)
	return c

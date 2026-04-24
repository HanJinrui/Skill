for s in [*open(0)][2::2]:
	(*a,) = map(int, s.split())
	r = 1
	p = 3000000000.0
	while a and p:
		q = a.pop()
		while q >= p:
			r += 1
			q >>= 1
		p = q
	print(r * (a == []) - 1)

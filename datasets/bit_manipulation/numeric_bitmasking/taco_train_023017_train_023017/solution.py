for s in [*open(0)][1:]:
	(n, k) = map(int, s.split())
	r = 0
	for x in f'{k:b}':
		r = r * n + int(x)
	print(r % (10 ** 9 + 7))

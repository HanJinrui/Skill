for s in [*open(0)][1:]:
	(a, b) = sorted(map(int, s.split()))
	s = a + b + 1
	r = [2 * i + b + j - s // 2 for i in range(a + 1) for j in range(2 - s % 2)]
	print(len(r), *r)

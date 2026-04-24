for s in [*open(0)][2::2]:
	n = len((a := s.split()))
	print((n, n // 2 + 1)[len({*a}) == 2])

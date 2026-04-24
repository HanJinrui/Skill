for s in [*open(0)][2::2]:
	n = len((a := s.split()))
	r = sum(map(int, a)) % n
	print(r * (n - r))

for s in [*open(0)][2::2]:
	print(sum(map(int, (a := s.lstrip('0 ').split()[:-1]))) + a.count('0'))

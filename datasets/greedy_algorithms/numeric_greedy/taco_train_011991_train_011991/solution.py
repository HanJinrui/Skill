for s in [*open(0)][2::2]:
	print(+(sum(map(int, (a := s.split()))) % len(a) > 0))

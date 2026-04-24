for s in [*open(0)][2::2]:
	print(len((a := s.split())))
	i = 0
	for x in map(int, a):
		i += 1
		print(i, 2 ** len(f'{x:b}') - x)

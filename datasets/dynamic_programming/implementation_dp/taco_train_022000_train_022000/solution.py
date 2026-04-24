I = input
for _ in [0] * int(I()):
	I()
	s = {0}
	i = 0
	for x in zip(I(), I()):
		if x[0] == x[1]:
			i ^= 1
		else:
			s |= {x[i]}
	print('YNEOS'[len(s) > 2::2])

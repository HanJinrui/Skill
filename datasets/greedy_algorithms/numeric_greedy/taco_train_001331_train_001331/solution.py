I = input
for _ in [0] * int(I()):
	I()
	a = b = 0
	f = 1
	for (x, y) in zip(I(), I()):
		a += 2 * int(x) - 1
		b += 2 * int(y) - 1
		f &= a in (b, -b)
	print('NYOE S'[f & (a == b)::2])

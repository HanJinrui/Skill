I = input
for _ in [0] * int(I()):
	s = ' '.join((I() for _ in [0] * int(I().split()[0])))
	a = (*map(abs, map(int, s.split())),)
	print(sum(a) - s.count('-') % 2 * 2 * min(a))

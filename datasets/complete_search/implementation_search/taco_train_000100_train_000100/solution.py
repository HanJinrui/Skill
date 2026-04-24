I = input
for _ in [0] * int(I()):
	n = int(I())
	a = [x for x in zip(*(I() for _ in [0] * n)) if 2 * x.count('1') >= n]
	print('YNEOS'[all(((*'00',) in [*zip(x, y)] for (i, x) in enumerate(a) for y in a[:i]))::2])

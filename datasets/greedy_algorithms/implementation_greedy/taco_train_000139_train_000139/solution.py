I = input
for _ in [0] * int(I()):
	a = (b, c) = ([0, 0], [0, 0])
	for _ in [0] * int(I()):
		for (l, y) in zip(a, map(int, I().split())):
			l[y < 0] = max(l[y < 0], abs(y))
	print(2 * sum(b + c))

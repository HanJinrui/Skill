I = input
for _ in [0] * int(I()):
	I()
	(a, b, c) = ({*I().split()} for _ in [0] * 3)
	print(*(3 * len(x - y - z) + len(x & y - z) + len(x & z - y) for (x, y, z) in ((a, b, c), (b, a, c), (c, a, b))))

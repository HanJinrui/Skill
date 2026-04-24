for _ in [0] * int(input()):
	d = int(input())
	D = d * (d - 4)
	if D < 0:
		print('N')
	else:
		x = (d - D ** 0.5) / 2
		print('Y', x, d - x)

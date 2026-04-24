for i in [*open(0)][1:]:
	i = int(i)
	print((i + 1) * (4 * i * i - i) * 337 % (10 ** 9 + 7))

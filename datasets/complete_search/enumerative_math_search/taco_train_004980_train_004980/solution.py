for n in [*open(0)][1::2]:
	k = 10 - int(n)
	print(k * (k - 1) * 3)

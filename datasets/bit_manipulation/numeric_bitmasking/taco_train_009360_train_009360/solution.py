for s in [*open(0)][1:]:
	print(pow(*map(int, s.split()), 10 ** 9 + 7))

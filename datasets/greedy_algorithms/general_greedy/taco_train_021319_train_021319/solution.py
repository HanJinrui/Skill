for s in [*open(0)][2::2]:
	print(max((int(x) - i - 1 for (i, x) in enumerate(s.split()))))

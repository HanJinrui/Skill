for s in [*open(0)][1:]:
	n = int(s)
	print(min(n - 1, 2 + n % 2))

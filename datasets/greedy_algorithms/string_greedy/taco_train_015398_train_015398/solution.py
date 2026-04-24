for s in [*open(0)][2::2]:
	n = len(s) - 1
	print(n - 2 * len(s[n // 2:-1].lstrip(s[n // 2])))

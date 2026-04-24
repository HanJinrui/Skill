for s in [*open(0)][1:]:
	n = int(s)
	f = 0
	while n & 1 ^ 1:
		n >>= 1
		f = 1
	print('YNEOS'[f * int(n ** 0.5) ** 2 < n::2])

for s in [*open(0)][1:]:
	(n, k) = map(int, s.split())
	z = (k - 1).bit_length()
	print(z - (2 ** z - n) // k)

for s in [*open(0)][1:]:
	n = int(s)
	print((c := (n // 3 + n % 3 % 2)), (n - c) // 2)

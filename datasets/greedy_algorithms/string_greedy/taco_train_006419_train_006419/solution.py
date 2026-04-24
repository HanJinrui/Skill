for X in [*map(int, open(0))][2::2]:
	F = ''
	while X:
		A = X % 10
		X //= 10
		if A < 1:
			A = X % 100
			X //= 100
		F = chr(96 + A) + F
	print(F)

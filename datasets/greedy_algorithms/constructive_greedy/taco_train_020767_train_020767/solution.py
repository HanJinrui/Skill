for _ in [0] * int(input()):
	(u, v, *x) = map(input().count, 'LRUD')
	a = min(u, v)
	b = min(x)
	if b < 1:
		a = a and 1
	elif a < 1:
		b = 1
	print(2 * (a + b), 'L' * a + 'U' * b + 'R' * a + 'D' * b)

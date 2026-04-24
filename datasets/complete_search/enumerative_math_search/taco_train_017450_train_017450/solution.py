for s in [*open(0)][1:]:
	(n, x, y) = map(int, s.split())
	d = y - x
	i = 1
	while d % i or d // i >= n:
		i += 1
	x = max(x % i or i, y - n * i + i)
	print(*range(x, x + n * i, i))

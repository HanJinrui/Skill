for n in [*map(int, open(0))][1:]:
	(*r,) = range(1, n + 1)
	r[n % 2:n - 2] = r[n % 2:n - 2][::-1]
	print(*r)

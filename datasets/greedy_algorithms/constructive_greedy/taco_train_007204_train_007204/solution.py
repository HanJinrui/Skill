for s in [*open(0)][2::2]:
	a = (x, *_, y) = [*map(int, s.split())]
	print((sorted(a) < a) + ((x, y) == ((n := len(a)), 1)) + (x > 1 <= n - y))

for s in [*open(0)][1:]:
	(n, a, b) = map(int, s.split())
	(*r,) = range(n, 0, -1)
	if a <= n // 2 < b:
		(r[-a], r[-b]) = (r[-b], r[-a])
	elif (n // 2 == a - 1 == b) < 1:
		r = (-1,)
	print(*r)

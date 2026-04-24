for n in [*open(0)][1:]:
	(n, r, b) = map(int, n.split())
	b += 1
	c = r // b * 'R' + 'B'
	print((('R' + c) * (r % b) + c * n)[:n])

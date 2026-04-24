for r in [*open(0)][2::2]:
	j = [int(x) % 2 for x in r.split()]
	print((sum((i % 2 ^ x for (i, x) in enumerate(j))) // 2, -1)[sum(j) != len(j) // 2])

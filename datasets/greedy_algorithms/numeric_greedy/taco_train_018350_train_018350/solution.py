for s in [*open(0)][1:]:
	(i, j, k) = map(int, s.split())
	print(2 * (i < k) - 1, (-1, j)[i * j > k])

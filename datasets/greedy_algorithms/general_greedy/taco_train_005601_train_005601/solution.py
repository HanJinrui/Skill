for s in [*open(0)][1:]:
	(k, m) = map(s.count, '01')
	print(min(k, m) - (k == m))

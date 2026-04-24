for s in [*open(0)][1:]:
	print(sum((min(2, s.count(x)) for x in {*s})) - 1 >> 1)

for s in [*open(0)][2::2]:
	print(sum((x != y for (x, y) in zip(s[:-1], sorted(s[:-1])))))

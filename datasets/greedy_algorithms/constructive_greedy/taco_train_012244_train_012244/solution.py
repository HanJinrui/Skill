for p in [*open(0)][2::2]:
	print(len(p) // 2 - p.count(p[0] + '01'[p[0] < '1']))

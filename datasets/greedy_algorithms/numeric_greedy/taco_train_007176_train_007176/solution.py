for l in [*map(int, open(0))][1:]:
	print((l < 2) - -l // 3)

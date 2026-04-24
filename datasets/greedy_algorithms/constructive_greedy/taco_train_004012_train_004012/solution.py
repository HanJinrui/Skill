for a in [*open(0)][2::2]:
	print(abs(sum(map(int, a.split()))))

for x in [*open(0)][2::2]:
	b = [0]
	for y in list(map(int, x.split())):
		b += [b[-1] + y]
	print(max(b) - min(b))

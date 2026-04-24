for s in [*open(0)][2::2]:
	c = [0] * 3
	for x in s.split():
		c[int(x) % 3] += 1
	print(max((c[i] - c[i - 1] for i in range(3))))

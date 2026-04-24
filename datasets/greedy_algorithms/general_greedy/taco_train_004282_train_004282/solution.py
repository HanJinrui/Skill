for s in [*open(0)][2::2]:
	a = [*map(int, s.split())]
	c = ans = 0
	for x in a[::-1]:
		if x > c:
			c = x
			ans += 1
	print(ans - 1)

for s1 in [*map(int, open(0))][1:]:
	rep = ''
	i = 9
	while s1:
		if i <= s1:
			s1 -= i
			rep = str(i) + rep
		i -= 1
	print(rep)

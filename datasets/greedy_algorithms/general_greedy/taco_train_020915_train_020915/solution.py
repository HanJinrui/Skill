for s in [*open(0)][2::2]:
	s = s[:-1] + '0'
	l = [*map(len, s.split('0'))]
	print(max(l[1:]) + l[0])

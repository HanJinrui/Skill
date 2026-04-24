for s in [*open(0)][2::2]:
	while '()' in s:
		s = s.replace('()', '')
	print(len(s) // 2)

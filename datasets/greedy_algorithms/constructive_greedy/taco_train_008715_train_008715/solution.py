for s in [*open(0)][1:]:
	print('NYOE S'[len(s) & (s[0] != ')' and '(' < s[-2])::2])

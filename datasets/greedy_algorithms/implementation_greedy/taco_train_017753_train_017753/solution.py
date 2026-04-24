for s in [*open(0)][2::2]:
	n = len(s)
	s += ')'
	i = c = 0
	while i < n:
		c += 1
		j = i
		if ')' > s[i]:
			i += 2
		else:
			i = s.find(')', i + 1) + 1
	print(c - 1, n - j - 1)

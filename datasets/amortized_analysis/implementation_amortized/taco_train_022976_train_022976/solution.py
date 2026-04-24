for s in [*open(0)][2::2]:
	i = 0
	j = len(s) - 2
	while (i < j) & (s[i] != s[j]):
		i += 1
		j -= 1
	print(j - i + 1)

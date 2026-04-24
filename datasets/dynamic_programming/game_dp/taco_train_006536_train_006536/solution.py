for s in [*open(0)][2::2]:
	i = 0
	while s[i:i + 2] == '1 ':
		i += 2
	print('FSiercsotn d'[i // 2 % 2::2])

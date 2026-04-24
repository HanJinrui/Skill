for s in [*open(0)][2::2]:
	k = i = s.count('2')
	j = 0
	while (i := (i - 2 * (s[j] > '1'))) > 0:
		j += 2
	print((j // 2 + 1, -1)[k % 2])

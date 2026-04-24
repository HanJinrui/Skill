for s in [*open(0)][1:]:
	i = 0
	j = k = len(s) - 1
	while k and (c := chr(96 + k)) in (s[i], s[j - 1]):
		if c == s[i]:
			i += 1
		else:
			j -= 1
		k -= 1
	print('YNEOS'[k > 0::2])

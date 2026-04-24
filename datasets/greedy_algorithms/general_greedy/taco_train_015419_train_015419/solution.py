for s in [*open(0)][2::2]:
	n = r = len(s)
	f = 1
	for x in s[:-1]:
		r -= 6 * (x > 'M') - 3
		f &= 0 < r <= n
	print('YNEOS'[f != r::2])

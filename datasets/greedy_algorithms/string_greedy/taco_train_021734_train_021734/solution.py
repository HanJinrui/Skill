for s in [*open(0)][2::2]:
	i = (s[:-1] + '1').find('1')
	j = ('0' + s).rfind('0')
	print(s[:i] + '0' * (j - i > 1) + s[j:])

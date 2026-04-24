for s in [*open(0)][1:]:
	a = 'abzy'
	b = 2
	print(''.join((a[(c == a[(b := (b ^ 2))]) + b] for c in s[:-1])))

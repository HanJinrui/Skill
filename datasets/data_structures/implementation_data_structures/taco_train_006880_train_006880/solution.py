I = input
for _ in [0] * int(I()):
	I()
	a = {1: 1}
	i = s = 1
	r = (-1,)
	m = 300000.0
	for c in I():
		s += ((c == 'R') - (c == 'L') << 16) + (c > 'R') - (c < 'L')
		j = a.get(s, -m)
		if i - j < m:
			m = i - j
			r = (j, i)
		i += 1
		a[s] = i
	print(*r)

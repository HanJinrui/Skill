x = 0
for s in [[1.0]] * int(input()):
	(t, c) = (input(), s.pop())
	if 'f' < t:
		s += [c, c * int(t[4:])]
	elif 'e' > t:
		x += c
		s += [c]
print(['OVERFLOW!!!', '%.f' % x][x < 2 ** 32])

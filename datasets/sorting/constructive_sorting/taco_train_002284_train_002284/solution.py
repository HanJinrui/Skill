import sys

def ask(x, y):
	print('?', x, y)
	return input() == 'y'
while input() == 'start':
	if not ask(0, 1):
		print('! 1')
		continue
	d = 1
	while ask(d, d * 2):
		d *= 2
	r = d
	l = d // 2
	while l + 1 < r:
		m = (l + r) // 2
		if ask(m, m * 2):
			l = m
		else:
			r = m
	print('!', r * 2 if not ask(r * 2 - 1, r * 2) else r * 2 - 1)

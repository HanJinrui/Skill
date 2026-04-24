I = input
for _ in range(int(I())):
	I()
	m = -1000000000.0
	l = 0
	for x in map(int, I().split()):
		m = max(m, x)
		l = max(l, m - x)
	print(l and len(f'{l:b}'))

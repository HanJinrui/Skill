m = 'z'
for c in input():
	print('MAinkne'[c > m::2])
	m = min(m, c)

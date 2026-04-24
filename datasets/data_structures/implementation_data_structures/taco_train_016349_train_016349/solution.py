for _ in [0] * int(input()):
	input()
	m = 10000000.0
	r = 0
	for x in [*map(int, input().split())][::-1]:
		r += x > m
		m = min(m, x)
	print(r)

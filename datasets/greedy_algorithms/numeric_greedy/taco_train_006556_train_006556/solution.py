R = lambda : map(int, input().split())
for _ in [0] * int(input()):
	(n, x) = R()
	l = m = 0
	for _ in [0] * n:
		(d, h) = R()
		l = max(l, d)
		m = max(m, d - h)
	print(1 if l >= x else -1 if m < 1 else -(-(x - l) // m) + 1)

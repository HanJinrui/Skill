R = lambda : map(int, input().split())
(t,) = R()
for _ in range(t):
	(n, m) = R()
	a = b = [0] * m
	for _ in range(n):
		a = list(map(max, [0] + a, a, a[1:] + [0], [0] + b, b, b[1:] + [0]))
		b = list(R())
		print(''.join(('01'[x < y] for (x, y) in zip(a, b))))

I = lambda : map(int, input().split())
for _ in [0] * int(input()):
	(x, y, z) = I()
	(a, b, c, d, e) = I()
	print('NYOE S'[x >= a and y >= b and (z >= c) and (z - c >= max(d + a - x, 0) + max(e + b - y, 0))::2])

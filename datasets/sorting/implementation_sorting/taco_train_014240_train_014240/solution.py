I = input
for _ in [0] * int(I()):
	a = sorted(([*map(int, I().split())] for _ in [0] * int(I())))
	b = [y for (x, y) in a]
	print(('YES ' + ''.join(('R' * (x - u) + 'U' * (y - v) for ((u, v), (x, y)) in zip([[0, 0]] + a, a))), 'NO')[b > sorted(b)])

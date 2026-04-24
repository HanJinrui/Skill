R = lambda : map(int, input().split())
(t,) = R()
for _ in [0] * t:
	(a, b, c, d) = R()
	(x, y, u, v, w, z) = R()
	print('NYOE S'[w - u >= (a == b > 0) and u <= x + b - a <= w and (z - v >= (c == d > 0)) and (v <= y + d - c <= z)::2])

P = lambda : map(int, input().split())
for _ in range(*P()):
	(n,) = P()
	d = [(1, 1)] + sorted(zip(P(), P()))
	a = 0
	for i in range(n):
		(r, c) = d[i]
		v = r - c
		(R, C) = d[i + 1]
		a += (R - C) // 2 - v // 2 + (R - r) * (v & 1 < 1 and v == R - C)
	print(a)

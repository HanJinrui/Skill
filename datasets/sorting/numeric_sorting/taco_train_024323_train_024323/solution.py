import math
Y = lambda : map(int, input().split())
for _ in range(next(Y())):
	(n, k) = Y()
	a = sorted(Y())
	v = a[-k]
	print(math.comb(a.count(v), a[-k:].count(v)) % (10 ** 9 + 7))

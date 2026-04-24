import math
p = 998244353
X = [(1, 0)]
for i in range(1, 31):
	Y = (math.comb(2 * i, i) // 2 + X[i - 1][1]) % p
	X += [(Y % p, (math.comb(2 * i, i) - Y - 1) % p)]
for i in range(int(input())):
	print(*X[int(input()) // 2], 1)

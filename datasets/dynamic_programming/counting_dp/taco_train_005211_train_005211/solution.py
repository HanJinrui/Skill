n = int(input())
m = 998244353
(x, y) = (1, 1)
for _ in range(2, n):
	(x, y) = (y, x + y)
print(y * pow(pow(2, n, m), m - 2, m) % m)

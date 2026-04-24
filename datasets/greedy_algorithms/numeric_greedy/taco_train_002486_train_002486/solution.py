(n, k) = map(int, input().split())
x = 0
y = 1
mod = 10 ** 9 + 7
for i in range(min(n, k) + 1):
	x = (x + y) % mod
	y = y * (n - i) * pow(i + 1, -1, mod) % mod
print(x)

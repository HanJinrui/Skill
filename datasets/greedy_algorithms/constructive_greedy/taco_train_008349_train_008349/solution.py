n = int(input())
m = int(n ** 0.5)
L = []
for i in range(0, n, m):
	L += range(min(i + m, n), i, -1)
print(*L)

t = int(input())
for _ in range(t):
	n = int(input())
	c = [[int(i) for i in input().split()] for j in range(2 * n)]
	a = min(c[0][n], c[n][0], c[2 * n - 1][0], c[0][2 * n - 1], c[n - 1][2 * n - 1], c[2 * n - 1][n - 1], c[n][n - 1], c[n - 1][n])
	for i in range(n):
		for j in range(n):
			a += c[i + n][j + n]
	print(a)

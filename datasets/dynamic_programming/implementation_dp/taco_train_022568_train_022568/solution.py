(n, m) = map(int, input().split())
(r, c) = ([[0 for i in range(m + 1)] for j in range(n + 1)], [[0 for i in range(m + 1)] for j in range(n + 1)])
g = [' ' * (m + 1)] + [' ' + input() for _ in range(n)]
for i in range(1, n + 1):
	for j in range(1, m + 1):
		r[i][j] = r[i][j - 1] + r[i - 1][j] - r[i - 1][j - 1] + (g[i][j] == g[i][j - 1] == '.')
		c[i][j] = c[i][j - 1] + c[i - 1][j] - c[i - 1][j - 1] + (g[i][j] == g[i - 1][j] == '.')
q = int(input())
for _ in ' ' * q:
	(r1, c1, r2, c2) = map(int, input().split())
	print(r[r2][c2] - r[r1 - 1][c2] - r[r2][c1] + r[r1 - 1][c1] + c[r2][c2] - c[r1][c2] - c[r2][c1 - 1] + c[r1][c1 - 1])

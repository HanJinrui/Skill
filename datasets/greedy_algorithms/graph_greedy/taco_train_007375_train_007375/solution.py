t = int(input())
for _ in range(t):
	(n, m) = map(int, input().split())
	a = [list(map(int, input())) for i in range(n)]

	def add(p):
		a[p[0]][p[1]] ^= 1
		a[p[2]][p[3]] ^= 1
		a[p[4]][p[5]] ^= 1
		ans.append(' '.join(map(lambda x: str(x + 1), p)))
	ans = []
	for i in range(n - 1, 1, -1):
		for j in range(m):
			if a[i][j]:
				add((i, j, i - 1, j, i - 1, j + (1 if j < m - 1 else -1)))
	for j in range(m - 1, 1, -1):
		for i in (0, 1):
			if a[i][j]:
				add((i, j, 0, j - 1, 1, j - 1))
	for i in (0, 1):
		for j in (0, 1):
			if (a[0][0] + a[0][1] + a[1][0] + a[1][1] + a[i][j]) % 2:
				add((i ^ 1, j, i, j ^ 1, i ^ 1, j ^ 1))
	print(len(ans))
	print('\n'.join(ans))

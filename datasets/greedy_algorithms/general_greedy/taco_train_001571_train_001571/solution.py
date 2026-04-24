(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def go():
	for i in range(n - 1, -1, -1):
		for j in range(m - 1, -1, -1):
			if not a[i][j]:
				a[i][j] = min(a[i + 1][j], a[i][j + 1]) - 1
			if i + 1 < n and a[i][j] >= a[i + 1][j] or (j + 1 < m and a[i][j] >= a[i][j + 1]):
				print(-1)
				return
	s = 0
	for v in a:
		s += sum(v)
	print(s)
go()

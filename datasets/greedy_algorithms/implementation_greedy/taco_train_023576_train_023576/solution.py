for _ in range(int(input())):
	(n, m) = map(int, input().split())
	l = [list(map(int, input())) for i in range(n)]
	ans = min([max(1, sum(l[i][j:j + 2]) + sum(l[i + 1][j:j + 2]) - 1) for i in range(n - 1) for j in range(m - 1)])
	print(sum((sum(l[i]) for i in range(n))) - ans + 1)

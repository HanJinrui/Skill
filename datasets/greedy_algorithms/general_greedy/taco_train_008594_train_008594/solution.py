for t in range(int(input())):
	n = int(input())
	g = [sorted(input()) for i in range(n)]
	print('YES' if all((g[i][j] <= g[i + 1][j] for i in range(n - 1) for j in range(n))) else 'NO')

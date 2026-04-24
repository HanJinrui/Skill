import sys
input = sys.stdin.readline
readline = lambda : map(int, input().split())
for _ in range(int(input())):
	(n, m) = readline()
	g = [[] for i in range(n)]
	for i in range(m):
		(a, b) = readline()
		g[a - 1].append(b - 1)
	f = [0] * n
	for i in range(n):
		if f[i] < 2:
			for j in g[i]:
				f[j] = max(f[j], f[i] + 1)
	ans = [i + 1 for i in range(n) if f[i] == 2]
	print(len(ans))
	print(*ans)

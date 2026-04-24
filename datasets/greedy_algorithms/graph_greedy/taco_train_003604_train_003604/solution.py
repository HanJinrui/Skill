import sys
input = sys.stdin.readline
N = 10 ** 5 + 5
g = [[] for _ in range(N)]
p = [0] * N

def bfs(cur):
	q = [cur]
	i = 0
	while i < len(q):
		cur = q[i]
		i += 1
		for nxt in g[cur]:
			if nxt != p[cur]:
				p[nxt] = cur
				q.append(nxt)
n = int(input())
for i in range(n - 1):
	(a, b) = map(int, input().split())
	g[a].append(b)
	g[b].append(a)
bfs(1)
print(n - 1)
for i in range(2, n + 1):
	print(2, i, p[i])
for i in range(len(g[1]) - 1):
	print(g[1][i] - 1, g[1][i + 1] - 1)
for i in range(2, n + 1):
	for c in g[i]:
		if c != p[i]:
			print(i - 1, c - 1)

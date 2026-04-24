import sys
sys.setrecursionlimit(10 ** 6)

def solve():
	n = int(input())
	adj = [[] for i in range(n + 1)]
	temp = [[], []]
	vec = []
	for i in range(0, n - 1):
		(u, v) = map(int, input().split())
		adj[u].append(v)
		adj[v].append(u)

	def dfs1(v, par, ct):
		temp[ct].append(v)
		for i in adj[v]:
			if i == par:
				continue
			dfs1(i, v, ct ^ 1)

	def dfs2(v, par):
		vec.append(v)
		for i in adj[v]:
			if i == par:
				continue
			dfs2(i, v)
	dfs1(1, 0, 0)
	if len(temp[0]) == len(temp[1]):
		print(1)
		print(*temp[0])
		print(*temp[1])
	else:
		print(2)
		temp[0] = []
		temp[1] = []
		vec = []
		dfs2(1, 0)
		ct = 0
		for i in vec:
			temp[ct].append(i)
			ct ^= 1
		print(*temp[0])
		print(*temp[1])
T = int(input())
for t in range(0, T):
	solve()

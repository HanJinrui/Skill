from sys import stdin
input = stdin.readline

def dfs(curr):
	vis[curr] = 1
	for i in graph[curr]:
		if vis[i] == 0:
			dfs(i)
for _ in range(int(input())):
	(c, n, m) = [int(i) for i in input().split()]
	sinc = [[] for i in range(c)]
	a = []
	for i in range(c):
		xi = int(input())
		pos = [int(i) for i in input().split()]
		for j in range(len(pos)):
			a.append([pos[j], j % 2, i])
	graph = [set() for i in range(c)]
	a.sort()
	first = []
	scnt = []
	ccnt = 0
	for i in a:
		if len(first) == 0:
			first = [i[0], i[2]]
			ccnt += 1
			continue
		if i[1] == 0:
			graph[i[2]].add(first[1])
			graph[first[1]].add(i[2])
			ccnt += 1
		else:
			if ccnt == 1:
				scnt.append(i[0] - first[0] + 1)
				first = []
			ccnt -= 1
	rem = n - sum(scnt)
	vis = [0] * c
	segments = 0
	for i in range(c):
		if vis[i] == 0:
			dfs(i)
			segments += 1
	total = rem + segments
	mod = 998244353
	print(pow(m, total, mod))

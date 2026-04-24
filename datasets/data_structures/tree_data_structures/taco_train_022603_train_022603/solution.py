from math import log2

def construct(root):
	stack = [root]
	while stack:
		u = stack.pop()
		for v in edges[u]:
			if v != parents[u]:
				parents[v] = u
				levels[v] = levels[u] + 1
				stack.append(v)
	table.append(parents)
	k = 1
	while 1 << k < n:
		new_row = [0] * n
		for i in range(n):
			new_row[i] = table[k - 1][table[k - 1][i]]
		table.append(new_row)
		k += 1

def getlca(a, b):
	depth_gap = levels[b] - levels[a]
	if depth_gap < 0:
		(a, b) = (b, a)
		depth_gap = -depth_gap
	if depth_gap != 0:
		k = int(log2(depth_gap))
		while depth_gap:
			if depth_gap >= 2 ** k:
				b = table[k][b]
				depth_gap = levels[b] - levels[a]
			k -= 1
	if b == a:
		return a
	for k in range(logn, -1, -1):
		if table[k][a] != table[k][b]:
			(a, b) = (table[k][a], table[k][b])
	return table[0][a]

def travel(a, b):
	lca = getlca(a, b)
	tally[a] += 1
	tally[b] += 1
	tally[lca] -= 2

def sum_subtree(root):
	stack = []
	for v in edges[root]:
		stack.append([v, 0])
	while stack:
		(u, i) = stack[-1]
		if i == len(edges[u]):
			tally[parents[u]] += tally[u]
			stack.pop()
		else:
			v = edges[u][i]
			stack[-1][1] += 1
			if v != parents[u]:
				stack.append([v, 0])

def count_fools(u, v):
	if levels[u] > levels[v]:
		return tally[u]
	else:
		return tally[v]
n = int(input())
logn = int(log2(n))
edges = [[] for _ in range(n)]
edges_list = []
for i in range(n - 1):
	(u, v) = map(int, input().split())
	(u, v) = (u - 1, v - 1)
	edges[u].append(v)
	edges[v].append(u)
	edges_list.append((u, v))
parents = [0] * n
levels = [0] * n
table = []
root = 0
construct(root // 2)
tally = [0] * n
k = int(input())
for _ in range(k):
	(a, b) = map(int, input().split())
	travel(a - 1, b - 1)
sum_subtree(root)
for (u, v) in edges_list:
	print(count_fools(u, v), end=' ')
print()

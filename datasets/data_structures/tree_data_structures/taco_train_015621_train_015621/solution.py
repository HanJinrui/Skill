from collections import deque

def solve(parent, depth, aa):
	(a, b) = list(map(int, input().split()))
	a -= 1
	b -= 1
	values = set()
	if depth[b] > depth[a]:
		(a, b) = (b, a)
	while depth[a] > depth[b]:
		if aa[a] in values:
			return 0
		values.add(aa[a])
		a = parent[a]
	while a != b:
		if aa[a] in values:
			return 0
		values.add(aa[a])
		a = parent[a]
		if aa[b] in values:
			return 0
		values.add(aa[b])
		b = parent[b]
	if aa[a] in values:
		return 0
	values.add(aa[a])
	l = list(values)
	l.sort()
	mn = 1000000.0
	for i in range(len(l) - 1):
		mn = min(mn, l[i + 1] - l[i])
		if mn == 1:
			break
	return mn
for T in range(int(input())):
	(n, q) = list(map(int, input().split()))
	aa = list(map(int, input().split()))
	adj = [set() for i in range(n)]
	for i in range(n - 1):
		(u, v) = list(map(int, input().split()))
		adj[u - 1].add(v - 1)
		adj[v - 1].add(u - 1)
	parent = [-1] * n
	parent[0] = 0
	depth = [0] * n
	dq = deque()
	dq.append(0)
	while dq:
		p = dq.popleft()
		for i in adj[p]:
			if parent[i] < 0:
				parent[i] = p
				depth[i] = depth[p] + 1
				dq.append(i)
	for i in range(q):
		v = solve(parent, depth, aa)
		print(v)

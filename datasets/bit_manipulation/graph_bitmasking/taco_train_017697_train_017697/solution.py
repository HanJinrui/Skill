stack = []
hashesSt = set()
t = int(input())
for _ in range(t):
	(n, st, fi) = map(int, input().split())
	st -= 1
	fi -= 1
	g = [[] for i in range(n)]
	for i in range(n - 1):
		(a, b, w) = map(int, input().split())
		a -= 1
		b -= 1
		g[a].append((b, w))
		g[b].append((a, w))
	hashesSt.clear()
	used = [False] * n
	used[fi] = True
	stack.append((st, 0))
	while stack:
		(ver, hsh) = stack.pop()
		used[ver] = True
		hashesSt.add(hsh)
		for (to, w) in g[ver]:
			if not used[to]:
				stack.append((to, hsh ^ w))
	used = [False] * n
	stack.append((fi, 0))
	found = False
	while stack:
		(ver, hsh) = stack.pop()
		used[ver] = True
		if ver != fi and hsh in hashesSt:
			stack.clear()
			found = True
			break
		for (to, w) in g[ver]:
			if not used[to]:
				stack.append((to, hsh ^ w))
	print('YES' if found else 'NO')

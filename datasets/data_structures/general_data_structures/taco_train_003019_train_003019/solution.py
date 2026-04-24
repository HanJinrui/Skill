def solve(pp, tree):
	return next((p[0] for p in pp if p[0] not in tree))
T = int(input())
for t in range(T):
	n = int(input())
	pp = list(enumerate(map(int, input().split())))
	pp.sort(key=lambda z: z[1], reverse=True)
	tree = [set([i]) for i in range(n)]
	for i in range(n - 1):
		(u, v) = map(lambda x: int(x) - 1, input().split())
		tree[u].add(v)
		tree[v].add(u)
	res = list(map(lambda x: solve(pp, tree[x]) + 1, range(n)))
	print(*res)

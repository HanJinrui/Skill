for _ in range(int(input())):
	input()
	(n, m) = map(int, input().split())
	adj = [[] for _ in range(n)]
	for _ in range(m):
		(u, v) = map(lambda x: int(x) - 1, input().split())
		adj[u].append(v)
	dis = [-1] * n
	dis[0] = 0
	que = [0]
	for i in range(n):
		u = que[i]
		for v in adj[u]:
			if dis[v] == -1:
				dis[v] = dis[u] + 1
				que.append(v)
	ans = [0] * n
	for u in sorted([i for i in range(n)], key=lambda x: dis[x], reverse=True):
		ans[u] = dis[u]
		for v in adj[u]:
			if dis[u] >= dis[v]:
				ans[u] = min(ans[u], dis[v])
			else:
				ans[u] = min(ans[u], ans[v])
	print(*ans)

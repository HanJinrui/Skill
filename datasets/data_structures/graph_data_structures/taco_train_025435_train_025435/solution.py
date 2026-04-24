for t in range(int(input())):
	(n, m, s, k) = map(int, input().split())
	adjlist = {i: [] for i in range(n + 1)}
	for i in range(m):
		(u, v) = map(int, input().split())
		adjlist[u].append(v)
		adjlist[v].append(u)
	s = list(map(int, input().split()))
	vis = [-1] * (n + 1)
	vis[0] = 0
	q = [0]
	while q != []:
		curr = q.pop(0)
		for i in adjlist[curr]:
			if vis[i] >= 0:
				continue
			else:
				vis[i] = vis[curr] + 1
				q.append(i)
	ans = []
	for i in range(len(s)):
		ans.append(vis[s[i]])
	ans.sort()
	print(sum(ans[:k]) * 2)

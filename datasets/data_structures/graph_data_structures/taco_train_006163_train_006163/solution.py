for _ in range(int(input())):
	(n, m) = map(int, input().split())
	graph = [[i] for i in range(n + 1)]
	for _ in range(m):
		(u, v) = map(int, input().split())
		graph[u].append(v)
		graph[v].append(u)
	mp = {}
	for item in graph:
		mp[tuple(sorted(item))] = 0
	for item in graph:
		mp[tuple(sorted(item))] += 1
	cnt = 0
	for item in mp:
		if mp[item] == len(item) and len(item) != n:
			cnt += 1
	print(cnt - 1)

from collections import defaultdict
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	graph = [1] * (n + 1)
	routes = []
	for _ in range(m):
		(a, b) = map(int, input().split())
		routes.append(sorted((a, b)))
		graph[a] += 1
		graph[b] += 1
	ans = []
	if m == n * (n - 1) / 2:
		print(3)
		for (a, b) in routes:
			if (a, b) == (1, 2):
				ans.append(3)
			elif a == 1:
				ans.append(2)
			else:
				ans.append(1)
	else:
		print(2)
		for i in range(1, n + 1):
			if graph[i] < n:
				v = i
				break
		for (a, b) in routes:
			if a == v or b == v:
				ans.append(1)
			else:
				ans.append(2)
	print(*ans)

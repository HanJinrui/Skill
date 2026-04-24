import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	g = [[] for _ in range(n)]
	for i in range(n - 1):
		(u, v) = map(int, input().split())
		g[u - 1].append(v - 1)
		g[v - 1].append(u - 1)
	q = [(0, -1)]
	h = 0
	c = 2
	while q:
		new_q = []
		for (i, j) in q:
			x = [child for child in g[i] if child != j]
			c = min(c, len(x))
			for k in x:
				new_q.append([k, i])
		if c < 2:
			print(n - 1 - c - 2 * h)
			break
		h += 1
		q = new_q

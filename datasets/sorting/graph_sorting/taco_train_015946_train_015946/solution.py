from collections import defaultdict
MAX = 10 ** 14

def Dijkstra(graph, s, n):
	visited = [False] * n
	d = [MAX] * n
	parents = {}
	d[s] = 0
	for i in range(n):
		(_, v) = min(((d[j], j) for j in range(n) if not visited[j]))
		visited[v] = True
		for (to, length) in graph[v]:
			if d[to] > d[v] + length:
				d[to] = d[v] + length
				parents[to] = v
	return (parents, d)

def PrintSol(graph, n_edges, n, zeros, edgesWithZero, leave):
	for i in range(n):
		for (to, length) in graph[i]:
			if to < i:
				if (i, to) in n_edges:
					print(i, to, n_edges[i, to])
				elif zeros and (i, to) in edgesWithZero and ((i, to) not in leave):
					print(i, to, MAX)
				else:
					print(i, to, length)
graphWithZero = defaultdict(list)
graphWithMax = defaultdict(list)
(n, m, L, s, t) = map(int, input().split(' '))
edgesWithZero = set()
for _ in range(m):
	(u, v, l) = map(int, input().split(' '))
	if l == 0:
		graphWithZero[u].append((v, 1))
		graphWithZero[v].append((u, 1))
		graphWithMax[u].append((v, MAX))
		graphWithMax[v].append((u, MAX))
		edgesWithZero |= {(u, v), (v, u)}
	else:
		graphWithZero[u].append((v, l))
		graphWithZero[v].append((u, l))
		graphWithMax[u].append((v, l))
		graphWithMax[v].append((u, l))
(a2, d2) = Dijkstra(graphWithMax, s, n)
(a1, d1) = Dijkstra(graphWithZero, s, n)
if d2[t] < L:
	print('NO')
elif d2[t] == L:
	print('YES')
	PrintSol(graphWithMax, dict(), n, False, edgesWithZero, set())
elif d1[t] <= L:
	print('YES')
	v = t
	leave = set()
	n_edges = dict()
	total = 0
	while v != s:
		leave |= {(v, a1[v]), (a1[v], v)}
		if (v, a1[v]) in edgesWithZero:
			cur = max(L - total - d2[a1[v]], 1)
			n_edges[max(v, a1[v]), min(v, a1[v])] = cur
			total += cur
		else:
			total += d1[v] - d1[a1[v]]
		v = a1[v]
	PrintSol(graphWithZero, n_edges, n, True, edgesWithZero, leave)
else:
	print('NO')

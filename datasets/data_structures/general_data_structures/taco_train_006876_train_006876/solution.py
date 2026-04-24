import collections
n = int(input())
node_colors = input().split()
edges = {i: [] for i in range(n)}
for _ in range(n - 1):
	(one, two) = [int(i) - 1 for i in input().split()]
	edges[one].append(two)
	edges[two].append(one)

def bfs_sum(i):
	value = 0
	seen = {i}
	q = collections.deque([(i, {node_colors[i]})])
	while q:
		(t, colors) = q.popleft()
		value += len(colors)
		for edge in edges[t]:
			if edge not in seen:
				seen.add(edge)
				q.append((edge, colors | {node_colors[edge]}))
	return value
for i in range(n):
	print(bfs_sum(i))

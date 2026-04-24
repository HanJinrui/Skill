from collections import defaultdict
II = lambda : [int(x) for x in input().split()]

def find_cycle(graph, start, visited, d_nodes):
	d_nodes = set(d_nodes)
	stack = [start]
	parent = defaultdict(int)
	while stack:
		state = stack.pop()
		for next_state in graph[state]:
			if next_state == parent[state]:
				continue
			if visited[next_state]:
				path = [state]
				while next_state != state:
					state = parent[state]
					path.append(state)
				return path
			if next_state not in d_nodes:
				parent[next_state] = state
				stack.append(next_state)
		visited[state] = True
	return None

def find_a_cycle(G, d_nodes):
	visited = defaultdict(bool)
	d_nodes = set(d_nodes)
	for node in G:
		if node not in visited and node not in d_nodes:
			cycle = find_cycle(G, node, visited, d_nodes)
			if cycle is not None:
				return cycle
	return []
T = int(input())
for _ in range(T):
	(N, E) = II()
	G = defaultdict(list)
	for _ in range(E):
		(a, b) = II()
		G[a].append(b)
		G[b].append(a)
	cycle = find_a_cycle(G, [])
	if not cycle:
		print(-1)
		continue
	if find_a_cycle(G, cycle):
		print(-1)
		continue
	f_node = -1
	cycle.sort()
	for node in cycle:
		new_cycle = find_a_cycle(G, [node])
		if not new_cycle:
			f_node = node
			break
	print(f_node)

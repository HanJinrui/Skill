import sys
from collections import deque

def eulerian_path(root, adj):
	path = []
	stack = [root]
	while stack:
		u = stack[-1]
		if len(adj[u]) == 0:
			path.append(u)
			stack.pop()
		else:
			v = adj[u][-1]
			adj[u].pop()
			adj[v] = [w for w in adj[v] if w != u]
			stack.append(v)
	return path

def main():
	test_cases = int(sys.stdin.readline())
	for _ in range(test_cases):
		(board_dim, marked_count) = (int(i) for i in sys.stdin.readline().split())
		marked = dict()
		adj = [[] for _ in range(2 * (board_dim + 1))]
		root = 0
		for i in range(1, marked_count + 1):
			(row, col) = (int(i) for i in sys.stdin.readline().split())
			marked[row, col] = i
			col = col + board_dim
			adj[row].append(col)
			adj[col].append(row)
			root = max(root, row)
		for (node, neighbors) in enumerate(adj):
			if len(neighbors) % 2:
				root = node
		path = eulerian_path(root, adj)
		soln = []
		for (row, col) in zip(path[:-1], path[1:]):
			if row > board_dim:
				row = row - board_dim
				(row, col) = (col, row)
			else:
				col = col - board_dim
			soln.append(marked[row, col])
		print(' '.join((str(i) for i in soln)))
main()

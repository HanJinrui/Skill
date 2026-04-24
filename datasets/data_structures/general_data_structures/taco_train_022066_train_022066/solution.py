class Node:

	def __init__(self, data):
		self.data = data
		self.neighbors = []

	def add(self, neighbor):
		self.neighbors.append(neighbor)

	def __str__(self):
		return '(' + str(self.data) + ', ' + str(self.parent) + ')'

def path(a, b):
	s = set()
	q = [[b]]
	s.add(b)
	i = 0
	while i < len(q):
		p = q[i]
		if p[0] == a:
			return p
		for n in nodes[p[0]].neighbors:
			if n not in s:
				s.add(n)
				q.append([n] + p)
		i += 1
	raise Exception
(n, r) = map(int, input().split())
nodes = [Node(0) for _ in range(n)]
for _ in range(n - 1):
	(a, b) = map(int, input().split())
	nodes[a - 1].add(b - 1)
	nodes[b - 1].add(a - 1)
(u, q) = map(int, input().split())
for _ in range(u):
	(i, j, x) = map(int, input().split())
	for asdf in path(i - 1, j - 1):
		node = nodes[asdf]
		node.data += x
		x *= r
for _ in range(q):
	(i, j) = map(int, input().split())
	print(sum((nodes[node].data for node in path(i - 1, j - 1))) % 100711433)

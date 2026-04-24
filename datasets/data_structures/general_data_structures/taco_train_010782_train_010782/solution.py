import sys

class Node:

	def __init__(self, a, b):
		self.set_function(a, b)
		self.edges = []
		self.func = None
		self.set_function(a, b)

	def set_function(self, a, b):
		self.func = lambda x: a * x + b

	def add_edge(self, edge):
		self.edges.append(edge)

	def calculate(self, x):
		return self.func(x)

class WhiteFalcon:

	def __init__(self, nodes, edges):
		self.nodes = {}
		self.edges = {}
		self.divisor = 10 ** 9 + 7
		self.known_path = {}
		self.predecessor = {}
		for (i, [a, b]) in enumerate(nodes):
			self.nodes[i + 1] = Node(a, b)
		for [n1, n2] in edges:
			self.nodes[n1].add_edge(n2)
			self.nodes[n2].add_edge(n1)
			if n2 in self.predecessor:
				raise Exception(f'n2 {n2} already has predecessor {self.predecessor[n2]} attempted another {n1}')
			self.predecessor[n2] = n1

	def find_path(self, u, v):
		if (u, v) in self.known_path:
			return self.known_path[u, v]
		v_path = [v]
		n = v
		while n in self.predecessor:
			p = self.predecessor[n]
			v_path.append(p)
			if p == u:
				v_path.reverse()
				self.known_path[u, v] = v_path
				return v_path
			n = p
		v_path.reverse()
		u_path = [u]
		n = u
		while n in self.predecessor:
			p = self.predecessor[n]
			u_path.append(p)
			if p == u:
				self.known_path[u, v] = u_path
				return u_path
			if p in v_path:
				v_path_ind = v_path.index(p)
				path = u_path + v_path[v_path_ind + 1:]
				self.known_path[u, v] = path
				return path
			n = p
		raise Exception(f'Path from {u} to {v} not found. So far: {path}')

	def set_function(self, u, v, a, b):
		path = self.find_path(u, v)
		for n in path:
			self.nodes[n].set_function(a, b)

	def run_functions(self, u, v, x):
		path = self.find_path(u, v)
		for n in path:
			x = self.nodes[n].calculate(x)
		return x % self.divisor
inp = sys.stdin
exp = 3
node_count = int(inp.readline())
functions = []
for _ in range(node_count):
	functions.append(list(map(int, inp.readline().rstrip().split())))
source_edges = []
for _ in range(node_count - 1):
	source_edges.append(list(map(int, inp.readline().rstrip().split())))
query_count = int(inp.readline())
queries = []
for _ in range(query_count):
	queries.append(list(map(int, inp.readline().rstrip().split())))
wf = WhiteFalcon(functions, source_edges)
for q in queries:
	if q[0] == 1:
		[t, u, v, a, b] = q
		wf.set_function(u, v, a, b)
	elif q[0] == 2:
		[t, u, v, x] = q
		print(wf.run_functions(u, v, x))
inp = sys.stdin

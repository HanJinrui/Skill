class heavy_light_node:

	def __init__(self, size):
		self.parent = None
		self.pos = -1
		self.weight = [0] * size
		self.fenwick = [0] * size

	def set_weight(self, i, x):
		d = x - self.weight[i]
		self.weight[i] = x
		N = len(self.weight)
		while i < N:
			self.fenwick[i] += d
			i |= i + 1

	def sum_weight(self, i):
		if i < 0:
			return 0
		x = self.fenwick[i]
		i &= i + 1
		while i:
			x += self.fenwick[i - 1]
			i &= i - 1
		return x

def build_tree(i, edges, location):
	children = []
	members = [i]
	ed = edges[i]
	while ed:
		for j in range(1, len(ed)):
			child = build_tree(ed[j], edges, location)
			child.pos = len(members) - 1
			children.append(child)
		i = ed[0]
		members.append(i)
		ed = edges[i]
	node = heavy_light_node(len(members))
	for child in children:
		child.parent = node
	for j in range(len(members)):
		location[members[j]] = (node, j)
	return node

def read_tree(N):
	edges = [[] for i in range(N)]
	for i in range(N - 1):
		(x, y) = map(int, input().split())
		edges[x].append(y)
		edges[y].append(x)
	size = [0] * N
	active = [0]
	while active:
		i = active[-1]
		if size[i] == 0:
			size[i] = 1
			for j in edges[i]:
				edges[j].remove(i)
				active.append(j)
		else:
			active.pop()
			edges[i].sort(key=lambda j: -size[j])
			size[i] = 1 + sum((size[j] for j in edges[i]))
	location = [None] * N
	build_tree(0, edges, location)
	return location

def root_path(i, location):
	loc = location[i]
	path = [loc]
	loc = loc[0]
	while loc.parent != None:
		path.append((loc.parent, loc.pos))
		loc = loc.parent
	path.reverse()
	return path

def max_weight(x, y):
	px = root_path(x, location)
	py = root_path(y, location)
	m = 1
	stop = min(len(px), len(py))
	while m < stop and px[m][0] == py[m][0]:
		m += 1
	(loc, a) = px[m - 1]
	b = py[m - 1][1]
	if a > b:
		(a, b) = (b, a)
	w = loc.sum_weight(b) - loc.sum_weight(a - 1)
	for j in range(m, len(px)):
		(loc, i) = px[j]
		w += loc.sum_weight(i)
	for j in range(m, len(py)):
		(loc, i) = py[j]
		w += loc.sum_weight(i)
	return w
(N, Q) = map(int, input().split())
location = read_tree(N)
for i in range(Q):
	(t, x, y) = map(int, input().split())
	if t == 1:
		(loc, i) = location[x]
		loc.set_weight(i, y)
	elif t == 2:
		print(max_weight(x, y))

import sys
from filecmp import cmp
from os import linesep
from time import time
from collections import Counter
memoized_BIT_prevs = [list() for _ in range(10 ** 5 + 1)]
for i in range(1, 10 ** 5 + 1):
	next = i + (i & -i)
	if next >= len(memoized_BIT_prevs):
		continue
	memoized_BIT_prevs[next].append(i)

class UF(object):
	__slots__ = ['uf', 'ranks']

	def __init__(self):
		self.uf = {}
		self.ranks = {}

	def UFadd(self, a):
		self.uf[a] = a
		self.ranks[a] = 0

	def UFfind(self, a):
		uf = self.uf
		curr = a
		while curr != uf[curr]:
			next = uf[uf[curr]]
			uf[curr] = next
			curr = next
		return curr

	def UFcombine(self, a, b):
		uf = self.uf
		ranks = self.ranks
		a_top = self.UFfind(a)
		b_top = self.UFfind(b)
		rank_a = ranks[a_top]
		rank_b = ranks[b_top]
		if rank_a < rank_b:
			uf[a_top] = b_top
		elif rank_a > rank_b:
			uf[b_top] = a_top
		else:
			uf[b_top] = a_top
			ranks[a_top] += 1

class mycounter(object):
	__slots__ = ['c']

	def __init__(self, key=None):
		if key is None:
			self.c = {}
		else:
			self.c = {key: 1}

	def inc(self, key):
		self.c[key] = self.c.get(key, 0) + 1

	def addto(self, other):
		for (key, otherval) in other.c.items():
			self.c[key] = self.c.get(key, 0) + otherval

	def subfrom(self, other, mult=1):
		for (key, otherval) in other.c.items():
			assert key in self.c
			self.c[key] = self.c[key] - mult * otherval

	def innerprodwith(self, other):
		X = self.c
		Y = other.c
		if len(X) > len(Y):
			(X, Y) = (Y, X)
		return sum((X[i] * Y[i] for i in X if i in Y))

class mycounter2(object):
	__slots__ = ['q', 'doubleneg']

	def __init__(self):
		self.q = []
		self.doubleneg = None

	def inc(self, key):
		self.q.append(key)

	def addto(self, other):
		self.q.extend(other.q)

	def subfrom(self, other, mult=1):
		assert self.doubleneg is None and other.doubleneg is None
		self.doubleneg = other.q

	def innerprodwith(self, other):
		X = self
		Y = other
		if len(X.q) > len(Y.q):
			(X, Y) = (Y, X)
		Xq = X.q
		Yq = Y.q
		Xn = X.doubleneg
		Yn = Y.doubleneg
		S = set(Xq)
		S.update(Xn)
		return sum(((Xq.count(s) - 2 * Xn.count(s)) * (Yq.count(s) - 2 * Yn.count(s)) for s in S))

class geodcounter(object):
	__slots__ = ['size', 'C', 'above', 'below', 'values', 'lca', 'dists']

	def __init__(self, neb, root, vals, pairs):
		self.size = len(neb)
		self.C = [mycounter() for _ in range(self.size)]
		self.above = [None] * self.size
		self.below = [list() for _ in range(self.size)]
		self.values = vals
		self.lca = {}
		self.dists = [None] * self.size
		above = self.above
		below = self.below
		lca = self.lca
		dists = self.dists
		geod = [None]
		gpush = geod.append
		gpop = geod.pop
		height = 0
		traverse_stack = [(root, None)]
		tpush = traverse_stack.append
		tpop = traverse_stack.pop
		visited = set()
		ancestors = {}
		lca_done = set()
		uf = UF()
		while traverse_stack:
			(curr, parent) = tpop()
			if curr is None:
				break
			if curr not in visited:
				dists[curr] = height
				height += 1
				aboveht = height - (height & -height)
				above[curr] = geod[aboveht]
				for nextht in memoized_BIT_prevs[height]:
					below[geod[nextht]].append(curr)
				uf.UFadd(curr)
				visited.add(curr)
				tpush((curr, parent))
				gpush(curr)
				ancestors[curr] = curr
				for child in neb[curr]:
					if child in visited:
						continue
					tpush((child, curr))
			else:
				gcurr = gpop()
				assert gcurr == curr
				self.notice(curr)
				height -= 1
				lca_done.add(curr)
				for v in pairs[curr]:
					if v in lca_done:
						rep_v = uf.UFfind(v)
						anc = ancestors[rep_v]
						assert (curr, v) not in lca and (v, curr) not in lca
						lca[curr, v] = anc
						lca[v, curr] = anc
				if parent is not None:
					uf.UFcombine(curr, parent)
					ancestors[uf.UFfind(curr)] = parent

	def notice(self, node):
		val = self.values[node]
		C = self.C
		below = self.below
		stack = [node]
		pop = stack.pop
		extend = stack.extend
		while stack:
			curr = pop()
			C[curr].inc(val)
			extend(below[curr])

	def find(self, node):
		acc = mycounter()
		C = self.C
		above = self.above
		while node is not None:
			acc.addto(C[node])
			node = above[node]
		return acc

	def get_incidence(self, a, b):
		l = self.lca[a, b]
		find_a = self.find(a)
		find_a.addto(self.find(b))
		find_a.inc(self.values[l])
		find_a.subfrom(self.find(l), 2)
		return find_a

	def size_intersection(self, a, b, c, d):
		prs = ((a, b), (c, d), (a, c), (a, d), (b, c), (b, d))
		verts = list((self.lca[x] for x in prs))
		(key1, key2) = (verts[0], verts[1])
		check = Counter(verts)
		if check[key1] == 1 or check[key2] == 1:
			return 0
		most = check.most_common()
		counts = list((freq for (val, freq) in most))
		if counts == [6] or counts == [3, 3]:
			return 1
		elif counts == [5, 1] or counts == [3, 2, 1]:
			close = most[-2][0]
			far = most[-1][0]
			return self.dists[far] - self.dists[close] + 1
		elif counts == [4, 1, 1]:
			left = most[1][0]
			right = most[2][0]
			mid = most[0][0]
			return self.dists[left] + self.dists[right] - 2 * self.dists[mid] + 1
		else:
			raise RuntimeError

	def process_commands(self, commands):
		measure_int = self.size_intersection
		get_incidence = self.get_incidence
		timer = 0
		for (w, x, y, z) in commands:
			A = get_incidence(w, x)
			B = get_incidence(y, z)
			innerprod = A.innerprodwith(B)
			len_inter = measure_int(w, x, y, z)
			ans = innerprod - len_inter
			assert ans >= 0
			yield ans

def test(num=None):
	if num is None:
		inp = sys.stdin
		out = sys.stdout
	else:
		inp = open('./input' + num + '.txt')
		out = open('./myoutput' + num + '.txt', 'w')
	start_time = time()
	(N, Q) = tuple(map(int, inp.readline().strip().split(' ')))
	vals = [0]
	vals.extend(map(int, inp.readline().strip().split(' ')))
	neb = [list() for x in range(N + 1)]
	for _ in range(N - 1):
		(a, b) = tuple(map(int, inp.readline().strip().split(' ')))
		neb[a].append(b)
		neb[b].append(a)
	pairs = [set() for _ in range(N + 1)]
	commands = []
	for _ in range(Q):
		(w, x, y, z) = tuple(map(int, inp.readline().strip().split(' ')))
		pairs[w].update((x, y, z))
		pairs[x].update((w, y, z))
		pairs[y].update((w, x, z))
		pairs[z].update((w, x, y))
		commands.append((w, x, y, z))
	count_geod = geodcounter(neb, 1, vals, pairs)
	for answer in count_geod.process_commands(commands):
		print(answer, file=out)
	end_time = time()
	if num is not None:
		inp.close()
		if num != '00':
			remove_chars = len(linesep)
			out.truncate(out.tell() - remove_chars)
		out.close()
		succeeded = cmp('myoutput' + num + '.txt', 'output' + num + '.txt')
		outcome = '  Success' if succeeded else '  Failure'
		print('#' + num + outcome, 'in {:f}s'.format(end_time - start_time))
test()

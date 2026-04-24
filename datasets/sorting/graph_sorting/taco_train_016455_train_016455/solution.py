from math import inf
import operator
from collections import defaultdict
import sys
time = 0
edges = []
ans = {}
orig_edges = []
l = {}
d = {}
f = {}
pi = {}
visited = {}

def process_edges(l, ds):
	if len(l) == 1:
		(u, v) = l[0]
		b = ds.SetOf(u) == ds.SetOf(v)
		ans[u, v] = 'none' if b else 'any'
		if not b:
			ds.Merge(u, v)
	else:
		dic = defaultdict(list)
		g = defaultdict(set)
		for e in l:
			(u, v) = e
			x = ds.SetOf(u)
			y = ds.SetOf(v)
			if x == y:
				ans[e] = 'none'
			else:
				(x, y) = tuple(sorted([x, y]))
				dic[x, y].append(e)
				g[x].add(y)
				g[y].add(x)
		a = DFS(g)
		for e in a:
			if len(dic[e]) == 1:
				ans[dic[e][0]] = 'any'
		for e in l:
			if ds.SetOf(e[1]) != ds.SetOf(e[0]):
				ds.Merge(e[0], e[1])

def sol(n):
	ds = DisjointSet(n)
	global edges
	prev_w = edges[0][1]
	same_weight = []
	for (e, w) in edges + [(1, None)]:
		if w == prev_w:
			same_weight.append(e)
		else:
			process_edges(same_weight, ds)
			same_weight = [e]
		prev_w = w

def DFS(graph):
	time = 0
	global l
	global d
	global f
	global pi
	global visited
	visited = {key: False for key in graph}
	l = {key: inf for key in graph}
	d = {key: -1 for key in graph}
	f = {key: -1 for key in graph}
	pi = {key: key for key in graph}
	a = []
	for i in graph.keys():
		if not visited[i]:
			DFS_Visit(graph, i, a)
	return a

def DFS_Visit(graph, v, a):
	visited[v] = True
	global time
	time += 1
	d[v] = l[v] = time
	for i in graph[v]:
		if not visited[i]:
			pi[i] = v
			DFS_Visit(graph, i, a)
			l[v] = min(l[v], l[i])
		elif pi[v] != i:
			l[v] = min(l[v], d[i])
	if pi[v] != v and l[v] >= d[v]:
		a.append(tuple(sorted([v, pi[v]])))
	time += 1
	f[v] = time

def read():
	global edges
	(n, m) = map(int, sys.stdin.readline().split())
	if m == n - 1:
		for _ in range(m):
			print('any')
		exit()
	for i in range(m):
		(x, y, w) = map(int, sys.stdin.readline().split())
		(x, y) = (x - 1, y - 1)
		e = tuple(sorted([x, y]))
		ans[e] = 'at least one'
		orig_edges.append((e, w))
	edges = sorted(orig_edges, key=lambda x: x[1])
	return n

def main():
	n = read()
	sol(n)
	for i in orig_edges:
		print(ans[i[0]])

class DisjointSet:

	def __init__(self, n):
		self.count = [1 for i in range(n)]
		self.father = [i for i in range(n)]

	def SetOf(self, x):
		if x == self.father[x]:
			return x
		return self.SetOf(self.father[x])

	def Merge(self, x, y):
		a = self.SetOf(x)
		b = self.SetOf(y)
		if self.count[a] > self.count[b]:
			temp = a
			a = b
			b = temp
		self.count[b] += self.count[a]
		self.father[a] = b
main()

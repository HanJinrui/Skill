from sys import *
from bisect import bisect_left
input = stdin.readline

def root(node):
	while parent[node] >= 0:
		node = parent[node]
	return node

def union(x, y):
	(x1, x2) = (root(x), root(y))
	if parent[x1] < parent[x2]:
		parent[x1] += parent[x2]
		parent[x2] = x1
	else:
		parent[x2] += parent[x1]
		parent[x1] = x2

def kruskal():
	min_cost = 0
	for (x, y, cst) in edges:
		if root(x) != root(y):
			min_cost += max(cst - k, 0)
			union(x, y)
	return min_cost
for _ in range(int(input())):
	(n, m, k) = map(int, input().split())
	edges = list((list(map(int, input().split())) for i in range(m)))
	edges.sort(key=lambda x: x[2])
	parent = [-1] * (n + 1)
	cost = kruskal()
	if not cost:
		cost = k
		for i in range(m):
			cost = min(cost, abs(edges[i][2] - k))
	print(cost)

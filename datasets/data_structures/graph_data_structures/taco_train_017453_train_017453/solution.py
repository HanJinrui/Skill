from collections import defaultdict
from heapq import heappush, heappop, heapify

class Solution:

	def exercise(self, N, M, A, src, dest, X):
		(d, q, r) = (defaultdict(list), [[0, src]], [float('inf')] * N)
		for (i, j, k) in A:
			d[i].append([j, k])
			d[j].append([i, k])
		heapify(q)
		while q:
			(dis, node) = heappop(q)
			if dis > r[node]:
				continue
			r[node] = dis
			for (cnode, cdis) in d[node]:
				heappush(q, [dis + cdis, cnode])
		if r[dest] <= X:
			return "Neeman's Cotton Classics"
		return "Neeman's Wool Joggers"

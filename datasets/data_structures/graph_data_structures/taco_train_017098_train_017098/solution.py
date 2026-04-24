import sys
sys.setrecursionlimit(10 ** 6)
INV = 1000000000.0

class Solution:

	def articulationPoints(self, V, adj):

		def _solve(u, par):
			nonlocal cur
			cur += 1
			disc[u] = low[u] = cur
			children = 0
			for v in adj[u]:
				if v == par:
					continue
				if disc[v] == INV:
					_solve(v, u)
					children += 1
					low[u] = min(low[u], low[v])
					if u > 0 and low[v] >= disc[u] or (u == 0 and children > 1):
						ans[u] = True
				else:
					low[u] = min(low[u], disc[v])
		(disc, low, ans) = ([INV] * V, [INV] * V, [False] * V)
		cur = -1
		_solve(0, 0)
		ret = [i for (i, v) in enumerate(ans) if v]
		return ret if ret else [-1]

class Solution:

	def eulerPath(self, N, graph):
		deg = len([1 for e in [sum(r) for r in graph] if e & 1 != 0])
		return 1 if deg == 0 or deg == 2 else 0

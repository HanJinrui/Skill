from typing import List
from queue import Queue

class Solution:

	def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
		q = [0]
		vis = [0]
		r = []
		while len(q) != 0:
			z = q.pop(0)
			r.append(z)
			for i in adj[z]:
				if i not in vis:
					q.append(i)
					vis.append(i)
		return r

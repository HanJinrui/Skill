from heapq import heappush, heappop, heapify

class Solution:

	def minCost(self, a, n):
		heapify(a)
		s = 0
		while len(a) != 1:
			x = heappop(a) + heappop(a)
			s += x
			heappush(a, x)
		return s

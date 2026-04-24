import heapq

class Solution:

	def maximizeSum(self, a, n, k):
		heapq.heapify(a)
		for _ in range(k):
			x = heapq.heappop(a)
			heapq.heappush(a, -x)
		return sum(a)

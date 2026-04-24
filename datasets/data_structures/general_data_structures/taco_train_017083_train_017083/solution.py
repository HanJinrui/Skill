from heapq import *

class Solution:

	def minOperations(self, a, n):
		q = []
		c = 0
		for v in a:
			if not q or q[0] >= v:
				heappush(q, v)
			else:
				c += v - heappop(q)
				heappush(q, v)
				heappush(q, v)
		return c

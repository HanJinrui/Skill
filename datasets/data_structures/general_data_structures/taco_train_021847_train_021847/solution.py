import heapq

class Solution:

	def __init__(self):
		self.g = []
		self.s = []

	def balanceHeaps(self):
		pass

	def getMedian(self):
		if len(self.g) > len(self.s):
			heapq.heappush(self.s, -heapq.heappop(self.g))
		if len(self.g) != len(self.s):
			return -self.s[0]
		else:
			return (self.g[0] - self.s[0]) / 2

	def insertHeaps(self, x):
		heapq.heappush(self.s, -x)
		heapq.heappush(self.g, -heapq.heappop(self.s))

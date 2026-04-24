from collections import defaultdict

class Solution:

	def numOfPairs(self, X, Y, N):
		c = 0
		m = defaultdict(int)
		n = defaultdict(int)
		o = defaultdict(int)
		for (x, y) in zip(X, Y):
			c += m[x] + n[y] - o[x, y] * 2
			m[x] += 1
			n[y] += 1
			o[x, y] += 1
		return c

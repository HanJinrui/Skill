from collections import Counter

class Solution:

	def minRemove(self, a, b, n, m):
		c1 = Counter(a)
		c2 = Counter(b)
		return sum((min(c1[item], c2[item]) for item in c1))

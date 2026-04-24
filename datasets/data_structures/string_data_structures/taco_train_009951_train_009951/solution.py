from collections import *

class Solution:

	def findDiff(self, a, n):
		c = Counter(a)
		return max(c.values()) - min(c.values())

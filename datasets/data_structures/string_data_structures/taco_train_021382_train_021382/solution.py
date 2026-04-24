from collections import Counter

class Solution:

	def equalPairs(self, s):
		c = Counter(s)
		return sum([item * item for item in c.values()])

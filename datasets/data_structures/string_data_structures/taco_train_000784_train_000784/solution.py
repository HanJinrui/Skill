from collections import Counter

class Solution:

	def secFrequent(self, arr, n):
		c = Counter(arr)
		return c.most_common(2)[1][0]

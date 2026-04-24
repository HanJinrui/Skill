class Solution:

	def getMoreAndLess(self, arr, n, x):
		l = [i for i in arr if i >= x]
		s = [j for j in arr if j <= x]
		return [len(s), len(l)]

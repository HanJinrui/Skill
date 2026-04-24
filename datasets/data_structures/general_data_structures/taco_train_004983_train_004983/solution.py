class Solution:

	def printMinimumProduct(self, a, n):
		l = [int(i) for i in a]
		l.sort()
		return l[0] * l[1]

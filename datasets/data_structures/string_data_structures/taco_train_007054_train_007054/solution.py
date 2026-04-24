class Solution:

	def printTriangleDownwards(self, s):
		for (i, j) in enumerate(s):
			print((len(s) - i - 1) * '.' + s[:i + 1])

class Solution:

	def printMinIndexChar(self, S, patt):
		for c in S:
			if c in patt:
				return c
		return '$'

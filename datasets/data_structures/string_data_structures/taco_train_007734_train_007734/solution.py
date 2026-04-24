class Solution:

	def commonSubseq(self, a, b):
		return any([item in b for item in a])

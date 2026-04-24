class Solution:

	def isIsogram(self, s):
		return len(s) == len(set(s))

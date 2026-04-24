class Solution:

	def minChange(self, S):
		return len(S) - len(set(S))

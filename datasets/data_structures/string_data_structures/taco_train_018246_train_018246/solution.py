class Solution:

	def isValid(self, s, n):
		if len(max(s.split('R'))) <= n:
			return 1
		else:
			return 0

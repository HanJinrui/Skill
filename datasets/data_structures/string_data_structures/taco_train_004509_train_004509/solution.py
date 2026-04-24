class Solution:

	def passed(self, s):
		n = len(s) // 2
		return sorted([*s[:n]]) == sorted([*s[-n:]])

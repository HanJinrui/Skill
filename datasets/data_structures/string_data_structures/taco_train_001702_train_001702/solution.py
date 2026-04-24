class Solution:

	def fun(self, s):
		return len(set([s[i:i + 2] for i in range(len(s) - 1)]))

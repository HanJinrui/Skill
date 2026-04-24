class Solution:

	def demonitize(self, S, m, n):
		S = S.replace(m, '')
		S = S.replace(n, '')
		return -1 if len(S) == 0 else S

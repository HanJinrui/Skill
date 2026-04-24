class Solution:

	def countSubstr(self, S):
		a = S.count('1')
		return a * (a - 1) // 2

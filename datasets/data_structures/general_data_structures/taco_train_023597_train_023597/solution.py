class Solution:

	def fascinating(self, n):
		return list('123456789') == sorted(str(n) + str(n * 2) + str(n * 3))

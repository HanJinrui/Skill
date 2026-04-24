class Solution:

	def binarySubstring(self, n, s):
		c = s.count('1')
		return c * (c - 1) // 2

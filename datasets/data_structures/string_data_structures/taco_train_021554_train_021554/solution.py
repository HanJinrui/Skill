class Solution:

	def colName(self, n):
		ans = ''
		while n:
			ans = chr(65 + (n - 1) % 26) + ans
			n = (n - 1) // 26
		return ans

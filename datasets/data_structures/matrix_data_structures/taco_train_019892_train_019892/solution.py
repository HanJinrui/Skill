class Solution:

	def sumMatrix(self, n, q):
		return max(0, n - abs(q - (n + 1)))

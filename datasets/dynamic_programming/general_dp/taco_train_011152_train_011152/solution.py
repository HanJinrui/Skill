class Solution:

	def maxSum(self, n):
		if n <= 10:
			return n
		return max(n, self.maxSum(n // 2) + self.maxSum(n // 3) + self.maxSum(n // 4))

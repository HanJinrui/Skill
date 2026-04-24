class Solution:

	def areConsecutives(self, a, n):
		return sum(a) == n * (2 * min(a) + n - 1) // 2

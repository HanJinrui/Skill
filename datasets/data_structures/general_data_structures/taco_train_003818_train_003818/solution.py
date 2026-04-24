class Solution:

	def minValueToBalance(self, a, n):
		return abs(sum(a[:int(n / 2)]) - sum(a[int(n / 2):]))

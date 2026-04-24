class Solution:

	def subarraySum(self, a, n):
		s = 0
		for i in range(n):
			s += a[i] * (i + 1) * (n - i)
		return s % 1000000007

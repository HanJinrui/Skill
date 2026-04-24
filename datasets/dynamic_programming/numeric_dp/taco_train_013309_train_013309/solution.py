class Solution:

	def nthFibonacci(self, n):
		(a, b) = (0, 1)
		for i in range(n - 1):
			(a, b) = (b, (a + b) % 1000000007)
		return b

class Solution:

	def lucas(self, n):
		a = 2
		b = 1
		for i in range(n - 1):
			(b, a) = (a + b, b)
		return b % (10 ** 9 + 7)

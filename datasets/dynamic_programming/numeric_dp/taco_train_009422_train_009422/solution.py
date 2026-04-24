class Solution:

	def climbStairs(self, n):
		a = 1
		b = 2
		if n < 2:
			return 1
		for i in range(n - 2):
			(a, b) = (b, a + b)
		return b

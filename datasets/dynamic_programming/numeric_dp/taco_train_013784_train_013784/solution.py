class Solution:

	def p(self, n):
		if n == 0 or n == 1 or n == 2:
			return 1
		else:
			return self.p(n - 2) + self.p(n - 3)

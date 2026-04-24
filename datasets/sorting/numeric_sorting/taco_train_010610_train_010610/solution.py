class Solution:

	def isPerfectSquare(self, num):
		n = num ** 0.5
		if n == int(n):
			return True
		else:
			return False

class Solution:

	def minStep(self, n):
		ans = 0
		while n >= 2:
			if n % 3 == 0:
				n //= 3
			else:
				n -= 1
			ans += 1
		return ans

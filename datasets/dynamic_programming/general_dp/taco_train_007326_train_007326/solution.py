class Solution:

	def sumOfDigits(self, n):
		ans = 0
		for i in range(1, n + 1):
			while i:
				ans += i % 10
				i //= 10
		return ans

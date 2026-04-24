class Solution:

	def count(self, n):
		if n == 0:
			return 1
		ans = 0
		for i in range(0, n, 2):
			ans += self.count(i) * self.count(n - 2 - i)
		return ans

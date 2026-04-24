class Solution:

	def countWays(self, n, m):
		arr = [1] * m
		for i in range(n):
			arr.append(arr[-1] + arr[-m])
		return arr[-m] % (10 ** 9 + 7)

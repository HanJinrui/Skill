class Solution:

	def nCr(self, n, r):
		res = 1
		for i in range(1, r + 1):
			res = res * (n - r + i) // i
		return res % 1000000007

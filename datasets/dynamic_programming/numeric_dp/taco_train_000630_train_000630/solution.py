class Solution:

	def printFibb(self, n):
		res = [0, 1]
		for i in range(n - 1):
			res.append(res[-1] + res[-2])
		return res[1:]

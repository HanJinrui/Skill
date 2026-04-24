class Solution:

	def minCost(self, c, N):
		for i in range(N - 2, -1, -1):
			for j in range(3):
				c[i][j] += min(c[i + 1][(j + 1) % 3], c[i + 1][(j + 2) % 3])
		return min(c[0])

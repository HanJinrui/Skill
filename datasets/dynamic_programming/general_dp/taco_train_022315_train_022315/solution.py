class Solution:

	def maxSum(self, N, mat):
		x = 0
		y = 0
		for i in range(N):
			z = max(x, y)
			x = y + max(mat[0][i], mat[1][i])
			y = z
		return max(x, y)

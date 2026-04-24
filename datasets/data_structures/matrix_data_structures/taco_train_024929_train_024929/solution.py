class Solution:

	def DiagonalSum(self, matrix):
		s = 0
		for i in range(n):
			s += matrix[i][i]
			s += matrix[i][n - i - 1]
		return s

class Solution:

	def isToeplitzMatrix(self, matrix):
		return all((True if len(matrix[i]) == 1 or matrix[i][:-1] == matrix[i + 1][1:] else False for i in range(len(matrix) - 1)))

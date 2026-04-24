class Solution:

	def sumTriangles(self, matrix, n):
		u = 0
		l = 0
		for i in range(n):
			u = u + sum(matrix[i][i:])
			l = l + sum(matrix[i][:i + 1])
		return (u, l)

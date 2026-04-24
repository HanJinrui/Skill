class Solution:

	def Count(self, matrix):
		output = 0
		n = len(matrix)
		m = len(matrix[0])
		for i in range(n):
			for j in range(m):
				if matrix[i][j]:
					count = 0
					count += i > 0 and matrix[i - 1][j] == 0
					count += i < n - 1 and matrix[i + 1][j] == 0
					count += j > 0 and matrix[i][j - 1] == 0
					count += j < m - 1 and matrix[i][j + 1] == 0
					count += i > 0 and j > 0 and (matrix[i - 1][j - 1] == 0)
					count += i > 0 and j < m - 1 and (matrix[i - 1][j + 1] == 0)
					count += i < n - 1 and j > 0 and (matrix[i + 1][j - 1] == 0)
					count += i < n - 1 and j < m - 1 and (matrix[i + 1][j + 1] == 0)
					output += count > 0 and count % 2 == 0
		return output

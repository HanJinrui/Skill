class Solution:

	def MakeZeros(self, matrix):
		x = [0, -1, 1, 0]
		y = [-1, 0, 0, 1]
		n = len(matrix)
		m = len(matrix[0])
		dummy = [[matrix[j][i] for i in range(m)] for j in range(n)]
		for i in range(n):
			for j in range(m):
				if dummy[i][j] == 0:
					s = 0
					for k in range(4):
						if -1 < i + x[k] < n and -1 < j + y[k] < m:
							s += dummy[i + x[k]][j + y[k]]
							matrix[i + x[k]][j + y[k]] = 0
					matrix[i][j] = s

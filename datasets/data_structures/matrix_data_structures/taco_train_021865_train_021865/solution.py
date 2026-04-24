class Solution:

	def matrixSum(self, n, m, mat, q, queries):
		output = []
		for (hop, i, j) in queries:
			output.append(0)
			if j - hop >= 0:
				for k in range(max(0, i - hop), min(n, i + hop)):
					output[-1] += mat[k][j - hop]
			if j + hop < m:
				for k in range(max(0, i - hop + 1), min(n, i + hop + 1)):
					output[-1] += mat[k][j + hop]
			if i - hop >= 0:
				for k in range(max(0, j - hop + 1), min(m, j + hop + 1)):
					output[-1] += mat[i - hop][k]
			if i + hop < n:
				for k in range(max(0, j - hop), min(m, j + hop)):
					output[-1] += mat[i + hop][k]
		return output

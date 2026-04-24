class Solution:

	def maxGold(self, m, n, mat):
		for j in range(1, n):
			for i in range(m):
				dup = ddown = 0
				left = mat[i][j - 1]
				if i > 0:
					dup = mat[i - 1][j - 1]
				if i < m - 1:
					ddown = mat[i + 1][j - 1]
				mat[i][j] += max(dup, ddown, left)
		return max((mat[i][-1] for i in range(m)))

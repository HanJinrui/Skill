class Solution:

	def celebrity(self, M, n):
		celebrity = False
		for j in range(n):
			if sum([M[x][j] for x in range(n)]) == n - 1:
				if all([M[j][x] == 0 for x in range(n)]):
					return j
		return -1

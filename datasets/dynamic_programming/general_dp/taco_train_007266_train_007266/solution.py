class Solution:

	def zigzagSequence(self, n, M):
		if n == 1:
			return M[0][0]
		for i in range(1, n):
			M[i][0] += max(M[i - 1][1:])
			M[i][-1] += max(M[i - 1][:-1])
			for j in range(1, n - 1):
				M[i][j] += max(M[i - 1][:j] + M[i - 1][j + 1:])
		return max(M[-1])

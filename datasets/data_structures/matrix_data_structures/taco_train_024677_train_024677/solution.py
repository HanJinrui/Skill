class Solution:

	def antiDiagonalPattern(self, matrix):
		ans = []
		n = len(matrix)
		for l in range(2 * n - 1):
			(b, t) = (min(l, n - 1), max(l + 1 - n, 0))
			for i in range(t, b + 1):
				ans.append(matrix[i][l - i])
		return ans

class Solution:

	def BoundaryTraversal(self, matrix, n, m):
		ans = []
		ans.extend(matrix[0])
		for row in range(1, n - 1):
			ans.append(matrix[row][m - 1])
		if n > 1:
			ans.extend(reversed(matrix[n - 1]))
		if m > 1:
			for row in range(n - 2, 0, -1):
				ans.append(matrix[row][0])
		return ans

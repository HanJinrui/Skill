class Solution:

	def minimizeSum(self, n, tr):
		for row in range(n - 2, -1, -1):
			for j in range(len(tr[row])):
				tr[row][j] = tr[row][j] + min(tr[row + 1][j], tr[row + 1][j + 1])
		return tr[0][0]

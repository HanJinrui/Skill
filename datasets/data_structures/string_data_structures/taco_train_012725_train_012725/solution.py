class Solution:

	def __init__(self):
		self.mod = 10 ** 9 + 7
		self.dp = {}

	def countOfPalindromicPaths(self, matrix):
		return self.path(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1) % self.mod

	def path(self, matrix, i, j, x, y):
		if i >= len(matrix) or j >= len(matrix[0]) or x < 0 or (y < 0) or (matrix[i][j] != matrix[x][y]):
			return 0
		if i == x and j == y or abs(i - x) + abs(j - y) <= 1:
			return 1
		if i > x or j > y:
			return 0
		if (i, j, x, y) in self.dp:
			return self.dp[i, j, x, y]
		op1 = self.path(matrix, i + 1, j, x - 1, y) % self.mod
		op2 = self.path(matrix, i + 1, j, x, y - 1) % self.mod
		op3 = self.path(matrix, i, j + 1, x - 1, y) % self.mod
		op4 = self.path(matrix, i, j + 1, x, y - 1) % self.mod
		temp = (op1 + op2 + op3 + op4) % self.mod
		self.dp[i, j, x, y] = temp
		return temp

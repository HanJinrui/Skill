class Solution:

	def findOccurrence(self, mat, target):
		r = len(mat)
		c = len(mat[0])
		n = len(target) - 1

		def dfs(i, j, k):
			if i < 0 or i >= r or j < 0 or (j >= c) or (mat[i][j] != target[k]):
				return 0
			if k == n:
				return 1
			cnt = 0
			store = mat[i][j]
			mat[i][j] = '*'
			cnt += dfs(i + 1, j, k + 1)
			cnt += dfs(i - 1, j, k + 1)
			cnt += dfs(i, j + 1, k + 1)
			cnt += dfs(i, j - 1, k + 1)
			mat[i][j] = store
			return cnt
		ans = 0
		for i in range(r):
			for j in range(c):
				ans += dfs(i, j, 0)
		return ans

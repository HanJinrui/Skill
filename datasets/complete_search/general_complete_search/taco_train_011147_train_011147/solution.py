class Solution:

	def findPath(self, m, n):

		def ax(vis, i, j, s):
			if i < 0 or j < 0 or j >= n or (i >= n):
				return False
			if m[i][j] == 0 or vis[i][j] == 1:
				return False
			if i == n - 1 and j == n - 1:
				r.append(s)
				return
			vis[i][j] = 1
			ax(vis, i - 1, j, s + 'U')
			ax(vis, i + 1, j, s + 'D')
			ax(vis, i, j - 1, s + 'L')
			ax(vis, i, j + 1, s + 'R')
			vis[i][j] = 0
		r = []
		vis = [[0] * n for _ in range(n)]
		ax(vis, 0, 0, '')
		return r

class Solution:

	def hopscotch(self, n, m, mat, ty, i, j):
		ans = 0
		t = -(-1) ** (j & 1)
		dx = [[0, -1, 0, 1, t, t], [0, -2, 0, 2, -1, -1, 1, 1, -t, -t, 2 * t, 2 * t]]
		dy = [[-1, 0, 1, 0, -1, 1], [-2, 0, 2, 0, -2, 2, -2, 2, -1, 1, -1, 1]]
		k = 0
		while k < 6 * (ty + 1):
			x = i + dx[ty][k]
			y = j + dy[ty][k]
			if x >= 0 and x < n and (y >= 0) and (y < m):
				ans += mat[x][y]
			k += 1
		return ans

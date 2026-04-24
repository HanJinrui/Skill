class Solution:

	def shortestXYDist(self, grid, N, M):
		X = []
		Y = []
		for i in range(N):
			for j in range(M):
				if grid[i][j] == 'X':
					X.append([i, j])
				elif grid[i][j] == 'Y':
					Y.append([i, j])
		mn = N + M + 1
		for a in X:
			for b in Y:
				mn = min(mn, abs(a[0] - b[0]) + abs(a[1] - b[1]))
				if mn == 1:
					break
		return mn

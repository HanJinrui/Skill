class Solution:

	def findMinCost(self, x, y, costX, costY):
		n = len(x)
		m = len(y)
		t = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if x[i - 1] == y[j - 1]:
					t[i][j] = 1 + t[i - 1][j - 1]
				else:
					t[i][j] = max(t[i - 1][j], t[i][j - 1])
		return (n - t[-1][-1]) * costX + (m - t[-1][-1]) * costY

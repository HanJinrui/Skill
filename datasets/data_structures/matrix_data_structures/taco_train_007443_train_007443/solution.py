class Solution:

	def maxArea(self, x, r, c):
		for i in range(r - 2, -1, -1):
			for j in range(c):
				if x[i][j]:
					x[i][j] += x[i + 1][j]
		ans = 0
		for i in range(r):
			x[i].sort()
			for j in range(c):
				ans = max(ans, (c - j) * x[i][j])
		return ans

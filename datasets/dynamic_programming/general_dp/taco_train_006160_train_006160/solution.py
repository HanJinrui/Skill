class Solution:

	def maxSquare(self, n, m, a):
		for i in range(1, n):
			for j in range(1, m):
				if a[i][j] != 0:
					a[i][j] = min(a[i - 1][j], min(a[i][j - 1], a[i - 1][j - 1])) + 1
		ans = 0
		for i in range(n):
			for j in range(m):
				ans = max(ans, a[i][j])
		return ans

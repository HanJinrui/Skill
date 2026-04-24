class Solution:

	def findMinOpeartion(self, matrix, n):
		m = 0
		t = 0
		for i in range(n):
			a = 0
			b = 0
			for j in range(n):
				a += matrix[i][j]
				b += matrix[j][i]
			m = max(m, a, b)
			t += a
		m = m * n
		return m - t

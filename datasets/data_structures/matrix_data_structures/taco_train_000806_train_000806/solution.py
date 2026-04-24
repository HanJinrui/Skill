class Solution:

	def FindCoverage(self, m):
		c = 0
		n = len(m)
		p = len(m[0])
		s = {}
		for i in range(n):
			for j in range(p):
				if m[i][j] == 0:
					if i - 1 >= 0 and m[i - 1][j] == 1:
						c += 1
					if j - 1 >= 0 and m[i][j - 1] == 1:
						c += 1
					if i + 1 < n and m[i + 1][j] == 1:
						c += 1
					if j + 1 < p and m[i][j + 1] == 1:
						c += 1
		return c

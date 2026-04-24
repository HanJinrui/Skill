class Solution:

	def snakePattern(self, m):
		a = []
		l = len(m)
		for i in range(l):
			if i % 2 == 0:
				p = 1
			else:
				p = -1
			a += m[i][::p]
		return a

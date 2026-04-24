class Solution:

	def getCount(self, N, D):
		l = 1
		h = N
		while l <= h:
			m = (l + h) // 2
			x = 0
			while m > 0:
				x += m % 10
				m = m // 10
			m = (l + h) // 2
			if m - x < D:
				l = m + 1
			else:
				h = m - 1
		return N - h

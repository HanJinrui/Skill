class Solution:

	def killinSpree(self, n):
		l = 0
		r = n
		while l <= r:
			m = l + r >> 1
			if m * (m + 1) * (2 * m + 1) <= 6 * n:
				l = m + 1
			else:
				r = m - 1
		return l - 1

class Solution:

	def fun(self, s, k, n, c):
		k = n // len(s) + 1
		s = s * k
		return s.count(c, 0, n)

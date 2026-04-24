class Solution:

	def arranged(self, a, n):
		p = [i for i in a if i > 0]
		n = [i for i in a if i < 0]
		a[::2] = p[:]
		a[1::2] = n[:]
		return a

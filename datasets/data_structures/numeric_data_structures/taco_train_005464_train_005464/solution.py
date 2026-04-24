from math import sqrt

class Solution:
	s = 1

	def factors(self, n):
		c = 2
		d = {}
		while n > 1:
			if n % c == 0:
				d[c] = d.get(c, 0) + 1
				n = n // c
			else:
				c += 1
		for i in d.keys():
			self.s = self.s * (d[i] + 1)

	def countDivisorsMult(self, a, n):
		m = 1
		for i in a:
			m = m * i
		self.factors(m)
		return self.s

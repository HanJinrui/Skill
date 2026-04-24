class Solution:

	def posIntSol(self, s):
		l = s.split('=')
		d = int(l[1])
		g = l[0].count('+')
		p = d - g
		s = 1
		h = 1
		for i in range(g):
			s *= p
			p += 1
			h *= i + 1
		return s // h

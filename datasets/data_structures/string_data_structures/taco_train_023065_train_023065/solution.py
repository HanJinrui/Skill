class Solution:

	def barcketNumbers(self, S):
		c = 0
		r = []
		s = []
		for i in S:
			if i == '(':
				c += 1
				r.append(c)
				s.append(c)
			if i == ')':
				r.append(s.pop())
		return r

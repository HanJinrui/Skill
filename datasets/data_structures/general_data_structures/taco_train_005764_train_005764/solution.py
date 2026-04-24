class Solution:

	def minEnergy(self, a, n):
		e = 0
		s = 0
		for x in a:
			s += x
			if s <= 0:
				e = e + abs(s)
				s = 0
		return 1 + e

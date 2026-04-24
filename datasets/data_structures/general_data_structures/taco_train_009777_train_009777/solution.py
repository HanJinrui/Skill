class Solution:

	def equilibrium(self, a, n):
		s = sum(a)
		x = 0
		for i in a:
			s -= i
			if x == s:
				return 'YES'
			x += i
		return 'NO'

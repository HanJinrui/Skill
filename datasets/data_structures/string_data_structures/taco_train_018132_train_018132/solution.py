class Solution:

	def swapDigits(self, n1, n2):
		s1 = n2[-1] + n1[1:-1] + n2[0]
		s2 = n1[-1] + n2[1:-1] + n1[0]
		global s, n
		(s, n) = (s1, s2)

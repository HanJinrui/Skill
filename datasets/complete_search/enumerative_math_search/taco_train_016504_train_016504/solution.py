class Solution:

	def lastNon0Digit(self, N):
		pass
		import math
		s = str(math.factorial(N))[::-1]
		s = str(int(s))
		return s[0]

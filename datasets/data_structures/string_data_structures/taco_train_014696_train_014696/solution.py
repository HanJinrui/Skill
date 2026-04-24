class Solution:

	def isEven(self, s, n):
		s1 = s.rstrip('0')
		return int(s1[-2]) % 2 == 0 if s1[-1] == '.' else int(s1[-1]) % 2 == 0

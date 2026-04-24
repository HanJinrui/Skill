class Solution:

	def removeConsecutiveCharacter(self, S):
		s1 = '' + s[0]
		for i in s:
			if s1[-1] != i:
				s1 += i
		return s1

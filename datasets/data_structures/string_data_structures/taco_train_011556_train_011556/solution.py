class Solution:

	def removeSpecialCharacter(self, S):
		s = ''
		for x in S:
			if x.isalpha():
				s += x
		return s if s else -1

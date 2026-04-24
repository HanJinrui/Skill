class Solution:

	def gameResult(self, s):
		if s[0] == s[1]:
			return 'DRAW'
		elif s in ('RS', 'SP', 'PR'):
			return 'A'
		else:
			return 'B'

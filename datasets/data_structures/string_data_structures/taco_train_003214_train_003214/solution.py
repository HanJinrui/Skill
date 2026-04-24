class Solution:

	def removeCharacters(self, S):
		return ''.join([c for c in S if c.isdigit()])

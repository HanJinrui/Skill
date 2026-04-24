class Solution:

	def PartyType(self, a, n):
		x = set(a)
		if len(x) == len(a):
			return 'GIRLS'
		return 'BOYS'

class Solution:

	def metaStrings(self, S1, S2):
		if S1 == S2:
			return 0
		elif sorted(S1) == sorted(S2):
			return 1

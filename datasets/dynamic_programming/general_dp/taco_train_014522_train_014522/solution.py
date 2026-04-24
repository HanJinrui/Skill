class Solution:

	def maxOnes(self, s):
		mdif = -1
		cdif = -1
		oone = 0
		for i in range(len(s)):
			if s[i] == '1':
				oone += 1
			val = 1 if s[i] == '0' else -1
			cdif = max(val, cdif + val)
			mdif = max(cdif, mdif)
		return oone + mdif

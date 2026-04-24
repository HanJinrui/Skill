class Solution:

	def modify(self, s):
		if s[0].islower():
			return s.lower()
		return s.upper()

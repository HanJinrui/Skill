class Solution:

	def areRotations(self, s1, s2):
		return s2 in s1 + s1 and len(s1) == len(s2)

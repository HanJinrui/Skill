class Solution:

	def Count(self, S):
		return sum((x.isalpha() for x in S))

class Solution:

	def isPanagram(self, S):
		return int(not set('abcdefghijklmnopqrstuvwxyz') - set(S.lower()))

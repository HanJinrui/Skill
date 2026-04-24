class Solution:

	def ExtractMessage(self, s):
		return ' '.join(s.replace('LIE', ' ').split())

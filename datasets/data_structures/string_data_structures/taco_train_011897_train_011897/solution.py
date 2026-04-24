class Solution:

	def countWords(self, s):
		return len(s.replace('\\n', ' ').replace('\\t', ' ').split())

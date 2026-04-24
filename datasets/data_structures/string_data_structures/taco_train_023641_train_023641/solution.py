class Solution:

	def reverseWords(self, s):
		words = s.split('.')
		return '.'.join((w[::-1] for w in words))

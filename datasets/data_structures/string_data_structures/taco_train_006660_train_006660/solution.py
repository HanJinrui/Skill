class Solution:

	def reverseAlternate(self, Str):
		s = list(Str.split(' '))
		for i in range(1, len(s), 2):
			s[i] = s[i][::-1]
		return ' '.join(s)

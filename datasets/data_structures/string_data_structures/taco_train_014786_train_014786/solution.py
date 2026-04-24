class Solution:

	def triDownwards(self, s):
		x = ''
		for i in range(len(s)):
			x += '.' * i + s[i:]
		return x

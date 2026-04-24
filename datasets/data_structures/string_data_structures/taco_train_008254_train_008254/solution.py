class Solution:

	def reverseString(self, s):
		a = ''
		for x in s[::-1]:
			if x != ' ' and x not in a:
				a += x
		return a

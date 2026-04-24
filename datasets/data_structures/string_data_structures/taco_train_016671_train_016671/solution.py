class Solution:

	def splitString(ob, S):
		s = ['', '', '']
		for i in S:
			if i.isalpha():
				s[0] += i
			elif i.isnumeric():
				s[1] += i
			else:
				s[2] += i
		return s

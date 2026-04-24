class Solution:

	def reciprocalString(self, S):
		x = ''
		for i in S:
			if i.isupper():
				x += chr(90 - (ord(i) - 65))
			elif i.islower():
				x += chr(122 - (ord(i) - 97))
			else:
				x += i
		return x

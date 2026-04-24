class Solution:

	def crossPattern(ob, s):
		a = ''
		for i in range(len(s)):
			for j in range(len(s)):
				if i == j or i + j == len(S) - 1:
					a = a + s[j]
				else:
					a = a + ' '
		return a

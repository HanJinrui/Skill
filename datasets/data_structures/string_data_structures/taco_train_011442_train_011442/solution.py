class Solution:

	def findpos(self, n):
		pos = 0
		for i in n:
			if i == '4':
				pos = 2 * pos + 1
			else:
				pos = 2 * pos + 2
		return pos

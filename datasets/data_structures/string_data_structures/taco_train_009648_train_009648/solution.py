class Solution:

	def printString(self, S, ch, count):
		r = ''
		c = 0
		for i in S:
			if c >= count:
				r += i
			if i == ch:
				c += 1
		if not r:
			return 'Empty string'
		return r

import re

class Solution:

	def findDays(self, S):
		l = 0
		c = 0
		k = re.findall('\\.+', S)
		for i in k:
			if len(i) > l:
				c = c + 1
				l = len(i)
		return c

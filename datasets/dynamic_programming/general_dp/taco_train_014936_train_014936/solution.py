import datetime

class Solution:

	def Count(self, a, b):
		c = 0
		for i in range(a, b + 1):
			x = datetime.datetime(i, 1, 1)
			if x.strftime('%A') == 'Sunday':
				c += 1
		return c

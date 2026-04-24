class Solution:

	def minDaysToEmpty(self, c, l):
		n = 1
		cap = c
		while c > n:
			c = c - n
			n += 1
			c = c + l
			if c > cap:
				c = cap
		return n

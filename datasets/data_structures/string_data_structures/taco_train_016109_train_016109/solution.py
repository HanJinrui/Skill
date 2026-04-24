class Solution:

	def arrangeString(self, s, x, y):
		m = ''
		c1 = s.count('0')
		c2 = s.count('1')
		while c1 > 0 or c2 > 0:
			for i in range(0, x):
				if c1 > 0:
					m += '0'
					c1 -= 1
			for j in range(0, y):
				if c2 > 0:
					m += '1'
					c2 -= 1
		return m

class Solution:

	def makeProductOne(self, arr, N):
		c = 0
		s = 0
		z = 0
		for i in arr:
			if i > 0:
				c += i - 1
			elif i == 0:
				c += 1
				z += 1
			else:
				c += -i - 1
				s += 1
		if s % 2 != 0:
			if z == 0:
				c += 2
		return c

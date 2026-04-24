class Solution:

	def countNumbers(self, n):
		c = 0
		for i in range(1, n + 1):
			for x in str(i):
				if x not in '12345':
					break
			else:
				c += 1
		return c

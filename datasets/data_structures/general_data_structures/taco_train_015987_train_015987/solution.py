class Solution:

	def longest(self, arr, n):
		m = 0
		c = 0
		for i in arr:
			if i >= m:
				m = i
				c += 1
		return c

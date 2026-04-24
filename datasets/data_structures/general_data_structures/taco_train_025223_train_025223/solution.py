class Solution:

	def countElements(self, arr, n):
		c = 0
		mx = -100000
		for x in arr:
			if mx < x:
				c += 1
				mx = x
		return c

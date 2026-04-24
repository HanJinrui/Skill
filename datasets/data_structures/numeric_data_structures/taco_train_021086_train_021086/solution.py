class Solution:

	def no_of_subarrays(self, n, arr):
		c = 0
		k = 0
		for i in arr:
			if i == 0:
				c += 1
				k += c
			else:
				c = 0
		return k

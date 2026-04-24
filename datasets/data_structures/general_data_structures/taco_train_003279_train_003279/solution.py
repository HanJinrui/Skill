class Solution:

	def countIncreasing(self, arr, n):
		p = 0
		c = 0
		for i in range(1, n):
			if arr[i] > arr[i - 1]:
				c += i - p
			else:
				p = i
		return c

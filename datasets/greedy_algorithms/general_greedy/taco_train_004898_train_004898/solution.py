class Solution:

	def binarySearchable(self, Arr, n):
		b = sorted(Arr)
		c = 0
		for i in range(n):
			if Arr[i] == b[i]:
				c += 1
			else:
				break
		return c

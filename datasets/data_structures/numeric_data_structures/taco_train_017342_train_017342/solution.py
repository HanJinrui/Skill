class Solution:

	def noOfTriangles(self, arr, n):
		arr.sort()
		c = 0
		for i in range(n - 1, 1, -1):
			l = 0
			h = i - 1
			while l < h:
				if arr[l] + arr[h] > arr[i]:
					c += h - l
					h -= 1
				else:
					l += 1
		return c

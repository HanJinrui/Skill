class Solution:

	def count_pair(self, arr, s, n, m):
		c = 0
		for i in range(0, len(arr), 2):
			if arr[i] in s and arr[i + 1] in s:
				c += 1
		return c

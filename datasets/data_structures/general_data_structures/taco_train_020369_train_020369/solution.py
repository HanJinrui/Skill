class Solution:

	def swapElements(self, arr, n):
		i = 0
		while i + 2 < n:
			(arr[i], arr[i + 2]) = (arr[i + 2], arr[i])
			i += 1

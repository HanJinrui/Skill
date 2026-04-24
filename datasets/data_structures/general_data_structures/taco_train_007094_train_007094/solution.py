class Solution:

	def leftRotate(self, arr, n, d):
		arr[:] = arr[d:] + arr[:d]
		return arr

class Solution:

	def leftRotate(self, arr, k, n):
		k = k % len(arr)
		arr[:] = arr[k:] + arr[:k]

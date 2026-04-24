class Solution:

	def reverseSubArray(self, arr, n, l, r):
		arr[l - 1:r] = arr[l - 1:r][::-1]

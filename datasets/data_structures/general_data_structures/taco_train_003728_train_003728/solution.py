class Solution:

	def printLargest(self, arr):
		return ''.join(sorted(arr, reverse=True, key=lambda _: _ * 18))

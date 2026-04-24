class Solution:

	def leftElement(self, arr, n):
		arr.sort()
		return arr[(n - 1) // 2]

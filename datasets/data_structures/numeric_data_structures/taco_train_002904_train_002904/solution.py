class Solution:

	def countArray(self, arr, n, x):
		return [arr.count((i + x) // 2) for i in arr]

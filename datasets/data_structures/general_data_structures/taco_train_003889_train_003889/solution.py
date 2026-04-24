class Solution:

	def pushZerosToEnd(self, arr, n):
		arr[:] = [i for i in arr if i != 0] + [0] * arr.count(0)

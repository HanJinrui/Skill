class Solution:

	def merge(self, arr1, arr2, n, m):
		arr1.extend(arr2)
		arr1.sort()
		arr2.clear()
		return arr1

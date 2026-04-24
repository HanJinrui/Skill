class Solution:

	def SoldierRequired(self, arr, n):
		arr.sort()
		return max(0, n - arr.count(arr[0]) - arr.count(arr[-1]))

class Solution:

	def getCount(self, arr, n, num1, num2):
		return len(arr[arr.index(num1) + 1:len(arr) - arr[::-1].index(num2) - 1])

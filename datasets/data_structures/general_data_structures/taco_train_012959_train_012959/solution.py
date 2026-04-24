class Solution:

	def findMidSum(self, ar1, ar2, n):
		arr = sorted(ar1 + ar2)
		return arr[n] + arr[n - 1]

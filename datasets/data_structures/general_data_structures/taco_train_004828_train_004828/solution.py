class Solution:

	def Pair_minimum(self, arr, n):
		arr.sort()
		maxi = 0
		for i in range(n):
			maxi = max(maxi, arr[i] + arr[-i - 1])
		return maxi

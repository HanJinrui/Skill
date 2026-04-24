class Solution:

	def checkIsAP(self, arr, n):
		arr.sort()
		dif = arr[1] - arr[0]
		return all([arr[i + 1] - arr[i] == dif for i in range(n - 1)])

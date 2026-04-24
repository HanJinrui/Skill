import bisect

class Solution:

	def minRemoval(self, arr, n):
		arr.sort()
		return n - max([bisect.bisect(arr, arr[i] * 2) - i for i in range(n)])

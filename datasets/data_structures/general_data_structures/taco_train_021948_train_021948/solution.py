class Solution:

	def maxSortedAdjacentDiff(self, arr, n):
		if n < 2:
			return 0
		arr.sort()
		return max([x - y for (x, y) in zip(arr[1:], arr[:-1])])

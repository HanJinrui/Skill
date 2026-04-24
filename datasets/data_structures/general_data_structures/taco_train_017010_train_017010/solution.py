class Solution:

	def findMaximumNum(self, arr, n):
		arr.sort(reverse=True)
		while len(arr) > arr[-1]:
			arr.pop()
		return len(arr)

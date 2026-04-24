class Solution:

	def minimumNumber(self, n, arr):
		for i in range(n):
			if arr[i] % 2 == 1:
				return 1
		return min(arr)

class Solution:

	def checkDuplicatesWithinK(self, arr, n, k):
		for i in range(n):
			if len(arr[i:i + k]) != len(set(arr[i:i + k])):
				return True
		return False

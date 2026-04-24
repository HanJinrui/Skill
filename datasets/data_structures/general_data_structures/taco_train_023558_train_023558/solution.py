class Solution:

	def findSmallest(self, arr, n):
		s = 1
		for i in range(n):
			if arr[i] <= s:
				s += arr[i]
		return s

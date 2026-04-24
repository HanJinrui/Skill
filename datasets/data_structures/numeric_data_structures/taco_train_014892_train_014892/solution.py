class Solution:

	def isPossible(self, N, arr):
		if sum(arr) % 3 == 0:
			return 1
		return 0

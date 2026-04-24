class Solution:

	def maxDistance(self, arr, n):
		maxi = 0
		d = {}
		for (i, j) in enumerate(arr):
			if j in d:
				maxi = max(maxi, i - d[j])
			else:
				d[j] = i

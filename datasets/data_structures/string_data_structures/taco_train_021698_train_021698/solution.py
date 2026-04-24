class Solution:

	def findPairs(self, a, n):
		d = {}
		for i in range(n - 1):
			for j in range(i + 1, n):
				if a[i] * a[j] in d:
					return 1
				else:
					d[a[i] * a[j]] = 1
		return -1

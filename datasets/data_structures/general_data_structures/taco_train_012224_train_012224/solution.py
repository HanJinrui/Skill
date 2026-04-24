class Solution:

	def maxRepeating(self, arr, n, k):
		b = [0] * k
		for i in arr:
			b[i] += 1
		return b.index(max(b))

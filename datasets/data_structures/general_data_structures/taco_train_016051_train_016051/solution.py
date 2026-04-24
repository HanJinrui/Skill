class Solution:

	def swapKth(self, a, n, k):
		(a[k - 1], a[n - k]) = (a[n - k], a[k - 1])
		return a

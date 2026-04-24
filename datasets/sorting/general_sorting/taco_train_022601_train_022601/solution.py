class Solution:

	def partSort(self, arr, n, l, r):
		l1 = min(l, r)
		r1 = max(l, r)
		ji = arr[l1:r1 + 1]
		ji.sort()
		arr[l1:r1 + 1] = ji

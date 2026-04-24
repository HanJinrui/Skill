class Solution:

	def immediateSmaller(self, a, n):
		for i in range(n - 1):
			if a[i] > a[i + 1]:
				a[i] = a[i + 1]
			else:
				a[i] = -1
		a[n - 1] = -1
		return

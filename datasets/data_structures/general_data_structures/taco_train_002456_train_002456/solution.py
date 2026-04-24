class Solution:

	def customSort(self, arr, n):
		a = arr[:n // 2]
		b = arr[n // 2:]
		a.sort()
		b.sort(reverse=True)
		arr[:] = a + b

class Solution:

	def maxNtype(self, arr, n):
		s = max(arr)
		l = 0
		a = sorted(arr)
		if a == arr:
			l = 1
		elif a[::-1] == arr:
			l = 2
		elif arr[-1] > arr[0]:
			l = 3
		else:
			l = 4
		return [l, s]

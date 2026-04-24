class Solution:

	def nextGreatest(self, arr, n):
		m = arr[n - 1]
		arr[n - 1] = -1
		for i in range(n - 2, -1, -1):
			t = arr[i]
			arr[i] = m
			if t > m:
				m = t

class Solution:

	def frequencyCount(self, arr, N, P):
		a = [0] * max(P, N)
		for i in arr:
			a[i - 1] += 1
		arr[:] = a[:N]
		return arr

class Solution:

	def minxorpair(self, N, arr):
		arr.sort()
		l = []
		for i in range(N - 1):
			l.append(arr[i] ^ arr[i + 1])
		return min(l)

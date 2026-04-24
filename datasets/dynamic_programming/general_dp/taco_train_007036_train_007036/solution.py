class Solution:

	def offerings(self, N, arr):
		off = [1] * N
		for i in range(1, N):
			if arr[i] > arr[i - 1]:
				off[i] = off[i - 1] + 1
		for i in range(N - 2, -1, -1):
			if arr[i] > arr[i + 1]:
				off[i] = max(off[i + 1] + 1, off[i])
		return sum(off)
